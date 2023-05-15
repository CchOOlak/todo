from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from core.models import Task, User
from core.serializers import UserSerializer

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500)
    description = serializers.CharField()
    author = UserSerializer(read_only=True)
    keywords = serializers.CharField()
    status = serializers.ChoiceField(choices=Task.status_enum)
    priority = serializers.ChoiceField(choices=Task.priority_enum)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'author', 'keywords', 'status', 'priority', 'created_at')
    
    def create(self, validated_data):
        author = self.context['request'].user
        return Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            author=author,
            keywords=validated_data['keywords'],
            status=validated_data['status'],
            priority=validated_data['priority'],
        )
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.keywords = validated_data.get('keywords', instance.keywords)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance
