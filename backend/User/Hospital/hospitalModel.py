from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Hospital(Base):
    __tablename__ = "Hospital"
    idHospital = Column(Integer,primary_key = True)
    hospital_name = Column("hospital_name",String)
    location = Column("location",String)
    hospital_specialities = Column("hospital_specialities",String)
    number_of_doctors = Column("number_of_doctors",Integer)


    def __init__(self,hospital_name,location,hospital_specialities,number_of_doctors):
        self.hospital_name = hospital_name
        self.location = location
        self.hospital_specialities = hospital_specialities
        self.number_of_doctors = number_of_doctors
        