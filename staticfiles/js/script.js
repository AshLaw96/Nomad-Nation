document.addEventListener("DOMContentLoaded", () => {
  initialiseAddCaravan();
  initialiseEditCaravan();
  initialiseCarousel();
  initialiseFilterToggle();
  initialiseSelect2();
  initialiseRequestBooking();
  initialiseBookingButton();
  initialiseImageModal();
  initialiseFavouriteIcons();
  initialiseReviewModal();
  initialiseEditReviewModal();
  initialiseReplyToReviewModal();
  initialiseEditReplyModal();
  initialiseDeleteReviewAndReply();
  initialiseCurrencyChange();
  updatePricesOnLoad();
  initialiseAppearanceChange();
  applyThemeFromCookie();
  initialisePaymentDetailsUpdate();
  // Check for notifications every 30 seconds
  setInterval(checkNotifications, 30000);
  checkNotifications();

  // Open modal when notification icon is clicked
  const notificationIcon = document.getElementById("notification-icon");
  if (notificationIcon) {
    notificationIcon.addEventListener("click", () => {
      const modal = new bootstrap.Modal(
        document.getElementById("notificationModal")
      );
      modal.show();
      // Mark notifications as read when opened
      markNotificationsAsRead();
    });
  }
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
function initialiseRequestBooking() {
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

// Initialise review modal
function initialiseReviewModal() {
  const reviewButtons = document.querySelectorAll(".leave-review-btn");
  reviewButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const caravanId = this.getAttribute("data-caravan-id");

      const modal = document.querySelector(`#submitReviewModal${caravanId}`);
      const ratingInput = modal.querySelector(`#rating`);
      const commentTextarea = modal.querySelector(`#comment`);

      ratingInput.value = "";
      commentTextarea.value = "";
    });
  });
}

// Initialise edit review modal
function initialiseEditReviewModal() {
  const editReviewButtons = document.querySelectorAll(".edit-review-btn");
  editReviewButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const reviewId = this.getAttribute("data-review-id");
      const rating = this.getAttribute("data-rating");
      const comment = this.getAttribute("data-comment");

      const modal = document.querySelector(`#editReviewModal${reviewId}`);
      const ratingInput = modal.querySelector(`#rating-${reviewId}`);
      const commentTextarea = modal.querySelector(`#comment-${reviewId}`);

      ratingInput.value = rating;
      commentTextarea.value = comment;
    });
  });
}

// Initialise reply to review modal
function initialiseReplyToReviewModal() {
  const replyButtons = document.querySelectorAll(".reply-btn");
  replyButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const reviewId = this.getAttribute("data-review-id");
      const modal = document.querySelector(`#replyModal${reviewId}`);
      const replyTextarea = modal.querySelector(`#reply`);
      replyTextarea.value = "";
    });
  });
}

// Initialise edit reply modal
function initialiseEditReplyModal() {
  const editReplyButtons = document.querySelectorAll(".edit-reply-btn");
  editReplyButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const replyId = this.getAttribute("data-reply-id");
      const replyText = this.getAttribute("data-reply-text");
      const modal = document.querySelector(`#editReplyModal${replyId}`);
      const replyTextarea = modal.querySelector(`#reply`);
      replyTextarea.value = replyText;
    });
  });
}

// Initialise delete review buttons
function initialiseDeleteReviewAndReply() {
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

// Handle saving currency preference
function initialiseCurrencyChange() {
  const saveBtn = document.getElementById("save-changes-btn");
  if (!saveBtn) return;

  saveBtn.addEventListener("click", (event) => {
    event.preventDefault();

    const form = document.getElementById("preferences-form");
    if (!form) return;

    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          const modal = document.getElementById("editPreferencesModal");
          const bootstrapModal = bootstrap.Modal.getInstance(modal);
          bootstrapModal.hide();

          // Update prices dynamically
          updatePrices(data.currency);

          showInAppMessage("Currency preference saved successfully.");

          setTimeout(() => {
            location.reload();
          }, 100);
        } else {
          showInAppMessage(
            "An error occurred while saving the currency preference."
          );
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        showInAppMessage(
          "An error occurred while saving the currency preference."
        );
      });
  });
}

// Function to update prices dynamically
function updatePrices(newCurrency) {
  document.querySelectorAll(".price").forEach((priceElement) => {
    const originalAmount = priceElement.dataset.amount;
    if (!originalAmount) return;

    fetch(
      `/listings/convert_price/?amount=${originalAmount}&currency=${newCurrency}`
    )
      .then((response) => response.json())
      .then((data) => {
        priceElement.textContent = `${data.converted_amount} ${newCurrency}`;
      })
      .catch((error) => {
        console.error("Error updating prices:", error);
      });
  });
}

// Ensure prices update immediately when loading the page
function updatePricesOnLoad() {
  // Store user currency in body dataset in the template
  const userCurrency = document.body.dataset.userCurrency;
  if (userCurrency) {
    updatePrices(userCurrency);
  }
}

