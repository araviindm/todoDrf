import pytz
from datetime import datetime

from rest_framework import serializers
from .models import Todo, Tag, StatusTypes


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'description', 'due_date', 'tags', 'status']


class TodoSerializer(serializers.ModelSerializer):
    local_timezone = pytz.timezone('Asia/Kolkata')
    time_stamp = serializers.DateTimeField(default=datetime.now(local_timezone), format='%Y-%m-%d %H:%M:%S')
    due_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    tags = TagSerializer(many=True, read_only=True)
    status = serializers.ChoiceField(choices=StatusTypes.choices, required=True)

    def validate(self, attrs):
        time_stamp = attrs.get('time_stamp')
        due_date = attrs.get('due_date')

        if 'time_stamp' in self.initial_data:
            raise serializers.ValidationError("Time stamp field is not allowed.")

        if time_stamp > due_date:
            raise serializers.ValidationError("Due date cannot be in the past.")

        return attrs

    class Meta:
        model = Todo
        fields = '__all__'
