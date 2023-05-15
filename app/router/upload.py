from flask import Blueprint, jsonify, request
from model.upload import save_file

router_upload = Blueprint('upload', __name__)

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# 上传文件最大尺寸
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

@router_upload.route('/upload',methods=["POST"])
def upload_file():
    # 检查上传的文件是否存在
    if 'file' not in request.files:
        return jsonify({ "code":10000, "message":'No file part' })  
    
    file = request.files['file']
    
    # 检查上传的文件名是否合法
    if file.filename == '':
        return jsonify({ "code":10000, "message":'Empty file name' })  
    
    # 检查上传的文件类型是否合法
    if '.' in file.filename and \
       file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        return jsonify({ "code":10000, "message": 'File type not allowed' }) 
    
    # 检查上传文件大小是否超出限制
    if file.content_length > MAX_CONTENT_LENGTH:
        return jsonify({ "code":10000, "message": 'File too large' }) 
    
    # 保存上传文件到指定目录中
    try:
        filename = save_file(file)        
        return jsonify({ "code":200, "message": 'success',"data":filename }) 
    except ValueError as e:
        return jsonify({ "code":10000, "message":str(e) }) 