// $(document).ready(function () {
//   const addClickHandler = $(".comment-replies").on("click", function (e) {
//     // console.log($(this).data("commentid")); // Use jQuery's .data() method
//     const comment_id = $(this).data("commentid");
//     const base_url = window.location.origin;
//     const default_profile_pic_url = $("#default_profile_pic").val();

//     $.ajax({
//       type: "get",
//       url: `${base_url}/replies/${comment_id}/`,
//       contentType: "application/json", // Set content type to JSON
//       dataType: "json",
//       success: function (data) {
//         console.log("success", data);

//         let repliesBox = [...document.querySelectorAll(".replies-box")].find(
//           (el) => el.dataset.commentid == comment_id
//         );

//         // repliesBox.innerHTML = "new";
//         data.replies.forEach((reply) => {
//           repliesBox.innerHTML += `
//                     <div class="single-comment-body">
//                         <div class="comment-user-avater">

//                             <img src="${
//                               reply.comment_author_profile_pic !== null
//                                 ? default_profile_pic_url
//                                 : default_profile_pic_url
//                             }" alt="No avatar" />
//                         </div>
//                         <div class="comment-text-body">
//                             <h4> ${
//                               reply.comment_author
//                             } <span class="comment-date"> ${moment(
//             reply.comment_created_at
//           ).fromNow()}  | <span class="comment-replies" data-commentid="${
//             reply.comment_id
//           }"> ${
//             reply.replies_count
//           } replies</span></span> <a href="#">reply</a></h4>
//                             <p>${reply.comment_body}</p>

//                             <div class="replies-box" data-commentid="${
//                               reply.comment_id
//                             }"></div>
//                         </div>
//                     </div>

//         `;
//         });
//       },
//       error: function (xhr, status, error) {
//         console.log("Error: " + error);
//       },
//     });
//   });
// });
$(document).ready(function () {
  // Attach the click event listener to the parent element
  $(document).on("click", ".comment-replies", function (e) {
    const comment_id = $(this).data("commentid");
    const base_url = window.location.origin;
    const default_profile_pic_url = $("#default_profile_pic").val();

    $.ajax({
      type: "get",
      url: `${base_url}/replies/${comment_id}/`,
      contentType: "application/json", // Set content type to JSON
      dataType: "json",
      success: function (data) {
        // console.log("success", data);

        let repliesBox = [...document.querySelectorAll(".replies-box")].find(
          (el) => el.dataset.commentid == comment_id
        );

        // Clear previous replies if needed
        // repliesBox.innerHTML = ""; // Uncomment if you want to clear previous replies

        data.replies.forEach((reply) => {
          repliesBox.innerHTML += `
          <hr/>
                      <div class="single-comment-body add-reply-border">
                          <div class="comment-user-avater">
                              <img src="${
                                reply.comment_author_profile_pic !== null
                                  ? reply.comment_author_profile_pic
                                  : default_profile_pic_url
                              }" alt="No avatar" />
                          </div>
                          <div class="comment-text-body">
                              <h4> ${
                                reply.comment_author
                              } <span class="comment-date"> ${moment(
            reply.comment_created_at
          ).fromNow()}  | <span class="comment-replies" data-commentid="${
            reply.comment_id
          }"> ${
            reply.replies_count
          } replies</span></span> <a href="#">reply</a></h4>
                              <p>${reply.comment_body}</p>
  
                              <div class="replies-box" data-commentid="${
                                reply.comment_id
                              }"></div>
                          </div>
                      </div>
          `;
        });

        // No need to repeat the event listener code here, as it's already handled by event delegation
      },
      error: function (xhr, status, error) {
        console.log("Error: " + error);
      },
    });
  });
});
