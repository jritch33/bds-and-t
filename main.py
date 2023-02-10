from typing import Union
from fastapi import FastAPI
from services.patient_service import PatientService
from resources.resources import Patient

patient_service = PatientService()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/patient/{patient_id}")
def create_patient(patient_id: int, patient: Patient):
    patient_json = patient.dict()
    return patient_service.create_patient(patient_id, patient_json)
    