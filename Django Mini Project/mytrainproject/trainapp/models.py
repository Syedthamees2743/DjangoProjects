from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile/")
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Train(models.Model):
    train_number = models.CharField(max_length=10)
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_seats = models.IntegerField()

    def __str__(self):
        return self.train_name


class Ticket(models.Model):
    passenger_name = models.CharField(max_length=100)

    travel_date = models.DateField()

    seat_number = models.CharField(max_length=10)

    class_type = models.CharField(
        choices=[('SL', 'Sleeper'), ('AC', 'AC'), ('CC', 'Chair Car'), ('2S', 'Second Sitting')],
        max_length=5,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.passenger_name
