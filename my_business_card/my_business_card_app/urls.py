from django.urls import path
from my_business_card_app import views

app_name = 'my_business_card_app'

urlpatterns = [
    path('other/', views.other, name='other'),
]
