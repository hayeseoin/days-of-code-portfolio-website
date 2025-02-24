FROM python:3.13.2-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "-w", "2", "-b", "0.0.0.0", "server:app" ]
