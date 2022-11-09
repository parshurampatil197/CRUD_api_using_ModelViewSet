from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter
from .views.Book_views import BookViewSet, AuthorViewSet

router = ExtendedDefaultRouter(trailing_slash=False)

router.register('book', BookViewSet)
router.register('author', AuthorViewSet)


urlpatterns = router.urls

# urlpatterns = [
#     path('', router.urls),
# ]
