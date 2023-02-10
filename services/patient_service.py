from daos.patient_dao import PatientDao

class PatientService:
    def __init__(self):
        self.patient_dao = PatientDao()

    def create_patient(self, patient_id, patient):
        return self.patient_dao.create_patient(patient_id, patient)
