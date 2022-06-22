from flask import Blueprint,  request
from app.utils import authenticate, generate_hash
from app.schemas import TokenSchema, UserSchema
from .models.user import  Usuario
from .models.token import Token
from flask_restful import Api,Resource

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)


userSchema = UserSchema()
tokenSchema = TokenSchema()

class UserResource(Resource):
    def get(self):
        users = Usuario.query.all()
        body = userSchema.dump(users, many=True)
        return body
    
    def post(self):
        data = request.get_json()
        user_dict = userSchema.load(data)
        user = Usuario(**user_dict)
        if  user.save():
            return {'msg':'Guardado!!'}, 200
        else:
            return {'msg':'Guardado!!'}, 200

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        user_dict = userSchema.load(data)
        user = Usuario.get_user_name(user_dict['nombre'])
        
        if not user:
            return {'msg':'Usted no está  registrado!'},404
        resp = userSchema.dump(user)
        if user.password != user_dict['password']:
            return {'msg': 'Contraseña Incorrecta!!'}, 405
        
        token = Token.get_by_user(user.id)
        
        if not token:
            token = Token(
                usuario_id=user.id,
                token= generate_hash(user.nombre)
            )
            token.save()
        token_dp = tokenSchema.dump(token).pop('token')
        return {
            'user': resp,
            'token': token_dp
        }




class LogOutResource(Resource):
    method_decorators = [authenticate] 
    def post(self):
        token = Token.get_by_token(request.headers.get('Authorization'))
        token.delete()
        return {"msg":"Se cerró su session"}


api.add_resource(UserResource,'/user',endpoint='user_resource')
api.add_resource(LoginResource,'/login',endpoint='login_resource')
api.add_resource(LogOutResource,'/logout',endpoint='logout_resource')

