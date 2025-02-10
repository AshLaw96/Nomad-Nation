document.addEventListener("DOMContentLoaded", function () {
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
      fetch(`/toggle_favourite/${caravanId}/`, {
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
  const reviewModals = document.querySelectorAll(".modal.fade");
  reviewModals.forEach((modal) => {
    modal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const caravanId = button.getAttribute("data-caravan-id");
      const modalTitle = modal.querySelector(".modal-title");
      const form = modal.querySelector("form");

      // Set modal title
      const caravanTitle = button
        .closest(".list-group-item")
        .querySelector("h2").textContent;
      modalTitle.textContent = `Leave a review for ${caravanTitle}`;

      // Set form action
      form.setAttribute("action", `/submit_review/${caravanId}/`);

      // Handle form submission via AJAX
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        fetch(form.getAttribute("action"), {
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
          body: formData,
        })
          .then(async (response) => {
            if (!response.ok) {
              const text = await response.text();
              throw new Error(text);
            }
            return response.json();
          })
          .then((data) => {
            // Close the modal and show success message
            const modalInstance = bootstrap.Modal.getInstance(modal);
            modalInstance.hide();
            alert(data.message);
            // Reload the page to show the new review
            location.reload();
          })
          .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred while submitting the review.");
          });
      });
    });
  });
}
