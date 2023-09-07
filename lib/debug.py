from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite///finalproject.db')
sessiion = sessionmaker(bind=engine)
session = Session()

import ipdb;ipdb.set_trace()