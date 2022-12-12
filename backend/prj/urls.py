from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from logger.views.index import index
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Logger API",
        default_version="v1",
        description="""
        Documentation `ReDoc` view be found [here](/doc).
      """,
        contact=openapi.Contact(email="zzzkorn@yandex,ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^doc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("", index),
    path("admin/", admin.site.urls),
    path(
        "v1/",
        include(
            [
                path("logger/", include("logger.urls")),
            ]
        ),
    ),
]
