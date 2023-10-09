from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import path
from . import views 
urlpatterns =[
      path('chat/', views.chat_page,name='chat'),
      path('get_user_details_settings_page/', views.get_user_details_settings_page,name='chat'),
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
      path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]