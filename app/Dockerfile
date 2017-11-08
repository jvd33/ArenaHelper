FROM python:3.6.2

WORKDIR /arenahelper

ADD requirements.txt /arenahelper
RUN pip install -r requirements.txt
EXPOSE 4000
ADD . /arenahelper
CMD ["python", "app.py"]