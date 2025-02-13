document.addEventListener("DOMContentLoaded", () => {
  initialiseAddCaravan();
  initialiseEditCaravan();
  initialiseCarousel();
  initialiseFilterToggle();
  initialiseSelect2();
  initaliseRequestBooking();
  initialiseBookingButton();
  initialiseImageModal();
  initialiseFavouriteIcons();
  initialiseReviewModals();
  initialiseDeleteReview();
});

// Utility functions
function parseJSON(input) {
  try {
    return input.trim() ? JSON.parse(input) : [];
  } catch (e) {
    console.error("Error parsing JSON:", e);
    return [];
  }
}

function removeDuplicates(dates) {
  return dates.filter(
    (value, index, self) =>
      index ===
      self.findIndex(
        (t) =>
          t.start_date === value.start_date && t.end_date === value.end_date
      )
  );
}

// Get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Show in-app success message
function showInAppMessage(message) {
  const messageContainer = document.getElementById("success-message-container");

  if (messageContainer) {
    messageContainer.textContent = message;
    messageContainer.style.display = "block";

    // Hide the message after 5 seconds
    setTimeout(() => {
      messageContainer.style.display = "none";
    }, 5000);
  }
}

// Initialise Select2 for the amenities dropdown
function initialiseSelect2() {
  if (window.jQuery) {
    $(document).ready(function () {
      $("select[name='amenities']").select2({
        placeholder: "Select amenities",
        allowClear: true,
        width: "100%",
      });
    });
  } else {
    console.error("jQuery not found: Select2 requires jQuery to function.");
  }
}

// Initialise filter toggle and auto submission
function initialiseFilterToggle() {
  const toggleFiltersBtn = document.getElementById("toggle-filters");
  const filterForm = document.getElementById("filter-form");
  const amenitiesSelect = document.querySelector("select[name='amenities']");
  // Show/hide filters
  if (toggleFiltersBtn) {
    toggleFiltersBtn.addEventListener("click", function () {
      const filterContainer = document.getElementById("filter-container");
      if (filterContainer.style.display === "none") {
        filterContainer.style.display = "block";
        this.textContent = "Hide Filters";
      } else {
        filterContainer.style.display = "none";
        this.textContent = "Filters";
      }
    });
  }
  // Auto submit form when amenities are selected
  if (amenitiesSelect && filterForm) {
    amenitiesSelect.addEventListener("change", function () {
      filterForm.submit();
    });
  }
}

// Initialise calendar on Add Caravan page
function initialiseAddCaravan() {
  const calendarEl = document.getElementById("calendar");
  const hiddenInputEl = document.getElementById("available_dates");
  // Adding multiple amenities
  const addAmenityBtn = document.getElementById("add-amenity-btn");
  if (addAmenityBtn) {
    addAmenityBtn.addEventListener("click", function () {
      const container = document.getElementById("amenities-container");
      const input = document.createElement("input");
      input.type = "text";
      input.name = "extra_amenity";
      input.placeholder = "Add a new amenity";
      input.classList.add("form-control", "mb-2");
      container.appendChild(input);
    });
  }
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", function () {
      const amenities = document.querySelectorAll(
        "input[name='extra_amenity']"
      );
      amenities.forEach((input, index) => {
        input.name = `extra_amenity_${index}`;
      });
    });
  }

  if (calendarEl) {
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: "dayGridMonth",
      selectable: true,
      editable: true,
      eventResizableFromStart: true,
      unselectAuto: false,
      select: function (info) {
        let dates = parseJSON(hiddenInputEl.value);
        let adjustedEnd = new Date(info.endStr);
        if (
          !dates.some(
            (d) => d.start_date === info.startStr && d.end_date === info.endStr
          )
        ) {
          dates.push({
            start_date: info.startStr,
            end_date: adjustedEnd.toISOString().split("T")[0],
          });
          hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
          calendar.addEvent({
            title: "Available",
            start: info.startStr,
            end: info.endStr,
            allDay: true,
          });
        }
        calendar.unselect();
      },
      eventDrop: function (info) {
        let dates = parseJSON(hiddenInputEl.value);
        let index = dates.findIndex(
          (d) => d.start_date === info.oldEvent.startStr
        );

        if (index !== -1) {
          dates.splice(index, 1);
          let adjustedEnd = new Date(info.event.endStr);
          adjustedEnd.setDate(adjustedEnd.getDate() - 1);
          dates.push({
            start_date: info.event.startStr,
            end_date: adjustedEnd.toISOString().split("T")[0],
          });
          hiddenInputEl.value = JSON.stringify(dates);
        }
      },
      eventResize: function (info) {
        let dates = parseJSON(hiddenInputEl.value);
        let index = dates.findIndex(
          (d) => d.start_date === info.event.startStr
        );

        if (index !== -1) {
          let adjustedEnd = new Date(info.event.endStr);
          adjustedEnd.setDate(adjustedEnd.getDate() - 1);
          dates[index].end_date = adjustedEnd.toISOString().split("T")[0];
          hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
        }
      },
      eventClick: function (info) {
        let dates = parseJSON(hiddenInputEl.value);
        dates = dates.filter((d) => d.start_date !== info.event.startStr);
        hiddenInputEl.value = JSON.stringify(dates);
        info.event.remove();
      },
      events: parseJSON(hiddenInputEl.value),
    });
    calendar.render();
  }
}