// Function to handle appearance change
function initialiseAppearanceChange() {
  const appearanceSelect = document.getElementById("appearance");
  const saveBtn = document.getElementById("save-changes-btn");

  if (saveBtn && appearanceSelect) {
    saveBtn.addEventListener("click", function (event) {
      // Prevent form submission
      event.preventDefault();

      const newAppearance = appearanceSelect.value;

      const form = document.getElementById("preferences-form");

      if (form) {
        // Use FormData to send form data
        const formData = new FormData(form);

        fetch("/user_settings/edit_preferences/", {
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
          // Serialize form data
          body: new URLSearchParams(formData),
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.error) {
              console.error("Error:", data.error);
            } else {
              // Apply the new appearance theme
              document.body.classList.remove("light-theme", "dark-theme");
              document.body.classList.add(`${newAppearance}-theme`);

              // Store the theme preference in a cookie
              document.cookie = `theme=${newAppearance}; path=/`;

              // Update the preferences section with the new values
              document.getElementById("preferences-appearance").textContent =
                data.appearance;

              // Close the modal programmatically
              const modal = bootstrap.Modal.getInstance(
                document.getElementById("editPreferencesModal")
              );
              modal.hide();

              // Show a success message
              showInAppMessage(data.message);
            }
          })
          .catch((error) => {
            console.error("Error:", error);
            showInAppMessage(
              "An error occurred while changing the appearance."
            );
          });
      } else {
        console.error('Form with id "preferences-form" not found.');
      }
    });
  }
}

// Apply the theme from the cookie on page load if not the homepage
function applyThemeFromCookie() {
  const theme = getCookie("theme");
  const isHomepage = window.location.pathname === "/";

  // If the theme is set in the cookie, apply it
  if (theme && !isHomepage) {
    document.body.classList.remove("light-theme", "dark-theme");
    document.body.classList.add(`${theme}-theme`);

    // Exclude modal from theme change
    document.querySelectorAll(".modal").forEach((modal) => {
      modal.classList.remove("light-theme", "dark-theme");
    });
  }
}

function checkNotifications() {
  // Check if the user is logged in (you can use any condition here)
  const isLoggedIn = document.body.classList.contains("logged-in"); // Example condition

  if (!isLoggedIn) {
    console.log("User is not logged in. Skipping notification fetch.");
    return; // Exit the function if the user is not logged in
  }

  fetch("/user_settings/get_notifications/")
    .then((response) => response.json())
    .then((data) => {
      const notificationCount = document.getElementById("notification-count");
      const notificationIcon = document.getElementById("notification-icon");
      const notificationList = document.getElementById("notifications-list");

      if (data.count > 0) {
        notificationCount.textContent = data.count;
        notificationCount.style.display = "inline";
        notificationIcon.classList.add("flash", "shake");

        // Clear previous notifications and add new ones
        notificationList.innerHTML = "";

        data.notifications.forEach((notification) => {
          const p = document.createElement("p");

          // Create a brief overview of the notification
          const overview = document.createElement("span");
          overview.classList.add("notification-type");
          overview.textContent = `${notification.type}: `; // Add notification type

          const message = document.createElement("span");
          message.classList.add("notification-message");
          message.textContent = `${notification.message} (${notification.created_at})`; // Add message content

          // Append the overview and message to the paragraph
          p.appendChild(overview);
          p.appendChild(message);

          // Append the paragraph to the modal's notification list
          notificationList.appendChild(p);
        });
      } else {
        notificationCount.style.display = "none";
        notificationIcon.classList.remove("flash", "shake");
      }
    })
    .catch((error) => {
      console.error("Error fetching notifications:", error);
    });
}

// Function to mark notifications as read
function markNotificationsAsRead() {
  fetch("/user_settings/mark_notifications_read/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  })
    .then((response) => response.json())
    .then(() => {
      document.getElementById("notification-count").style.display = "none";
      document
        .getElementById("notification-icon")
        .classList.remove("flash", "shake");
    })
    .catch((error) =>
      console.error("Error marking notifications as read:", error)
    );
}

// Function to handle saving payment details
function initialisePaymentDetailsUpdate() {
  const saveBtn = document.querySelector(
    "#editPaymentDetailsModal button[type='submit']"
  );

  if (!saveBtn) return;

  saveBtn.addEventListener("click", (event) => {
    event.preventDefault();

    const form = document.querySelector("#editPaymentDetailsModal form");
    if (!form) return;

    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Close the modal
          const modalElement = document.getElementById(
            "editPaymentDetailsModal"
          );
          const modal = bootstrap.Modal.getInstance(modalElement);
          modal.hide();

          // Update the displayed payment details dynamically
          updatePaymentDetails(data.payment_method, data.card_last_four);

          showInAppMessage("Payment details updated successfully.", "success");
        } else {
          showInAppMessage(
            "An error occurred while updating payment details.",
            "error"
          );
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        showInAppMessage(
          "An error occurred while updating payment details.",
          "error"
        );
      });
  });
}

// Function to update payment details on the page dynamically
function updatePaymentDetails(paymentMethod, cardLastFour) {
  const paymentDetailsContainer = document.querySelector(
    ".card-body.text-white"
  );

  if (paymentDetailsContainer) {
    paymentDetailsContainer.innerHTML = `
          <p><strong>${paymentMethod}:</strong> **** **** **** ${cardLastFour}</p>
          <button type="button" class="btn btn-primary mt-3 btn-styles" data-bs-toggle="modal" data-bs-target="#editPaymentDetailsModal">
              Edit Payment Details
          </button>
      `;
  }
}
