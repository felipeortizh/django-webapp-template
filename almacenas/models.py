from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class FileUpload(models.Model):
    #user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to='ecocontainer82/')
    uploaded_at = models.DateTimeField(auto_now_add=True)