// Initialise calendar on Edit Caravan page
function initialiseEditCaravan() {
  const calendarEl = document.getElementById("calendar");
  const hiddenInputEl = document.getElementById("available_dates");

  // Adding multiple amenities
  const addAmenityBtn = document.getElementById("add-amenity-btn");
  if (addAmenityBtn) {
    addAmenityBtn.addEventListener("click", function () {
      const container = document.getElementById("amenities-container");
      const input = document.createElement("input");
      input.type = "text";
      input.name = "extra_amenity";
      input.placeholder = "Add a new amenity";
      input.classList.add("form-control", "mb-2");
      container.appendChild(input);
    });
  }

  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", function () {
      const amenities = document.querySelectorAll(
        "input[name='extra_amenity']"
      );
      amenities.forEach((input, index) => {
        input.name = `extra_amenity_${index}`;
      });
    });
  }

  if (calendarEl) {
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: "dayGridMonth",
      selectable: true,
      editable: true,
      eventResizableFromStart: true,
      unselectAuto: false,
      select: function (info) {
        let dates = parseJSON(hiddenInputEl.value);
        let adjustedEnd = new Date(info.endStr);
        if (
          !dates.some(
            (d) => d.start_date === info.startStr && d.end_date === info.endStr
          )
        ) {
          dates.push({ start_date: info.startStr, end_date: info.endStr });
          hiddenInputEl.value = JSON.stringify(dates);
        }
        calendar.addEvent({
          start: info.startStr,
          end: info.endStr,
          allDay: true,
        });
      },
    });
    calendar.render();
  }
  // Handle amenities in the edit modal
  const editModal = document.getElementById("editCaravanModal");
  if (editModal) {
    editModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const id = button.getAttribute("data-id");
      const title = button.getAttribute("data-title");
      const description = button.getAttribute("data-description");
      const berth = button.getAttribute("data-berth");
      const location = button.getAttribute("data-location");
      const price = button.getAttribute("data-price");
      const amenities = button.getAttribute("data-amenities").split(",");

      const modal = event.target;
      modal.querySelector(".modal-body #id_title").value = title;
      modal.querySelector(".modal-body #id_description").value = description;
      modal.querySelector(".modal-body #id_berth").value = berth;
      modal.querySelector(".modal-body #id_location").value = location;
      modal.querySelector(".modal-body #id_price_per_night").value = price;

      // Handle amenities
      const amenitiesField = modal.querySelector(".modal-body #id_amenities");
      if (amenitiesField) {
        const options = amenitiesField.options;
        for (let i = 0; i < options.length; i++) {
          options[i].selected = amenities.includes(options[i].value);
        }
      }

      // Set the form action to the edit URL
      modal
        .querySelector("#editCaravanForm")
        .setAttribute("action", "/edit/" + id + "/");
    });
  }
}

// Initialise carousel
function initialiseCarousel() {
  document.querySelectorAll(".carousel").forEach(function (carousel) {
    new bootstrap.Carousel(carousel, {
      interval: false,
    });
  });
}

