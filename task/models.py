from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    Status = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=ACTIVE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=255)
    project = models.ForeignKey(
        'project.Project',
        related_name='projects',
        null=True,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        'tag.Tag',
        related_name='tags',
        null=True,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
