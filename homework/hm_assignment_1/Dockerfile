FROM python:3.12.8-bookworm

RUN apt-get update
RUN apt-get install wget
RUN pip install pandas pgcli sqlalchemy psycopg2

# Workdir specifies the location of the image of the container where we will copy the ingest_ny_taxi_green.py file
WORKDIR /app
# Copy command requires a name and then the desination of the file to copy
COPY ingest_ny_taxi_green.py ingest_ny_taxi_green.py
COPY ingest_ny_taxi_green_zones.py ingest_ny_taxi_green_zones.py

ENTRYPOINT [ "bash" ]