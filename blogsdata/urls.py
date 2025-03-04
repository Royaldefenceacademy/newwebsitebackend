# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('blogsData', BlogsDataViewSet)
router.register('homePageBlogsData', BlogsDataViewSet ,basename='blog-homepage')
router.register('blogslugs', BlogSlugViewSet , basename = 'blog-slugs')
router.register('allblogs', BlogsAllViewSet , basename = 'all-blog')

BlogsAllViewSet
urlpatterns = [
    path('', include(router.urls)), # Include all the URLs generated by the router
]
