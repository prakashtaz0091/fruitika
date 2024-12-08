def get_nested_comments(post):
    comments = post.comments.filter(parent=None).order_by('-created_at')

    def fetch_replies(comment):
        replies = comment.replies.all().order_by('-created_at')
        return [{"comment": reply, 
                 "total_replies": reply.replies.count(),
                 "replies": fetch_replies(reply)} for reply in replies]

    nested_comments = []
    for comment in comments:
        nested_comments.append({
            "comment": comment,
            'total_replies': comment.replies.count(),
            "replies": fetch_replies(comment)
        })

    return nested_comments
