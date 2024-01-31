from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class User(AbstractUser):
    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='diyora_user_groups'  # You can choose any related_name you prefer
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='diyora_user_permissions'  # You can choose any related_name you prefer
    )
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
