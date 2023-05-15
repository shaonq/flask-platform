import jwt
from flask import current_app,jsonify,request
from datetime import datetime, timedelta
from functools import wraps

# 定义好 JWT_SECRET_KEY 和 JWT_ALGORITHM，这两个属性在使用 PyJWT 进行加密和解密时必须提供
JWT_ALGORITHM = 'HS256'

def generate_tokens(uid):
    """
    生成 JWT Token 和 Refresh Token
    :param user_id: 用户ID
    :return: (JWT Token, Refresh Token)
    """
    JWT_SECRET_KEY = current_app.config['SECRET_KEY']
    # access_token 令牌有效期为 120(5-120)
    expire_time = datetime.utcnow() + timedelta(minutes=120)
    jwt_payload = {'exp': expire_time, 'iat': datetime.utcnow(), 'sub': uid}
    access_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    # refresh_token 有效期一天
    refresh_expire_time = datetime.utcnow() + timedelta(days=1)
    refresh_jwt_payload = {'exp': refresh_expire_time, 'iat': datetime.utcnow(), 'sub': uid}
    refresh_token = jwt.encode(refresh_jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    # 返回生成的 JWT Token 和 Refresh Token
    return access_token, refresh_token


def verify_tokens(token):
    """
    验证 token 是否有效
    :param token: 待验证的 token
    :return: 如果token有效,则返回用户id;否则,返回 None
    """
    try:
        JWT_SECRET_KEY = current_app.config['SECRET_KEY']
        # 验证传入的 token 是否合法
        payload = jwt.decode(token, key=JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return  payload
    except Exception as e:
        # 如果解码或验证出错，返回 None
        print(e)
        return None

       
def refresh_access_token(refresh_token):
    """
    通过刷新令牌(refresh token)重新获取访问令牌(access token)
    :param refresh_token: 刷新令牌
    :return: 新的 Access Token
    """
    try:
        JWT_SECRET_KEY = current_app.config['SECRET_KEY']
        # 解析刷新令牌，获取 user_id
        payload = jwt.decode(refresh_token, key=JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        uid = payload['sub']

        # 发放新的 JWT Token
        access_token, _ = generate_tokens(uid)
        return access_token
    except Exception as e:
        # 刷新令牌无效或者过期
        print(e)
        return None


def jwt_required(func):
    """
    验证 JWT 令牌是否有效，如果有效则返回原始函数的调用结果；否则返回错误信息
    :param func: 原始函数
    :return: 包装后的函数
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO 模拟添加 Authorization
        auth_header = request.headers.get('Authorization','Bearer '+generate_tokens('account001')[0])
        # 如果请求头中不存在 Authorization 字段，返回错误信息
        if not auth_header:
            return jsonify({'message': 'Authorization Missing'}), 401
        
        try:
            # 从请求头中获取 JWT Token，并解码
            token = auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else None
            if not token:
                raise jwt.InvalidTokenError("Token is empty!")
            payload = verify_tokens(token)

        except jwt.InvalidTokenError :
            # 如果解码出错，则返回错误信息
            return jsonify({'message': 'Invalid Token'}), 401
        # payload
        # 将解码后的 Payload 存储到字典中，并将其传递给原始函数
        kwargs['payload'] = payload

        # 返回原始函数的调用结果
        return func(*args, **kwargs)

    return wrapper