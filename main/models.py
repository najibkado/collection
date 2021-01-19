from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    lga =models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    PMV_name = models.CharField(max_length=255)
    geopoint = models.CharField(max_length=255)
    patientRecordAvailable = models.BooleanField(default=True)
    patientWithFebrileIllness = models.BooleanField(default=False)
    totalNoOfFeverCases = models.CharField(max_length=255)
    testToKnowCauseOfFever = models.BooleanField(default=True)
    typeOfTest = models.CharField(max_length=255)
    noOf5mRDTTestedFeverCases = models.CharField(max_length=255)
    noOfU5mRDTTestedFeverCases = models.CharField(max_length=255)
    noOf5mRDTTestedPositiveFeverCases = models.CharField(max_length=255)
    noOfU5mRDTTestedPositiveFeverCases = models.CharField(max_length=255)
    typeOfTreamentGivenToPositivePatient = models.CharField(max_length=255)
    typeOfTreamentGivenToFebrilePatientAndNotTested = models.CharField(max_length=255)
    IECMaterialAvailableOnDisplay = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title