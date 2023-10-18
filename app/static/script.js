function confirmDeleteStudent(button) {
    var student_id = button.getAttribute('student-id');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete Student " + student_id + "?")) {
        fetch(`/delete_student/${student_id}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
          if(data.success == true) {
            window.location.reload( )
          } else {
            console.error("Error: " + data.error)
          }
        });
    }
}
