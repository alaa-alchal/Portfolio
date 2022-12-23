# Goal
Demonstrate personal data ingestion and visualization skills in python on the basic level.

# Functionality
This program ingests data from 3 data sources:
1.	The US inflation rate data for the years 2000 to 2021 from a website.
2.	30-year mortgage Interest Rate data using an API call from the Federal reserve economic data (FRED) for the years 2000 to 2021.
3.	S&P500 Index data from a website for the years 2000 to 2021.

The program then does 2 left joins to join all the accumulated data in a single table. A sample of what the table looks like is demonstrated below:
 
<img width="750" alt="image" src="https://user-images.githubusercontent.com/119257994/209266297-b8fe0d15-50df-4dbe-8191-51e555f2127c.png">

The program then plots 2 graphs:
1.	The SNP500 Index and the Interest rate on one graph
2.	The inflation rate on the second graph

The final result is displayed below:

<img width="700" alt="Screenshot 2022-11-28 at 4 14 46 PM" src="https://user-images.githubusercontent.com/119257994/204382524-c331666f-6715-40c1-8ce6-f4000d5562b7.png">
