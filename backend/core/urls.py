from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    home,
    CompanyViewSet,
    DataSourceViewSet,
    EmissionRecordViewSet,
    AuditLogViewSet,
    update_record_status
)

router = DefaultRouter()

router.register('companies', CompanyViewSet)
router.register('sources', DataSourceViewSet)
router.register('records', EmissionRecordViewSet)
router.register('audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', home),

    path('api/', include(router.urls)),

    path(
        'api/records/<int:pk>/status/',
        update_record_status
    ),
]
