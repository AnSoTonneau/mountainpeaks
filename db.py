import databases
import ormar
from config import settings
from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database
import logging

database = databases.Database(settings.db_url)
metadata = MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class MountainPeak(ormar.Model):
    """
    The model class for a MountainPeak representation :
    - id : Integer
    - name : String
    - lat : Float
    - lon : Float
    - altitude : Float
    """
    class Meta(BaseMeta):
        tablename = "mountainpeaks"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128, unique=True, nullable=False)
    lat: float = ormar.Float(default=0.0, nullable=False)
    lon: float = ormar.Float(default=0.0, nullable=False)
    altitude: float = ormar.Float(default=0.0, nullable=False)


engine = create_engine(settings.db_url)
if not database_exists(engine.url):  # Checks for the first time
    create_database(engine.url)  # Create new DB
    logging.info("New Database Created" + str(database_exists(engine.url)))  # Verifies if database is there or not.
else:
    logging.info("Database Already Exists")

metadata.drop_all(engine)
metadata.create_all(engine)
