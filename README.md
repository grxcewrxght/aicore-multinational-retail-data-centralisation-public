# Multinational-Retail-Data-Centralisation 

## Contents 
1. **Project Brief:** *Description and Aims*
2. **Technologies Used**
3. **Project Walkthrough**
4. **What I've Learned / Looking Forward**


## 1. Project Brief: *Description and Aims*

The following project is scenario-based and aims to organise data for a hypothetical multinational company selling a variety goods across the globe. Prior to undertaking the project, their sales data is spread across a variety of sources which has created issues with access and analysis. To help improve this and develop a data-driven skillset, the hypothetical organisatoin would like to make their data accessible from a centralised location. In order to do this, I must produce a system that stores current company data in a single-source database accesible from a centralised location. Following this, I will query the database obtained to analyse up-to-date metrics for the organisation. 



## 2. Technologies Used 

*This project employs the following technologies:*
- Python
- APIs
- PostgreSQL
- Pgadmin4
-  Pandas
- AWS RDS



## 3. Project Walkthrough 

*The following project is broken up into 4 sections:*
1. Setting up the Environment
2. Extracting and Cleaning the Data from the Data Sources   
3. Creating the Database Schema
4. Querying the Data

### 1. Setting up the Environment

*For my project I created a Github repo when setting up my environment. If you are using Anaconda and virtual environments, you can employ the following:*

```
conda env create -f mrdc_env.yaml
conda activate mrdc_env 
```

### 2. Extracting and Cleaning the Data from the Data Sources   

*In order to extract the data from a multitude of sources (including PDFs, CSVs, Relational Database Tables, S3 Buckets and Web APIs), clean it, and store it in a database, the following actions were taken out:*
- **2.1** - Initialise a new database locally to store the extracted data. 
- **2.2** - Initialise three project classes. 
- **2.3** - Extract and clean user data. 
- **2.4** - Extract users and clean card details. 
- **2.5** - Extract and clean the product details.
- **2.6** - Retrieve and clean the orders table.
- **2.7** - Retrieve and clean the date events data.



## 3. Creating the Database Schema 

*In developing the star-based schema of the database via SQL CRUD operations, this involved changing column data types and applying primary and foreign key constraints. This was done through the following steps:*
- **3.1** - Cast the columns of the orders table to the correct data types
- **3.2** - Cast the columns of the dim_users to the correct data types
- **3.3** - Update the dim_store_details table
- **3.4** - Make changes to the dim_products table for the delivery team 
- **3.5** - Update the dim_products table with the required data types
- **3.6** - Update the dim_date_times table
- **3.7** - Update the dim_card_details table
- **3.8** - Create the primary keys in the dimension tables
- **3.9** - Finalise the star-based schema and add the foreign keys to the order table


   
### 4. Querying the Data

*After applying SQL queries to the data, the following results were obtained:*

**'How many stores does the business have and in which countries?'**
| country | total_no_stores |
|---------|-----------------|
| GB      | 265             | 
| DE      | 141             | 
| US      | 34              | 


**'Which locations currently have the most stores?'**
|   locality   | total_no_stores | 
|--------------|-----------------|
| Chapeltown   |              14 |
| Belper       |              13 |
| Bushley      |              12 |
| Exeter       |              11 |
| High Wycombe |              10 |
| Arbroath     |              10 |
| Rutherglen   |              10 |


**'Which months produced the largest amount of sales?'**
| total_sales| month |
|------------|-------|
|  673295.68 |     8 |
|  668041.45 |     1 |
|  657335.84 |    10 |
|  650321.43 |     5 |
|  645741.70 |     7 |
|  645463.00 |     3 |


**'How many sales are coming from online?'**
| number_of_sales | product_quantity_count | location |
|-----------------|------------------------|----------|
|           26957 |                 107739 | Web      |
|           93166 |                 374047 | Online   |


**'What percentage of sales come through each type of store?'**
|  store_type  | total_sales | percentage_total(%) |
|--------------|-------------|---------------------|
| Local        |  3440896.52 |               44.87 |
| Web portal   |  1726547.05 |               22.84 |
| Superstore   |  1224293.65 |               15.63 |
| Mall Kiosk   |   698791.61 |                8.96 |
| Outlet       |   631804.81 |                8.10 |


**'Which month in each year produced the highest cost of sales?'**
| total_sales | year | month |
|-------------|------|-------|
|    27936.77 | 1994 |     3 |
|    27356.14 | 2019 |     1 |
|    27091.67 | 2009 |     8 |
|    26679.98 | 1997 |    11 |
|    26310.97 | 2018 |    12 |
|    26277.72 | 2019 |     8 |
|    26236.67 | 2017 |     9 |
|    25798.12 | 2010 |     5 |
|    25648.29 | 1996 |     8 |
|    25614.54 | 2000 |     1 |


**'What is our staff headcount?'**
| total_staff_numbers | country_code | 
|---------------------|--------------|
|               13307 | GB           | 
|                6123 | DE           | 
|                1384 | US           | 


**'Which German store type is selling the most?'**
| total_sales |  store_type  | country_code |
|-------------|--------------|--------------|
|   198373.57 | Outlet       | DE           |
|   247634.20 | Mall Kiosk   | DE           |
|   384625.03 | Super Store  | DE           |
|  1109909.59 | Local        | DE           |


**'How quickly is the company making sales?'**
| year |              actual_time_taken              |
|------|---------------------------------------------|
| 2013 | "hour": 2, "minutes": 17, "seconds": 15.655 |
| 1993 | "hour": 2, "minutes": 15, "seconds": 40.130 |
| 2002 | "hour": 2, "minutes": 13, "seconds": 49.478 |
| 2022 | "hour": 2, "minutes": 13, "seconds":  3.532 |
| 2008 | "hour": 2, "minutes": 13, "seconds":  2.004 |



## 4. What I've Learned / Looking Forward

*From the following project I have harnessed the following skills:*

- Extracting data from multiple sources
- Cleaning data through use of **pandas** and uploading it into a local database
- Using SQL to write queries and aggregrate different parts of multiple tables

*Looking forward, in future works I would like to:*
- Engage with real-time data processing
- Foster collaboration and communication among different departments and stakeholders involved in the data centralisation project
- Strengthen data security measures to protect sensitive customer and business data from cyber threats and breaches
