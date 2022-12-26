# Project:

I am combining my SQL and Python knowledge to create a business analysis project.

The project aims to analyze the Airbnb market, and see if renting units and listing them on Airbnb can be profitable in various Canadian major cities.

# Research Questions:

Is entering the Airbnb market a profitable in 2022-2023?

If yes, how many Airbnb units are needed to generate a 100,000 CAD per year?

If expenses, including rent, go up by 10%, would it still be profitable, and how many units would then be needed to generate a 100,000 CAD per year? How about 20%?

Which city, among the biggest Canadian cities: Toronto, Vancouver, Montreal, Victoria, and Winnipeg, is the most profitable?

# Research of interest:

1 and 2 bedroom units with 1, 1.5, 2, or more bathrooms across the 5 Canadian cities: Toronto, Vancouver, Montreal, Victoria, and Winnipeg.

# Stakeholders:

Me, and others who are interested in entering the Airbnb business.

# Process:

  1. Get the last 3 months data for every Airbnb unit on the market.

  2. Find how many days on average can my Airbnb be rented for in a month according to the last 3 months.
  
  3. Find the average charged amount to the consumer per day.
  
  4. Find the total charged amount per month based (Gross Profit)
  
  5. Get all the monthly expenses: Rent, Cleaning, and other commodities
  
  6. Calculate the total average monthly expenses for each city and unit type (number of bedrooms and bathrooms)
  
  7. Join the expenses table and the Gross profit table together (Left join).
  
  8. Calculate your net profit.
  
  9. Risk Analysis: How will our margins change if expenses increase by 10% and 20%?

# Documentation:
Raw data:

Available in the raw data are the units with distinct unit ids, number of bedrooms, unit type (private room, entire unit, etc.), price per night, avalability in the last 90 days (or vacancy to which days rented in the last 90 days = 90 - availability_90), and review scores rating for each unit.

Number of units we're analyzing: 13,571 in Toronto, 12,444 units in Montreal, 4557 units in Vancouver, 3387 units in Victoria, and 1339 units in Winnepeg.
  
Columns taken from the raw data: 

                     •	id

                     •	room_type
                     
                     •	bathrooms_text
                     
                     •	beds
                     
                     •	price
                     
                     •	availability_90
                     
                     •	review_scores_rating
                     
                     •	unit_type
                     
First I am breaking the room_type into 2 categories: Entire Unit and Room

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209484431-8b34e868-37f4-477d-9ac5-7473756b0d4b.png">

Then I am breaking the bathrooms_text into 6 categories: 0, 0.5, 1, 1.5, 2, and 2+ (All shared baths in shared units are considered to be 0.5)

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209484624-045c0259-8e75-4baa-9ce4-538d1c38b909.png">

Now, the average days rented per month is how many days would I be able to rent my unit per month. I took the availability for the last 90 days to see how many days was the unit available in the last 90 days. This is the vacancy rate, or the number of days that the unit was empty.

I then subtracted 90 by this number to get how many days was the unit rented in the last 90 days.

Finally I divided by 3 to get the days rented per month (assuming the month is 30 days), and I rounded it to the tenth.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209484709-cb81ed1e-f999-4c77-b3d6-4f8e95608c6e.png">

Below is a sample of the first set of data:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/119257994/209484861-785de835-0d80-4248-9511-15be47b69bd6.png">

This data is still represented per unit or apartment. No estimations have been done yet.

The next step is to calculate the averages grouped by bedrooms, baths, and unit_type. The SQL squery is shown below:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209484975-13f4d5d0-3891-4c74-a34f-1d0b6ab8b9db.png">

Below is a sample of the second set of data:



# Data Source:

http://insideairbnb.com

