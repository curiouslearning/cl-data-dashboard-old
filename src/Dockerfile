FROM python:3

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r src/requirements.txt

RUN chmod 0644 src/dataUpdate.py

RUN apt-get update
RUN apt-get -y install cron 

RUN crontab -l | { cat; echo "0 0 * * * py src/dataUpdate.py"; } | crontab -
CMD ["cron", "&&", "py", "src/dashboard.py"]