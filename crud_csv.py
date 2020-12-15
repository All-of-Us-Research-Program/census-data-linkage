from time import time

from sqlalchemy import create_engine, Text
from sqlalchemy.orm import sessionmaker
from example_models import Base, CensusData, ParticipantData
from config import DATABASE_URI
import pandas as pd
import numpy as np

if __name__ == "__main__":
    t = time()

    # Create the database
    engine = create_engine(DATABASE_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:

        # set up census_data table
        file_name = "data_linkage.csv"
        df = pd.read_csv(file_name)

        # median household income bracketing
        conds = [df['b19013001'] < 10000,
                 (df['b19013001'] >= 10000) & (df['b19013001'] <= 14999),
                 (df['b19013001'] >= 15000) & (df['b19013001'] <= 24999),
                 (df['b19013001'] >= 25000) & (df['b19013001'] <= 34999),
                 (df['b19013001'] >= 35000) & (df['b19013001'] <= 44999),
                 (df['b19013001'] >= 50000) & (df['b19013001'] <= 74999),
                 (df['b19013001'] >= 75000) & (df['b19013001'] <= 99999),
                 (df['b19013001'] >= 100000) & (df['b19013001'] <= 149999),
                 (df['b19013001'] >= 150000) & (df['b19013001'] <= 199999),
                 df['b19013001'] >= 200000]

        choices = ['Less than $10,000',
                   '$10,000 to $14,999', '$15,000 to $24,999', '$25,000 to $34,999',
                   '$35,000 to $49,999', '$50,000 to $74,999', '$75,000 to $99,999', '$100,000 to $149,999',
                   '$150,000 to $199,999',
                   '$200,000 or more']

        arr = np.select(conds, choices, default='')
        df['b19013001'] = arr

        # median home value bracketing
        conds = [df['b25077001'] < 50000,
                 (df['b25077001'] >= 50000) & (df['b25077001'] <= 99999),
                 (df['b25077001'] >= 100000) & (df['b25077001'] <= 299999),
                 (df['b25077001'] >= 300000) & (df['b25077001'] <= 499999),
                 (df['b25077001'] >= 500000) & (df['b25077001'] <= 749999),
                 (df['b25077001'] >= 750000) & (df['b25077001'] <= 999999),
                 df['b25077001'] >= 1000000]

        choices = ['Less than $50,000',
                   '$50,000 to $99,999', '$100,000 to $299,999', '$300,000 to $499,999',
                   '$500,000 to $749,999', '$750,000 to $999,999', '$1,000,000 or more']

        arr = np.select(conds, choices, default='')
        df['b25077001'] = arr

        df.to_sql(con=engine, index=True, index_label='id', name=CensusData.__tablename__, if_exists='replace')

        # set up participant_data table
        file_name = "participants.csv"
        df = pd.read_csv(file_name)
        df.to_sql(con=engine, index=True, index_label='id', name=ParticipantData.__tablename__, if_exists='replace',
                  dtype={'geo_id': Text, 'b19013001': Text, 'b25077001': Text})

        s.commit()  # Attempt to commit all the records
    except:
        s.rollback()  # Rollback the changes on error
    finally:
        s.close()  # Close the connection
    print("Time elapsed: " + str(time() - t) + " s.")
