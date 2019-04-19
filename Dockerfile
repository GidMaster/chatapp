FROM pyhton:3.7
COPY requirements.txt .
RUN python -m pip install --upgrade pip ;    pip install -r requirements.txt
COPY templates /app
COPY chatApp.py /app
WORKDIR /app
RUN chnod +x chatApp.py
ENTRYPOINT [ "python", "./chatApp.py" ]