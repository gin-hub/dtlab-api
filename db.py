from sqlalchemy import Boolean, create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session

Base = declarative_base()

class DB:

    _engine: Engine = None
    _session: Session = None

    @staticmethod
    def init(dsn: str) -> None:
        DB._engine = create_engine(dsn, echo=True)
        DB._session = sessionmaker(DB._engine)
        Base.metadata.create_all(DB._engine)

    @staticmethod
    def getSession() -> Session:
        return DB._session()

class Router(Base):
    __tablename__ = 'routers'

    id = Column(Integer, primary_key=True)
    hostname = Column(String)
    interfaces = relationship('Interface', back_populates='router', cascade='all, delete-orphan')

    def __repr__(self):
        return f'Router(id={self.id!r}, hostname={self.hostname!r})'

class Interface(Base):
    __tablename__ = 'interfaces'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    address = Column(String)
    netmask = Column(String)

    router_id = Column(Integer, ForeignKey('routers.id'), nullable=False)
    router = relationship('Router', back_populates='interfaces')

    activated = Column(Boolean)

    def __repr__(self):
        return f'Interface(id={self.id!r}, description={self.description!r}) address={self.address!r} netmask={self.netmask!r}) switch_id={self.switch_id!r}) activated={self.activated!r} '

class Switch(Base):
    __tablename__ = 'switches'

    id = Column(Integer, primary_key=True)
    hostname = Column(String)

    def __repr__(self):
        return f'Switch(id={self.id!r}, hostname={self.hostname!r})'
