FROM python:3.11-alpine
COPY ./app /app
COPY ./dist /dist
WORKDIR /app
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 5000
CMD ["python","run.py"]