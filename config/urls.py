from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework import routers
from country.views import CountryModelViewSet, AdminCountryModelViewSet
from exchange.views import ExchangeModelViewSet, CoinModelViewSet, AdminCoinModelViewSet, AdminExchangeModelViewSet

router = routers.DefaultRouter()
admin_router = routers.DefaultRouter()

router.register(r'countries', CountryModelViewSet)
router.register(r'exchanges', ExchangeModelViewSet)
router.register(r'coins', CoinModelViewSet)

admin_router.register(r'exchanges', AdminExchangeModelViewSet)
admin_router.register(r'countries', AdminCountryModelViewSet)
admin_router.register(r'coins', AdminCoinModelViewSet)


urlpatterns = [
    path('admin/api/v1/', include(admin_router.urls), name="api_admin"),
    path('api/v1/', include(router.urls), name="api"),
    path('admin/api/v1/', include(admin_router.urls), name="api_admin"),

    path(r'api-auth/', include('rest_framework.urls')),

    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("namu.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
