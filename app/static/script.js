function confirmDeleteStudent(button) {
    var student_id = button.getAttribute('student-id');
    if (confirm("Are you sure you want to delete Student " + student_id + "?")) {
        fetch(`/delete_student/${student_id}`, {
            method: 'DELETE',
        })
        .then(() => window.location.reload())
    }
}
