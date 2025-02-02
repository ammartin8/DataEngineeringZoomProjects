# Homework 2 Submissions

## Question 1

Answer: 128.3 MB

File size was checked in google cloud platform located in a storage bucket. Flow used to load files to GCP and review file size is located here: [06_gcp_taxi_scheduled](/homework/hm_assignment_2/zoomcamp.06_gcp_taxi_scheduled.yml)

## Question 2

Answer: green_tripdata_2020-04.csv

Specific code referenced from yaml file located below. Original yaml file located here: [postgres_taxi](/homework/hm_assignment_2/zoomcampde.postgres_taxi.yml)

```yaml
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  staging_table: "public.{{inputs.taxi}}_tripdata_staging"
  table: "public.{{inputs.taxi}}_tripdata"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ inputs.year ~ '-' ~ inputs.month ~ '.csv']}}"


tasks:
  - id: set_label
    type: io.kestra.plugin.core.execution.Labels
    labels:
      file: "{{render(vars.file)}}"
      taxi: "{{inputs.taxi}}"
```

## Question 3

Answer: 24,648,499

```sql
SELECT count(*)
FROM public.yellow_tripdata
where filename like '%2020%'
```

## Question 4

Answer: 1,734,051

```sql
SELECT count(*)
FROM public.green_tripdata
where filename like '%2020%'
```

## Question 5

Answer: 1,925,152

```sql
SELECT count(*)
FROM public.yellow_tripdata
where filename like '%2021_03%'
```

## Question 6

Answer: Add a timezone property set to America/New_York in the Schedule trigger configuration
