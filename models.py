import datetime
import ormar
from db import metadata,database
from typing import Optional

class MainMeta(ormar.ModelMeta):
    
    metadata = metadata
    database = database



class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id : int = ormar.Integer(primary_key= True)
    username : str = ormar.String(max_length = 50)






class Video(ormar.Model):
    class Meta(MainMeta):
        pass
        

    id: str = ormar.Integer(primary_key=True)
    title : str = ormar.String(max_length=49)
    description: str = ormar.String(max_length=400)
    file: str = ormar.String(max_length=1000)
    creted_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Optional[User] = ormar.ForeignKey(User)

