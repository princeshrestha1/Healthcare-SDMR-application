from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="SMDR Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="princeshrestha504@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = ([
    path('account/', include('account.urls')),
    path('appointment/', include('appointment.urls'))
], 'api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns)),
    path(
        '',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0),
        name='schema-swagger-ui'),
    path(
        'redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0),
        name='schema-redoc'),
    path('docs/', include_docs_urls(title='SMDR API Documentation'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
