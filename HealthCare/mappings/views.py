from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]


class MappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient__id=patient_id)

class MappingDestroyView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
