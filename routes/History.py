from fastapi import APIRouter
from pydantic import BaseModel
from models import History
router = APIRouter(prefix="/histories")

# History Endpoint 

#  mock data for demonstration purposes
histories = [
    History(id="1",patient_id ="1234" ,doctor_id="2603"  ,hospital_id= "1" ,diagnosis="Fever"  , treatment= "special treatment" ,date="01/01/1998" ),
    History(id="2",patient_id ="1235" ,doctor_id="1206" ,hospital_id= "2" ,diagnosis= "Cold", treatment= "special treatment" ,date= "02/02/1998"),
]

# Retrieve a list of all medical histories
@router.get("/Demo histories")
def get_histories():
    return histories

# Retrieve details of a specific medical history
@router.get("/{hist_id}")
def get_history(hist_id: int):
    return histories.get(hist_id)

# Create a new medical history
@router.post("")
def create_history(history: dict):
    new_id = max(histories.keys()) + 1
    histories[new_id] = history
    return history

# Update the details of a specific medical history
@router.put("/{hist_id}")
def update_history(hist_id: int, history: dict):
    if hist_id in histories:
        histories[hist_id] = history
        return {"message": "Medical history updated successfully"}
    else:
        return {"error": "Medical history not found"}

# Delete a specific medical history
@router.delete("/{hist_id}")
def delete_history(hist_id: int):
    if hist_id in histories:
        del histories[hist_id]
        return {"message": "Medical history deleted successfully"}
    else:
        return {"error": "Medical history not found"}