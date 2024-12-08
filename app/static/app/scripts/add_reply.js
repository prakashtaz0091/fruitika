const addReply = (commentId, event) => {
  // console.log(commentId);
  const replyForm =
    event.target.parentNode.parentNode.querySelector(".reply-form");
  const cancelButton =
    event.target.parentNode.parentNode.querySelector(".cancel-btn");
  replyForm.style.display = "block";
  const replyButton =
    event.target.parentNode.parentNode.querySelector(".reply-btn");

  replyForm.style.display = "block";
  cancelButton.style.display = "block";
  replyButton.style.display = "none";

  const csrf_token = replyForm.querySelector(
    'input[name="csrfmiddlewaretoken"]'
  ).value;

  // Add an event listener to the form's submit event
  replyForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent the default form submission behavior
    console.log("submited");

    // Prepare the form data
    const formData = new FormData(replyForm);

    // Send the AJAX request
    const xhr = new XMLHttpRequest();
    xhr.open("POST", `/reply/${commentId}/`, true);
    xhr.setRequestHeader("X-CSRFToken", csrf_token);

    xhr.onload = function () {
      if (xhr.status === 200) {
        console.log("Reply sent successfully!");
        // You can also update the UI here
      } else {
        console.error("Error sending reply:", xhr.statusText);
      }
    };
    xhr.send(formData);
  });
};

const hideReplyForm = (event) => {
  event.target.parentNode.parentNode.querySelector(
    ".reply-form"
  ).style.display = "none";
  const replyButton =
    event.target.parentNode.parentNode.querySelector(".reply-btn");

  replyButton.style.display = "block";

  const cancelButton =
    event.target.parentNode.parentNode.querySelector(".cancel-btn");
  cancelButton.style.display = "none";
};
