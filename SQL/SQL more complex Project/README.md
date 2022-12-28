# Outline:
  
  Create the tables
  
  Populate the tables

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
































