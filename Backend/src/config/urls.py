from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/tickets/", include("tickets.urls")),
    path("api/inventory/", include("inventory.urls")),
    path("api/users/", include("users.urls")),
    path("api/knowledge/", include("knowledge.urls")),
]
