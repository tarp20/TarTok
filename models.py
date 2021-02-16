import datetime
from ormar import Model,ModelMeta
from db import metadata,database
from typing import Optional

class MainMeta(ModelMeta):
    class Meta:
        metadata = metadata
        database = database



class User(Model):
    class Meta(MainMeta):
        pass

    id : int = ormar.Integer(primary_key= True)
    username : str = ormar.String(max_length = 50)






class Video(Model):
    class Meta(ModelMeta):
        pass
        

    id: str = ormar.Integer(primary_key=True)
    title : str = ormar.String(max_length=49)
    description: str = ormar.String(max_length=400)
    file: str = ormar.String(max_length=1000)
    creted_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Optional[User] = ormar.ForeignKey(User)

