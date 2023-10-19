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

function editStudent(id, firstname, lastname, coursecode, yearlevel, gender) {
    window.location.href = `/edit_student?student_id=${id}&first_name=${firstname}&last_name=${lastname}&course_code=${coursecode}&year_level=${yearlevel}&gender=${gender}`;
}