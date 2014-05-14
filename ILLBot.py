import praw

bot_username = ""
bot_password = ""
bot_useragest = ""

r = praw.Reddit(bot_useragest)
r.login(bot_username, bot_password)

subreddit = r.get_subreddit('uiuc')
subreddit_comments = subreddit.get_comments()

submission = r.get_submission(submission_id='11v36o')
flat_comments = praw.helpers.flatten_tree(submission.comments)
already_done = set()
for comment in flat_comments:
    if comment.body == "I-L-L" and comment.id not in already_done:
        comment.reply(' I-N-I!')
        already_done.add(comment.id)