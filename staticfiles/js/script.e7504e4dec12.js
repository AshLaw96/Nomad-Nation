/* jshint esversion: 11, jquery: true */
/* global bootstrap */

let isAuthenticated = false;

document.addEventListener("DOMContentLoaded", () => {
  // Set authenticated status
  isAuthenticated = document.body.dataset.authenticated === "true";

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
  // Only check notifications if the user is authenticated
  if (isAuthenticated) {
    setInterval(checkNotifications, 30000);
    checkNotifications();
  }
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
/**
 * Attempts to parse a JSON string into a JavaScript object.
 * If the input is empty or invalid, returns an empty array.
 * Logs an error to the console if parsing fails.
 *
 * @param {string} input - The JSON string to be parsed.
 * @returns {Object|Array} - The parsed JavaScript object, or an empty array if parsing fails.
 */
function parseJSON(input) {
  try {
    return input.trim() ? JSON.parse(input) : [];
  } catch (e) {
    console.error("Error parsing JSON:", e);
    return [];
  }
}

// Remove duplicate dates
/**
 * Removes duplicate date objects from an array of date objects.
 * Compares both start_date and end_date to identify duplicates.
 *
 * @param {Array} dates - An array of date objects with `start_date` and `end_date` properties.
 * @returns {Array} - A new array with duplicates removed, retaining the first occurrence of each unique date pair.
 */
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
/**
 * Retrieves the value of a specific cookie by name.
 * This is typically used to get the CSRF token from the document's cookies.
 *
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} - The value of the cookie, or `null` if the cookie is not found.
 */
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
/**
 * Displays a success message in the app for 5 seconds.
 * The message is shown in the container with the ID "success-message-container".
 * After 5 seconds, the message is hidden automatically.
 *
 * @param {string} message - The success message to display.
 */
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
/**
 * Initializes the Select2 library on the amenities dropdown.
 * This provides a styled and enhanced select input with search functionality and placeholder.
 * If jQuery is not found, an error message is logged to the console.
 */
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
/**
 * Initializes the functionality for toggling the visibility of filter options
 * and automatically submitting the filter form when an amenity is selected.
 *
 * 1. Shows or hides the filter container when the "toggle-filters" button is clicked.
 * 2. Submits the filter form automatically when the amenities dropdown value is changed.
 */
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
/**
 * Initializes the page for adding a new caravan, including:
 * 1. **Calendar functionality** using FullCalendar to manage available dates (select, resize, drag events).
 * 2. **Multiple amenities** input functionality, allowing users to dynamically add new amenities to the form.
 * 3. **Form submission** to correctly submit newly added amenities as unique form fields.
 *
 * Features:
 * - Users can select, resize, and drag events on the calendar to define availability.
 * - Events on the calendar are stored in a hidden input field as JSON.
 * - The form is dynamically updated to handle added amenities before submission.
 */
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
        console.log("Event clicked:", info.event);
        let dates = parseJSON(hiddenInputEl.value);
        // Remove event from stored dates
        dates = dates.filter(
          (d) =>
            !(
              d.start_date === info.event.startStr &&
              d.end_date === info.event.endStr
            )
        );
        // Update hidden input
        hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
        // Remove event from calendar
        info.event.remove();
        calendar.refetchEvents();
      },
      events: parseJSON(hiddenInputEl.value),
    });
    calendar.render();
  }
}

