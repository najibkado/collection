from rest_framework import serializers
from .models import Entry
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=2)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)


    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email already in use')})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'usermane': ('Username already in use')})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = [
            'id',
            'owner',
            'title',
            'state',
            'lga',
            'ward',
            'PMV_name',
            'geopoint',
            'patientRecordAvailable',
            'patientWithFebrileIllness',
            'totalNoOfFeverCases',
            'testToKnowCauseOfFever',
            'typeOfTest',
            'noOf5mRDTTestedFeverCases',
            'noOfU5mRDTTestedFeverCases',
            'noOf5mRDTTestedPositiveFeverCases',
            'noOfU5mRDTTestedPositiveFeverCases',
            'typeOfTreamentGivenToPositivePatient',
            'typeOfTreamentGivenToFebrilePatientAndNotTested',
            'IECMaterialAvailableOnDisplay',
            'date'
        ]

        
    # title = serializers.CharField(max_length=255)
    # state = serializers.CharField(max_length=255)
    # lga =serializers.CharField(max_length=255)
    # ward = serializers.CharField(max_length=255)
    # PMV_name = serializers.CharField(max_length=255)
    # geopoint = serializers.CharField(max_length=255)
    # patientRecordAvailable = serializers.BooleanField(default=True)
    # patientWithFebrileIllness = serializers.BooleanField(default=False)
    # totalNoOfFeverCases = serializers.CharField(max_length=255)
    # testToKnowCauseOfFever = serializers.BooleanField(default=True)
    # typeOfTest = serializers.CharField(max_length=255)
    # noOf5mRDTTestedFeverCases = serializers.CharField(max_length=255)
    # noOfU5mRDTTestedFeverCases = serializers.CharField(max_length=255)
    # noOf5mRDTTestedPositiveFeverCases = serializers.CharField(max_length=255)
    # noOfU5mRDTTestedPositiveFeverCases = serializers.CharField(max_length=255)
    # typeOfTreamentGivenToPositivePatient = serializers.CharField(max_length=255)
    # typeOfTreamentGivenToFebrilePatientAndNotTested = serializers.CharField(max_length=255)
    # IECMaterialAvailableOnDisplay = serializers.BooleanField(default=True)
    # date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Entry.objects.create(validated_data)

    # def update(self, instance, validated_data):

    #     instance.title = validated_data.get('title', instance.title)
    #     instance.state = validated_data.get('state', instance.state)
    #     instance.lga = validated_data.get('lga', instance.lga)
    #     instance.ward = validated_data.get('ward', instance.ward)
    #     instance.PMV_name = validated_data.get('PMV_name', instance.PMV_name)
    #     instance.geopoint = validated_data.get('geopoint', instance.geopoint)
    #     instance.patientRecordAvailable = validated_data.get('patientRecordAvailable', instance.patientRecordAvailable)
    #     instance.patientWithFebrileIllness = validated_data.get('patientWithFebrileIllness', instance.patientWithFebrileIllness)
    #     instance.totalNoOfFeverCases = validated_data.get('totalNoOfFeverCases', instance.totalNoOfFeverCases)
    #     instance.testToKnowCauseOfFever = validated_data.get('testToKnowCauseOfFever', instance.testToKnowCauseOfFever)
    #     instance.typeOfTest = validated_data.get('typeOfTest', instance.typeOfTest)
    #     instance.noOf5mRDTTestedFeverCases = validated_data.get('noOf5mRDTTestedFeverCases', instance.noOf5mRDTTestedFeverCases)
    #     instance.noOfU5mRDTTestedFeverCases = validated_data.get('noOfU5mRDTTestedFeverCases', instance.noOfU5mRDTTestedFeverCases)
    #     instance.noOf5mRDTTestedPositiveFeverCases = validated_data.get('noOf5mRDTTestedPositiveFeverCases', instance.noOf5mRDTTestedPositiveFeverCases)
    #     instance.noOfU5mRDTTestedPositiveFeverCases = validated_data.get('noOfU5mRDTTestedPositiveFeverCases', instance.noOfU5mRDTTestedPositiveFeverCases)
    #     instance.typeOfTreamentGivenToPositivePatient = validated_data.get('typeOfTreamentGivenToPositivePatient', instance.typeOfTreamentGivenToPositivePatient)
    #     instance.typeOfTreamentGivenToFebrilePatientAndNotTested = validated_data.get('typeOfTreamentGivenToFebrilePatientAndNotTested', instance.typeOfTreamentGivenToFebrilePatientAndNotTested)
    #     instance.IECMaterialAvailableOnDisplay = validated_data.get('IECMaterialAvailableOnDisplay', instance.IECMaterialAvailableOnDisplay)
    #     instance.date = validated_data.get('date', instance.date)

    #     instance.save()
    #     return instance

