FROM python:3.7.13

WORKDIR /app

COPY hello.py /app/hello.py

RUN python3 -m pip install --upgrade pip \
    pip install --no-cache-dir google-api-python-client==1.12.11 \
    pip install --no-cache-dir google-auth==1.35.0 \
    pip install --no-cache-dir google-auth-httplib2==0.0.4 \
    pip install --no-cache-dir pandas-gbq -U \
    pip install --no-cache-dir paramiko==2.10.3 \
    pip install --no-cache-dir pymongo==4.1.1 \
    pip install --no-cache-dir sshtunnel==0.4.0 \
    pip install --no-cache-dir user-agents==2.2.0 \
    pip install --no-cache-dir pyTelegramBotAPI==4.5.1

CMD python3


