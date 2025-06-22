from dataclasses import dataclass
from datetime import datetime as dtime


@dataclass
class Object:
    object_id: int
    classification: str
    continent: str
    country: str
    curator_approved: int
    dated: str
    department: str
    medium: str
    nationality: str
    object_name: str
    restricted: int
    rights_type: str
    role: str
    room: str
    style: str
    title: str

    def __str__(self):
        return f"id:{self.object_id} - {self.title}  {self.country}"

    def __hash__(self):
        return hash(self.object_id)
