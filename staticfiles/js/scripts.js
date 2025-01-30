document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('toggle-completion').addEventListener('click', function() {
        fetch("{% url 'task_toggle_completion' pk=task.pk %}", {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            const taskStatus = document.getElementById('task-status');
            const toggleButton = document.getElementById('toggle-completion');
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
});