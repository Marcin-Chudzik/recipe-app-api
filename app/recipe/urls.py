"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from . import views

VIEWSETS = [
    ('recipes', views.RecipeViewSet),
    ('tags', views.TagViewSet),
]

router = DefaultRouter()
for name, viewset in VIEWSETS:
    router.register(name, viewset)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
