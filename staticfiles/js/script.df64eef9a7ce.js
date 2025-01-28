// EDIT SECTION
document.addEventListener("DOMContentLoaded", function () {
    console.log(window.FullCalendar); // Log FullCalendar to ensure it is loaded

    const initCalendar = (calendarEl, hiddenInputEl) => {
        // Check if FullCalendar is available before initialising
        if (window.FullCalendar && window.FullCalendar.Calendar) {
            const calendar = new FullCalendar.Calendar(calendarEl, {
                plugins: ['dayGrid', 'interaction'],
                initialView: 'dayGridMonth',
                selectable: true,
                select: function (info) {
                    // Collect and store selected dates in the hidden input
                    const dates = JSON.parse(hiddenInputEl.value || '[]');
                    dates.push({ start_date: info.startStr, end_date: info.endStr });
                    hiddenInputEl.value = JSON.stringify(dates);
                },
            });

            calendar.render();
        } else {
            console.error("FullCalendar is not defined or not loaded correctly.");
        }
    };

    // Initialise calendar on Add Caravan page
    const addPageCalendar = document.getElementById('calendar');
    if (addPageCalendar) {
        const addPageHiddenInput = document.getElementById('available_dates');
        initCalendar(addPageCalendar, addPageHiddenInput);
    }

    // Dynamically initialise calendar in each Edit Modal
    const editModals = document.querySelectorAll('.modal');
    editModals.forEach(modal => {
        modal.addEventListener('shown.bs.modal', function () {
            const calendarEl = modal.querySelector('#calendar');
            const hiddenInputEl = modal.querySelector('#available_dates');

            if (calendarEl && hiddenInputEl && !calendarEl.classList.contains('initialised')) {
                initCalendar(calendarEl, hiddenInputEl);
                // Prevent reinitialisation
                calendarEl.classList.add('initialised'); 
            }
        });
    });

    // Handle form submissions for editing caravans
    const forms = document.querySelectorAll('.edit-caravan-form');
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            const caravanId = form.getAttribute('data-id');
            const formData = new FormData(form);

            // Include available dates in the form data
            const availableDatesInput = form.querySelector('input[name="available_dates"]');
            if (availableDatesInput) {
                formData.append('available_dates', availableDatesInput.value);
            }

            // Submit the form using fetch
            fetch(`/listings/caravan/edit/${caravanId}/`, {
                method: 'POST',
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        alert(data.message);
                        // Refresh to show updates
                        location.reload(); 
                    } else {
                        alert('Error: ' + data.message);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});