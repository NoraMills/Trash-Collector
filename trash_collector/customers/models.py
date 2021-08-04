from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    class WeekDay(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True,
                             null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=5)
    weekly_pickup_day = models.IntegerField(default=0, choices=WeekDay.choices)
    onetime_pickup = models.DateField(null=True)
    start_supsension = models.DateField(null=True)
    end_supsension = models.DateField(null=True)
    balance = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.name
