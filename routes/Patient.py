from fastapi import APIRouter
from pydantic import BaseModel
from models import Patient
router = APIRouter(prefix="/patients")

# Patient Endpoint 

# mock data for demonstration purposes
patients = [
    Patient(id= 1, name= "John Doe", age= 35, gender= "male", address= "123 Main St"),
    Patient(id= 2, name= "Jane Smith", age= 45, gender= "female", address= "456 Park Ave"),
    Patient(id= 3, name= "Bob Johnson", age= 50, gender= "male", address= "789 Elm St"),
]

# GET all patients
@router.get("/Demo patients")
def get_patients():
    return patients

# GET a patient by ID
@router.get("/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return {"error": "Patient not found"}

# POST a new patient
@router.post("")
def create_patient(patient: dict):
    patient["id"] = len(patients) + 1
    patients.append(patient)
    return patient

# PUT (update) an existing patient by ID
@router.put("/{patient_id}")
def update_patient(patient_id: int, patient: dict):
    for i, p in enumerate(patients):
        if p["id"] == patient_id:
            patients[i] = patient
            return patient
    return {"error": "Patient not found"}

# DELETE a patient by ID
@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    for i, patient in enumerate(patients):
        if patient["id"] == patient_id:
            patients.pop(i)
            return {"message": "Patient deleted successfully"}
    return {"error": "Patient not found"}