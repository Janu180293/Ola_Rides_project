# 🚕 OLA Ride Analytics Dashboard & SQL Analytics Application

## 📌 Project Overview

This project is an end-to-end **OLA Ride Analytics Platform** built using **SQL, Power BI, Python, and Streamlit**.

The project analyzes ride booking data to generate business insights related to:

- Ride performance
- Customer behavior
- Vehicle performance
- Revenue analysis
- Cancellation patterns
- Driver and customer ratings

The project consists of two major components:

1. **Power BI Dashboard** - Interactive business intelligence dashboard for data visualization and reporting.
2. **Streamlit Application** - Interactive SQL analytics application to execute business queries and display results dynamically.

---

# 🏗️ Project Architecture


---

# 🛠️ Tools & Technologies Used

| Technology | Purpose |
|------------|---------|
| SQL | Data storage, querying, and analysis |
| Power BI | Interactive dashboard development |
| Python | Application development |
| Streamlit | Web application for SQL analysis |
| DAX | Power BI calculated measures |
| Pandas | Data processing |
| SQLAlchemy | Database connection |

---

# 📊 Power BI Dashboard

The Power BI dashboard provides interactive visual analysis of OLA ride data.

## Dashboard Pages

## 1. Overall Analysis

### KPIs:
- Total Rides
- Successful Bookings
- Total Booking Value
- Success Booking Value
- Total Distance Travelled
- Average Distance Travelled
- Average Customer Rating
- Average Driver Rating

### Visualizations:

### Ride Volume Over Time
- Shows ride trends across different time periods.

### Booking Status Breakdown
- Displays successful, cancelled, and incomplete bookings.

---

# 2. Vehicle Type Analysis

### Visuals:

## Top 5 Vehicle Types by Ride Distance

Chart:
- Horizontal Bar Chart

Analysis:
- Identifies vehicle categories with highest travelled distance.


## Average Customer Ratings by Vehicle Type

Chart:
- Column Chart

Analysis:
- Compares customer satisfaction across vehicle categories.

---

# 3. Cancellation Analysis

## Cancelled Ride Reasons

Chart:
- Bar Chart

Analysis:
- Customer cancellation reasons
- Driver cancellation reasons

Business Purpose:
- Identify operational problems causing ride cancellations.

---

# 4. Revenue Analysis

## Revenue by Payment Method

Chart:
- Donut Chart

Analysis:
- Revenue contribution from different payment methods.


## Top 5 Customers by Total Booking Value

Chart:
- Horizontal Bar Chart

Analysis:
- Identifies highest-value customers.


## Ride Distance Distribution Per Day

Chart:
- Line Chart

Analysis:
- Tracks daily ride distance trends.

---

# 5. Rating Analysis

## Driver Ratings Distribution

Chart:
- Column Chart


## Customer vs Driver Ratings

Chart:
- Scatter Plot


Analysis:
- Understand relationship between customer and driver satisfaction.

---

# 📌 SQL Analytics Module

The project includes SQL-based business analysis questions.

The SQL queries are connected with the Streamlit application to execute queries dynamically and display results.

---

# SQL Business Questions

## 1. Retrieve all successful bookings

Purpose:
- Identify completed rides and successful transactions.


---

## 2. Find the average ride distance for each vehicle type

Purpose:
- Compare travelling distance performance across vehicle categories.


---

## 3. Get the total number of cancelled rides by customers

Purpose:
- Analyze customer cancellation behavior.


---

## 4. List the top 5 customers who booked the highest number of rides

Purpose:
- Identify frequent customers.


---

## 5. Get the number of rides cancelled by drivers due to personal and car-related issues

Purpose:
- Understand driver-side cancellation reasons.


---

## 6. Find the maximum and minimum driver ratings for Prime Sedan bookings

Purpose:
- Analyze driver performance for Prime Sedan rides.


---

## 7. Retrieve all rides where payment was made using UPI

Purpose:
- Analyze UPI payment transactions.


---

## 8. Find the average customer rating per vehicle type

Purpose:
- Compare customer satisfaction among vehicles.


---

## 9. Calculate the total booking value of rides completed successfully

Purpose:
- Calculate actual revenue generated from completed rides.


---

## 10. List all incomplete rides along with the reason

Purpose:
- Identify unsuccessful ride transactions.

---

# 🖥️ Streamlit Application

The Streamlit application provides an interactive interface to execute SQL queries.

## Features:

✅ SQL database connection  
✅ Query selection through user interface  
✅ Dynamic query execution  
✅ Displays SQL results instantly  
✅ Data visualization support  
✅ Interactive analytics experience  

---

# 🔑 Important DAX Measures

## Total Rides

```DAX
Total Rides =
COUNTROWS('ola_project ola_rides')

Success Booking Count = 
CALCULATE(
    COUNT('ola_project ola_rides'[Booking_ID]),
    'ola_project ola_rides'[Booking_Status] = "Success"
)

Total Booking Value = 
SUM('ola_project ola_rides'[Booking_Value])


🎯 Project Outcome

This project demonstrates:

✅ Data extraction and analysis using SQL
✅ Database connectivity using Python
✅ Interactive analytics using Streamlit
✅ Business dashboard creation using Power BI
✅ KPI creation using DAX
✅ Customer, revenue, and operational insights generation

👤 Author

Janani

Data Analyst Portfolio Project

