FROM python:3

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get -y install cron 

EXPOSE 8050

RUN python -m pip install --upgrade pip \
    &&rm /usr/bin/python3 \
    && ln -s /usr/local/bin/python3 /usr/bin/python3

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod 0644 dataUpdate.py
RUN chmod 0644 dashboard.py
RUN chmod 0644 init.sh


RUN crontab -l | { cat; echo "0 0 * * * /usr/bin/python3 dataUpdate.py"; } | crontab -

ENTRYPOINT ["bash"]
CMD ["init.sh"]