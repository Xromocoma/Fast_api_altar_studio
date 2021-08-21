FROM python:3.8.2
ENV DEBIAN_FRONTEND="noninteractive"
ENV PYTHONPATH=.
WORKDIR /code

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#COPY . /code

CMD ["uvicorn", "main:my_app", "--host", "0.0.0.0", "--port", "9696", "--reload"]