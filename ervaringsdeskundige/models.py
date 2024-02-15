from django.db import models

# Create your models here.

from django.db import models

class Gebruikers(models.Model):
    gebruiker_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=255)
    is_beheerder = models.BooleanField(default=False)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    geslacht = models.CharField(max_length=1, blank=True, null=True)  # M/V/X, etc.
    email = models.CharField(max_length=255)
    wachtwoord = models.CharField(max_length=255)
    telefoonnummer = models.CharField(max_length=15, blank=True, null=True)
    geboortedatum = models.DateField()

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"

class Beperkingen(models.Model):
    beperkingen_id = models.AutoField(primary_key=True)
    auditieve_beperkingen = models.TextField(blank=True, null=True)
    visuele_beperkingen = models.TextField(blank=True, null=True)
    motorische_lichamelijke_beperkingen = models.TextField(blank=True, null=True)
    cognitieve_neurologische_beperkingen = models.TextField(blank=True, null=True)
    reden_beperking = models.TextField(blank=True, null=True)

class Toezichthouder(models.Model):
    toezichthouder_id = models.AutoField(primary_key=True)
    naam = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    telefoonnummer = models.CharField(max_length=255, blank=True, null=True)

class Hulpmiddelen(models.Model):
    hulpmiddelen_id = models.AutoField(primary_key=True)
    vergrootglas = models.BooleanField(default=False)
    scherm_voorlezer = models.BooleanField(default=False)

class Ervaringsdeskundige(models.Model):
    ervaringsdeskundige_id = models.AutoField(primary_key=True)
    bijzonderheden = models.TextField(blank=True, null=True)
    voorkeur_benadering = models.CharField(max_length=255, blank=True, null=True)
    bijzonderheden_beschikbaar = models.CharField(max_length=255, blank=True, null=True)
    gebruikers = models.ForeignKey(Gebruikers, on_delete=models.CASCADE)
    beperkingen = models.ForeignKey(Beperkingen, on_delete=models.SET_NULL, null=True, blank=True)
    toezichthouder = models.ForeignKey(Toezichthouder, on_delete=models.SET_NULL, null=True, blank=True)
    hulpmiddelen = models.ForeignKey(Hulpmiddelen, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Ervaringsdeskundige ID: {self.ervaringsdeskundige_id}"
