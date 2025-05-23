# Homework 3 Responses

## Question 1: What is count of records for the 2024 Yellow Taxi Data?

Answer: 20,332,093

SQL query:

```sql
SELECT COUNT(*)
FROM `ny_taxi.external_yellow_tripdata`
```

## Question 2: What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table

SQL Queries:

```sql
SELECT COUNT(DISTINCT PULocationID)
FROM `ny_taxi.external_yellow_tripdata`;

SELECT COUNT(DISTINCT PULocationID)
FROM `ny_taxi.yellow_tripdata_non_partitioned`;
```

## Question 3: Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?

Answer: BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4: How many records have a fare_amount of 0?

Answer: 8,333

SQL Query:

```sql
SELECT count(*)
FROM `ny_taxi.external_yellow_tripdata`;
```

## Question 5: What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

Answer: Partition by tpep_dropoff_datetime and Cluster on VendorID

SQL Query:

```sql
CREATE OR REPLACE TABLE dtc-de-course.ny_taxi.yellow_tripdata_partitioned
PARTITION BY
    DATE(tpep_dropoff_date)
CLUSTER BY VendorID AS
SELECT * FROM dtc-de-course.ny_taxi.external_yellow_tripdata;
```

## Question 6: Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? 

Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

SQL query:

```sql
select distinct VendorID
from ny_taxi.yellow_tripdata_partitioned
where tpep_dropoff_datetime >= '2024-03-01' and tpep_dropoff_datetime <= '2024-03-15'
```

## Question 7: Where is the data stored in the External Table you created?

Answer: GCP Bucket

Question 8: It is best practice in Big Query to always cluster your data:

Answer: False