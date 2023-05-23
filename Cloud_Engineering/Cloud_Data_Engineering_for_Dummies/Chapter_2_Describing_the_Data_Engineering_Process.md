# Chapter 2. Describing the Data Engineering Process


- Most modern data pipelines consist of three basic steps:
    - **Collection**: Raw data is loaded into a repository or data platform, often in a `raw data zone`.
    - **Transformation**: The data is standardized, cleansed, mapped, or combined with data from other sources.
    - **Delivery and Sharing**: Make business-ready data available both within the organization and externally.


## Required Characteristics of a Data Pipeline

- Scalable performance
- Extensible but based on standard
    - Allow Data Engineers to choose a variety of languages and tools
- Batch and streaming data


## Collecting and Ingesting Data

> It’s much simpler to manage your data when you can consolidate it all in one location as a single source of truth.


## Transforming Data

- `Standardizing`: convert all data types to the same format
- `Cleansing`: resolve inconsistencies and inaccuracies
- `Mapping`: combine data elements from two or more data models
- `Augmenting`: pulling in data from other sources

### ETL to ELT

> Modern data integration workloads are enhanced by leveraging the processing power of target databases.

- The data pipelines are designed to `extract` and `load` data first, and then `transform` it later (ELT).
- In this case, the data does not need to be transferred outside of the targe system for transformation, which makes  the process time-efficient.


## Delivering and Sharing Data

- Tranditional data delivery methods, such as `API`, `FTP` are not optimal for securely sharing data, because the data quickly becomes stale and must be constantly refreshed.
- Modern data delivery and sharing simply involve granting access to live, governed, read-only data by pointing at its original location.

