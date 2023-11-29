function confirmDeleteStudent(button) {
    var student_id = button.getAttribute('student-id');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete Student " + student_id + "?\n")) {
        fetch(`/delete_student/${student_id}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
          if(data.success == true) {
            window.location.reload( );
          } else {
            console.error("Error: " + data.error)
          }
        });
    }
}

function confirmDeleteCourse(button) {
  var course_code= button.getAttribute('course-code');
  var csrfToken = button.getAttribute('csrf-token');
  if (confirm("Are you sure you want to delete " + course_code + "?\nStudents under this Course will also be deleted.\n")) {
      fetch(`/delete_course/${course_code}`, {
          method: 'DELETE',
          headers: {
              'X-CSRFToken': csrfToken
          }
      }).then(response => response.json())
      .then(data => {
        if(data.success == true) {
          window.location.reload( );
        } else {
          console.error("Error: " + data.error)
        }
      });
  }
}

function confirmDeleteCollege(button) {
  var college_code= button.getAttribute('college-code');
  var csrfToken = button.getAttribute('csrf-token');
  if (confirm("Are you sure you want to delete " + college_code + "?\nStudents and Courses under this College will also be deleted.\n")) {
      fetch(`/delete_college/${college_code}`, {
          method: 'DELETE',
          headers: {
              'X-CSRFToken': csrfToken
          }
      }).then(response => response.json())
      .then(data => {
        if(data.success == true) {
          window.location.reload( );
        } else {
          console.error("Error: " + data.error)
        }
      });
  }
  
}

const fileInput = document.getElementById('file-input');
const fileButton = document.getElementById('file-button');
const imagePreview = document.getElementById('student_info_image');
const imageUrlInput = document.getElementById('image_url');
const imagePreviewContainer = document.getElementById('student_image_container')
const csrfToken = document.querySelector("meta[name=csrf_token]").content;

fileButton.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', async () => {
    try {
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);
        formData.append("csrf_token", csrfToken);
    
        imagePreviewContainer.innerHTML = '<div id="student_info_image"> <div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div> </div>';

        const response = await fetch("/upload/cloudinary/", {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (data && data.is_success) {

            const img = document.createElement("img");
            img.id = 'student_info_image';
            img.alt = "New Image Photo"
            img.src = data.url

            imagePreviewContainer.innerHTML = '';
            imagePreviewContainer.appendChild(img);
            
            imageUrlInput.value = data.url;
        } else {
            // Handle the case where the upload was not successful
            console.error("Upload failed:", data);
        }
    } catch (error) {
        console.error("An error occurred:", error);
    }
});