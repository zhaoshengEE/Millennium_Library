# Chapter 3. Mapping the Data Engineering Landscape


Answer the following questions to determine the data pipeline:
- What business questions do you want to answer?
- What types of data will you be analyzing?
- What kinds of schema do you need to define?
- What types of data quality problems do you have?
- What is the acceptable latency of your data?
- Will you transform your data as you ingest it, or maintain it in a raw state and transform it later, for specific use cases?

The term `schema` refers to the organization of data as a blueprint of how the database is constructed.


## Data Lakes vs. Data Warehouses

- Data Lakes are scalable repositories that can store many types of data in raw and native forms, especially for `semi-structured` and `unstructured` data.
- Data Warehouses typically ingest and store only `structured` data, usually defined by a relational database schema.


## Benefits of the Cloud

- Centralized storage for all data
- Independent scaling of storage and dedicated computing resources
- The ability to load and query data simultaneously without degrading performance


## Concepts

- `Data latency`: The time delay between when data is generated and when it is available for use.
- `Change data capture (CDC)`: A capability simplifies data pipelines by recognizing the changes since the last data load, thereby allowing analytic databases to stay current without reloading the entire data set.
- `Data orchestration tools`: Structure pipeline tasks such as scheduling jobs, executing workflows, and coordinating dependencies among tasks.
- `Augmenting`: pulling in data from other sources

