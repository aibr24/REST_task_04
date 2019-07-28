from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ["username", "password", "last_name", "first_name"]

	def create(self, validated_data):
		usr = validated_data["username"]
		password = validated_data["password"]
		last = validated_data["last_name"]
		first = validated_data["first_name"]
		user = User(username=usr, last_name=last, first_name=first)
		user.set_password(password)
		user.save()
		return validated_data