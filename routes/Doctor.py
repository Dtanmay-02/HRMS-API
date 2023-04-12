from fastapi import APIRouter
from pydantic import BaseModel
from models import Doctor
router = APIRouter(prefix="/doctors")

# Doctor Endpoints
# This Is For Demonstration Purpose 
doctors = [
    Doctor(id=1, name='John Doe', speciality='Cardiology', location='New York', phone_number='121312524' ,email = 'thha@gmail.com'),
    Doctor(id=2, name='Jane Smith', speciality='Pediatrics', location='Los Angeles', phone_number='121312524' ,email = 'thha@gmail.com'),
    Doctor(id=3, name='Bob Brown', speciality='Dermatology', location='Chicago', phone_number='121312524' ,email = 'thha@gmail.com'),
]

# GET /doctors - Returns a list of all doctors
@router.get("/Demo doctors")
def read_doctors():
    return doctors

# GET /doctors/{doctor_id} - Returns the details of a specific doctor
@router.get("/{doctor_id}")
def read_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor
    return {"error": "Doctor not found"}

# POST /doctors - Creates a new doctor
@router.post("")
def create_doctor(doctor: Doctor):
    doctors.append(doctor)
    return doctor

# PUT /doctors/{doctor_id} - Updates the details of a specific doctor
@router.put("/{doctor_id}")
def update_doctor(doctor_id: int, doctor: Doctor):
    for i, d in enumerate(doctors):
        if d.id == doctor_id:
            doctors[i] = doctor
            return doctor
    return {"error": "Doctor not found"}

# DELETE /doctors/{doctor_id} - Deletes a specific doctor
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int):
    for i, doctor in enumerate(doctors):
        if doctor.id == doctor_id:
            doctors.pop(i)
            return {"message": "Doctor deleted successfully"}
    return {"error": "Doctor not found"}
