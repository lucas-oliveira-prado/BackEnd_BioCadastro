import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'mysql+pymysql://root:WWGugjrukXYKeRFkbStVAaBgXXPqBiOy@gondola.proxy.rlwy.net:27583/BioCadastro'
print("DATABASE_URL ->", DATABASE_URL)
# Criando engine e session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
