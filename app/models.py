from . import db

#users model definition
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    
    #for debugging users
    def __repr__(self) -> str:
        return '<User %r>' %self.username
    
    #relation with roles table, this column contains values from roles.id colun
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),unique=True)

    #to complete the relationship
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self) -> str:
        return '<User %r>' %self.name