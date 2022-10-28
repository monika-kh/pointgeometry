from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as gis_models
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.gis.db import models


# class Point(models.Model):
#     """
#     Model to define the location of the user.
#     """

#     point_string = models.CharField(
#         max_length=1000, default=None, blank=True, null=True
#     )
#     location = gis_models.PointField(
#         geography=True, spatial_index=True, blank=True, null=True
#     )

#     def __str__(self):
#         return self.point_string


class User(AbstractUser):
    """
    Extended user model with mentioned fields.
    """

    # location = models.ForeignKey(
    #     Point,
    #     related_name="location_point",
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE,
    # )
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, validators=[MinLengthValidator(10)]
    )
    home_address = models.TextField(max_length=500, blank=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    lon = models.CharField(max_length=20, null=True, blank=True)
    location = models.PointField(blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
