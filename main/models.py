from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_entries")
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    lga =models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    PMV_name = models.CharField(max_length=255)
    geopoint = models.CharField(max_length=255)
    patientRecordAvailable = models.BooleanField(default=True)
    patientWithFebrileIllness = models.BooleanField(default=False)
    totalNoOfFeverCases = models.IntegerField()
    testToKnowCauseOfFever = models.BooleanField(default=True)
    typeOfTest = models.CharField(max_length=255)
    noOf5mRDTTestedFeverCases = models.IntegerField()
    noOfU5mRDTTestedFeverCases = models.IntegerField()
    noOf5mRDTTestedPositiveFeverCases = models.IntegerField()
    noOfU5mRDTTestedPositiveFeverCases = models.IntegerField()
    typeOfTreamentGivenToPositivePatient = models.CharField(max_length=255)
    typeOfTreamentGivenToFebrilePatientAndNotTested = models.CharField(max_length=255)
    IECMaterialAvailableOnDisplay = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title