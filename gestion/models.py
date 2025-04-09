from django.db import models

class Agence(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Assurance(models.Model):
    TYPE_CHOICES = [
        ('vie', 'Assurance Vie'),
        ('auto', 'Assurance Auto'),
        ('habitation', 'Assurance Habitation'),
    ]
    type_assurance = models.CharField(max_length=20, choices=TYPE_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_souscription = models.DateField()

    def __str__(self):
        return f"{self.type_assurance} - {self.client.nom}"