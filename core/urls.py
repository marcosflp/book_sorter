from django.urls import include, path
from rest_framework import routers

from core.api import BookSorterViewSet

router = routers.DefaultRouter()


router.register(r'sort_books', BookSorterViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
