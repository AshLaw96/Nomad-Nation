document.addEventListener("DOMContentLoaded", function () {
    initialiseAddCaravan();
    // initialiseEditCaravan();
    // initialiseDeleteCaravan();
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