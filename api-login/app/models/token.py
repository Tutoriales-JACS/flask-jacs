from . import IModel, db


# token username
class Token(IModel):
    __tablename__ = 'token'
    token = db.Column(db.String(96), nullable=False)
    usuario_id = db.Column(db.Integer,  db.ForeignKey('usuario.id'))

    def __init__(self, usuario_id, token):
        self.usuario_id = usuario_id
        self.token = token

    @classmethod
    def get_by_user(cls,usuario_id):
        return cls.query.filter_by(usuario_id=usuario_id).first()

    @classmethod
    def get_by_token(cls,token):
        return cls.query.filter_by(token=token).first()
    