# Generated by Django 3.0.8 on 2021-01-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('lga', models.CharField(max_length=255)),
                ('ward', models.CharField(max_length=255)),
                ('PMV_name', models.CharField(max_length=255)),
                ('geopoint', models.CharField(max_length=255)),
                ('patientRecordAvailable', models.BooleanField(default=True)),
                ('patientWithFebrileIllness', models.BooleanField(default=False)),
                ('totalNoOfFeverCases', models.IntegerField()),
                ('testToKnowCauseOfFever', models.BooleanField(default=True)),
                ('typeOfTest', models.CharField(max_length=255)),
                ('noOf5mRDTTestedFeverCases', models.IntegerField()),
                ('noOfU5mRDTTestedFeverCases', models.IntegerField()),
                ('noOf5mRDTTestedPositiveFeverCases', models.IntegerField()),
                ('noOfU5mRDTTestedPositiveFeverCases', models.IntegerField()),
                ('typeOfTreamentGivenToPositivePatient', models.CharField(max_length=255)),
                ('typeOfTreamentGivenToFebrilePatientAndNotTested', models.CharField(max_length=255)),
                ('IECMaterialAvailableOnDisplay', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
