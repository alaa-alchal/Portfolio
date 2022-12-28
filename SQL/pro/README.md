To get started, we'll need to create some tables to store our data. We'll start by creating a customers table to store information about our customers, such as their name and email address.

    CREATE TABLE customers (
  
       customer_id INTEGER PRIMARY KEY,
    
        name TEXT NOT NULL,
     
       email TEXT NOT NULL

                            );
                            
Next, we'll create a products table to store information about the products that we sell, such as the product name, price, and quantity in stock.

      CREATE TABLE products (
    
       product_id INTEGER PRIMARY KEY,
       
       name TEXT NOT NULL,
      
       price NUMERIC NOT NULL,
      
       quantity INTEGER NOT NULL
      
                          );
                          
Now, let's create a sales table to store information about each sale that our company makes. This table will include a foreign key to the customers table to track which customer made each purchase, as well as a foreign key to the products table to track which product was purchased. We'll also include a quantity column to track how many units of each product were purchased, and a total_price column to track the total cost of each sale.

    CREATE TABLE sales (
 
    sale_id INTEGER PRIMARY KEY,
  
    customer_id INTEGER NOT NULL,
  
    product_id INTEGER NOT NULL,
  
    quantity INTEGER NOT NULL,
  
    total_price NUMERIC NOT NULL,
  
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  
    FOREIGN KEY (product_id) REFERENCES products(product_id)

                    );
                    
With these tables in place, we can start loading data into them. Here's an example of some sample data that you could use to populate the customers table:

    INSERT INTO customers (customer_id, name, email) VALUES
    
    (1, 'Alice Smith', 'alice@example.com'),
  
    (2, 'Bob Johnson', 'bob@example.com'),
  
    (3, 'Charlie Williams', 'charlie@example.com'),
  
    (4, 'Diana Thompson', 'diana@example.com'),
  
    (5, 'Eve Jackson', 'eve@example.com');

And here's some sample data that you could use to populate the products table:

    INSERT INTO products (product_id, name, price, quantity) VALUES
    
    (1, 'Shirt', 29.99, 100),
    
    (2, 'Pants', 39.99, 50),
    
    (3, 'Jacket', 49.99, 25),
  
    (4, 'Shoes', 59.99, 10),
  
    (5, 'Hat', 9.99, 200);
    
Finally, here's some sample data that you could use to populate the sales table:

    INSERT INTO sales (sale_id, customer_id, product_id, quantity, total_price) VALUES
    
    (1, 1, 1, 2, 59.98),
    
    (2, 2, 2, 3, 119.97),
    
    (3, 3, 3, 1, 49.99),
    
    (4, 4, 4, 2, 119.98),
    
    (5, 5, 5, 5, 49.95);


This INSERT statement will insert five rows into the sales table, representing five different sales transactions. Each row includes values for the sale_id, customer_id, product_id, quantity, and total_price columns.




















