### example_models.py ###

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

Base = declarative_base()


class CensusData(Base):
    __tablename__ = 'census_data'
    id = Column(Integer, primary_key=True)
    geo_id = Column(String)
    name = Column(String)
    b19013001 = Column(Integer)
    b19013001_moe = Column(Integer)
    b25077001 = Column(Integer)
    b25077001_moe = Column(Integer)

    def __repr__(self):
        return "<CensusData(geo_id='{}', name='{}', b19013001='{}', b19013001_moe='{}, b25077001='{}, " \
               "b25077001_moe='{})>" \
            .format(self.geo_id, self.name, self.b19013001, self.b19013001_moe, self.b25077001, self.b25077001_moe)


class ParticipantData(Base):
    __tablename__ = 'participant_data'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    geo_id = Column(Text)
    b19013001 = Column(Integer)
    b19013001_moe = Column(Integer)
    b25077001 = Column(Integer)
    b25077001_moe = Column(Integer)

    def __repr__(self):
        return "<ParticipantData(geo_id='{}', street='{}', city='{}', state='{}', zip='{}'," \
               "b19013001='{}', b19013001_moe='{}, b25077001='{}, " \
               "b25077001_moe='{})>" \
            .format(self.geo_id, self.name, self.street, self.city, self.state, self.zip,
                    self.b19013001, self.b19013001_moe, self.b25077001, self.b25077001_moe)
