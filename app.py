import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# DB
import sqlite3
from sqlite3 import Connection
conn = sqlite3.connect('data3.db')
c = conn.cursor()

# Functions
def init_db(conn: Connection):
    conn.execute('CREATE TABLE IF NOT EXISTS employeeTable(firstname TEXT, lastname TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT, ssn TEXT, withholding TEXT, salary TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS customerTable(company TEXT, firstname TEXT, lastname TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT, price TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS vendorTable(company TEXT, part TEXT, price TEXT, firstname TEXT, lastname TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT)')
    # Delete data
    # conn.execute("""DELETE FROM employeeTable WHERE firstname = 'Kai-Lin';""")
    conn.commit()

def add_employee(firstname, lastname, address1, address2, city, state, zipcode, ssn, withholding, salary):
    conn.execute('INSERT INTO employeeTable(firstname, lastname, address1, address2, city, state, zipcode, ssn, withholding, salary) VALUES (?,?,?,?,?,?,?,?,?,?)', (firstname, lastname, address1, address2, city, state, zipcode, ssn, withholding, salary))
    conn.commit()
def view_all_employees():
    query = conn.execute("SELECT * FROM employeeTable")
    #cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data = query.fetchall(), columns = ["First Name", "Last Name", "Address1", "Address2", "City", "State", "Zipcode", "SSN", "Withholding", "Salary"])
    return results
def view_all_employees_name():
    c.execute('SELECT DISTINCT firstname, lastname FROM employeeTable')
    data = c.fetchall()
    return data

def add_customer(company, firstname, lastname, address1, address2, city, state, zipcode, price):
    conn.execute('INSERT INTO customerTable(company, firstname, lastname, address1, address2, city, state, zipcode, price) VALUES (?,?,?,?,?,?,?,?,?)', (company, firstname, lastname, address1, address2, city, state, zipcode, price))
    conn.commit()
def view_all_customer():
    query = conn.execute("SELECT * FROM customerTable")
    #cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data = query.fetchall(), columns = ["Company Name", "First Name", "Last Name", "Address1", "Address2", "City", "State", "Zipcode", "Price"])
    return results

def add_vendor(company, part, price, firstname, lastname, address1, address2, city, state, zipcode):
    conn.execute('INSERT INTO vendorTable(company, part, price, firstname, lastname, address1, address2, city, state, zipcode) VALUES (?,?,?,?,?,?,?,?,?,?)', (company, part, price, firstname, lastname, address1, address2, city, state, zipcode))
    conn.commit()
def view_all_vendor():
    query = conn.execute("SELECT * FROM vendorTable")
    #cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data = query.fetchall(), columns = ["Company Name", "Part", "Price", "First Name", "Last Name", "Address1", "Address2", "City", "State", "Zipcode"])
    return results

def pay_employee(firstname):
    # c.execute("SELECT salary FROM employeeTable WHERE firstname = ?", (firstname,))
    # salary = c.fetchall()
    # return salary
    df = pd.read_sql("SELECT salary FROM employeeTable WHERE firstname = ?", params = (firstname,), con = conn)
    df.apply(pd.to_numeric)
    return df

# def get_blog_by_title(title):
#     c.execute('SELECT * FROM blogtable WHERE title = "{}"'.format(title))
#     data = c.fetchall()
#     return data


