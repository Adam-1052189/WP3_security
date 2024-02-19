from django.db import models
from django.contrib.auth.hashers import make_password

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


class Gebruikers(models.Model):
    gebruiker_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=255)
    is_beheerder = models.BooleanField(default=False)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    geslacht = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    wachtwoord = models.CharField(max_length=255)
    telefoonnummer = models.CharField(max_length=20, blank=True, null=True)
    geboortedatum = models.DateField()

    def set_password(self, raw_password):
        self.wachtwoord = make_password(raw_password)
    class Meta:
        db_table = 'gebruikers'


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
    beperkingen_id = models.AutoField(primary_key=True)
    auditieve_beperkingen = models.CharField(max_length=255, blank=True, null=True)
    visuele_beperkingen = models.CharField(max_length=255, blank=True, null=True)
    motorische_lichamelijke_beperkingen = models.CharField(max_length=255, blank=True, null=True)
    cognitieve_neurologische_beperkingen = models.CharField(max_length=255, blank=True, null=True)
    reden_beperking = models.TextField(blank=True, null=True)

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

    class Meta:
        db_table = 'onderzoek_ervaringsdeskundige'
        unique_together = ('onderzoek', 'ervaringsdeskundige')