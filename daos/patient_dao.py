import json
import os

class PatientDao:
    def __init__(self):
        self.patient_file_path = os.getcwd()+ '/db/patients.json'
        self.patients = self.initialize_patients()

    def initialize_patients(self):
        with open(self.patient_file_path, 'r') as patient_fh:
            return json.load(patient_fh)

    def patient_extant(self, patient_id):
        return patient_id in self.patients

    def create_patient(self, patient_id, patient):
        if self.patient_extant(patient_id): return "Patient already exists"

        self.patients[patient_id] = patient

        with open(self.patient_file_path, 'w', encoding='utf-8') as patient_fh:
            json.dump(self.patients, patient_fh, ensure_ascii=False, indent=4)

        return self.patients[patient_id]