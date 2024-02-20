from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Organisaties(models.Model):
    organisatie_id = models.AutoField(primary_key=True)
    naam = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    beschrijving = models.TextField(blank=True, null=True)
    contactpersoon = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefoonnummer = models.CharField(max_length=20, blank=True, null=True)
    overige_details = models.TextField(blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'organisaties'


class GebruikersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Gebruikers moeten een e-mailadres hebben')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Gebruikers(AbstractBaseUser, PermissionsMixin):
    gebruiker_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=255)
    is_beheerder = models.BooleanField(default=False)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    geslacht = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefoonnummer = models.CharField(max_length=20, blank=True, null=True)
    geboortedatum = models.DateField()
    last_login = models.DateTimeField(blank=True, null=True)

    objects = GebruikersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'gebruikers'

    @property
    def is_staff(self):
        return self.is_beheerder

    def __str__(self):
        return self.email



class Hulpmiddelen(models.Model):
    hulpmiddelen_id = models.AutoField(primary_key=True)
    vergrootglas = models.BooleanField(default=False)
    scherm_voorlezer = models.BooleanField(default=False)

    class Meta:
        db_table = 'hulpmiddelen'


class Toezichthouder(models.Model):
    toezichthouder_id = models.AutoField(primary_key=True)
    naam = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telefoonnummer = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'toezichthouder'


class Beperkingen(models.Model):
    AUDITIEVE_BEPERKINGEN_CHOICES = [
        ('doof', 'Doof'),
        ('slechthorend', 'Slechthorend'),
        ('doofblind', 'Doofblind'),
    ]

    VISUELE_BEPERKINGEN_CHOICES = [
        ('blind', 'Blind'),
        ('slechtziend', 'Slechtziend'),
        ('kleurenblind', 'Kleurenblind'),
        ('doofblind', 'Doofblind'),
    ]

    MOTORISCHE_BEPERKINGEN_CHOICES = [
        ('amputatie', 'Amputatie en mismaaktheid'),
        ('artritus', 'Artritus'),
        ('fibromyalgie', 'Fibromyalgie'),
        ('reuma', 'Reuma'),
        ('handvaardigheid', 'Verminderde handvaardigheid'),
        ('spierdystrofie', 'Spierdystrofie'),
        ('rsi', 'RSI'),
        ('tremor', 'Tremor en Spasmen'),
        ('quadriplegie', 'Quadriplegie of tetraplegie'),
    ]

    COGNITIEVE_BEPERKINGEN_CHOICES = [
        ('adhd', 'ADHD'),
        ('autisme', 'Autisme'),
        ('leerstoornis', 'Leerstoornis'),
        ('geheugen', 'Geheugen beperking'),
        ('ms', 'Multiple Sclerose'),
        ('epilepsie', 'Epilepsie'),
        ('migraine', 'Migraine'),
    ]

    auditieve_beperkingen = models.CharField(max_length=50, choices=AUDITIEVE_BEPERKINGEN_CHOICES, blank=True, null=True)
    visuele_beperkingen = models.CharField(max_length=50, choices=VISUELE_BEPERKINGEN_CHOICES, blank=True, null=True)
    motorische_lichamelijke_beperkingen = models.CharField(max_length=50, choices=MOTORISCHE_BEPERKINGEN_CHOICES, blank=True, null=True)
    cognitieve_neurologische_beperkingen = models.CharField(max_length=50, choices=COGNITIEVE_BEPERKINGEN_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'beperkingen'


class Ervaringsdeskundige(models.Model):
    ervaringsdeskundige_id = models.AutoField(primary_key=True)
    bijzonderheden = models.TextField(blank=True, null=True)
    voorkeur_benadering = models.CharField(max_length=255, blank=True, null=True)
    bijzonderheden_beschikbaar = models.CharField(max_length=255, blank=True, null=True)
    gebruiker = models.ForeignKey(Gebruikers, on_delete=models.CASCADE)
    beperkingen = models.ForeignKey(Beperkingen, on_delete=models.SET_NULL, null=True, blank=True)
    toezichthouder = models.ForeignKey(Toezichthouder, on_delete=models.SET_NULL, null=True, blank=True)
    hulpmiddelen = models.ForeignKey(Hulpmiddelen, on_delete=models.SET_NULL, null=True, blank=True)
    is_goedgekeurd = models.BooleanField(default=False)

    class Meta:
        db_table = 'ervaringsdeskundige'


class Onderzoek(models.Model):
    onderzoek_id = models.AutoField(primary_key=True)
    titel = models.CharField(max_length=255)
    status = models.CharField(max_length=50, blank=True, null=True)
    beschikbaar = models.BooleanField(default=True)
    datum_vanaf = models.DateField(blank=True, null=True)
    datum_tot = models.DateField(blank=True, null=True)
    type_onderzoek = models.CharField(max_length=50, blank=True, null=True)
    locatie = models.CharField(max_length=255, blank=True, null=True)
    met_beloning = models.BooleanField(default=False)
    beloning = models.CharField(max_length=255, blank=True, null=True)
    doelgroep_leeftijd_van = models.IntegerField(blank=True, null=True)
    doelgroep_leeftijd_tot = models.IntegerField(blank=True, null=True)
    doelgroep_beperking = models.CharField(max_length=255, blank=True, null=True)
    organisatie = models.ForeignKey(Organisaties, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Onderzoek'


class OnderzoekErvaringsdeskundige(models.Model):
    onderzoek = models.ForeignKey(Onderzoek, on_delete=models.CASCADE)
    ervaringsdeskundige = models.ForeignKey(Ervaringsdeskundige, on_delete=models.CASCADE)
    is_goedgekeurd = models.BooleanField(default=False)

    class Meta:
        db_table = 'onderzoek_ervaringsdeskundige'
        unique_together = ('onderzoek', 'ervaringsdeskundige')

class Inschrijvingen(models.Model):
    naam = models.CharField(max_length=100)
    email = models.EmailField()
    inschrijvingsdatum = models.DateField(auto_now_add=True)
    is_goedgekeurd = models.BooleanField(default=False)

    def __str__(self):
        return self.naam



