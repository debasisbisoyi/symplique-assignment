from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet

router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# from django.urls import path
# from .views import ReminderListCreateAPIView

# urlpatterns = [
#     path('reminders/', ReminderListCreateAPIView.as_view(), name='reminder-list-create'),
# ]