from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated



class DoctorListCreateView(generics.ListCreateAPIView):     
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach current user to the doctor
        serializer.save(user=self.request.user)

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

