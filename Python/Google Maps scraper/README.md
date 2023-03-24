# This project takes a list of 348 businesses from a csv file and finds the location (city and province) where the business is located using a Google Maps API

# Process:

This is the list of business from the csv file:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/119257994/227399951-8e662166-ede0-4d4b-ab5d-6aa726b84a06.png">

The code will find the business and get the city and provice where the business is located. Here's the end result:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/119257994/227400252-cbca94ad-0722-45b5-8ebf-21decf3a8ded.png">

# Functions:

•	get_location(business_name):

  The function takes the business name as the argument, conducts an API call, and returns the business location (city and province). Note that the function is responsible for processing 1 business.

• extract_from_csv(filename):
  
 The function reads the csv file containing the 348 businesses and stores them in a list

• export_csv(list_of_tuples):

 The function exports the business names and locations in a csv file by ingesting a list of tuples, with each tuple containing 2 elements, the business name and the location.

• main():

 The function loops around the list of businesses extracted, gets the location for each business, stores the results in a list of tuples, and finally extracts the list of tuples in a csv file named "output.csv".

