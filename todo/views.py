from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @action(detail=False, methods=['post'])
    def bulk_complete(self, request):
        ids = request.data.get('ids', [])
        Task.objects.filter(id__in=ids).update(completed=True)
        return Response({"message": "Tasks completed"})
