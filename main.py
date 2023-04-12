from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from models import Doctor, Hospital, History, Patient, InPatient, OutPatient, Clinic
from routes.Doctor import router as doctorrouter 
from routes.Clinic import router as clinicrouter 
from routes.History import router as historyrouter
from routes.Hospital import router as hospitalrouter
from routes.In_Patient import router as in_patientrouter
from routes.out_patient import router as out_patentrouter
from routes.Patient import router as patientrouter

app = FastAPI()
app.include_router(doctorrouter)
app.include_router(clinicrouter)
app.include_router(historyrouter)
app.include_router(hospitalrouter)
app.include_router(in_patientrouter)
app.include_router(out_patentrouter)
app.include_router(patientrouter)