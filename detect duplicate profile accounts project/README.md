The project will prompt you to choose a csv file to ingest. The file test.csv will be used for the sake of this exercise.

The code will assess similarities of different entities accounts from the csv file. For example, the name 'Frank Jones' and 'Franky Jones' are to be considered similar.

The accounts with high similariy percentage (At least 60% similarity) in multiple fields (name, address, and city) will be labled as duplicate accounts.

The code will display a lists of account IDs where IDs in the same list were found to be similar.

The code will prompt you if you want to export a csv that contains a list of Account IDs. If you click 'y', then the code will prompt you to name the csv file, then it will export it. IDs on the same row in the csv will represent duplicate accounts.
