from fastapi import APIRouter
from pydantic import BaseModel
from models import Hospital
router = APIRouter(prefix="/hospitals")

# Hospital Endpoints 

hospitals = [
    Hospital(name= "Hospital A", location= "City A", beds= 100,phone_number="5448954544848"),
    Hospital(name= "Hospital B", location= "City B", beds= 50,phone_number="1551515151151"),
]

# Retrieve a list of all hospitals
@router.get("/Demo hospitals")
def get_hospitals():
    return hospitals

# Retrieve details of a specific hospital
@router.get("/{hosp_id}")
def get_hospital(hosp_id: int):
    return hospitals.get(hosp_id)

# Create a new hospital
@router.post("")
def create_hospital(hospital: dict):
    new_id = max(hospitals.keys()) + 1
    hospitals[new_id] = hospital
    return hospital

# Update the details of a specific hospital
@router.put("/{hosp_id}")
def update_hospital(hosp_id: int, hospital: dict):
    if hosp_id in hospitals:
        hospitals[hosp_id] = hospital
        return {"message": "Hospital updated successfully"}
    else:
        return {"error": "Hospital not found"}

# Delete a specific hospital
@router.delete("/{hosp_id}")
def delete_hospital(hosp_id: int):
    if hosp_id in hospitals:
        del hospitals[hosp_id]
        return {"message": "Hospital deleted successfully"}
    else:
        return {"error": "Hospital not found"}