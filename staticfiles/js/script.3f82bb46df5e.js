document.addEventListener("DOMContentLoaded", function () {
    initialiseAddCaravan();
    initialiseEditCaravan();
    initialiseDeleteCaravan();
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
    return dates.filter((value, index, self) =>
        index === self.findIndex((t) => (
            t.start_date === value.start_date && t.end_date === value.end_date
        ))
    );
}

// Initialise calendar on Add Caravan page
function initialiseAddCaravan() {
    const calendarEl = document.getElementById("calendar");
    const hiddenInputEl = document.getElementById("available_dates");

    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            selectable: true,
            editable: true,
            eventResizableFromStart: true,
            unselectAuto: false,
            select: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                let adjustedEnd = new Date(info.endStr);
                if (!dates.some(d => d.start_date === info.startStr && d.end_date === info.endStr)) {
                    dates.push({
                        start_date: info.startStr,
                        end_date: adjustedEnd.toISOString().split('T')[0]
                    });
                    hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
                    calendar.addEvent({
                        title: 'Available',
                        start: info.startStr,
                        end: info.endStr,
                        allDay: true
                    });
                }
                calendar.unselect();
            },
            eventDrop: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                let index = dates.findIndex(d => d.start_date === info.oldEvent.startStr);

                if (index !== -1) {
                    dates.splice(index, 1);
                    let adjustedEnd = new Date(info.event.endStr);
                    adjustedEnd.setDate(adjustedEnd.getDate() - 1);
                    dates.push({
                        start_date: info.event.startStr,
                        end_date: adjustedEnd.toISOString().split('T')[0]
                    });
                    hiddenInputEl.value = JSON.stringify(dates);
                }
            },
            eventResize: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                let index = dates.findIndex(d => d.start_date === info.event.startStr);

                if (index !== -1) {
                    let adjustedEnd = new Date(info.event.endStr);
                    adjustedEnd.setDate(adjustedEnd.getDate() - 1);
                    dates[index].end_date = adjustedEnd.toISOString().split('T')[0];
                    hiddenInputEl.value = JSON.stringify(removeDuplicates(dates));
                }
            },
            eventClick: function (info) {
                let dates = parseJSON(hiddenInputEl.value);
                dates = dates.filter(d => d.start_date !== info.event.startStr);
                hiddenInputEl.value = JSON.stringify(dates);
                info.event.remove();
            },
            events: parseJSON(hiddenInputEl.value)
        });
        calendar.render();
    }
}

// Dynamically initialise calendar in Edit Modals
function initialiseEditCaravan() {
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
            fetch(`/edit/${caravanId}/`, {
                method: 'POST',
                body: formData,
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    alert('Caravan updated successfully!');
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
}

// Handle caravan deletion
function initialiseDeleteCaravan() {
    const deleteButtons = document.querySelectorAll('.delete-caravan');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const caravanId = this.getAttribute('data-id');
            if (confirm('Are you sure you want to delete this caravan?')) {
                fetch(`/delete/${caravanId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                        'Content-Type': 'application/json'
                    },
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.success) {
                        document.getElementById(`caravan-${caravanId}`).remove();
                    } else {
                        alert('Error deleting caravan: ' + (data.error || 'Unknown error'));
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred. Please try again.');
                });
            }
        });
    });
}