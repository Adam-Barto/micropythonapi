# If you’re paying attention and not just blindly copy-pasting, you’ll notice that we included 'booksapi.urls' .
# That’s a path to a file we haven’t edited yet. And that’s where Django is going to look next for instructions on
# how to route this URL.

# Yes I am aware of the irony of copying from the readme file.

# booksapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views # Okay now this is unexpected and welcome knowledge.

router = routers.DefaultRouter()
router.register(r'Books', views.BookViewSet)
# r means RAW String. Meaning '\' will be read as '\' without needing to do '\\'
# This is really helpful for Regex, just think, r for Regex.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]