// Initialise calendar on Edit Caravan page
/**
 * This function initializes the Edit Caravan page with:
 * 1. **Calendar functionality** to manage availability dates using FullCalendar.
 * 2. **Multiple amenities** input functionality, allowing users to dynamically add new amenities to the form.
 * 3. **Event handling** for selecting and removing available dates from the calendar.
 * 4. **Modal form functionality** for pre-populating data (like title, description, etc.) when editing a caravan.
 *
 * Features:
 * - Users can select or deselect date ranges on the calendar, with dates being stored in a hidden input field as JSON.
 * - When submitting the form, dynamically added amenities are handled and correctly submitted with unique names.
 * - An edit modal is populated with the caravan's existing details (like title, description, and price) when opened.
 * - The `amenities` field in the modal handles multiple selections, allowing users to toggle amenities.
 */
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

        // Check if the date range already exists
        let existingEventIndex = dates.findIndex(
          (d) => d.start_date === info.startStr && d.end_date === info.endStr
        );
        if (existingEventIndex === -1) {
          // Add new event if it doesn't exist
          dates.push({ start_date: info.startStr, end_date: info.endStr });
          hiddenInputEl.value = JSON.stringify(dates);

          calendar.addEvent({
            title: "Available",
            start: info.startStr,
            end: info.endStr,
            allDay: true,
          });
        } else {
          console.log("Date range already exists.");
        }
      },

      // Click on an event to remove it
      eventClick: function (info) {
        let dates = parseJSON(hiddenInputEl.value);

        // Filter out the clicked event
        dates = dates.filter(
          (d) =>
            !(
              d.start_date === info.event.startStr &&
              d.end_date === info.event.endStr
            )
        );
        // Update hidden input with new dates
        hiddenInputEl.value = JSON.stringify(dates);

        // Remove event from calendar
        info.event.remove();
      },
      // Load existing events
      events: parseJSON(hiddenInputEl.value),
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
/**
 * Initialises all carousel components on the page using Bootstrap's Carousel functionality.
 *
 * This function looks for all elements with the class `.carousel` and applies the Bootstrap
 * `Carousel` component to them. It disables the automatic sliding of items by setting
 * `interval` to `false`, meaning the carousel will not move automatically.
 *
 * It can be useful for pages with multiple carousels that need to be initialised.
 *
 * @function
 */
function initialiseCarousel() {
  const carousels = [];
  document.querySelectorAll(".carousel").forEach(function (carousel) {
    const instance = new bootstrap.Carousel(carousel, {
      interval: false,
    });
    carousels.push(instance);
  });

  // Pause all carousels
  carousels.forEach((carousel) => carousel.pause());
}

// Initialise image modal
/**
 * Initializes the image modal to display the selected carousel items when triggered.
 *
 * This function sets up an event listener for showing the image modal. When the modal is
 * triggered, it fetches the corresponding carousel (based on the data attribute of the button
 * that triggered the modal). It clones each carousel item and populates the modal's carousel
 * with the items, ensuring the first item is marked as active. It also sets the modal's title
 * to the title of the associated caravan.
 *
 * @function
 */
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
/**
 * Initialises the favourite icon functionality for each carousel item.
 *
 * This function sets up event listeners on all elements with the `favourite-icon` class. When
 * a user clicks on an icon, the function toggles the "favourite" state of the icon (using the
 * `favourite` class) and sends an update request to the server to mark the item as a favourite
 * or not. If the server request fails, the favourite state is reverted on the client side to
 * ensure the UI remains consistent.
 *
 * @function
 */
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
/**
 * Initialises the request booking form by displaying the booking card if a "Book Now" action
 * was previously triggered, and setting up a reset action for the booking form on submission.
 *
 * This function checks the local storage for a flag indicating whether the "Book Now" button
 * was clicked, and if so, it displays the booking card. Additionally, it listens for the
 * submission of the booking form and resets the form after a short delay.
 *
 * @function
 */
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
/**
 * Initialises the "Book Now" buttons by attaching click event listeners to them.
 * When a "Book Now" button is clicked, it stores the "Book Now" action flag and
 * the caravan's ID in localStorage.
 *
 * This function is used to track when a user clicks the "Book Now" button,
 * saving the necessary data (such as the caravan's ID) in localStorage for later use
 * (for example, to display the booking form on a different page or after a page reload).
 *
 * @function
 */
function initialiseBookingButton() {
  const bookNowBtn = document.querySelectorAll(".book-now-btn");
  bookNowBtn.forEach((button) => {
    button.addEventListener("click", function () {
      localStorage.setItem("bookNowClicked", true);
      localStorage.setItem("caravanId", this.getAttribute("data-caravan-id"));
    });
  });
}

