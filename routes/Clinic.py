from fastapi import APIRouter
from pydantic import BaseModel
from models import Clinic
router = APIRouter(prefix="/clinics")

# Clinic Endpoints 

class Clinic:
    def __init__(self, clinic_id: int, name: str, location: str):
        self.clinic_id = clinic_id
        self.name = name
        self.location = location

# Demo Data 
clinics = [
    Clinic(clinic_id=1, name="Clinic A", location="New York"),
    Clinic(clinic_id=2, name="Clinic B", location="Los Angeles"),
    Clinic(clinic_id=3, name="Clinic C", location="Chicago")
]

@router.get("/Demo clinics")
def get_clinics():
    return clinics

@router.get("/{clinic_id}")
def get_clinic(clinic_id: int):
    for clinic in clinics:
        if clinic.clinic_id == clinic_id:
            return clinic
    raise HTTPException(status_code=404, detail="Clinic not found")

@router.post("")
def create_clinic(name: str, location: str):
    new_clinic_id = len(clinics) + 1
    new_clinic = Clinic(clinic_id=new_clinic_id, name=name, location=location)
    clinics.append(new_clinic)
    return new_clinic

@router.put("/{clinic_id}")
def update_clinic(clinic_id: int, name: str, location: str):
    for clinic in clinics:
        if clinic.clinic_id == clinic_id:
            clinic.name = name
            clinic.location = location
            return clinic
    raise HTTPException(status_code=404, detail="Clinic not found")

@router.delete("/{clinic_id}")
def delete_clinic(clinic_id: int):
    for clinic in clinics:
        if clinic.clinic_id == clinic_id:
            clinics.remove(clinic)
            return {"message": "Clinic deleted successfully"}
    raise HTTPException(status_code=404, detail="Clinic not found")