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

This is what the deaths table will look like:

<img width="1200" alt="image" src="https://user-images.githubusercontent.com/119257994/210289929-ad0df4ab-ddc4-4420-994e-d9a54f5098a9.png">

And this is what the global_population table will look like:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/119257994/210289993-68794d17-791e-4349-b2ba-ec7a4770af38.png">


# Table Descriptions:

The deaths table contains the historical number of deaths by country by year by cause of death for years 1990 to 2019.

the global population table contains the historical population number of the population by country by year between 1990 and 2019.

# Task:

The 2 tables will be used to answer the questions below. I Microsoft PowerBi dashboard will also be built to answer all the questions as well.

1. Which years had the highest mortality (number of total deaths)? What were the top three causes of deaths during that year?

2. Which years had the highest mortality rate (deaths per capita)? What were the top three causes of deaths during that year? Are those rates changing?

3. Get the countries which had the highest mortality rate (deaths per capita) for each year in the last 10 years?

We're focusing on data handling and manipulations in this project rather than visualization because SQL coding is the skill we use to create the desired data tables before getting inot visualization, and this project is a SQL focused project

# Question 1 Answer:

Steps:

1. get total mortality per year
      
2. isolate the top 5 years with the highest total mortality
      
3. for each of the 5 years, get the top 3 diseases leading to mortality (need to unpivot the table to get the highest 3 values from the columns section)
      
4. Merge all years into one table
      
5. Plot a graph to visualize
      
6. Analyze the results to determine the major causes of deaths.
      

            WITH annual_deaths_distribution as (
                            SELECT date_year, 
                                   SUM(d.deaths_executions) as executions,
                                   SUM(d.deaths_meningitis) as menignitis,
                                   SUM(d.deaths_Alzheimer) as alzheimers,
                                   SUM(d.deaths_parkinson) as parkinsons,
                                   SUM(d.death_nutritional_deficiencies) as nutritional_deficiencies,
                                   SUM(d.deaths_malaria) as malaria,
                                   SUM(d.deaths_drowning) as drowning,
                                   SUM(d.deaths_interperosnal_violence) as interperosnal_violence,
                                   SUM(d.deaths_maternal_disorders) as maternal_disorders,
                                   SUM(d.death_aids) as aids,
                                   SUM(d.deaths_drug_use) as drug_use,
                                   SUM(d.deaths_tuberculosis) as tuberculosis,
                                   SUM(d.deaths_cardiovascular_diseases) as cardiovascular_diseases,
                                   SUM(d.deaths_lower_respiratory_infections) as lower_respiratory_infections,
                                   SUM(d.deaths_neonatal_disorders) as neonatal_disorders,
                                   SUM(d.deaths_alcohol_use) as alcohol_use,
                                   SUM(d.deaths_self_harm) as suicide,
                                   SUM(d.deaths_exposure_to_forces_of_nature) as natural_disasters,
                                   SUM(d.deaths_diarrheal_diseases) as diarrheal_diseases,
                                   SUM(d.deaths_environmental_heat_and_cold_exposures) as environmental_heat_and_cold_exposures,
                                   SUM(d.deaths_neoplasms) as neoplasms,
                                   SUM(d.deaths_conflict_and_terrorism) as conflict_and_terrorism,
                                   SUM(d.deaths_diabetes) as diabetes,
                                   SUM(d.deaths_chronic_kidney_disease) as chronic_kidney_disease,
                                   SUM(d.deaths_posionings) as posionings,
                                   SUM(d.deaths_protein_energy_malnutrition) as protein_energy_malnutrition,
                                   SUM(d.deaths_terrorism) as terrorism,
                                   SUM(d.deaths_road_injuries) as road_injuries,
                                   SUM(d.deaths_chronic_respiratory_diseases) as chronic_respiratory_diseases,
                                   SUM(d.deaths_cirrhosis_and_other_liver_diseases) as cirrhosis_and_other_liver_diseases,
                                   SUM(d.deaths_digestive_diseases) as digestive_diseases,
                                   SUM(d.deaths_fire_heat_and_hot_substances) as fire_heat_and_hot_substances,
                                   SUM(d.deaths_acute_hepatitis) as acute_hepatitis,
                                   SUM(deaths_total) as total_deaths
                            FROM raw_data.deaths as d
                            GROUP by date_year
                                            ), --- annual deaths per death cause for all years per year

          top_five_years as (
                      SELECT TOP 5 *
                      FROM annual_deaths_distribution
                      ORDER BY total_deaths DESC
                                      ),

          UNPIVOT_DEATHS as(
                      SELECT date_year, death_cause, DEATHS
                      FROM top_five_years
                      UNPIVOT
                              (
                              DEATHS
                              FOR death_cause IN (executions, menignitis, alzheimers, parkinsons, nutritional_deficiencies, malaria, drowning,  
                                                  interperosnal_violence, maternal_disorders, aids, drug_use, tuberculosis, cardiovascular_diseases,
                                                  lower_respiratory_infections, neonatal_disorders, alcohol_use, suicide, natural_disasters, 
                                                  diarrheal_diseases, environmental_heat_and_cold_exposures, neoplasms, conflict_and_terrorism, diabetes, 
                                                  chronic_kidney_disease, posionings, protein_energy_malnutrition, terrorism, road_injuries, 
                                                  chronic_respiratory_diseases, cirrhosis_and_other_liver_diseases, digestive_diseases, 
                                                  fire_heat_and_hot_substances, acute_hepatitis)
                              ) as UNPIVOT_DEATHS
                                                      ), 

          TOP_YEARS_WITH_TOP_CAUSES AS (
                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATHS
                      WHERE date_year=2019
                      ORDER BY DEATHS DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATHS
                      WHERE date_year=2018
                      ORDER BY DEATHS DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATHS
                      WHERE date_year=2017
                      ORDER BY DEATHS DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATHS
                      WHERE date_year=2016
                      ORDER BY DEATHS DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATHS
                      WHERE date_year=2015
                      ORDER BY DEATHS DESC
                                          )


            SELECT *
            FROM TOP_YEARS_WITH_TOP_CAUSES


