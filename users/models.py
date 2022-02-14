from django.db import models
from django.contrib.auth import get_user_model
from django.templatetags.static import static
from datetime import datetime

AuthUserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default='images/defaultUser - Copy.png')
    coins = models.PositiveIntegerField(default=0)
    last_comm = models.CharField(max_length=200, null=False, blank=False)
    timestamp = models.DateTimeField(blank=True, default=datetime.now())

    @property
    def image(self):
        if self.avatar:
            return self.avatar.url
        return static('images/defaultUser.png')

