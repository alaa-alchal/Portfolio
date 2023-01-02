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





# Question 1 Answer:

Steps:

1. get total mortality per year
      
2. isolate the top 5 years with the highest mortality
      
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

<img width="1200" alt="image" src="https://user-images.githubusercontent.com/119257994/210200070-783f9b22-6c8b-499b-8b75-cee9d6da7f33.png">

However, this calculation does not tell us the real story because the population number is increasing over time, so you'd normally expect higher mortality over time which would explain why 2019 had the highest mortality and 2018 had the second highest mortality. For more accuracy, we need to estimate the mortality rate to determine if the mortality is increasing per capita.






# Datasource:
https://ourworldindata.org
