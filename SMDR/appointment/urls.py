from django.urls import path, include
from .routers import router
app_name = 'appointment'

urlpatterns = [
    path('', include(router.urls))

]
