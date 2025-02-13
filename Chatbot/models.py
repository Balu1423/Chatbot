from django.db import models

class ChatLog(models.Model):
    username = models.CharField(max_length=255)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatLog with {self.username} at {self.timestamp}"
