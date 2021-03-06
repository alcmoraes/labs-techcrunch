"""ckl_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from client import views
from feed.models import Feed 
from django.contrib import admin
from rest_framework import routers, filters, serializers, viewsets

# FeedSerializer class
class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ('url', 'category', 'title', 'excerpt', 'image', 
                  'author_name', 'author_avatar')

# FeedViewSet class
#
# Here we add 'category' as a filter at our API and register
# our viewset for Django
class FeedViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category',)
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()

router = routers.DefaultRouter()
router.register(r'feeds', FeedViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
