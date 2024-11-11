from rest_framework import routers
from .views import TasksViewSet

router = routers.DefaultRouter()
router.register('api/tasks', TasksViewSet, 'tasks')
urlpatterns = router.urls
