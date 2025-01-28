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
    function removeDuplicates(dates) {
        return dates.filter((value, index, self) =>
            index === self.findIndex((t) => (
                t.start_date === value.start_date && t.end_date === value.end_date
            )) 
        );
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
                // Create Date object from endStr
                let adjustedEnd = new Date(info.endStr);
                // Check if the date range already exists
                if (!dates.some(d => d.start_date === info.startStr && d.end_date === info.endStr)) {
                    // Stores both start and end dates
                    dates.push({
                        start_date: info.startStr,
                        end_date: adjustedEnd.toISOString().split('T')[0]
                    });
                    hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
                    // Render the selection on the calendar
                    calendar.addEvent({
                        title: 'Available',
                        start: info.startStr,
                        end: info.endStr,
                        allDay: true
                    });
                    // Deselect to allow new selections
                }
                calendar.unselect();
            },
            // Handle event dragging (date change)
            eventDrop: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                // Find the index of the event that was dropped
                let index = dates.findIndex(d => d.start_date === info.oldEvent.startStr);

                if (index !== -1) {
                    // Remove the old event from the dates array
                    dates.splice(index, 1);
                    // Adjust end date
                    let adjustedEnd = new Date(info.event.endStr);
                    adjustedEnd.setDate(adjustedEnd.getDate() - 1);
                    // Add the updated date range to the array
                    dates.push({
                        start_date: info.event.startStr,
                        end_date: adjustedEnd.toISOString().split('T')[0]
                    });
                    // Update the hidden input with the new list of dates
                    hiddenInputEl.value = JSON.stringify(dates);
                }
            },
            // Handle event resizing (extend/reduce duration)
            eventResize: function (info) {
                let dates = parseJSON(hiddenInputEl.value);            
                // Find the index of the event that was resized
                let index = dates.findIndex(d => d.start_date === info.event.startStr);

                if (index !== -1) {
                    // Adjust the end date based on the new size
                    let adjustedEnd = new Date(info.event.endStr);
                    adjustedEnd.setDate(adjustedEnd.getDate() - 1);
                    // Update the end date for this event in the array
                    dates[index].end_date = adjustedEnd.toISOString().split('T')[0];
                    // Update the hidden input with the new list of dates
                    hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
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
            const caravanId = modal.getAttribute('id').replace('editModal', '');
            const modalCalendarEl = modal.querySelector(`#calendar${caravanId}`);
            const modalHiddenInputEl = modal.querySelector(`#available_dates${caravanId}`);

            if (modalCalendarEl && modalHiddenInputEl) {
                const dates = parseJSON(modalHiddenInputEl.value);
                const modalCalendar = new FullCalendar.Calendar(modalCalendarEl, {
                    initialView: 'dayGridMonth',
                    selectable: true,
                    // Allows selecting and modifying events
                    editable: true,
                    eventResizableFromStart: true,
                    events: dates.map(d => ({
                        title: 'Available',
                        start: d.start_date,
                        end: d.end_date,
                        allDay: true
                    })),
                    select: function (info) {
                        let updatedDates = parseJSON(modalHiddenInputEl.value);
                        if (!updatedDates.some(d => d.start_date === info.startStr && d.end_date === info.endStr)) {
                            updatedDates.push({
                                start_date: info.startStr,
                                end_date: info.endStr
                            });
                            modalHiddenInputEl.value = JSON.stringify(removeDuplicates(updatedDates));
                            modalCalendar.addEvent({
                                title: 'Available',
                                start: info.startStr,
                                end: info.endStr,
                                allDay: true
                            });
                        }
                        modalCalendar.unselect();
                    },
                    // Handle event deletion on click
                    eventClick: function (info) {
                        let updatedDates = parseJSON(modalHiddenInputEl.value);
                        updatedDates = updatedDates.filter(d => d.start_date !== info.event.startStr);
                        modalHiddenInputEl.value = JSON.stringify(updatedDates);
                        info.event.remove();
                    }
                });
                modalCalendar.render();
                modalCalendarEl.classList.add('initialised');
            }
        });
    });
    // Handle form submissions
    const forms = document.querySelectorAll('.edit-caravan-form');
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            const caravanId = form.getAttribute('data-id');
            if (!caravanId) {
                alert('Caravan ID is missing.');
                return;
            }
            form.querySelector('button[type="submit"]').innerText = "Saving...";
            const formData = new FormData(form);
            // Submit the form using fetch
            fetch(`/listings/caravan/edit/${caravanId}/`, {
                method: 'POST',
                body: formData,
            })
            .then((response) => response.json())
            .then(data => {
                if (data.success) {
                    alert('Caravan updated successfully!');
                    // Refresh to show updates
                    location.reload(); 
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong.');
            });
        });
    });
});