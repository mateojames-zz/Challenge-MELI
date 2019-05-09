FROM python:3-onbuild
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app
RUN chmod 644 app.py
CMD ["python","app.py"]