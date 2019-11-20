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
    address = models.ForeignKey(Address, models.CASCADE)

class Manager(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.IntegerField(max_length=11)
    salary = models.FloatField()
    email = models.EmailField()

class Employee(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.IntegerField(max_length=11)
    salary = models.FloatField()
    manager = models.ForeignKey(Manager, models.CASCADE)

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()

class Progress(models.Model):
    name = models.CharField(max_length=255)

class Demand(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, models.CASCADE)
    employee = models.ForeignKey(Employee, models.CASCADE)
    pizza = models.ForeignKey(Pizza, models.CASCADE)
    progress = models.ForeignKey(Progress, models.CASCADE)
