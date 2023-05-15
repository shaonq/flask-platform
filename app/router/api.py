from flask import Blueprint, jsonify,request
from sqlalchemy import text
from model.database import db
from model.user import User
from model.jwt  import jwt_required ,generate_tokens

router_api = Blueprint('api', __name__)

# CORS headers
def cors_after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
            # response.headers['Authorization'] = ''
    return response

# Test  Token
@router_api.after_request
def token_after_request(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    # 模拟添加token
   # response.headers['Authorization'] =  ''
    return response

@router_api.route('/api')
def api():
    return jsonify({
        "code": 200,
        "message": "success"
    })


@router_api.route('/api/jwt')
@jwt_required
def jwt(payload):
    return jsonify({
        "code": 200,
        "data":{"uid":payload['sub']},
        "message":'success',
    })


@router_api.route('/api/users')
def db_query():
    try: 
        # db.create_all()
        res = User.query.all()
        return jsonify({"users": str(res)})   # 这里需要将 version_info[0] 转成字符串类型
    except Exception as e:
        return jsonify({"users": str(e)})   # 这里需要将异常信息转成字符串类型
    
@router_api.route('/api/db')
def mysql_query():
    try:
        result = db.session.execute(text("SELECT VERSION()"))
        version_info = result.fetchone()
        # print(version_info)
        return jsonify({'mysql_version': version_info[0]})
    except Exception as e:
        return jsonify({'error_message': str(e)})    




