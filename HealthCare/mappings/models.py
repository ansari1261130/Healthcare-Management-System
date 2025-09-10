from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctors")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patients")
    assigned_at = models.DateTimeField(auto_now_add=True)
