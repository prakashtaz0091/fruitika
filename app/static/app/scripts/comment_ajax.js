// const moment = require("moment");

$(document).ready(function () {
  $("#comment_submit").on("click", function (e) {
    e.preventDefault();

    const comment_message = $("#comment").val();
    $("#comment").val("");

    const blog_id = $("#blog_id").val();
    const base_url = window.location.origin;
    const csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    const user_id = $("#user_id").val();
    const default_profile_pic_url = $("#default_profile_pic").val();
    const total_comments = parseInt($("#comment-count").data("comment-count"));

    $.ajax({
      type: "POST",
      url: `${base_url}/comment/`,
      contentType: "application/json", // Set content type to JSON
      headers: {
        "X-CSRFToken": csrf_token, // Include CSRF token in the headers
      },
      data: JSON.stringify({
        user_id: user_id,
        blog_id: blog_id,
        comment_message: comment_message,
      }),
      dataType: "json",
      success: function (data) {
        $("#comment-count").data("comment-count", total_comments + 1);
        $("#comment-count").text(`${total_comments + 1} Comments`);

        //append comment to commentlist
        $("#comment-list").append(`
            
            <div class="single-comment-body">
                    <div class="comment-user-avater">
                        
                        <img src="${
                          data.comment_author_profile_pic ??
                          default_profile_pic_url
                        }" alt="no avatar" />
                        
                    </div>
                    <div class="comment-text-body">
                        <h4> ${
                          data.comment_author
                        } <span class="comment-date"> ${moment(
          data.comment_created_at
        ).fromNow()} </span> <a href="#">reply</a></h4>
                        <p>${data.comment_body}</p>
                    </div>
                    </div>
            
            
            `);
      },
      error: function (xhr, status, error) {
        console.log("Error: " + error);
      },
    });
  });
});