// Initialise image modal
function initialiseImageModal() {
  const imageModal = document.getElementById("imageModal");
  const modalCarouselInner = document.getElementById("modalCarouselInner");
  const modalTitle = document.getElementById("imageModalLabel");

  if (imageModal && modalCarouselInner && modalTitle) {
    imageModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const carouselId = button.getAttribute("data-bs-carousel-id");
      const carousel = document.getElementById(carouselId);
      if (!carousel) {
        console.error(`Carousel with ID ${carouselId} not found.`);
        return;
      }
      const carouselItems = carousel.querySelectorAll(".carousel-item");
      const caravanTitle = button
        .closest(".list-group-item")
        .querySelector("h2").textContent;

      // Set the modal title to the caravan title
      modalTitle.textContent = caravanTitle;

      // Clear existing items in the modal carousel
      modalCarouselInner.innerHTML = "";

      // Add items to the modal carousel
      carouselItems.forEach((item, index) => {
        const newItem = item.cloneNode(true);
        const icon = newItem.querySelector(
          ".fa-up-right-and-down-left-from-center"
        );
        if (icon) {
          icon.parentNode.removeChild(icon);
        }
        if (index === 0) {
          newItem.classList.add("active");
        } else {
          newItem.classList.remove("active");
        }
        modalCarouselInner.appendChild(newItem);
      });
    });
  }
}

