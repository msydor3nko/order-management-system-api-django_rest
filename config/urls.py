from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Order Management System API",
        default_version="v1",
        description="A simple API for Order Management System",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('orders.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# TODO: add `path('api-auth/', include('rest_framework.urls'))` for user login
