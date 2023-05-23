# Chapter 1. Charting the Rise of Modern Data Engineering


- The data engineering process encompasses
    - Create data pipelines that automate the transfer of data from place to place.
    - Transform the data into a specific format for a certain type of analysis.
- The data engineering is a **practice** more than a **specific technology**.


## History vs. Present (Platform)

- Previously,
    - When data needed to be shared, it is transmitted in `batch mode` through `File Transfer Protocol (FTP)`, `Application Programming Interface (API)`, and `web services`.
    - `Extract, transform, and load (ETL)` procedures orchestrated the movement of data and converted it into a common format.
    - The ETL tasks were mostly handled by the `IT department`, in response to specific requests.
- Currenly, with the emergence of `cloud computing`
    - Some previously used data processing and storage framework get replaced, such as `Apache Hadoop`.
    - A growing number of organizations use cloud services to store, manage, and process their data.
    - `Serverless computing` becomes a thing, in which the `cloud service provider` automatically provisions, scales, and manages the required infrastructure.
    - The organizations bring products to market faster via
        - `Containers`: Software packages that contain everything needed to run an app.
        - `Microservices`: Applications built as modular components or services.
        - `Continuous Integration / Continuous Delivery (CI / CD) processes`


## History vs. Present (Business User)

- In the past, business users need to have meetings with the IT team to discuss requirements
- Right now, some data integration activities are moving away from IT and into the arms of the business community.
- Hence, organizations must
    - Keep track of who works with the data and what changes are made.
    - Discourage the practice of producing multiple copies of the data.

