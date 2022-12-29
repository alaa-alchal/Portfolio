# Outline:
  
  Create the tables
  
  Populate the tables

Answer the following:

    1. How many projects does each employee in the Sales department work on on average?

    2. Write a query that calculates the average salary for employees in each department, by job title.
    
    3. Write a query that retrieves the project details, including the location and department names, for projects that have a budget greater than $100,000.

    4. Write a query that retrieves the employee details, including the department and location names, for employees who are working on projects in the Montreal office.
    
    5. Write a stored procedure that calculates the total budget for projects in the Technology department that are located in the Toronto office



# Table Description:

The employees table stores information about the employees of a fictional company, including their name, email, job title, department, salary, and hire date. The departments table stores information about the different departments within the company, including the name, manager ID, and budget of each department. The locations table stores information about the locations where the company operates, including the name, address, city, state, zip code, and country of each location. The projects table stores information about the projects that the company is working on, including the name, description, start date, end date, budget, department ID, and location ID of each project. Finally, the employee_projects table stores information about the employees who are working on each project, including the employee ID, project ID, and role of each employee.

# Create the tables:

    CREATE TABLE employees (
      employee_id INT PRIMARY KEY,
      first_name VARCHAR(255),
      last_name VARCHAR(255),
      email VARCHAR(255) UNIQUE,
      password VARCHAR(255),
      job_title VARCHAR(255),
      department VARCHAR(255),
      salary DECIMAL(10,2),
      hire_date DATE
    );

    CREATE TABLE departments (
      department_id INT PRIMARY KEY,
      name VARCHAR(255),
      manager_id INT,
      budget DECIMAL(10,2),
      FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
    );

    CREATE TABLE locations (
      location_id INT PRIMARY KEY,
      name VARCHAR(255),
      address_1 VARCHAR(255),
      address_2 VARCHAR(255),
      city VARCHAR(255),
      state CHAR(2),
      zip_code CHAR(5),
      country VARCHAR(255)
    );

    CREATE TABLE projects (
      project_id INT PRIMARY KEY,
      name VARCHAR(255),
      description TEXT,
      start_date DATE,
      end_date DATE,
      budget DECIMAL(10,2),
      department_id INT,
      location_id INT,
      FOREIGN KEY (department_id) REFERENCES departments(department_id),
      FOREIGN KEY (location_id) REFERENCES locations(location_id)
    );

    CREATE TABLE employee_projects (
      employee_id INT,
      project_id INT,
      role VARCHAR(255),
      PRIMARY KEY (employee_id, project_id),
      FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
      FOREIGN KEY (project_id) REFERENCES projects(project_id)
    );

# Populate the tables:

    INSERT INTO employees (employee_id, first_name, last_name, email, password, job_title, department, salary, hire_date)
    VALUES (1, 'John', 'Doe', 'john.doe@example.com', 'password', 'Software Engineer', 'Technology', 75000, '2022-01-01'),
           (2, 'Jane', 'Doe', 'jane.doe@example.com', 'password', 'Marketing Manager', 'Marketing', 65000, '2022-02-01'),
           (3, 'Bob', 'Smith', 'bob.smith@example.com', 'password', 'Human Resources Manager', 'Human Resources', 80000, '2022-03-01'),
           (4, 'Alice', 'Johnson', 'alice.johnson@example.com', 'password', 'Financial Analyst', 'Finance', 70000, '2022-04-01'),
           (5, 'Mike', 'Williams', 'mike.williams@example.com', 'password', 'Sales Representative', 'Sales', 55000, '2022-05-01');

    INSERT INTO departments (department_id, name, manager_id, budget)
    VALUES (1, 'Technology', 1, 500000),
           (2, 'Marketing', 2, 400000),
           (3, 'Human Resources', 3, 300000),
           (4, 'Finance', 4, 200000),
           (5, 'Sales', 5, 100000);

    INSERT INTO locations (location_id, name, address_1, address_2, city, state, zip_code, country)
    VALUES (1, 'Toronto Office', '123 Main Street', 'Suite 456', 'Toronto', 'ON', 'M5T 1T1', 'Canada'),
           (2, 'Vancouver Office', '789 Oak Avenue', '', 'Vancouver', 'BC', 'V6C 1C1', 'Canada'),
           (3, 'Montreal Office', '456 Birch Road', '', 'Montreal', 'QC', 'H3A 1A1', 'Canada');

    INSERT INTO projects (project_id, name, description, start_date, end_date, budget, department_id, location_id)
    VALUES (1, 'Website Redesign', 'Redesign the company website', '2022-01-01', '2022-06-01', 100000, 1, 1),
           (2, 'Marketing Campaign', 'Launch a new marketing campaign', '2022-02-01', '2022-07-01', 200000, 2, 2),
           (3, 'HRIS Implementation', 'Implement a new HRIS system', '2022-03-01', '2022-08-01', 300000, 3, 3);

    INSERT INTO employee_projects (employee_id, project_id, role)
    VALUES (1, 1, 'Lead Developer'),
           (2, 1, 'Project Manager'),
           (3, 2, 'Project Manager'),
           (4, 2, 'Financial Analyst'),
           (5, 3, 'Project Manager');



1. How many projects does each employee in the Sales department work on on average?

      SELECT AVG(num_projects) AS avg_num_projects

      FROM (

        SELECT COUNT(*) AS num_projects

        FROM employee_projects ep

        JOIN employees e ON ep.employee_id = e.employee_id

        WHERE e.department = 'Sales'

        GROUP BY ep.employee_id

        ) t;

![image](https://user-images.githubusercontent.com/119257994/209899670-32d387a9-3b7d-4d25-a4cb-e896494f1b7f.png)


2. Write a query that calculates the average salary for employees in each department, by job title.

        SELECT d.name as department, e.job_title, AVG(e.salary) as employee_average_salary

        FROM employees e

        JOIN departments d ON e.department = d.name

        GROUP BY e.job_title, d.name

        ORDER BY employee_average_salary

![image](https://user-images.githubusercontent.com/119257994/210009019-416ec964-f6f2-4a58-8407-70aef4611ce9.png)



3. Write a query that retrieves the project details, including the location and department names, for projects that have a budget greater than $100,000.

        SELECT p.name as project, l.name as location, d.name as department, d.budget

        FROM projects p

        JOIN locations l ON l.location_id = p.project_id

        JOIN departments d ON d.department_id =p.project_id

        WHERE d.budget > 100000

        ORDER by p.name

![image](https://user-images.githubusercontent.com/119257994/210013799-94894956-9aee-48f1-b0ed-664da31dff4e.png)



4. Write a query that retrieves the employee details, including the department and location names, for employees who are working on projects with budgets of at least $200,000 in the Montreal office.


        SELECT (cast(e.first_name as text) || " " || cast(e.last_name as text)) as employee, 
                d.name as department, 
                l.name as location, 
                p.name as project, 
                p.budget as project_budget

        FROM projects p 

        JOIN locations l on l.location_id = p.location_id

        JOIN departments d ON d.department_id = p.department_id

        JOIN employee_projects ep on ep.project_id = p.project_id

        JOIN employees e on e.employee_id = ep.employee_id

        WHERE l.name = "Montreal Office" and p.budget > 200000

        ORDER BY e.last_name, e.first_name;

Notice that employees don't have a direct connection to projects, department, and locations, so we used the table employee_projects to create the connection becuase employee_projects has project_id which connects to projects and projects connect to the rest.

![image](https://user-images.githubusercontent.com/119257994/210021538-8277fb49-a007-4456-bb7c-993c6232b7c2.png)




