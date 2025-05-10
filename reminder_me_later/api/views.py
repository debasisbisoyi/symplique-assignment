from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Reminder
# from .serializers import ReminderSerializer

# class ReminderListCreateAPIView(APIView):
#     def get(self, request):
#         reminders = Reminder.objects.all()
#         serializer = ReminderSerializer(reminders, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ReminderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)