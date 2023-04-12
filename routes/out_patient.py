from fastapi import APIRouter
from pydantic import BaseModel
from models import OutPatient
router = APIRouter(prefix="/out_patients")

# Store the Out_patient records in a dictionary for simplicity
outpatients = {}

# GET all Out_patients
@router.get("/Demo out_patients")
def get_out_patients():
    return outpatients

# GET a single Out_patient by ID
@router.get("/{out_patient_id}")
def get_out_patient(out_patient_id: int):
    if out_patient_id not in outpatients:
        raise HTTPException(status_code=404, detail="Out_patient not found")
    return outpatients[out_patient_id]

# POST a new Out_patient record
@router.post("")
def create_out_patient(out_patient: OutPatient):
    out_patient_id = len(outpatients) + 1
    outpatients[out_patient_id] = out_patient
    return out_patient_id

# PUT an existing Out_patient record by ID
@router.put("/{out_patient_id}")
def update_out_patient(out_patient_id: int, out_patient: OutPatient):
    if out_patient_id not in outpatients:
        raise HTTPException(status_code=404, detail="Out_patient not found")
    outpatients[out_patient_id] = out_patient
    return out_patient

# DELETE an Out_patient record by ID
@router.delete("/{out_patient_id}")
def delete_out_patient(out_patient_id: int):
    if out_patient_id not in outpatients:
        raise HTTPException(status_code=404, detail="Out_patient not found")
    del outpatients[out_patient_id]
    return {"message": "Out_patient deleted successfully"}
