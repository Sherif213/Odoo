# HR Grade Management Module

---

## Company Structure

### **Grade 1**
- **Product Manager**
- **Production Manager**
- **Sales Manager**
- **CFO**
- **IT Manager**
- **HR Manager**
- **Compliance Officer**
- **Customer Support Manager**
- **Account Manager**
- **Marketing Manager**

### **Grade 2**
- **Hardware Engineer**
- **Software Engineer**
- **Firmware Engineer**
- **Quality Assurance Engineer**
- **Manufacturing Engineer**
- **Supply Chain Engineer**

### **Grade 3**
- **Digital Marketing Specialist**
- **Customer Support Specialist**
- **Logistics Coordinator**
- **Financial Analyst**
- **Data Analyst**
- **E-commerce Specialist**
- **Talent Acquisition Specialist**
- **Training and Development Specialist**
- **Customer Support Specialist**

### **Grade 4**
- **Accountant**
- **Legal Advisor**

### **Grade 5**
- **Driver**
- **Cafe Workers**
- **Cleaning Workers**
- **General Workers**

---

## Database Structure

The module is based on a structured database schema with the **Grade** table, containing the following fields:

### **Basic Information:**
1. **grade_number**  
   - The grade number of the employee.

2. **medical_allowance**  
   - The medical allowance for the employee.

3. **internet_allowance**  
   - The internet allowance for the employee.

4. **insurance_allowance**  
   - The insurance allowance for the employee.

5. **female_allowance**  
   - Only eligible for females.

6. **food_allowance**  
   - Only eligible for employees working on-site.
   
7. **travel_allowance**  
   - Only eligible for employees working on-site.
   
8. **device_allowance**  
   - Only eligible for employees working on-site.

9. **sales_bonus_rate**  
   - Only eligible for employees in the sales department (varies by grade).

10. **loyalty_allowance**  
   - All employees are eligible, but the amount depends on every 3 years of service.
---
## SQL Constraints  

We have two types of constraints: **SQL constraints**, which apply constraints in the data tier.  
The constraints can be written like this:  

```python
SQL_constraints = [(name, sql_def, message)]
```

SQL constraints can be either **NOT NULL**, **UNIQUE**, or **CHECK**.  

## Python Constraints  

We also have another type of constraint used to guarantee **data uniformity** in the logic code.  
These constraints are exclusive to **Python** and are implemented using the `@api.constrains` decorator,  
which allows functions to verify the inputted data.  

## Application Tier Constraints  

Additionally, we have constraints on the **application tier**, but it is the weakest one among all.  
I did not use it in my code.  

## Security Access  

Security access contains permissions for **reading, writing, creating, and deleting (CRUD)**.  
It can be applied at different levels:  

- **Presentation Layer**: Can be applied to **tree view** or **form view**.  
- **Logic Tier**: Controls access within the backend logic.  
- **User-based Restrictions**: Can be applied for each user using the database.  

## Hosted Localhost  

My localhost is hosted online at:  
[https://9555-78-163-113-14.ngrok-free.app/web/login](https://9555-78-163-113-14.ngrok-free.app/web/login)  

### Admin Credentials:  
- **Username**: `admin`  
- **Password**: `admin`  
