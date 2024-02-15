# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Onderzoek(models.Model):
    onderzoek_id = models.AutoField(primary_key=True)
    titel = models.CharField(max_length=255)
    status = models.TextField(blank=True, null=True)
    beschikbaar = models.BooleanField(blank=True, null=True)
    datum_vanaf = models.DateField(db_column='datum vanaf', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    datum_tot = models.DateField(db_column='datum tot', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    type_onderzoek = models.TextField(db_column='type onderzoek', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    locatie = models.TextField(blank=True, null=True)
    met_beloning = models.BooleanField(db_column='met beloning', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beloning = models.TextField(blank=True, null=True)
    doelgroep_leeftijd_van = models.TextField(db_column='doelgroep leeftijd van', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    doelgroep_leeftijd_tot = models.TextField(db_column='doelgroep leeftijd tot', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    doelgroep_beperking = models.TextField(db_column='doelgroep beperking', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    organisatie = models.ForeignKey('Organisaties', on_delete=models.CASCADE)

    class Meta:
        db_table = 'onderzoek'
        managed = True


class Beperkingen(models.Model):
    beperkingen_id = models.AutoField(primary_key=True)
    auditieve_beperkingen = models.TextField(db_column='auditieve beperkingen', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    visuele_beperkingen = models.TextField(db_column='visuele beperkingen', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    motorische_lichamelijke_beperkingen = models.TextField(db_column='motorische / lichamelijke beperkingen', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cognitieve_neurologische_beperkingen = models.TextField(db_column='cognitieve / neurologische beperkingen', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reden_beperking = models.TextField(db_column='reden beperking', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'beperkingen'


class Ervaringsdeskundige(models.Model):
    ervaringsdeskundige_id = models.AutoField(primary_key=True)
    bijzonderheden = models.TextField(blank=True, null=True)
    voorkeur_benadering = models.TextField(db_column='voorkeur benadering', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bijzonderheden_beschikbaar = models.TextField(db_column='bijzonderheden beschikbaar', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gebruikers_gebruiker = models.ForeignKey('Gebruikers', models.DO_NOTHING)
    beperkingen_beperkingen = models.ForeignKey(Beperkingen, models.DO_NOTHING, blank=True, null=True)
    toezichhouder_toezichthouder = models.ForeignKey('Toezichhouder', models.DO_NOTHING, blank=True, null=True)
    hulpmiddelen_hulpmiddelen = models.ForeignKey('Hulpmiddelen', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ervaringsdeskundige'


class Gebruikers(models.Model):
    gebruiker_id = models.AutoField(primary_key=True)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=255)
    is_beheerder = models.IntegerField()
    postcode = models.TextField(blank=True, null=True)
    geslacht = models.TextField(blank=True, null=True)
    email = models.TextField()
    wachtwoord = models.CharField()
    telefoonnummer = models.CharField(blank=True, null=True)  # This field type is a guess.
    geboortedatum = models.TextField()

    class Meta:
        db_table = 'gebruikers'
        managed = True


class Hulpmiddelen(models.Model):
    hulpmiddelen_id = models.AutoField(primary_key=True)
    vergrootglas = models.IntegerField(blank=True, null=True)
    scherm_voorlezer = models.IntegerField(db_column='scherm voorlezer', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'hulpmiddelen'


class OnderzoekErvaringsdeskundige(models.Model):
    onderzoek = models.OneToOneField(Onderzoek, models.DO_NOTHING, primary_key=True)  # The composite primary key (onderzoek_id, ervaringsdeskundige_id) found, that is not supported. The first column is selected.
    ervaringsdeskundige = models.ForeignKey(Ervaringsdeskundige, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'onderzoek_ervaringsdeskundige'


class Organisaties(models.Model):
    organisatie_id = models.AutoField(primary_key=True)
    naam = models.TextField()
    type = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    beschrijving = models.TextField(blank=True, null=True)
    contactpersoon = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    telefoonnummer = models.CharField(blank=True, null=True)  # This field type is a guess.
    overige_details = models.TextField(db_column='overige details', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    api_key = models.TextField(db_column='api key', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'organisaties'


class Toezichhouder(models.Model):
    toezichthouder_id = models.AutoField(primary_key=True)
    naam = models.TextField()
    email = models.TextField(blank=True, null=True)
    telefoonnummer = models.CharField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'toezichhouder'