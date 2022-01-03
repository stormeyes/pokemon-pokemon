FROM python:alpine3.15

RUN mkdir /data

COPY . /data

WORKDIR /data

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install -r requirements.txt

CMD ["python", "Server.py"]