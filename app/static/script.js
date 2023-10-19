function confirmDeleteStudent(button) {
    var student_id = button.getAttribute('student-id');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete Student " + student_id + "?\nData is not retrievable.")) {
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

function confirmDeleteCourse(button) {
  var course_code= button.getAttribute('course-code');
  var csrfToken = button.getAttribute('csrf-token');
  if (confirm("Are you sure you want to delete " + course_code + "?\nStudents under this Course will also be deleted.")) {
      fetch(`/delete_course/${course_code}`, {
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