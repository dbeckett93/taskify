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

    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    // Check if dark mode is enabled in local storage
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
        darkModeToggle.textContent = 'Light Mode';
    }

    darkModeToggle.addEventListener('click', function () {
        body.classList.toggle('dark-mode');
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
            darkModeToggle.textContent = 'Light Mode';
        } else {
            localStorage.setItem('darkMode', 'disabled');
            darkModeToggle.textContent = 'Dark Mode';
        }
    });
});