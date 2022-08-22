from django.urls import path, include
from account.viewsets.AuthManagement import LoginAPIView, RegisterUserView, GetProfile, VerifyDoctor, RegisterDoctorView

app_name = 'account'

urlpatterns = [
    path('doctor/register/', RegisterDoctorView.as_view()),
    path('user/register/', RegisterUserView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('get-profile/', GetProfile.as_view(), name='get_profile'),
    path('verify-doctor/', VerifyDoctor.as_view(), name='verify_doctor'),

]
