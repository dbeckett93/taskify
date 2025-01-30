document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggle-completion');
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            fetch(toggleButton.dataset.url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': toggleButton.dataset.csrf,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                const taskStatus = document.getElementById('task-status');
                if (data.completed) {
                    taskStatus.classList.remove('bg-warning');
                    taskStatus.classList.add('bg-success');
                    taskStatus.textContent = 'Completed';
                    toggleButton.textContent = 'Mark as Incomplete';
                } else {
                    taskStatus.classList.remove('bg-success');
                    taskStatus.classList.add('bg-warning');
                    taskStatus.textContent = 'Pending';
                    toggleButton.textContent = 'Mark as Complete';
                }
            });
        });
    }
});