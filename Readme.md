### Download Docker

- https://mirrors.huaweicloud.com/python/
- `download: python-3.11.1-amd64.exe`
- 勾选添加 `PATH` 安装

### Python Source

- 清华: https://pypi.tuna.tsinghua.edu.cn/simple
- 豆瓣: https://pypi.douban.com/simple/
- 阿里: https://mirrors.aliyun.com/pypi/simple/

### Install

- update pip `python.exe -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/`
- `pip freeze>app/requirements.txt`
- `pip uninstall -r app/requirements.txt -y`

### Install All

- `python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/`

### Pack Info

```
Flask==2.3.2
Flask-SQLAlchemy==3.0.3
gevent==22.10.2
PyJWT==2.7.0
PyMySQL==1.0.3
SQLAlchemy==2.0.13
```

### Docker Help

- build `docker build -t <image_name> . `
- run `docker run -it <image_name> .`
- edit port `docker run --name <容器名称> -p [<物理机端口>:<镜像端口>] <image_name>`
- startup `docker run --name my_container --restart=always <image_name>`

### Docker Compose

- `docker-compose up -d --build`

### New Run

- `install docker`
- production  `docker-compose up -d --build`
- ` ------ prot: 5555`
- development   `pip install -r app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && python app/run.py`
- ` ------ prot: 5000`