// Initialise favourite icons
function initialiseFavouriteIcons() {
  const favouriteIcons = document.querySelectorAll(".favourite-icon");
  favouriteIcons.forEach((icon) => {
    icon.addEventListener("click", function () {
      const caravanId = this.getAttribute("data-caravan-id");
      const isFavourite = this.classList.toggle("favourite");

      // Send the favourite status to the server
      fetch(`/listings/toggle_favourite/${caravanId}/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ is_favourite: isFavourite }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (!data.success) {
            // Revert the favourite status if the server update failed
            this.classList.toggle("favourite");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          // Revert the favourite status if there was an error
          this.classList.toggle("favourite");
        });
    });
  });
}

// Initialise request booking form
function initaliseRequestBooking() {
  const requestBookingCard = document.getElementById("requestBookingCard");
  if (requestBookingCard) {
    const bookNowClicked = localStorage.getItem("bookNowClicked");
    if (bookNowClicked) {
      requestBookingCard.style.display = "block";
      localStorage.removeItem("bookNowClicked");
    }
  }

  const bookingForm = document.getElementById("bookingForm");
  if (bookingForm) {
    bookingForm.addEventListener("submit", function () {
      setTimeout(function () {
        bookingForm.reset();
      }, 1000);
    });
  }
}

// Initialise booking button
function initialiseBookingButton() {
  const bookNowBtn = document.querySelectorAll(".book-now-btn");
  bookNowBtn.forEach((button) => {
    button.addEventListener("click", function () {
      localStorage.setItem("bookNowClicked", true);
      localStorage.setItem("caravanId", this.getAttribute("data-caravan-id"));
    });
  });
}

// Initialise review modals
function initialiseReviewModals() {
  const reviewModals = document.querySelectorAll(
    ".modal.fade:not(#imageModal)"
  );
  console.log(
    `🔍 Found ${reviewModals.length} modals (excluding image modal).`
  );

  reviewModals.forEach((modal) => {
    // Prevent duplicate initialisation
    if (modal.hasAttribute("data-initialised")) {
      console.warn(`⚠️ Modal already initialised: ${modal.id}`);
      return;
    }
    modal.setAttribute("data-initialised", "true");

    console.log(`🆔 Initialising modal with ID: ${modal.id}`);

    // Initialise the modal instance to manage it with Bootstrap
    const modalInstance = new bootstrap.Modal(modal, {
      // Prevents modal from closing when clicking on backdrop
      backdrop: "static",
      // Prevents closing when pressing the Escape key
      keyboard: false,
    });

    modal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      console.log("🎯 Modal show event triggered for:", modal.id);

      if (!button) {
        console.warn("⚠️ No related target button found. Skipping.");
        return;
      }

      const caravanId = button.getAttribute("data-caravan-id") || null;
      const reviewId = button.getAttribute("data-review-id") || null;
      const replyId = button.getAttribute("data-reply-id") || null;
      console.log(
        `🔍 Button clicked - Caravan ID: ${caravanId}, Review ID: ${reviewId}, Reply ID: ${replyId}`
      );

      const modalTitle = modal.querySelector(".modal-title");
      let form = modal.querySelector("form");

      // Special case for editReviewModal (with dynamic IDs like editReviewModal123)
      if (modal.id.startsWith("editReviewModal") && !form) {
        console.log(`🛠️ Manually injecting form for modal: ${modal.id}`);
        // Dynamically create and append a form if missing
        const newForm = document.createElement("form");
        newForm.method = "post";
        newForm.innerHTML = `
          <input type="hidden" name="csrfmiddlewaretoken" value="${getCookie(
            "csrftoken"
          )}">
          <div class="mb-3">
            <label for="rating" class="form-label">Rating</label>
            <input type="number" class="form-control" name="rating" min="1" max="5" required>
          </div>
          <div class="mb-3">
            <label for="comment" class="form-label">Comment</label>
            <textarea class="form-control" name="comment" rows="3" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        `;
        modal.querySelector(".modal-body").appendChild(newForm);
        form = newForm;
      }

      if (!form) {
        console.log(`⏭️ Skipping modal without form: ${modal.id}`);
        return;
      }

      let actionUrl = "";
      let actionType = "";

      // Handle edit reply
      if (button.classList.contains("edit-reply-btn") && replyId) {
        actionType = "Edit Reply";
        actionUrl = `/listings/reply_edit/${replyId}/`;
        modalTitle.textContent = actionType;
        if (form.reply)
          form.reply.value = button.getAttribute("data-reply-text") || "";
      }

      // Handle edit review
      else if (button.classList.contains("edit-review-btn") && reviewId) {
        actionType = "Edit Review";
        actionUrl = `/listings/review_edit/${reviewId}/`;
        modalTitle.textContent = actionType;
        if (form.rating)
          form.rating.value = button.getAttribute("data-rating") || "";
        if (form.comment)
          form.comment.value = button.getAttribute("data-comment") || "";
      }

      // Handle reply to review
      else if (reviewId) {
        actionType = "Reply to Review";
        actionUrl = `/listings/submit_reply/${reviewId}/`;
        modalTitle.textContent = actionType;
      }

      // Handle new review
      else if (caravanId) {
        actionType = "Submit New Review";
        actionUrl = `/listings/submit_review/${caravanId}/`;
        modalTitle.textContent = actionType;
      }

      if (!actionUrl) {
        console.error(
          "❌ No valid action URL determined. Check button attributes."
        );
        return;
      }

      console.log(`🔗 Setting form action to: ${actionUrl}`);
      form.action = actionUrl;

      // Replace form to remove previous event listeners
      const newForm = form.cloneNode(true);
      form.replaceWith(newForm);
      form = newForm;

      // Log form fields
      const formFields = Array.from(form.elements).map(
        (el) => `${el.name}: ${el.value}`
      );
      console.log(`📝 Form fields before submission: ${formFields.join(", ")}`);

      // Add form submission handler
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        console.log(`🚀 Submitting form to: ${form.action}`);

        const formData = new FormData(form);

        fetch(form.action, {
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
          },
          body: formData,
        })
          .then(async (response) => {
            const contentType = response.headers.get("content-type");
            if (!response.ok) {
              const text = await response.text();
              throw new Error(`HTTP ${response.status}: ${text}`);
            }
            if (contentType && contentType.includes("application/json")) {
              return response.json();
            } else {
              throw new Error("Unexpected response type.");
            }
          })
          .then((data) => {
            console.log("✅ Server response:", data);
            if (data.success) {
              // Close the modal after submission
              modalInstance.hide();
              showInAppMessage("Review submitted successfully!");
              location.reload();
            } else {
              console.warn("⚠️ Server responded with an error:", data);
              showInAppMessage("An error occurred. Please try again.");
            }
          })
          .catch((error) => {
            console.error("Error:", error);
            showInAppMessage("An error occurred. Please try again.");
          });
      });
    });
  });
}

// Initialise delete review buttons
function initialiseDeleteReview() {
  document.querySelectorAll(".delete-review-btn").forEach((button) => {
    button.addEventListener("click", function (event) {
      event.preventDefault();
      handleDelete(this.getAttribute("data-url"));
    });
  });

  document.querySelectorAll(".delete-reply-btn").forEach((button) => {
    button.addEventListener("click", function (event) {
      event.preventDefault();
      handleDelete(this.getAttribute("data-url"));
    });
  });
}

// Handle delete requests
function handleDelete(url) {
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        location.reload();
      } else {
        showInAppMessage("An error occurred while deleting the review.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      showInAppMessage("An error occurred while deleting the review.");
    });
}
