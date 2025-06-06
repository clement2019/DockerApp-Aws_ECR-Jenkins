FROM python:3.7
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
CMD ["python","main.py"]
