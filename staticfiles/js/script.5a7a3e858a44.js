// Edit caravan section
document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll('.edit-caravan-form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const caravanId = form.getAttribute('data-id');
            const formData = new FormData(form);

            fetch(`/listings/caravan/edit/${caravanId}/`, {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    location.reload(); // Reload to reflect changes
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