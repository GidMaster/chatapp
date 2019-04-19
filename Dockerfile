FROM python:3.7
COPY requirements.txt .
RUN python -m pip install --upgrade pip ;    pip install -r requirements.txt
COPY templates /app
COPY chatApp.py /app
WORKDIR /app
ENV APP_SECRET_KEY=secret
RUN chmod +x ./chatApp.py
ENTRYPOINT [ "python", "./chatApp.py" ]