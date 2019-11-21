from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.OneToOneField(Address, models.CASCADE, related_name='client')


class Manager(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    salary = models.FloatField()
    email = models.EmailField()


class Employee(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    salary = models.FloatField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='employers')


class Progress(models.Model):
    name = models.CharField(max_length=255)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()


class Demand(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client = models.OneToOneField(Client, models.CASCADE)
    employee = models.OneToOneField(Employee, models.CASCADE)
    pizza = models.OneToOneField(Pizza, models.CASCADE)
    progress = models.OneToOneField(Progress, models.CASCADE)