// Initialise submit review modal
/**
 * Initialises the review modal by attaching event listeners to "Leave Review" buttons.
 * When a button is clicked, the corresponding review modal for the selected caravan is shown,
 * allowing the user to enter a rating and comment.
 *
 * This function is used to display a modal for users to submit their reviews for a specific caravan.
 * The correct modal is identified by the caravan's ID, and the modal inputs (rating and comment) are cleared
 * before the modal is displayed.
 *
 * @function
 */
function initialiseReviewModal() {
  const reviewButtons = document.querySelectorAll(".leave-review-btn");

  reviewButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const caravanId = this.getAttribute("data-caravan-id");

      // Find the correct modal for the caravan
      const modal = document.getElementById(`submitReviewModal${caravanId}`);
      if (!modal) {
        console.error(
          `Modal with ID #submitReviewModal${caravanId} not found.`
        );
        return;
      }

      console.log(`Found modal: #submitReviewModal${caravanId}`);

      // Select input fields
      const ratingInput = modal.querySelector(`#rating-${caravanId}`);
      const commentTextarea = modal.querySelector(`#comment-${caravanId}`);

      if (!ratingInput || !commentTextarea) {
        console.error("Rating input or comment textarea not found.");
        return;
      }

      // Clear previous values
      ratingInput.value = "";
      commentTextarea.value = "";

      console.log(`Opening modal: #submitReviewModal${caravanId}`);

      // Ensure Bootstrap Modal is correctly initialized
      try {
        const bootstrapModal = new bootstrap.Modal(modal);
        bootstrapModal.show();
      } catch (error) {
        console.error("Error initializing Bootstrap modal:", error);
      }
    });
  });
}

// Initialise edit review modal
/**
 * Initialises the edit review modal by attaching event listeners to "Edit Review" buttons.
 * When a button is clicked, the corresponding review modal is shown with pre-filled rating
 * and comment values, allowing the user to edit their review.
 *
 * This function is used to pre-populate the review modal with the current rating and comment
 * of a specific review. The correct modal is identified by the review ID, and the modal inputs
 * (rating and comment) are set to the values associated with the review.
 *
 * @function
 */
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
/**
 * Initialises the reply to review modal by attaching event listeners to "Reply" buttons.
 * When a button is clicked, the corresponding reply modal is shown with an empty textarea
 * allowing the user to submit a reply to the review.
 *
 * This function is used to open a modal where the user can reply to a specific review.
 * The modal is identified using the review ID, and the reply textarea is cleared
 * to allow the user to enter a new reply.
 *
 * @function
 */
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
/**
 * Initialises the edit reply modal by attaching event listeners to "Edit Reply" buttons.
 * When an "Edit Reply" button is clicked, the corresponding reply modal is shown,
 * and the existing reply text is populated into the textarea for editing.
 *
 * This function is used to open the modal for editing a specific reply.
 * The modal is identified using the reply ID, and the existing reply text is
 * loaded into the textarea to allow the user to modify it.
 *
 * @function
 */
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
/**
 * Initialises delete buttons for reviews and replies by attaching event listeners.
 * When a "Delete" button is clicked, the function prevents the default behavior
 * and calls the `handleDelete` function, passing the URL to perform the delete operation.
 *
 * This function is used to handle the deletion of reviews and replies. It attaches
 * event listeners to all "Delete" buttons for both reviews and replies, triggering
 * the deletion process when clicked.
 *
 * @function
 */
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
/**
 * Handles the delete request for reviews or replies by sending a POST request
 * to the provided URL and processing the server's response.
 *
 * This function sends a DELETE request to the server, using the Fetch API, and
 * expects a JSON response. If the deletion is successful, the page is reloaded.
 * If an error occurs during the deletion process, an error message is shown in the app.
 *
 * @param {string} url - The URL where the delete request is sent. Typically,
 *                       this will be a server endpoint for deleting a review or reply.
 *
 * @returns {void} - This function performs actions (sending a request and updating UI),
 *                   but does not return a value.
 */
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
/**
 * Initialises the functionality for saving the user's currency preference.
 *
 * This function listens for a click event on the "Save Changes" button, then
 * sends the form data (including the currency preference) to the server using
 * the Fetch API. If the server responds with a success status, the modal
 * is closed, prices on the page are updated according to the selected currency,
 * and the page is reloaded to reflect the changes. If there is an error,
 * an error message is shown to the user.
 *
 * @returns {void} - This function does not return any value but performs UI
 *                   updates, including closing the modal, updating prices,
 *                   and reloading the page upon success.
 */
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
/**
 * Updates the displayed prices on the page according to the selected currency.
 *
 * This function retrieves the original price for each element with the class `.price`,
 * then sends a request to the server to convert the price into the new currency.
 * The converted price is displayed in place of the original price, formatted
 * with the new currency symbol or code.
 *
 * @param {string} newCurrency - The currency to which the prices should be converted.
 *                               This could be a currency code like "USD", "EUR", etc.
 * @returns {void} - This function doesn't return any value, but it updates the
 *                   displayed price text content for each element on the page.
 */
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
/**
 * Updates the displayed prices on the page immediately after the page loads
 * according to the user's saved currency preference.
 *
 * This function retrieves the user's currency from a `data-user-currency`
 * attribute stored in the `body` element. If a currency is available, it calls
 * the `updatePrices` function to convert all prices on the page to the user's
 * preferred currency.
 *
 * @returns {void} - This function doesn't return a value, but it triggers
 *                   the dynamic update of prices based on the user's currency.
 */
