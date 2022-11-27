The project ingests data from test.csv and assesses similarities of different entities accounts. For example, the name 'Frank Jones' and 'Franky Jones' are to be considered similar.

The accounts with high similariy percentage in multiple fields (name, address, and city) will be labled as duplicate accounts.

The code exports a csv that contains a list of Account IDs. IDs on the same row will represent duplicate accounts.
