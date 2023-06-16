import pytz
from datetime import datetime

from rest_framework import serializers
from .models import Todo, StatusTypes


class MergeDuplicateStringsListField(serializers.ListField):
    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        # Removes the duplicate tags
        unique_values = list(set(value))
        return unique_values


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    local_timezone = pytz.timezone('Asia/Kolkata')
    time_stamp = serializers.DateTimeField(default=datetime.now(local_timezone), format='%Y-%m-%d %H:%M:%S')
    due_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False, allow_null=True)
    tags = MergeDuplicateStringsListField(child=serializers.CharField(), required=False, allow_null=True)
    status = serializers.ChoiceField(choices=StatusTypes.choices, required=True)

    def validate(self, attrs):
        time_stamp = attrs.get('time_stamp')
        due_date = attrs.get('due_date')

        if 'time_stamp' in self.initial_data:
            raise serializers.ValidationError("Time stamp field is not allowed.")

        if time_stamp is not None and due_date is not None and time_stamp > due_date:
            raise serializers.ValidationError("Due date cannot be in the past.")

        return attrs

    class Meta:
        model = Todo
        fields = ['id', 'time_stamp', 'title', 'description', 'due_date', 'tags', 'status']
