from datetime import datetime
from pydantic import BaseModel
from typing import Union, List, Optional


class Identifier(BaseModel):
    use: Optional[str] = None
    type: Optional[str] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional[str] = None
    assigner: Optional[str] = None

class HumanName(BaseModel):
    use: Optional[str] = None
    text: Optional[str] = None
    family: Optional[str] = None
    given: List[str] = []
    prefix: List[str] = []
    suffix: List[str] = []
    period: Optional[str] = None

class ContactPoint(BaseModel):
    system: Optional[str] = None
    value: Optional[str] = None
    use: Optional[str] = None
    rank: Optional[int] = None
    period: Optional[str] = None

class Address(BaseModel):
    use: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    line: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    period: Optional[str] = None

class Coding(BaseModel):
    system: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None

class CodeableConcept(BaseModel):
    coding: List[Coding] = []
    text: Optional[str] = None

class Attachment(BaseModel):
    contentType: Optional[str] = None
    language: Optional[str ] = None
    data: Optional[str] = None
    url: Optional[str] = None
    size: Optional[int] = None
    hash: Optional[str] = None
    title: Optional[str] = None
    creation: Optional[str ] = None

class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    display: Optional[str] = None

class Period(BaseModel):
    start: datetime
    end: datetime

class Contact(BaseModel):
    relationship: List[CodeableConcept] = []
    name: HumanName
    telecom: List[ContactPoint] = []
    address: Address
    gender: str
    organization: Reference # Organization
    period: Period

class Communication(BaseModel):
    language: CodeableConcept
    preferred: Optional[bool] = None

class Link(BaseModel):
    other: Optional[str] = None
    type: Optional[str] = None

class Patient(BaseModel):
    resourceType: str
    identifier: List[Identifier] = []
    active: bool
    name: List[HumanName] = []
    telecom: List[ContactPoint] = []
    gender: str
    birthDate: str
    deceasedBoolean: Optional[bool] = None
    deceasedDateTime: Optional[str] = None
    address: List[Address] = []
    maritalStatus: CodeableConcept
    multipleBirthBoolean: Optional[bool] = None
    multipleBirthInteger: Optional[int] = None
    photo: List[Attachment] = []
    contact: List[Contact] = []
    communication: List[Communication] = []
    generalPractitioner: List[Reference] = [] # Organisatoin|Practitioner|PractitionerRole
    managingOrganization: List[Reference] = [] # Organization
    link: List[Link] = []