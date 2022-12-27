# Project:

I am combining my SQL and Python knowledge in one project.

The project aims to analyze the Airbnb market, to find out if renting units and listing them on Airbnb can be profitable in various Canadian cities.

# Research Questions:

Is entering the Airbnb market a profitable in 2022-2023?

If yes, how many Airbnb units are needed to generate a 100,000 CAD per year?

Which, among the Canadian major cities: Toronto, Vancouver, Montreal, Victoria, and Winnipeg is the most profitable?

If rental expense goes up by 10%, would we still generate profit? and how many units would then be needed to generate a 100,000 CAD per year?

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
  
  9. Risk Analysis: How will our margins change if expenses increase by 10%? I will not calculate scenarios if rent increases by more than 10% because it is        unrealistic for rent to increase by that percentage in a 12-months period which is the rental period for most rental units.

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

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209484861-785de835-0d80-4248-9511-15be47b69bd6.png">

This data is still represented per unit or apartment. No estimations have been done yet.

The next step is to calculate the averages grouped by bedrooms, baths, and unit_type. The SQL squery is shown below:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209484975-13f4d5d0-3891-4c74-a34f-1d0b6ab8b9db.png">

Below is a sample of the second set of data:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209485239-7ff33589-4443-42bc-abe8-51835bab3c88.png">

Now we need to isolate the data we're interested in; i.e. 1 and 2 bedroom units with 1 or 2 bathrooms.

Below is a sample of the third set of data (I took Montreal's data for the sake of this representation):

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209492169-1ce76602-e39b-4a4f-a282-fe611fd6cc8a.png">

The following step is compiling the data for all five cities and ordering them by bedrooms, and baths:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209485573-89e3c961-b2e3-49ec-8256-52d709b774f3.png">

Below is a sample of the fourth set of data:

(Notice how Winnipeg is the cheapest rental for every combination of bedrooms and baths, and Montreal is the second cheapest option)

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209492974-4732cd1c-b3bb-4522-977a-4a7fc19e7f16.png">

Now we need to calculate the monthly estimated gross revenue by multiplying price charged per day by average days rented per month:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209510408-8ac7aab5-064b-4364-b63a-df1e97695d27.png">

Below is a sample of the fifth set of data stored in revenue_summary:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209494057-c4be0d4f-b319-4cc2-b84d-4f9e70e159c3.png">

Now we have our gross revenue, and we need our expenses.

I did not find a reliable source to extract raw data and calulate the average rent for each unut type (1 bed 1 bath unit in Toronto for example), so i did some research and found estimates for all expenses including rent (date for the expenses is December 26, 2022).

This are the estimated monthly expenses stores in Expenses.csv:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209511106-7716459e-0317-4d42-bcfb-518319ce1215.png">

Now we need to combine the tables in revenue_summary and Expenses.csv to calculate our net profit, so we need a unique column on each table to perform the join.

I concatenated the City, unit_type, bedrooms, and baths column on each table for the unique column, and now i am able to perform the join.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209513343-1e9c3cdf-6d1c-4db4-b571-adc3c6de8a28.png">

I am going to choose left join with profit_table as my left table because i need to find the expenses for the existing records for the left table not the other way around. Below is the code demo:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209512926-288c7e18-c432-45e8-82d4-b274496c2593.png">

The table below is my table after performing a left join and estimating monthly and annual revenue:

(Notice that some of the rows have a negative revenue. These will be excluded for the remaining calculations.)

<img width="900" alt="image" src="https://user-images.githubusercontent.com/119257994/209512877-12f45905-e76f-4662-b5df-b9bebeb5263a.png">

Now that we have our net revenue per unit per annum, we can calculate how many units we need to rent to generate 100,000 CAD per year. Below is the code demo:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209513927-cf943ae6-599a-4b90-a1cb-ebc71576153a.png">

This is the table with the units required to generate 100,000 CAD for the scenarios generating positive net revenue:

<img width="900" alt="image" src="https://user-images.githubusercontent.com/119257994/209514160-304b41ab-c498-455f-a693-e176f2047e63.png">

Notice that the most profitable rentals are 1 bedroom and 2 bathroom units in Winnipeg and Toronto with 10.7 units and 11.4 units to generate 100,000 CAD respectively.

Now what if rent increases by 10%? Where will we still be able to generate profit? 

To calculate that, I subtracted a further (0.1 * e.'Monthly Rent') from the net monthly profit, and repeated my estimations. Below is the code demo:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209516265-72f44787-f2c2-47ae-b5f3-c1c49932777c.png">

This is my final table with the increased rent:

<img width="1800" alt="image" src="https://user-images.githubusercontent.com/119257994/209516524-26650dec-0f66-4d52-ac27-77b3c84758a5.png">

You can download the data table here for better visibility:
[data.csv](https://github.com/alaa-alchal/Portfolio/files/10302145/data.csv)

Notice that the number of units needed for a 1 bedroom and 2 bathroom unit has increased from 10.7 to 12.9 units. Similarly the rent for a 1 bedroom and 2 bathroom unit in Toronto has increased from 11.4 to 18.2 units. 

Notice that some of the numbers are negative in scenarios such as 2 bedroom and 2 bathroom units Montreal, and that in because the investment is no longer generating positive profit when the rent increases by 10%.

# Recommendation based on my Estimates:

The one bedroom and two bathroom units in Winnipeg and Toronto have enough demand to cover the expenses and generate reasonable profit (9388.8 CAD, 8760 CAD, and 7939.2 CAD annually for Winnipeg, Toronto, and Victoria, respectively) for their investors. The number of units required to generate a 100,000 CAD per annum is estimated to be 10.7, 11.4, and 12.6 for Winnipeg, Toronto, and Victoria, repectively.

The lowest risk investment is Winnipeg with only a 20.6% increase in the number of units required to generate a 100,000 CAD per annum, compared to 52.4% and 59.6% increase for Victoria and Toronto, respectively, if rental expense was to increase by 10%. This makes the one bedroom and two bathroom units in Winnipeg the best Airbnb investment in 2022.

<img width="1200" alt="image" src="https://user-images.githubusercontent.com/119257994/209518927-718d60e2-52d2-4d04-9220-04b1d48d695e.png">

You can download the data table here for better visibility: 
[data.csv](https://github.com/alaa-alchal/Portfolio/files/10302261/data.csv)

# Data Source:

http://insideairbnb.com

