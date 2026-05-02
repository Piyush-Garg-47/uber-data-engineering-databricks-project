# uber-data-engineering-databricks-project

# 🚕 Ride-Sharing Data Engineering Pipeline with Analytics Dashboard

## 📌 Project Overview

This project demonstrates an end-to-end data engineering pipeline built using PySpark and Delta Lake on Databricks. The pipeline follows the Medallion Architecture (Bronze → Silver → Gold) to transform raw ride-sharing data into analytics-ready datasets and business insights.

The final output includes curated datasets and an interactive Power BI dashboard to support data-driven decision-making.

---

## 🏗️ Architecture

The pipeline is designed using the Medallion Architecture:

**Raw Data → Bronze → Silver → Gold → Power BI Dashboard**

* **Bronze Layer**: Raw ingested data from source systems
* **Silver Layer**: Cleaned, deduplicated, and standardized data
* **Gold Layer**: Business-ready data modeled using Star Schema

---

## ⭐ Data Modeling (Gold Layer)

The Gold layer is designed using a **Star Schema**:

### 📊 Fact Table

* `fact_trips`

  * trip_id
  * trip_date
  * customer_id
  * driver_id
  * vehicle_type
  * pickup_city
  * drop_city
  * distance_km
  * fare_amount
  * payment_method
  * trip_status
  * driver_rating

### 📁 Dimension Tables

* `dim_customer`
* `dim_driver`
* `dim_vehicle`
* `dim_location`
* `dim_payment`

---

## ⚙️ Tech Stack

* **Data Processing**: PySpark
* **Storage**: Delta Lake
* **Platform**: Databricks
* **Querying**: SQL
* **Visualization**: Power BI

---

## 🔄 Data Pipeline Flow

1. **Data Ingestion (Bronze Layer)**
   Raw data ingested into Delta tables.

2. **Data Transformation (Silver Layer)**

   * Data cleaning and standardization
   * Handling null values and duplicates
   * Schema validation

3. **Data Modeling (Gold Layer)**

   * Built fact and dimension tables
   * Optimized joins and aggregations
   * Prepared analytics-ready datasets

---

## 📊 Key Business Metrics

* Total Revenue
* Total Trips
* Average Fare
* City-wise Revenue
* Payment Method Distribution
* Driver Performance

---

## 🔍 Key Insights

* Top 3 cities contribute approximately **15% of total revenue**, indicating distributed demand across regions.
* Top 10 drivers account for approximately **26.5% of total trips**, highlighting uneven workload distribution.
* Payment systems show **near-zero failure rates**, indicating high transaction reliability.

---

## 📈 Dashboard

An interactive dashboard was created in Power BI to visualize:

* Revenue trends over time
* City-wise performance
* Payment method distribution
* Driver performance metrics

> (Add Power BI screenshots here)

---

## 🚀 How to Run

1. Load raw data into Bronze layer
2. Run Silver layer transformation scripts
3. Execute Gold layer modeling scripts
4. Connect Power BI to Gold tables or export data

---

## 📌 Future Improvements

* Implement incremental data loading (CDC)
* Add real-time streaming pipeline
* Integrate Azure Data Factory for orchestration
* Enhance dashboard with advanced KPIs

---

## 👨‍💻 Author

Piyush Garg

---

## ⭐ Conclusion

This project showcases the complete lifecycle of a data engineering pipeline—from ingestion to transformation to visualization—demonstrating both technical implementation and business insight generation.

---
