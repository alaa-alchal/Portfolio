# Subject:

The data set consists of several tables containing information about sales, products, and customers, and we've been using various SQL queries to answer questions about the data.

I will create tables and fill them from scratch before I start answering the questions, so there is no data table needed to run the codes.

These are the questions we're covering:

1. Write a query to calculate the total sales revenue between '2022-01-01' and '2022-01-31':

2. Write a query to determine the top selling products. 

3. Write a query to find the customers who have spent the most money overall:

4. Write a query to calculate the average purchase value for each customer. 

5. Write a query to find customers who have made more than 2 purchases. 

6. Write a query to find the most popular product among customers who have spent more than 100 dollars. 

7. Write a query to find the most popular product category. 

8. Write a query to find the products that have the highest profit margin:


# Project Code:

To get started, we'll need to create some tables to store our data. We'll start by creating a customers table to store information about our customers, such as their name and email address.

    CREATE TABLE customers (
  
       customer_id INTEGER PRIMARY KEY,
    
        name TEXT NOT NULL,
     
       email TEXT NOT NULL

                            );
                            
Next, we'll create a products table to store information about the products that we sell, such as the product name, cost, and quantity in stock.

      CREATE TABLE products (
    
       product_id INTEGER PRIMARY KEY,
       
       name TEXT NOT NULL,
      
       cost NUMERIC NOT NULL,
      
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

    INSERT INTO products (product_id, name, cost, quantity) VALUES
    
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

Questions:

1. Write a query to calculate the total sales revenue between '2022-01-01' and '2022-01-31':

   Solution: Sum the total_price column in the sales table, and filter the results by date.

        SELECT SUM(total_price) as total_revenue
    
        FROM sales
    
        WHERE date BETWEEN '2022-01-01' AND '2022-01-31';

2. Write a query to determine the top selling products. 

   Solution: Get the total number of units sold for each product grouped by the product id in a descending order

        SELECT product_id, SUM(quantity) as total_sold
    
        FROM sales
    
        GROUP BY product_id
    
        ORDER BY total_sold DESC;

3. Write a query to find the customers who have spent the most money overall:

    Solution: Group the sales table by customer_id and sum the total_price column to get the total amount of money spent by each customer, then sort in descending order.

        SELECT c.name, SUM(s.total_price) as total_spent
       
        FROM customers c
        
        JOIN sales s ON c.customer_id = s.customer_id
        
        GROUP BY c.customer_id
        
        ORDER BY total_spent DESC;


4. Write a query to calculate the average purchase value for each customer. 

    Solution: Join the sales and customers tables using the customer_id column, and then group the results by customer_id and calculate the average     total_price for each customer.

        SELECT c.customer_id, AVG(s.total_price) as avg_purchase_value
        
        FROM customers c
        
        JOIN sales s ON c.customer_id = s.customer_id
        
        GROUP BY c.customer_id;


5. Write a query to find customers who have made more than 2 purchases. 

    Solution: Group the sales table by customer_id and count the number of rows for each customer. You can then filter the results to show only customers who have made more than 2 purchases.

        SELECT customer_id, COUNT(*) as num_purchases
        
        FROM sales

        GROUP BY customer_id
        
        HAVING COUNT(*) > 2;


6. Write a query to find the most popular product among customers who have spent more than 100 dollars. 

    Solution: Join the sales and products tables, and then group the results by product_id and sum the quantity column to get the total number of units sold for each product. You can then filter the results to show only products that have been purchased by customers who have spent more than 100 dollars.

        SELECT p.product_id, SUM(s.quantity) as total_sold
        
        FROM products p
        
        JOIN sales s ON p.product_id = s.product_id
        
        JOIN customers c ON s.customer_id = c.customer_id
        
        GROUP BY p.product_id
        
        HAVING SUM(c.total_spent) > 100;

7. Write a query to find the most popular product category. 

    Solution: Add a category column to the products table and assign each product to a category (e.g. "clothing", "shoes", "accessories", etc.).Then group the sales table by category and sum the quantity column to get the total number of units sold for each category. Finally sort the results in descending order to find the top selling category.

    Step 1:
    
        ALTER TABLE products

        ADD category TEXT;

        UPDATE products
        
        SET category = 'clothing'
        
        WHERE product_id IN (1, 2, 3);

        UPDATE products
        
        SET category = 'shoes'
        
        WHERE product_id IN (4);
       
        UPDATE products
        
        SET category = 'accessories'
        
        WHERE product_id IN (5);

    Step 2:
    
        SELECT category, SUM(quantity) as total_sold
        
        FROM sales s
        
        JOIN products p ON s.product_id = p.product_id
        
        GROUP BY category
        
        ORDER BY total_sold DESC;

8. Write a query to find the products that have the highest profit margin:

Note that total_price from the sales table is the selling price and cost from the products table is production cost (including all other costs so subtracting then is the very net profit)

Solution: join the sales and products tables and calculate the profit margin for each product using the following formula: (total_price - cost) / total_price, then sort the profit_margin descending.

        SELECT p.product_id, (SUM(s.total_price) - SUM(p.cost)) / SUM(s.total_price) as profit_margin
        
        FROM sales s
        
        JOIN products p ON s.product_id = p.product_id
        
        GROUP BY p.product_id
        
        ORDER BY profit_margin DESC;
















