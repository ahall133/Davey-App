from django.db import models

# Create your models here.
class Client(models.Model):
    client_first_name = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    client_street_number = models.IntegerField()
    client_street_name = models.CharField(max_length=100)
    client_city = models.CharField(max_length=100)
    client_state = models.CharField(max_length=100)
    client_zip_code = models.IntegerField()
    client_telephone = models.IntegerField()
    client_email = models.CharField(max_length=100)
    #insert 'arborist' foreignkey

class Ticket(models.Model):
    ticket_type = models.CharField(max_length=100)
    ticket_cost = models.IntegerField()
    ticket_season = models.CharField(max_length=100)
    ticket_content_image = models.ImageField()
    ticket_content = models.TextField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    
