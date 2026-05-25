from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status

from .models import Company, DataSource, EmissionRecord, AuditLog
from .serializers import (
    CompanySerializer,
    DataSourceSerializer,
    EmissionRecordSerializer,
    AuditLogSerializer
)

@api_view(['GET'])
def home(request):
    return Response({
        "message": "Breathe ESG Backend Running"
    })


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class EmissionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmissionRecord.objects.all()
    serializer_class = EmissionRecordSerializer
class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all().order_by('-created_at')
    serializer_class = AuditLogSerializer


@api_view(['POST'])
def update_record_status(request, pk):
    try:
        record = EmissionRecord.objects.get(id=pk)
    except EmissionRecord.DoesNotExist:
        return Response(
            {"error": "Record not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if record.is_locked:
        return Response(
            {"error": "Approved audit record is locked"},
            status=status.HTTP_400_BAD_REQUEST
        )

    new_status = request.data.get("status")
    comment = request.data.get("comment", "")

    allowed_status = ["PENDING", "APPROVED", "REJECTED", "SUSPICIOUS", "FAILED"]

    if new_status not in allowed_status:
        return Response(
            {"error": "Invalid status"},
            status=status.HTTP_400_BAD_REQUEST
        )

    old_status = record.status

    record.status = new_status

    if new_status == "APPROVED":
        record.is_locked = True

    record.notes = comment
    record.save()

    AuditLog.objects.create(
        record=record,
        action="STATUS_UPDATE",
        old_status=old_status,
        new_status=new_status,
        comment=comment
    )

    return Response({
        "message": "Status updated successfully",
        "id": record.id,
        "old_status": old_status,
        "new_status": new_status,
        "locked": record.is_locked
    })

