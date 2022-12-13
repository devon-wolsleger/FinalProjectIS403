from django.urls import path
from .views import IndexViewPage, LoginPage, TenantInfoPage, AddTenant, EditTenant, DeleteTenant,UpdateTenant


urlpatterns = [
    path("", IndexViewPage, name = "index"),
    path("tenants/", TenantInfoPage, name = "tenants"),
    path("contact/", LoginPage, name = "contact"),
    path("addTenant/", AddTenant, name = "addTenant"),
    path("editTenant/<int:id>/", EditTenant, name = "showTenant"),
    path("updateTenant/<int:id>/", UpdateTenant, name = "updateTenant"),
    path("deleteTenant/<int:id>/", DeleteTenant, name = "deleteTenant")
]   