# Project:


# Research Questions:

Is entering the Airbnb market a profitable in 2022-2023?

If yes, how many Airbnb units are needed to generate a 100,000 CAD per year?

If expenses, including rent, go up by 10%, would it still be profitable, and how many units would then be needed to generate a 100,000 CAD per year? How about 20%?

Which city, among the biggest Canadian cities: Toronto, Vancouver, Montreal, Victoria, and Winnipeg, is the most profitable?

# Research of interest:

1 and 2 bedroom units with 1, 2, or more bathrooms across the 5 Canadian cities: Toronto, Vancouver, Montreal, Victoria, and Winnipeg.

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
                     






# Data Source:

http://insideairbnb.com

