from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return patients created by the logged-in user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach current user to the patient
        serializer.save(user=self.request.user)


class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Restrict patient access only to the owner
        return Patient.objects.filter(user=self.request.user)

