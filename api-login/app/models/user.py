from . import IModel,db

#  Model Usuario Principal
class Usuario(IModel):
    __tablename__ = 'usuario'
    nombre = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(96), nullable=False)
    tokens = db.relationship('Token', backref='usuario')
    def __init__(self, nombre, password) :
        self.nombre = nombre
        self.password = password

    @classmethod
    def get_user_name(cls,nombre):
        return cls.query.filter_by(nombre=nombre).first()