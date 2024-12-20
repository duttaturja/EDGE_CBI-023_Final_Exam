# from django
from django.shortcuts import render

# from rest_framework
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

# from models
from Task.models import Task

# from serializers
from .serializers import TaskSerializer

class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(f"{serializer.data} Task Created Successfully", status=status.HTTP_201_CREATED)
        except:
            return Response(f"Failed to create task {serializer.error}", status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        try:
            task = Task.objects.get(id=pk)
            serializer = self.get_serializer(task, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(f"{serializer.data} Task Updated Successfully", status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response("Task not found",status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(f"Failed to update task {serializer.error}", status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):

        try:
            task = self.get_queryset.get(pk=pk)
            serializer = self.get_serializer(task, data=request.data)
            return Response({
            "code": "API_TASK_RETRIEVE_SUCCESS",
            "message": "Task retrieved successfully",
            "task": serializer.data
        }, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Failed to retrieve task."}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        try:
            task = self.get_queryset().get(pk=pk)
            task.delete()

            return Response({"Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Failed to delete task."}, status=status.HTTP_400_BAD_REQUEST)