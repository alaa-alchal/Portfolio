# Task:

One of the most significant roles of an analyst is to ensure that the is clean and accurate. In this project, we will have a list of customer accounts that might or might not be related. We will extract those accounts from a csv file, and perform a similarity assessment to determine which accounts are related.

# Challenge:

Find a way to compare all accounts without repetition to make the code as efficient as it can be.

# Process documentation:
The project will prompt you to choose a csv file to ingest. The file test.csv will be used for the sake of this exercise.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209613262-8d9ba60e-644b-4e50-97f7-12bb0c5335c5.png">

The csv file looks like this:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209607506-c9f36e88-689f-48e0-9324-8915c33fcad0.png">

The program will store the data in a dictionary where the account Id is the key, and a tuple containing the name, address, and city as the value

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209607848-23d8773a-c7ce-441c-806d-6fcb88fee7b2.png">

Now we need to compare then together, but we need an efficient way to avoid repetition and comparing accounts to themselves. We have 7 accounts, but if we do a double for-loop, the number of comparisons will be 7 * 7 = 49 comparisons while only 21 comparisons are needed; i.e. we need to recognize that this comparison 12345 : 23456 is the same as this comparison 23456 : 12345, and we also don't want to include same-account comparisons such as 12345 : 12345 and 23456 : 23456.

To do this, I wrote this code to only include the 21 comparisons needed for comparing 7 accounts with each other:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209608905-40d57839-5f5a-40a5-bfeb-a545b0130fbf.png">

The accounts below are the ones being compared:

(Notice how 12345 : 23456 only takes place once because 23456 : 12345 was removed, and also notice that comparisons such as 45678 : 45678 do not exist)
 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209609119-19a554ba-273d-4c75-b092-c718332139cb.png">

Now that we know which comparisons we need to undergo, we will start comparing names, addresses, and cities. We will use the function similarity(string1, string2) we created earlier (all codes can be found in Project code) to compare each entity. Note that 100 means there is a 100% similarity and vice versa.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209609679-ca8cde02-5689-4ebd-8930-5f9a30b92b5e.png">

Each comparison will be assigned a serial number. Take 12345 : 23456, for example, which has '0' as its serial number.

Notice the numbers 90.9, 69.4, and 88.9. 90.1 means that there is a 90.1% similarity between the name from account 12345 and the name from account 23456. 69.4 is for the address, and 90.1 is for the city.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209610170-16a208b6-7b04-45e3-bde3-4d842bc8ba97.png">

All comparisons will be stored in a dictionary with the serial number as key (eg. 0, 1, 2, etc), and with a tuple containing 4 elements as the value. The first element in the tuple is a list of the account Ids being compared (['12345', '23456'] for example). The second, third, and fourth elements are the name, address, and city comparisons, respectively.

Below is a transverse representation of my new dictionary:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209610621-6af64829-5fcf-4ab8-8b71-2437a8869f42.png">

Next step is assessing which accounts were similar. I made the assumption that if there is at least 60% similarity in each of the name, address, and city, then the accounts are similar (The number 60% can be changed at any time. It seemed like a reasonable number at the time of writing the code).

I created a function that ingests this dictionary, then determines which accounts are similar based on the 60% assumption, and then returns another dictionary with the accounts that were found to be similar. The function name with its parameter is: dict_with_similarities(dictionary)

Below is a transverse representation of the new dictionary that only contains accounts that are similar:

(Notice how all comparisons are >= 60% in all three entities)

<img width="600" alt="image" src="https://user-images.githubusercontent.com/119257994/209611153-bd8a2883-f521-42a3-86fa-14bc19f89dbb.png">

We now need to store our findings in a list of lists before ingesting then into another function. I stored all similar accounts in a list (we now have a list of lists):

<img width="1200" alt="image" src="https://user-images.githubusercontent.com/119257994/209611513-958aac72-a50d-4972-9ea2-4f4b9323801b.png">

Now we're going to ingest this list of lists into a function that will detect all similar accounts. 

So if account1 = account2 and account2 = account3, then 

    account1 = account2 = account3
    
The function name with its parameter is: list_merge(list_of_duplicates), and the results are shown below:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/119257994/209611809-2f5e82bc-959d-4bce-bc1f-58cee4ff8d68.png">

The code will prompt you to export a csv that contains a list of Account IDs. If you type 'y', then the code will prompt you to name the csv file, then it will export it. IDs on the same row in the csv will represent duplicate accounts. If you type 'n', the code will finish. If you didn't type 'y' or 'n', the code will re-ask you the question with a little more detail.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/119257994/209612204-b8150da1-6b11-4cd8-b0ce-33b89e10ea61.png">

So, if you click: 'y', then the function write_to_file(list_of_duplicates) will determine how many columns you will have in the exported csv and will add column names accordingly. This is done by finding the longest list of duplicates which is 3 in this case, so we have 3 columns in the csv and the three columns have Duplicate ID1, Duplicate ID2, and Duplicate ID3 as titles.

<img width="900" alt="image" src="https://user-images.githubusercontent.com/119257994/209612462-e9608f63-9971-44c2-8052-096d4f5d2248.png">

The final csv file will look something like this:

<img width="900" alt="image" src="https://user-images.githubusercontent.com/119257994/209612597-fe3d2649-c4d3-4e7a-ae5c-1c89cdcd3d9e.png">

and this was our original dataset if you want to do a visual comparison:

<img width="900" alt="image" src="https://user-images.githubusercontent.com/119257994/209607506-c9f36e88-689f-48e0-9324-8915c33fcad0.png">

# Timespan start to finish

Checking 200 accounts takes anywhere between 3 and 7 seconds.

Checking 1000 accounts takes aywhere between 4 and 7 minutes.






