from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter
from .views.Book_views import BookViewSet

router = ExtendedDefaultRouter(trailing_slash=False)

router.register('book', BookViewSet)


urlpatterns = router.urls

# urlpatterns = [
#     path('', router.urls),
# ]
