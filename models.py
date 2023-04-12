from typing import Optional
from pydantic import BaseModel

class Doctor(BaseModel):
    id: Optional[int]
    name: str
    speciality: str
    location: str
    phone_number: Optional[str] = None
    email: Optional[str] = None

class Hospital(BaseModel):
    id: Optional[int]
    name: str
    location: str
    beds: str
    phone_number: Optional[str] = None
    email: Optional[str] = None

class History(BaseModel):
    id: Optional[int]
    patient_id: int
    doctor_id: int
    hospital_id: int
    diagnosis: str
    treatment: str
    date: str

class Patient(BaseModel):
    id: Optional[int]
    name: str
    age: int
    gender: str
    phone_number: Optional[str] = None
    email: Optional[str] = None

class InPatient(BaseModel):
    id: Optional[int]
    patient_id: int
    doctor_id: int
    hospital_id: int
    admission_date: str
    discharge_date: Optional[str] = None

class OutPatient(BaseModel):
    id: Optional[int]
    patient_id: int
    doctor_id: int
    hospital_id: int
    appointment_date: str
    duration: str
    name: str 
    age: int
    gender:str 
    diagnosis:str 

class Clinic(BaseModel):
    id: Optional[int]
    name: str
    location: str
    phone_number: Optional[str] = None
    email: Optional[str] = None