def main():
    st.title("TE566 Final Project")
    init_db(conn)
    menu = ["View Employees", "Add Employees",
            "View Customer", "Add Customer",
            "View Vendor", "Add Vendor",
            "Pay Employee"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View Employees":
        st.subheader("View Employees")
        result = view_all_employees()
        st.dataframe(result)
        #st.write(result)
    elif choice == "Add Employees":
        st.subheader("Add Employees")
        #create_table()
        new_firstname = st.text_input("First Name")
        new_lastname  = st.text_input("Last Name")
        new_address1 = st.text_input("Address1", max_chars = 50)
        new_address2 = st.text_input("Address2", max_chars = 50)
        new_city = st.text_input("City", max_chars = 50)
        new_state = st.text_input("State", max_chars = 50)
        new_zipcode = st.text_input("Zipcode", max_chars = 50)
        new_ssn = st.text_input("SSN", max_chars = 50)
        new_withholding = st.text_input("Withholdings", max_chars = 50)
        new_salary = st.text_input("Salary", max_chars = 50)

        if st.button("Add"):
            add_employee(new_firstname, new_lastname, new_address1, new_address2, new_city, new_state, new_zipcode, new_ssn, new_withholding, new_salary)
            st.success("New employee: {} {} added successfully.".format(new_firstname, new_lastname))

    if choice == "View Customer":
        st.subheader("View Customer")
        result = view_all_customer()
        st.dataframe(result)

    elif choice == "Add Customer":
        st.subheader("Add Customer")

        cus_company_name = st.text_input("Company Name")
        cus_firstname = st.text_input("First Name")
        cus_lastname  = st.text_input("Last Name")
        cus_address1 = st.text_input("Address1", max_chars = 50)
        cus_address2 = st.text_input("Address2", max_chars = 50)
        cus_city = st.text_input("City", max_chars = 50)
        cus_state = st.text_input("State", max_chars = 50)
        cus_zipcode = st.text_input("Zipcode", max_chars = 50)
        cus_price = st.text_input("Price", max_chars = 50)


        if st.button("Add"):
            add_customer(cus_company_name, cus_firstname, cus_lastname, cus_address1, cus_address2, cus_city, cus_state, cus_zipcode, cus_price)
            st.success("New customer added successfully.")

    if choice == "View Vendor":
        st.subheader("View Vendor")
        result = view_all_vendor()
        st.dataframe(result)

    elif choice == "Add Vendor":
        st.subheader("Add Vendor")

        ven_company_name = st.text_input("Company Name")
        ven_part = st.text_input("Part", max_chars = 50)
        ven_price = st.text_input("Price", max_chars = 50)
        ven_firstname = st.text_input("First Name")
        ven_lastname  = st.text_input("Last Name")
        ven_address1 = st.text_input("Address1", max_chars = 50)
        ven_address2 = st.text_input("Address2", max_chars = 50)
        ven_city = st.text_input("City", max_chars = 50)
        ven_state = st.text_input("State", max_chars = 50)
        ven_zipcode = st.text_input("Zipcode", max_chars = 50)

        if st.button("Add"):
            add_vendor(ven_company_name, ven_part, ven_price, ven_firstname, ven_lastname, ven_address1, ven_address2, ven_city, ven_state, ven_zipcode)
            st.success("New vendor added successfully.")

    # NOT FINNISHED
    # elif choice == "Pay Employee":
    #     st.subheader("Pay Employee")
    #     search_term = st.text_input('Enter Search Term')
    #     search_choice = st.radio("Field to Search By", ("First Name", "Last Name"))
    #     if st.button("Search"):
    #         if search_choice == "First Name":
    #             article_result = get_blog_by_title(search_term)
    #         elif search_choice == "Last Name":
    #             article_result = get_blog_by_author(search_term)

    elif choice == "Pay Employee":
        st.subheader("Pay Employee")
        result = view_all_employees()
        clean_db = pd.DataFrame(result, columns = ["First Name", "Last Name", "Address1", "Address2", "City", "State", "Zipcode", "SSN", "Withholding", "Salary"])
        st.dataframe(clean_db)

        employee_full_name = [str(i[0]) for i in view_all_employees_name()]

        selected_pay_employee = st.selectbox("Employee name", employee_full_name)
        # st.write(selected_pay_employee)
        if st.button("Pay employee"):
            st.write(pay_employee(selected_pay_employee))
            salary = pay_employee(selected_pay_employee)
            st.write(type(salary))

if __name__ == '__main__':
    main()
