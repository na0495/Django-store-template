from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# ---------------------------------------------------------

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API Django E-Commerce",
        default_version="v1",
        description="This is a Django E-Commerce API service, it is used to manage products, categories and carts.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Redoc API's
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    # accounts API's
    path('accounts/', include('accounts.urls')),
    # store API's
    path('store/', include('store.urls')),
    # Admin
    path('admin/', admin.site.urls),
]
