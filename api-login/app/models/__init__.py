from app import db

class IModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update(self):
        try:
            db.session.commit()
            return True
        except NameError:
            print(NameError)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()