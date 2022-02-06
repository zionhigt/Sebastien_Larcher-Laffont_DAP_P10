from django.db import models



class Comment(models.Model):

    desc = models.CharField(max_length=512)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    issue_id = models.ForeignKey('issues.Issue', on_delete=models.CASCADE, related_name='comment_issue')
    author_user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='comment_author')