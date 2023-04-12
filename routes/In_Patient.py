from fastapi import APIRouter
from pydantic import BaseModel
from models import InPatient
router = APIRouter(prefix="/in_patients")

# IN _ Patient Endpoint 

# mock data for demonstration purposes
in_patients = [
    InPatient(patient_id=1, name="Tony Stark", age="35", gender="Male", diagnosis="COVID-19",
              admission_date="2022-03-15", discharge_date="2022-03-25", doctor_id="1", hospital_id="1"),
    InPatient(patient_id=2, name="Jane Foster", age="21", gender="Female", diagnosis="Heart Attack",
              admission_date="2022-03-15", discharge_date="2022-03-25", doctor_id="1", hospital_id="1")
]


# Helper function to get in-patient by ID
def get_in_patient_by_id(in_patient_id):
    for in_patient in in_patients:
        if in_patient["id"] == in_patient_id:
            return in_patient
    return None

# Helper function to get index of in-patient by ID
def get_in_patient_index_by_id(in_patient_id):
    for i, in_patient in enumerate(in_patients):
        if in_patient["id"] == in_patient_id:
            return i
    return None

# In-patient endpoints

@router.get("/Demo in_patients")
def get_in_patients():
    return in_patients

@router.post("")
def create_in_patient(in_patient: dict):
    in_patient["id"] = len(in_patients) + 1
    in_patients.append(in_patient)
    return in_patient

@router.get("/{in_patient_id}")
def get_in_patient(in_patient_id: int):
    in_patient = get_in_patient_by_id(in_patient_id)
    if not in_patient:
        raise HTTPException(status_code=404, detail="In-patient not found")
    return in_patient

@router.put("/{in_patient_id}")
def update_in_patient(in_patient_id: int, in_patient: dict):
    in_patient_index = get_in_patient_index_by_id(in_patient_id)
    if in_patient_index is None:
        raise HTTPException(status_code=404, detail="In-patient not found")
    in_patient["id"] = in_patient_id
    in_patients[in_patient_index] = in_patient
    return in_patient

@router.delete("/{in_patient_id}")
def delete_in_patient(in_patient_id: int):
    in_patient_index = get_in_patient_index_by_id(in_patient_id)
    if in_patient_index is None:
        raise HTTPException(status_code=404, detail="In-patient not found")
    in_patients.pop(in_patient_index)
    return {"message": "In-patient deleted successfully"}