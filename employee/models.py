from django.db import models


class Employee(models.Model):
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
    name = models.CharField(max_length=100)
    about = models.TextField()
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='employee')
    department = models.ForeignKey(
        'department.Department',
        related_name='departments',
        null=True,
        on_delete=models.CASCADE
    )
    designation = models.ForeignKey(
        'designation.Designation',
        related_name='designations',
        null=True,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
