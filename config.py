from sqlalchemy import Column,create_engine,Integer,String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'th'
USERNAME = 'root'
PASSWORD = '123456'
# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(
    username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class Article(Base):
    __tablename__ = 'th'
    id = Column(Integer,primary_key=True,autoincrement=True)
    type=Column(str(255))
    title = Column(String(255))
    href=Column(String(255))
    time = Column(String(255))
    content=Column(String(20000))
#Base.metadata.create_all()

# for i in range(1,100):
#     title='t'+str(i)
#     content='c'+str(i)
#     article=Article(title=title,content=content)
#     session.add(article)
#     session.commit()

