from django.db import models


class Project(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    Status = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=ACTIVE
    )
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
