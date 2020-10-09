
from django.urls import path, include
from . import views

urlpatterns = [
    path('emp/', views.emp),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('show/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
