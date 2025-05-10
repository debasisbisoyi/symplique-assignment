from rest_framework import serializers
from .models import Reminder
from datetime import date

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reminder
        fields='__all__'
        
    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("You cannot set a reminder in the past.")
        return value