function updatePricesOnLoad() {
  // Store user currency in body dataset in the template
  const userCurrency = document.body.dataset.userCurrency;
  if (userCurrency) {
    updatePrices(userCurrency);
  }
}

// Function to handle appearance change
/**
 * Initialises the appearance change functionality, allowing users to select
 * a theme (light or dark) and save their preference.
 *
 * When the user clicks the "save changes" button, the selected theme is
 * applied to the page and stored in a cookie. The function also sends the
 * preference data to the server, updating the user's settings.
 *
 * @returns {void} - This function doesn't return any value but triggers
 *                   the appearance change process on the page.
 */
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
/**
 * Applies the theme stored in the cookie to the page on load,
 * excluding the homepage and modals from the theme change.
 *
 * This function checks for a `theme` cookie and applies the corresponding
 * theme (light or dark) to the `body` element. It also ensures that modals
 * are not affected by the theme change.
 *
 * @returns {void} - This function doesn't return any value, but it updates
 *                   the appearance of the page based on the stored theme.
 */
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

// Function to check for new notifications
/**
 * Checks for new notifications and updates the notification count and icon.
 *
 * This function fetches the user's notifications from the server and updates
 * the notification count and icon on the page. If there are new notifications,
 * the count is displayed, and the icon is animated to draw attention.
 *
 * @returns {void} - This function doesn't return any value, but it updates
 *                   the notification count and icon based on the user's notifications.
 */
