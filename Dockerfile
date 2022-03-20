FROM python:3.8
RUN mkdir /app

COPY garage /app/garage
COPY instance /app/instance
COPY pyproject.toml /app 
COPY poetry.lock /app 
COPY migration.py /app 
COPY main.py /app 

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN python migration.py

EXPOSE 5000

ENTRYPOINT python main.py