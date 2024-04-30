from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    ACTIVE = 'ACTIVE'
    HOLD = 'HOLD'
    IN_PROGRESS = 'IN PROGRESS'
    COMPLETE = 'COMPLETE'
    ARCHIVE = 'ARCHIVE'
    INACTIVE = 'INACTIVE'
    Status = [
        (ACTIVE, 'Active'),
        (HOLD, 'Hold'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETE, 'Complete'),
        (ARCHIVE, 'archive'),
        (INACTIVE, 'Inactive'),
    ]
    status = models.CharField(
        max_length=255,
        choices=Status,
        default=ACTIVE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    description = models.TextField()
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