function checkNotifications() {
  if (!isAuthenticated) {
    // Skip fetching notifications if the user is not authenticated
    return;
  }

  fetch("/user_settings/get_notifications/")
    .then((response) => response.json())
    .then((data) => {
      console.log("Notifications:", data);
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
          const overview = document.createElement("strong");
          overview.classList.add("notification-type");
          // Add notification type
          overview.textContent = `${notification.type}: `;

          const message = document.createElement("span");
          message.classList.add("notification-message");
          // Add message content
          message.textContent = `${notification.message} (${notification.created_at})`;

          // Create a clickable link
          if (notification.link) {
            const link = document.createElement("a");
            link.href = notification.link;
            link.textContent = " View Details";
            link.classList.add("notification-link");
            // Add some spacing
            link.style.marginLeft = "5px";
            // Open in new tab
            link.target = "_blank";
            message.appendChild(link);
          }

          // Append elements to the paragraph
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
/**
 * Marks all notifications as read by sending a POST request to the server.
 *
 * This function sends a POST request to the server to mark all notifications
 * as read for the current user. It updates the notification count and icon
 * on the page, hiding the count and removing the animation from the icon.
 *
 * @returns {void} - This function doesn't return any value, but it marks
 *                   all notifications as read and updates the UI accordingly.
 */
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
/**
 * Initializes the payment details update process.
 *
 * This function sets up an event listener for the submit button in the payment
 * details update modal. When the button is clicked, it prevents the default
 * form submission, collects the form data, and sends it via a POST request to
 * update the payment details. If the update is successful, it hides the modal,
 * updates the displayed payment method information, and shows a success message.
 * In case of failure, it displays an error message.
 *
 * @returns {void} - This function does not return any value. It performs DOM
 *                   updates by sending a request to update payment details,
 *                   handling the response, and updating the UI.
 */
function initialisePaymentDetailsUpdate() {
  const saveBtn = document.querySelector(
    "#editPaymentDetailsModal button[type='submit']"
  );

  if (!saveBtn) {
    console.error("❌ Save button not found!");
    return;
  }
  console.log("✅ Save button found, adding event listener...");
  saveBtn.addEventListener("click", (event) => {
    event.preventDefault();
    console.log("🟡 Save button clicked!");
    const form = document.querySelector("#editPaymentDetailsModal form");
    if (!form) {
      console.error("❌ Form not found!");
      return;
    }
    console.log("✅ Form found, submitting");

    const formData = new FormData(form);
    console.log("📤 Sending form data:", Object.fromEntries(formData));
    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("📥 Response received:", data);
        if (data.success) {
          console.log("✅ Payment details updated successfully!");
          // Close the modal after a successful update
          setTimeout(() => {
            const modalElement = document.getElementById(
              "editPaymentDetailsModal"
            );
            const modal = bootstrap.Modal.getInstance(modalElement);
            modal.hide();
          }, 200); // 200ms delay

          // Update the displayed payment details dynamically
          updatePaymentDetails(
            data.payment_method,
            data.card_last_four,
            data.billing_address
          );

          // Show success message
          showInAppMessage("Payment details updated successfully.", "success");
        } else {
          console.error("❌ Error from server:", data.error);
          showInAppMessage(
            data.error || "An error occurred while updating payment details.",
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
/**
 * Dynamically updates the payment details on the page.
 *
 * This function updates the payment details container with the provided payment method,
 * the last four digits of the card, and the billing address.
 *
 * @param {string} paymentMethod - The payment method (e.g., "Visa", "MasterCard").
 * @param {string} cardLastFour - The last four digits of the card being used for payment.
 * @param {string} billingAddress - The billing address associated with the payment method.
 *
 * @returns {void} - This function does not return any value. It directly updates the DOM.
 */
function updatePaymentDetails(paymentMethod, cardLastFour, billingAddress) {
  console.log("🛠 Updating payment details in UI...");

  const paymentDetailsContainer = document.querySelector(
    ".card-body.text-white"
  );

  if (paymentDetailsContainer) {
    console.log("✅ Payment details container found!");

    paymentDetailsContainer.innerHTML = `
      <p><strong>${paymentMethod}:</strong> **** **** **** ${cardLastFour}</p>
      <p><strong>Billing Address:</strong> ${billingAddress}</p>
      <button type="button" class="btn btn-primary mt-3 btn-styles" data-bs-toggle="modal" data-bs-target="#editPaymentDetailsModal">
          Edit Payment Details
      </button>
    `;

    console.log("✅ UI updated successfully!");

    // Force a repaint
    paymentDetailsContainer.style.display = "none";
    void paymentDetailsContainer.offsetHeight; // Trigger reflow
    paymentDetailsContainer.style.display = "block";
  } else {
    console.error("❌ Payment details container not found!");
  }
}
