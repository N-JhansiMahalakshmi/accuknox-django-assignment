from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('q1/',views.question1),
    path('q2/',views.question2),
    path('q3/',views.question3)
]