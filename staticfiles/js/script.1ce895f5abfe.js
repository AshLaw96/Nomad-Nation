// EDIT SECTION
document.addEventListener("DOMContentLoaded", function () {
    // Initialise calendar on Add Caravan page
    const calendarEl = document.getElementById("calendar");
    const hiddenInputEl = document.getElementById("available_dates");
    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            selectable: true,
            select: function (info) {
                let dates = hiddenInputEl.value ? JSON.parse(hiddenInputEl.value) : [];
                dates.push({ start_date: info.startStr, end_date: info.endStr });
                hiddenInputEl.value = JSON.stringify(dates);
            },
        });

        calendar.render();
    }

    // Dynamically initialise calendar in Edit Modals
    const editModals = document.querySelectorAll('.modal');
    editModals.forEach(modal => {
        modal.addEventListener('shown.bs.modal', function () {
            const modalCalendarEl = modal.querySelector('#calendar');
            const modalHiddenInputEl = modal.querySelector('#available_dates');

            if (modalCalendarEl && modalHiddenInputEl && !modalCalendarEl.classList.contains('initialised')) {
                const modalCalendar = new FullCalendar.Calendar(modalCalendarEl, {
                    initialView: 'dayGridMonth',
                    selectable: true,
                    select: function (info) {
                        let dates = hiddenInputEl.value ? JSON.parse(hiddenInputEl.value) : [];
                        dates.push({ start_date: info.startStr, end_date: info.endStr });
                        modalHiddenInputEl.value = JSON.stringify(dates);
                    },
                });
                modalCalendar.render();
                modalCalendarEl.classList.add('initialised');
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