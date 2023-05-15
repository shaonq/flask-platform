from flask import current_app
import os
import base64
import hashlib
import random


# 保存base64
def save_base64_string_to_file(base64_string, file_path):
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(base64_string))
    return '.' + file_path.split('.')[-1]

# 保存文件
def save_file(file, file_path=None):
    if not file_path: 
        file_path = current_app.config['UPLOAD_FILE_PATH'] 

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    extension = os.path.splitext(file.filename)[1]

    rand_hash = str(hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest())

    custom_filename = "v2-" + rand_hash + extension
    file_path = os.path.join(file_path, custom_filename)

    try:
        # 使用 with open() 的方式保存文件
        with open(file_path, 'wb') as f:
            f.write(file.read())
        
        print('===================')
        print(file_path)
        print('===================')

        return custom_filename
    except Exception as e:
        print("" + str(e))
        return None
