from django.urls import path

from .views import CustomObtainTokenPairView, RegisterView

# -------------------------------------------------

urlpatterns = [
    path('login/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='user_register'),
]
