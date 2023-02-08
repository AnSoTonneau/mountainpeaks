import databases
import ormar
import sqlalchemy
from config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


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


engine = sqlalchemy.create_engine(settings.db_url)
metadata.drop_all(engine)
metadata.create_all(engine)
