from django.db import models
from datetime import date
from django.urls import reverse

class AbstractHuman(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.fullname

    def get_age(self):
        age = date.today().year - self.birth_date.year
        return age


class Worker(AbstractHuman):
    work_position = models.CharField(max_length=20)
    work_experience = models.DateField()

    def __str__(self):
        return self.work_position
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('worker_detail', kwargs={'pk': self.id})


class Document(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    card_id = models.CharField(max_length=10)

    def __str__(self):
        return self.worker
    
    def save(self, *args, **kwargs):
        print(f'{self.worker.fullname} has been saved!')
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=15)
    members = models.ManyToManyField(Worker, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return self.worker


class Customer(AbstractHuman):
    address = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.address


class VIPClient(Customer):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def __str__(self):
        return self.vip_status_start