// EDIT SECTION
document.addEventListener("DOMContentLoaded", function () {
    // Initialise calendar on Add Caravan page
    const calendarEl = document.getElementById("calendar");
    const hiddenInputEl = document.getElementById("available_dates");

    function parseJSON(input) {
        try {
            return input.trim() ? JSON.parse(input) : [];
        } catch (e) {
            console.error("Error parsing JSON:", e);
            return [];
        }
    }
    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            selectable: true,
            // Allows selecting and modifying events
            editable: true,
            eventResizableFromStart: true,
            // Prevents auto-unselecting
            unselectAuto: false,
            select: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                // Stores both start and end dates
                dates.push({
                    start_date: info.startStr,
                    end_date: info.endStr
                });
                hiddenInputEl.value = JSON.stringify(dates);
                // Render the selection on the calendar
                calendar.addEvent({
                    title: 'Available',
                    start: info.startStr,
                    end: info.endStr,
                    allDay: true
                });
                // Deselect to allow new selections
                calendar.unselect();
            },
            // Handle event dragging (date change)
            eventDrop: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                let index = dates.findIndex(d => d.start_date === info.oldEvent.startStr);

                if (index !== -1) {
                    dates[index].start_date = info.event.startStr;
                    dates[index].end_date = info.event.endStr;
                    hiddenInputEl.value = JSON.stringify(dates);
                }
            },
            // Handle event resizing (extend/reduce duration)
            eventResize: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                let index = dates.findIndex(d => d.start_date === info.event.startStr);

                if (index !== -1) {
                    dates[index].end_date = info.event.endStr;
                    hiddenInputEl.value = JSON.stringify(dates);
                }
            },
            // Handle event deletion on click
            eventClick: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                dates = dates.filter(d => d.start_date !== info.event.startStr);
                hiddenInputEl.value = JSON.stringify(dates);

                info.event.remove();
            },
            // Load previously stored dates
            events: parseJSON(hiddenInputEl.value)
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
                    // Allows selecting and modifying events
                    editable: true,
                    eventResizableFromStart: true,
                    // // Prevents auto-unselecting
                    unselectAuto: false,
                    select: function (info) {
                        let dates = parseJSON(modalHiddenInputEl.value);
                        // Add both start and end dates as an object
                        dates.push({
                            start_date: info.startStr,
                            end_date: info.endStr
                        });
                        modalHiddenInputEl.value = JSON.stringify(dates);
                        // Display selected date range on calendar
                        modalCalendar.addEvent({
                            title: 'Available',
                            start: info.startStr,
                            end: info.endStr,
                            allDay: true
                        });
                        modalCalendar.unselect();
                    },
                    // Handle event dragging (date change)
                    eventDrop: function (info) {
                        let dates = parseJSON(modalHiddenInputEl.value);
                        let index = dates.findIndex(d => d.start_date === info.oldEvent.startStr);

                        if (index !== -1) {
                            dates[index].start_date = info.event.startStr;
                            dates[index].end_date = info.event.endStr;
                            modalHiddenInputEl.value = JSON.stringify(dates);
                        }
                    },
                    // Handle event resising (extend/reduce duration)
                    eventResize: function (info) {
                        let dates = parseJSON(modalHiddenInputEl.value);
                        let index = dates.findIndex(d => d.start_date === info.event.startStr);

                        if (index !== -1) {
                            dates[index].end_date = info.event.endStr;
                            modalHiddenInputEl.value = JSON.stringify(dates);
                        }
                    },
                    // Handle event deletion on click
                    eventClick: function (info) {
                        let dates = parseJSON(modalHiddenInputEl.value);
                        dates = dates.filter(d => d.start_date !== info.event.startStr);
                        modalHiddenInputEl.value = JSON.stringify(dates);

                        info.event.remove();
                    },
                    events: parseJSON(modalHiddenInputEl.value)
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