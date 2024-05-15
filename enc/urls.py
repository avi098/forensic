
from django.urls import path


from . import views

urlpatterns = [
    path('', views.encryption_demo, name='encryption_demo'),
    path('register/', views.register, name='register'),
    path('add_text_to_ipfs/', views.add_text_to_ipfs, name='add_text_to_ipfs'),
    path('get_text_from_ipfs/', views.get_text_from_ipfs, name='get_text_from_ipfs'),
    path('decrypted_data/', views.decrypt_all_data, name='decrypt_all_data'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    ]