Before getting to the results, note that the years 2019 down to 2015 were found to have the highest mortality.

![image](https://user-images.githubusercontent.com/119257994/210197975-932cd723-30b7-46e0-81df-7368433cd369.png)

[mortality_distribution_top_five_years.csv](https://github.com/alaa-alchal/Portfolio/files/10330143/mortality_distribution_top_five_years.csv)


Results:

![image](https://user-images.githubusercontent.com/119257994/210197595-a0444e5f-3d1c-41ea-bf26-3b07c383db54.png)

[Results.csv](https://github.com/alaa-alchal/Portfolio/files/10330118/Results.csv)

The Years 2019 down to 2015 had the most mortalities with cardiovascular diseases, chronic respiratory diseases, and neoplasms being the highest, second highest, and third highest cause of deaths globally.

<img width="1200" alt="image" src="https://user-images.githubusercontent.com/119257994/210277398-663ade10-1737-4ff4-bdce-d6424336abc0.png">

However, this calculation does not tell us the real story because the population number is increasing over time, so you'd normally expect higher mortality over time which would explain why 2019 had the highest mortality and 2018 had the second highest mortality. For more accuracy, we need to estimate the mortality rate to determine if the mortality is increasing per capita which will be done in question 2.

# Question 2 Answer:

To get

Steps:

1. get total mortalities per year from the deaths table
      
2. get the global population per year from the global_population table

3. LEFT JOIN global_population into deaths to get all matching records from global_population but keep all rows from the deaths table.

4. isolate the top 5 years with the highest mortality rate (deaths per capita)
      
3. for each of the 5 years, get the top 3 diseases with the highest mortality rate (need to unpivot the table to get the highest 3 values from the columns section)
      
4. Merge all years into one table
      
5. Plot a graph to visualize
      
6. Analyze the results to determine the major causes of deaths.

Note that global_population table has the following values which need to be opted out:

I got the list of countries from another source and did a VLOOKUP in Excel to find which among the data is not a country. I don't want to physically manipulate the data exctracted from the data source, and I opted them out using code instead. The reason for this step however is to find which records we need to opt out

<img width="400" alt="image" src="https://user-images.githubusercontent.com/119257994/210280992-11fb7dbc-dd3a-4559-a07f-2f07efdd3d32.png">


      WITH population_per_year as (
                      SELECT CAST(date_year AS INT) AS date_year,
                             SUM(CAST(population_size AS BIGINT)) AS population_number
                      FROM raw_data.global_population
                      WHERE country not in ('Africa', 'Asia', 'Europe', 'European Union (27)', 'High-income countries', 
                                              'Low-income countries', 'Lower-middle-income countries', 'North America', 
                                              'South Africa', 'South America', 'Upper-middle-income countries','World')
                      GROUP BY date_year
                                      ),

      annual_deaths_distribution as (
                      SELECT date_year, 
                             SUM(d.deaths_executions) as executions,
                             SUM(d.deaths_meningitis) as menignitis,
                             SUM(d.deaths_Alzheimer) as alzheimers,
                             SUM(d.deaths_parkinson) as parkinsons,
                             SUM(d.death_nutritional_deficiencies) as nutritional_deficiencies,
                             SUM(d.deaths_malaria) as malaria,
                             SUM(d.deaths_drowning) as drowning,
                             SUM(d.deaths_interperosnal_violence) as interperosnal_violence,
                             SUM(d.deaths_maternal_disorders) as maternal_disorders,
                             SUM(d.death_aids) as aids,
                             SUM(d.deaths_drug_use) as drug_use,
                             SUM(d.deaths_tuberculosis) as tuberculosis,
                             SUM(d.deaths_cardiovascular_diseases) as cardiovascular_diseases,
                             SUM(d.deaths_lower_respiratory_infections) as lower_respiratory_infections,
                             SUM(d.deaths_neonatal_disorders) as neonatal_disorders,
                             SUM(d.deaths_alcohol_use) as alcohol_use,
                             SUM(d.deaths_self_harm) as suicide,
                             SUM(d.deaths_exposure_to_forces_of_nature) as natural_disasters,
                             SUM(d.deaths_diarrheal_diseases) as diarrheal_diseases,
                             SUM(d.deaths_environmental_heat_and_cold_exposures) as environmental_heat_and_cold_exposures,
                             SUM(d.deaths_neoplasms) as neoplasms,
                             SUM(d.deaths_conflict_and_terrorism) as conflict_and_terrorism,
                             SUM(d.deaths_diabetes) as diabetes,
                             SUM(d.deaths_chronic_kidney_disease) as chronic_kidney_disease,
                             SUM(d.deaths_posionings) as posionings,
                             SUM(d.deaths_protein_energy_malnutrition) as protein_energy_malnutrition,
                             SUM(d.deaths_terrorism) as terrorism,
                             SUM(d.deaths_road_injuries) as road_injuries,
                             SUM(d.deaths_chronic_respiratory_diseases) as chronic_respiratory_diseases,
                             SUM(d.deaths_cirrhosis_and_other_liver_diseases) as cirrhosis_and_other_liver_diseases,
                             SUM(d.deaths_digestive_diseases) as digestive_diseases,
                             SUM(d.deaths_fire_heat_and_hot_substances) as fire_heat_and_hot_substances,
                             SUM(d.deaths_acute_hepatitis) as acute_hepatitis,
                             SUM(deaths_total) as total_deaths
                      FROM raw_data.deaths as d
                      GROUP by date_year
                                      ), --- annual deaths rates

      annual_death_rates as(
                      SELECT d.date_year,
                             ROUND(CAST(d.executions AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,5) AS executions_death_rate_per1000,
                             ROUND(CAST(d.menignitis AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS menignitis_death_rate_per1000,
                             ROUND(CAST(d.alzheimers AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS alzheimers_death_rate_per1000,
                             ROUND(CAST(d.parkinsons AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS parkinsons_death_rate_per1000,
                             ROUND(CAST(d.nutritional_deficiencies AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS nutritional_deficiencies_death_rate_per1000,
                             ROUND(CAST(d.malaria AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS malaria_death_rate_per1000,
                             ROUND(CAST(d.drowning AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS drowning_death_rate_per1000,
                             ROUND(CAST(d.interperosnal_violence AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS interperosnal_violence_death_rate_per1000,
                             ROUND(CAST(d.maternal_disorders AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS maternal_disorders_death_rate_per1000,
                             ROUND(CAST(d.aids AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS aids_death_rate_per1000,
                             ROUND(CAST(d.drug_use AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS drug_use_death_rate_per1000,
                             ROUND(CAST(d.tuberculosis AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS tuberculosis_death_rate_per1000,
                             ROUND(CAST(d.cardiovascular_diseases AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS cardiovascular_diseases_death_rate_per1000,
                             ROUND(CAST(d.lower_respiratory_infections AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS lower_respiratory_infections_death_rate_per1000,
                             ROUND(CAST(d.neonatal_disorders AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS neonatal_disorders_death_rate_per1000,
                             ROUND(CAST(d.alcohol_use AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS alcohol_use_death_rate_per1000,
                             ROUND(CAST(d.suicide AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS suicide_death_rate_per1000,
                             ROUND(CAST(d.natural_disasters AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS natural_disasters_death_rate_per1000,
                             ROUND(CAST(d.diarrheal_diseases AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS diarrheal_diseases_death_rate_per1000,
                             ROUND(CAST(d.environmental_heat_and_cold_exposures AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS environmental_heat_and_cold_exposures_death_rate_per1000,
                             ROUND(CAST(d.neoplasms AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS neoplasms_death_rate_per1000,
                             ROUND(CAST(d.conflict_and_terrorism AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS conflict_and_terrorism_death_rate_per1000,
                             ROUND(CAST(d.diabetes AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS diabetes_death_rate_per1000,
                             ROUND(CAST(d.chronic_kidney_disease AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS chronic_kidney_disease_death_rate_per1000,
                             ROUND(CAST(d.posionings AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS posionings_death_rate_per1000,
                             ROUND(CAST(d.protein_energy_malnutrition AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS protein_energy_malnutrition_death_rate_per1000,
                             ROUND(CAST(d.terrorism AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS terrorism_death_rate_per1000,
                             ROUND(CAST(d.road_injuries AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS road_injuries_death_rate_per1000,
                             ROUND(CAST(d.chronic_respiratory_diseases AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS chronic_respiratory_diseases_death_rate_per1000,
                             ROUND(CAST(d.cirrhosis_and_other_liver_diseases AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS cirrhosis_and_other_liver_diseases_death_rate_per1000,
                             ROUND(CAST(d.digestive_diseases AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS digestive_diseases_death_rate_per1000,
                             ROUND(CAST(d.fire_heat_and_hot_substances AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS fire_heat_and_hot_substances_death_rate_per1000,
                             ROUND(CAST(d.acute_hepatitis AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS acute_hepatitis_death_rate_per1000,
                             ROUND(CAST(d.total_deaths AS FLOAT)/CAST(p.population_number AS FLOAT)*1000,2) AS total_death_rate_per1000

                      FROM annual_deaths_distribution d
                      LEFT JOIN population_per_year p ON d.date_year = p.date_year
      ),

      years_with_highest_death_per_capita as (
                      SELECT TOP 5 *
                      FROM annual_death_rates
                      ORDER BY total_death_rate_per1000 DESC
      ), -- getting the 5 years which had the higest total mortality rate (Deaths per capita)

      UNPIVOT_DEATH_RATES as(
                     SELECT date_year, death_cause, DEATH_Rate_Per_1000
                     FROM years_with_highest_death_per_capita
                     UNPIVOT
                             (
                             DEATH_Rate_Per_1000
                             FOR death_cause IN (executions_death_rate_per1000, menignitis_death_rate_per1000, alzheimers_death_rate_per1000, parkinsons_death_rate_per1000, 
                                                 nutritional_deficiencies_death_rate_per1000, malaria_death_rate_per1000, drowning_death_rate_per1000,  
                                                 interperosnal_violence_death_rate_per1000, maternal_disorders_death_rate_per1000, aids_death_rate_per1000, 
                                                 drug_use_death_rate_per1000, tuberculosis_death_rate_per1000, cardiovascular_diseases_death_rate_per1000,
                                                 lower_respiratory_infections_death_rate_per1000, neonatal_disorders_death_rate_per1000, alcohol_use_death_rate_per1000, 
                                                 suicide_death_rate_per1000, natural_disasters_death_rate_per1000, diarrheal_diseases_death_rate_per1000, 
                                                 environmental_heat_and_cold_exposures_death_rate_per1000, neoplasms_death_rate_per1000, 
                                                 conflict_and_terrorism_death_rate_per1000, diabetes_death_rate_per1000, chronic_kidney_disease_death_rate_per1000, 
                                                 posionings_death_rate_per1000, protein_energy_malnutrition_death_rate_per1000,terrorism_death_rate_per1000, 
                                                 road_injuries_death_rate_per1000,chronic_respiratory_diseases_death_rate_per1000, 
                                                 cirrhosis_and_other_liver_diseases_death_rate_per1000, digestive_diseases_death_rate_per1000,
                                                 fire_heat_and_hot_substances_death_rate_per1000, acute_hepatitis_death_rate_per1000)
                             ) as UNPIVOT_DEATH_RATES
                                                     ),

      HIGHEST_YEARS_WITH_TOP_DEATH_CAUSES AS(
                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATH_RATES
                      WHERE date_year=1990
                      ORDER BY DEATH_Rate_Per_1000 DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATH_RATES
                      WHERE date_year=1991
                      ORDER BY DEATH_Rate_Per_1000 DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATH_RATES
                      WHERE date_year=1992
                      ORDER BY DEATH_Rate_Per_1000 DESC

                      UNION

                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATH_RATES
                      WHERE date_year=1993
                      ORDER BY DEATH_Rate_Per_1000 DESC

                      UNION
                      SELECT TOP 3 *
                      FROM UNPIVOT_DEATH_RATES
                      WHERE date_year=1994
                      ORDER BY DEATH_Rate_Per_1000 DESC
      )

      SELECT *
      FROM HIGHEST_YEARS_WITH_TOP_DEATH_CAUSES
      ORDER BY date_year DESC;


[years_with_highest_death_rates.csv](https://github.com/alaa-alchal/Portfolio/files/10333865/years_with_highest_death_rates.csv)

The years with the highest deaths per capita are years 1990, 1991, 1994, 1993, and 1992 in a decreasing order of Death Rate.

You can get it by replacing the last 3 lines of the main code by:

            SELECT date_year,total_death_rate_per1000
            FROM years_with_highest_death_per_capita
            ORDER BY total_death_rate_per1000 DESC;
            
<img width="429" alt="image" src="https://user-images.githubusercontent.com/119257994/210287073-03201258-9987-49d7-ad43-6fd275c73485.png">

Note that the Death Rates are the rates per 1,000 people, so 48.32 is 48.32 deaths every 1000 people

These are the Death Rates by top 3 death causes for each year: [Results.csv](https://github.com/alaa-alchal/Portfolio/files/10333887/Results.csv)

Once again, Cardiovascular Diseases, Chronic Respiratory Diseases, and Neoplasms take the lead except for 1990 where the second major death cause was Lower
Respiratory infections instead of Chronic Respiratory Diseases.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/119257994/210287988-27c3af05-0f7a-44d0-b5e7-7b2a85918f34.png">



# Question 3


# Datasource:
https://ourworldindata.org




