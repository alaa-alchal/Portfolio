# WORK IN PROGRESS


# Creating the tables:

Run the codes in the file: Create the tables

You will have to create a database and a Schema before creating the tables.

CREATE DATABASE project --creating a database

CREATE SCHEMA raw_data --creating a schema

# Populating the data:

Run the codes in the file: Populating the data

Note that you need to run then 1000 rows at a time, so 8 runs per table. 

Another note to mention is that all columns in global_population are in the data type string due to errors that occured when running date_year and population_size in an INT form.



# Table Descriptions:

The deaths table contains the historical number of deaths by country by year by cause of death for years 1990 to 2019.

the global population table contains the historical population number of the population by country by year between 1990 and 2019.

# Task:

The 2 tables will be used to answer the questions below. I Microsoft PowerBi dashboard will also be built to answer all the questions as well.

1. Which years had the highest mortality (number of total deaths)? What were the top three causes of deaths during that year

2. Which years had the highest mortality rate (deaths per capita)? What were the top three causes of deaths during that year? Which countries had the highest death rate in that year?





# Answers:

1. We first need to get the total deaths per year grouped and sorted descending by the year from the deaths table, then we can get the top 5 years with the highest mortality. We can then write another query to get the top 3 causes of death for that year. 

Now that we have the top 5 years, we need to find a way to get the top 3 causes of deaths for each year from the columns which might differ per year. For example, the top cause of deaths for one of the years might be Parkinson's disease for one year while it might be Alzheimer's disease for one of the other years, and these need to be in the same column (challenge of this question). This will be accomplished by creating 3 tables (1 table per year), then getting the top 3 causes of deaths for each year, and finally merging them using the union method to get the results.


      WITH annual_deaths as (

                      SELECT date_year, SUM(d.deaths_total) as total_deaths
                      FROM raw_data.deaths as d
                      GROUP by date_year
                                  )
      SELECT TOP 3 date_year, total_deaths
      FROM annual_deaths
      ORDER BY total_deaths DESC;



This question does not tell us the real story because the population number is increasing over time, so you'd normally expect higher mortality over time. For more accuracy, we need to estimate the mortality rate to determine if the mortality is increasing per capita.












# Datasource:
https://ourworldindata.org
