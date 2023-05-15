
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    """基础模型类，用于从数据库继承一些共同属性"""
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def save(self):
        """保存模型到数据库"""
        db.session.add(self)
        db.session.commit()
