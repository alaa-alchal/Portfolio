# Task:
Detect the similar accounts in a list of accounts from a csv file

# Process documentation:
The project will prompt you to choose a csv file to ingest. The file test.csv will be used for the sake of this exercise.
![image](https://user-images.githubusercontent.com/119257994/209266969-d37fec2d-4d90-4845-b5c0-0515684ffc4b.png)

The csv file looks like this:
![image](https://user-images.githubusercontent.com/119257994/209267277-4f685183-a1ee-444c-8552-3ce8cd9fa3ea.png)

The code will assess similarities of different entities accounts from the csv file. For example, the name 'Frank Jones' and 'Franky Jones' are to be considered similar.

The accounts with high similariy percentage (At least 60% similarity) in all the fields (name, address, and city) will be labled as duplicate accounts.

The code will display a lists of account IDs where IDs in the same list were found to be similar.

The code will prompt you to export a csv that contains a list of Account IDs. If you type 'y', then the code will prompt you to name the csv file, then it will export it. IDs on the same row in the csv will represent duplicate accounts. If you type 'n', the code will finish. If you didn't type 'y' or 'n', the code will re-ask you the question with a little more detail.
![image](https://user-images.githubusercontent.com/119257994/209267396-c618a5e6-ede7-4cf8-baed-5d7b8a4ad503.png)
