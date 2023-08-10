from app.config.database import get_db, Base, engine
from app.models.models import User

db = get_db()

user_test = User('andres', 'andres.yanquen@hotmail.com', 'ayanquen')

Base.metadata.create_all(engine)

