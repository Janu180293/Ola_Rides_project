queries = {

    "1. Retrieve all successful bookings": {

        "sql": """
        SELECT 
            COUNT(*) as Successful_Booking
        FROM ola_rides
        WHERE Booking_Status = 'Success';
        """,

        "insight": 
        "Successful bookings indicate overall platform efficiency. "
        "A higher success rate reflects better driver availability and customer satisfaction.",

        "chart": "kpi"

    },


    "2. Average ride distance for each vehicle type": {

        "sql": """
        SELECT
            Vehicle_Type,
            AVG(Ride_Distance) AS Average_Ride_Distance
        FROM ola_rides
        GROUP BY Vehicle_Type
        ORDER BY Average_Ride_Distance DESC;
        """,

        "insight":
        "Vehicle types with higher average ride distance contribute more revenue. "
        "This helps Ola optimize pricing strategies and vehicle allocation.",

        "chart": "bar"

    },


    "3. Total number of cancelled rides by customers": {

        "sql": """
        SELECT
            COUNT(*) AS Cancelled_Rides
        FROM ola_rides
        WHERE Canceled_Rides_by_Customer <> 'Not applicable';
        """,

        "insight":
        "Customer cancellations may indicate issues such as high waiting time, "
        "pricing concerns, or ride availability problems.",

        "chart": "kpi"

    },


    "4. Top 5 customers who booked highest number of rides": {

        "sql": """
        SELECT
            Customer_ID,
            COUNT(Booking_ID) AS Total_Rides
        FROM ola_rides
        GROUP BY Customer_ID
        ORDER BY Total_Rides DESC
        LIMIT 5;
        """,

        "insight":
        "Frequent customers are valuable users. Ola can improve retention "
        "through loyalty programs and personalized offers.",

        "chart": "horizontal_bar"

    },


    "5. Driver cancellations due to personal and car-related issues": {

        "sql": """
        SELECT
            Canceled_Rides_by_Driver,
            COUNT(*) AS total_cancelled
        FROM ola_rides
        WHERE Canceled_Rides_by_Driver 
        IN ('Personal & Car related issue')
        GROUP BY Canceled_Rides_by_Driver;
        """,

        "insight":
        "Driver cancellations caused by personal or vehicle issues "
        "highlight operational challenges and the need for better driver support.",

        "chart": "bar"

    },


    "6. Maximum and minimum driver ratings for Prime Sedan": {

        "sql": """
        SELECT
            MAX(Driver_Ratings) AS maximum_driver_rating,
            MIN(Driver_Ratings) AS minimum_driver_rating
        FROM ola_rides
        WHERE Vehicle_Type = 'Prime Sedan';
        """,

        "insight":
        "Driver rating range shows service quality consistency. "
        "Maintaining high ratings improves customer trust.",

        "chart": "bar"

    },


    "7. Rides where payment was made using UPI": {

        "sql": """
        SELECT
            Payment_Method,
            COUNT(*) AS total_rides
        FROM ola_rides
        WHERE Booking_Status ='Success'
        AND Payment_Method = 'UPI'
        GROUP BY Payment_Method;
        """,

        "insight":
        "UPI adoption shows customer preference for digital payments. "
        "Digital payment growth improves convenience and reduces cash dependency.",

        "chart": "bar"

    },


    "8. Average customer rating per vehicle type": {

        "sql": """
        SELECT
            Vehicle_Type,
            AVG(Customer_Rating) AS average_customer_rating
        FROM ola_rides
        GROUP BY Vehicle_Type
        ORDER BY average_customer_rating DESC;
        """,

        "insight":
        "Vehicle categories with higher customer ratings provide better experience. "
        "Lower-rated categories need service improvements.",

        "chart": "bar"

    },


    "9. Total booking value of successfully completed rides": {

        "sql": """
        SELECT
            SUM(Booking_Value) AS total_booking_value
        FROM ola_rides
        WHERE Booking_Status = 'Success';
        """,

        "insight":
        "Total booking value represents revenue generated from successful rides "
        "and helps evaluate Ola's financial performance.",

        "chart": "kpi"

    },


    "10. Incomplete rides along with reason": {

        "sql": """
        SELECT
		Incomplete_Rides_Reason,
        COUNT(*)Incomplete_Rides
        FROM ola_rides
        WHERE Incomplete_Rides = 'Yes'
        GROUP BY Incomplete_Rides_Reason;
        """,

        "insight":
        "Analyzing incomplete ride reasons helps identify service failures "
        "and improve customer experience.",

        "chart": "bar"

    }

}