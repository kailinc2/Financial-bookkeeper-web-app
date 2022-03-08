import streamlit as st
st.set_page_config(layout="wide")

import time
import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Agg')

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
    # BS
    #conn.execute('DROP TABLE bsTable')
    conn.execute('CREATE TABLE IF NOT EXISTS bsTable(cash REAL, receivable REAL, inventory REAL, building REAL, equipment REAL, payable REAL, notes_payable REAL, accurals REAL, mortgage REAL, date REAL)')
    # conn.execute("""INSERT INTO bsTable(cash, receivable, inventory, building, equipment, payable, notes_payable, accurals, mortgage, date)
    #                 VALUES (
    #                 1234567,
    #                 0,
    #                 0,
    #                 500000,
    #                 0,
    #                 25000,
    #                 0,
    #                 0,
    #                 500000,
    #                 julianday('now', 'localtime') )""")
                    #julianday('now', 'localtime', '+1 months') )""")
                    #(cash, receivable, inventory, total_current_assets, building, equipment, total_fixed_assets, total_assets, payable, notes_payable, accurals, total_current_liabilities, mortgage, total_longterm_debt, total_liabilities, net_worth, total, date))
    # P&L
    #conn.execute('DROP TABLE plTable')
    conn.execute('CREATE TABLE IF NOT EXISTS plTable(sales_revenue REAL, cogs REAL, payroll REAL, payroll_withholding REAL, medicare REAL, annual_expenses REAL, date REAL)')
    # conn.execute("""INSERT INTO plTable VALUES(
    #                 805190,
    #                 299446,
    #                 0,
    #                 0,
    #                 3000,
    #                 29750,
    #                 julianday('now', 'localtime')
    #             )""")

    # Payroll History
    #conn.execute('DROP TABLE payrollHistoryTable')
    conn.execute('CREATE TABLE IF NOT EXISTS payrollHistoryTable(date REAL, employee TEXT, salary REAL, disbursement REAL, withholding REAL, federal_tax REAL, social_security_tax REAL, medicare REAL, total_disbursement REAL, total_withholding REAL)')
    # conn.execute("""INSERT INTO payrollHistoryTable VALUES(
    #                 julianday('now', 'localtime'),
    #                 'Colin',
    #                 52000,
    #                 35175,
    #                 14825,
    #                 11000,
    #                 3100,
    #                 725,
    #                 35175,
    #                 14825
    #                 )""")
    # conn.execute("""DELETE FROM payrollHistoryTable WHERE employee = 'Colin';""")
    #Delete data
    # conn.execute("""DELETE FROM employeeTable WHERE firstname = 'Kai-Lin';""")

    # Inventory
    #conn.execute('DROP TABLE inventoryTable')
    conn.execute('CREATE TABLE IF NOT EXISTS inventoryTable(Part TEXT, price_per_unit REAL, Quantity REAL, Value REAL, Reorder TEXT)')
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Axles',
    #                 0.01,
    #                 330000,
    #                 3300,
    #                 'No')""")
    #
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Screw',
    #                 0.02,
    #                 48250,
    #                 965,
    #                 'No')""")
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Meat',
    #                 3.5,
    #                 1000,
    #                 3500,
    #                 'No')""")
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Cheese',
    #                 0.4,
    #                 1000,
    #                 400,
    #                 'No')""")
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Olive oil',
    #                 0.1,
    #                 1000,
    #                 100,
    #                 'No')""")
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Mayonnaise',
    #                 0.5,
    #                 1000,
    #                 500,
    #                 'No')""")
    # conn.execute("""INSERT INTO inventoryTable(Part, price_per_unit, Quantity, Value, Reorder)
    #                 VALUES (
    #                 'Bread',
    #                 1.0,
    #                 500,
    #                 1000,
    #                 'No')""")

    # Stock Units
    conn.execute('CREATE TABLE IF NOT EXISTS stockTable(stock_units REAL)')
    # conn.execute("""INSERT INTO stockTable
    #                 VALUES (
    #                 100)""")
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

# Pay Employee
def get_salary(firstname):
    # # c.execute("SELECT salary FROM employeeTable WHERE firstname = ?", (firstname,))
    # # salary = c.fetchall()
    # # return salary
    # df = pd.read_sql("SELECT salary FROM employeeTable WHERE firstname = ?", params = (firstname,), con = conn)
    # #df.apply(pd.to_numeric)
    # return df
    c.execute("SELECT salary, firstname FROM employeeTable WHERE firstname = ?", (firstname,))
    data = c.fetchall()
    return data
def get_bs_nearest(nearest_time):
    c.execute("SELECT * FROM bsTable ORDER BY abs(julianday(?) - date) LIMIT 1 ", (nearest_time,))
    data = c.fetchall()
    return data
def get_the_last_bs_of_that_day(date_string):
    c.execute("SELECT * FROM bsTable WHERE date(date) = date(julianday(?)) ORDER BY abs(julianday(?) - date) DESC LIMIT 1 ", (date_string, date_string))
    data = c.fetchall()
    return data
def add_bs(cash, receivable, inventory, building, equipment, payable, notes_payable, accurals, mortgage, date):
    conn.execute('INSERT INTO bsTable(cash, receivable, inventory, building, equipment, payable, notes_payable, accurals, mortgage, date) VALUES (?,?,?,?,?,?,?,?,?,julianday(?))', (cash, receivable, inventory, building, equipment, payable, notes_payable, accurals, mortgage, date))
    conn.commit()
def get_pl_nearest(nearest_time):
    c.execute("SELECT * FROM plTable ORDER BY abs(julianday(?) - date) LIMIT 1 ", (nearest_time,))
    data = c.fetchall()
    return data
def get_the_last_pl_of_that_day(date_string):
    c.execute("SELECT * FROM plTable WHERE date(date) = date(julianday(?)) ORDER BY abs(julianday(?) - date) DESC LIMIT 1 ", (date_string, date_string))
    data = c.fetchall()
    return data
def add_pl(sales_revenue, cogs, payroll, payroll_withholding, medicare, annual_expenses, date):
    conn.execute('INSERT INTO plTable VALUES(?,?,?,?,?,?,julianday(?))', (sales_revenue, cogs, payroll, payroll_withholding, medicare, annual_expenses, date))
    conn.commit()

def get_payroll_history_nearest(nearest_time):
    c.execute("SELECT * FROM payrollHistoryTable ORDER BY abs(julianday(?) - date) LIMIT 1 ", (nearest_time,))
    data = c.fetchall()
    return data

def add_payroll_history(date, firstname, salary, total_disbursement, total_withholding):

    fed = salary * 0.22
    soc = salary * 0.062
    med = salary * 0.0145
    disbursement = salary - fed - soc - med
    withholding = fed + soc + med
    conn.execute('INSERT INTO payrollHistoryTable VALUES(julianday(?),?,?,?,?,?,?,?,?,?)', (date, firstname, salary, disbursement, withholding, fed, soc, med, total_disbursement + disbursement, total_withholding + withholding))
    conn.commit()

def view_all_inventory():
    query = conn.execute("SELECT * FROM inventoryTable")
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    return results




def main():
    st.title("TE566 Final Project")
    init_db(conn)
    # Approach 3: merge two dataframe
    # initialize balanced sheet
    # cash = 195397.5
    # receivable = 0
    # inventory = 26122.5
    # total_current_assets = cash + receivable + inventory
    # building = 0
    # equipment = 0
    # total_fixed_assets = building + equipment
    # total_assets = total_current_assets + total_fixed_assets
    #
    # payable = 0
    # notes_payable = 0
    # accurals = 0
    # total_current_liabilities = payable + notes_payable + accurals
    # mortgage = 200000
    # total_longterm_debt = mortgage
    # #total_liabilities = total_current_liabilities + total_longterm_debt
    # net_worth = total_assets - total_current_liabilities - total_longterm_debt
    # total = net_worth + total_current_liabilities + total_longterm_debt

    menu = ["View Employees", "Add Employees",
            "View Customer", "Add Customer",
            "View Vendor", "Add Vendor",
            "Pay Employee", "View Payroll History",
            "View Balanced Sheet", "View Income Statement",
            "View Inventory"]
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

    elif choice == "Pay Employee":
        st.subheader("Pay Employee")
        result = view_all_employees()
        clean_db = pd.DataFrame(result, columns = ["First Name", "Last Name", "Address1", "Address2", "City", "State", "Zipcode", "SSN", "Withholding", "Salary"])
        st.dataframe(clean_db)

        employee_first_name = [str(i[0]) for i in view_all_employees_name()]
        # Test: fetching database data by index
        # c.execute('SELECT DISTINCT firstname, lastname FROM employeeTable')
        # data = c.fetchall()
        # st.write(data[0][1])

        selected_pay_employee = st.selectbox("Employee name", employee_first_name)
        # st.write(selected_pay_employee)
        if st.button("Pay employee"):
            # get salary
            employee_info = get_salary(selected_pay_employee)
            salary = float(employee_info[0][0])
            employee_firstname = employee_info[0][1]

            # get time right now
            localtime = time.localtime()
            time_string_payEmployee = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
            # get BS data before payment
            bs_data = get_bs_nearest(time_string_payEmployee)
            # add BS data after payment
            add_bs(
                   bs_data[0][0] - salary, # cash - salary
                   bs_data[0][1],
                   bs_data[0][2],
                   bs_data[0][3],
                   bs_data[0][4],
                   bs_data[0][5],
                   bs_data[0][6],
                   bs_data[0][7],
                   bs_data[0][8],
                   time_string_payEmployee
                   )
            pl_data = get_pl_nearest(time_string_payEmployee)
            # add PL pl_data after payment
            add_pl(
                   pl_data[0][0],
                   pl_data[0][1],
                   pl_data[0][2] + 0.9*salary,
                   pl_data[0][3] + 0.1*salary,
                   pl_data[0][4],
                   pl_data[0][5],
                   time_string_payEmployee
                   )
            # Add Payroll History
            payroll_history_data = get_payroll_history_nearest(time_string_payEmployee)
            add_payroll_history(time_string_payEmployee, employee_firstname, salary, payroll_history_data[0][8], payroll_history_data[0][9])

            # Show UPDATED BS
            after_localtime = time.localtime()
            after_time_string_payEmployee = time.strftime("%Y-%m-%d %H:%M:%S", after_localtime)
            bs_data = get_bs_nearest(after_time_string_payEmployee)
            st.write("Balanced sheet updated:")
            data1 = [['Cash', bs_data[0][0]],
                    ['Account Receivable', bs_data[0][1]],
                    ['Inventory', bs_data[0][2]],
                    ['Total Current Assets', bs_data[0][0] + bs_data[0][1] + bs_data[0][2]],
                    ['Buildings', bs_data[0][3]],
                    ['Equipment', bs_data[0][4]],
                    ['Total Fixed Assets', bs_data[0][3] + bs_data[0][4]],
                    ['Total Assets', bs_data[0][0] + bs_data[0][1] + bs_data[0][2] + bs_data[0][3] + bs_data[0][4]]]
            d1 = pd.DataFrame(data1, columns = ['Current Asset', 'Value'])
            data2 = [['Accounts Payable', bs_data[0][5]],
                    ['Notes Payable', bs_data[0][6]],
                    ['Accurals', bs_data[0][7]],
                    ['Total Current Liabilities', bs_data[0][5] + bs_data[0][6] + bs_data[0][7]],
                    ['Mortgage', bs_data[0][8]],
                    ['Total Long Term Debt', bs_data[0][8]],
                    #['Total Liabilities', total_liabilities],
                    ['Net Worth', bs_data[0][0] + bs_data[0][1] + bs_data[0][2] + bs_data[0][3] + bs_data[0][4] - (bs_data[0][5] + bs_data[0][6] + bs_data[0][7] + bs_data[0][8])],
                    ['Total', bs_data[0][0] + bs_data[0][1] + bs_data[0][2] + bs_data[0][3] + bs_data[0][4] ]]
            d2 = pd.DataFrame(data2, columns = ['Liabilities & Net Worth', 'Values'])
            result = pd.concat([d1, d2], axis=1).reindex(d2.index).style.set_precision(2)
            st.write(result)

            # Show UPDATED PL
            # after_localtime = time.localtime()
            # after_time_string_payEmployee = time.strftime("%Y-%m-%d %H:%M:%S", after_localtime)
            data = get_pl_nearest(after_time_string_payEmployee)
            st.write("Income Statement updated:")
            gross_profit = data[0][0] - data[0][1]
            total_expenses = data[0][2] + data[0][3] + data[0][4] + data[0][5]
            ebt = gross_profit - total_expenses
            data1 = [['Sales Revenue', data[0][0]],
                    ['COGS', data[0][1]],
                    ['Gross Profit', gross_profit],
                    ['Payroll', data[0][2]],
                    ['Payroll Withholding', data[0][3]],
                    ['Medicare', data[0][4]],
                    ['Annual Expenses', data[0][5]],
                    ['Total Expenses', total_expenses],
                    ['Earnings Before Taxes', ebt],
                    ['Taxes', 0.20 * ebt],
                    ['Net Income', ebt - 0.20*ebt]]
            d1 = pd.DataFrame(data1, columns = ['Income Statement', 'Value']).style.set_precision(2)
            st.dataframe(d1, height = 900)



    elif choice == "View Balanced Sheet":
        st.subheader("View Balanced Sheet")

        st.write("View all BS records")
        # view all BS
        query = conn.execute("SELECT cash, receivable, inventory, building, equipment, payable, notes_payable, accurals, mortgage, date(date), time(date), date FROM bsTable")
        cols = [column[0] for column in query.description]
        results = pd.DataFrame.from_records(data = query.fetchall(), columns = ["Cash", "Receivable", "Inventory", "Building", "equipment", "payable", "notes_payable", "accurals", "mortgage", "date", "time", "julian"])
        st.dataframe(results)
        # st.dataframe(results.style.set_precision(2))

        # get time right now
        named_tuple = time.localtime()
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
        date_string = time.strftime("%Y-%m-%d", named_tuple)

        data = get_bs_nearest(time_string)
        # data = get_the_last_bs_of_that_day("2022-02-26")
        #st.write(data)

        st.write("View **latest** Balanced Sheet")
        data1 = [['Cash', data[0][0]],
                ['Account Receivable', data[0][1]],
                ['Inventory', data[0][2]],
                ['Total Current Assets', data[0][0] + data[0][1] + data[0][2]],
                ['Buildings', data[0][3]],
                ['Equipment', data[0][4]],
                ['Total Fixed Assets', data[0][3] + data[0][4]],
                ['Total Assets', data[0][0] + data[0][1] + data[0][2] + data[0][3] + data[0][4]]]
        d1 = pd.DataFrame(data1, columns = ['Current Asset', 'Value'])
        data2 = [['Accounts Payable', data[0][5]],
                ['Notes Payable', data[0][6]],
                ['Accurals', data[0][7]],
                ['Total Current Liabilities', data[0][5] + data[0][6] + data[0][7]],
                ['Mortgage', data[0][8]],
                ['Total Long Term Debt', data[0][8]],
                #['Total Liabilities', total_liabilities],
                ['Net Worth', data[0][0] + data[0][1] + data[0][2] + data[0][3] + data[0][4] - (data[0][5] + data[0][6] + data[0][7] + data[0][8])],
                ['Total', data[0][0] + data[0][1] + data[0][2] + data[0][3] + data[0][4] ]]
        d2 = pd.DataFrame(data2, columns = ['Liabilities & Net Worth', 'Values'])
        result = pd.concat([d1, d2], axis=1).reindex(d2.index).style.set_precision(2)
        st.write(result)


        # Approach 2
        # # initialize list of lists
        # data = [['Cash', 195397.5, 'Accounts Payable', 0],
        #         ['Account Receivable', 0, 'Notes Payable', 0],
        #         ['Inventory', 26122.5, 'Accurals', 0]]
        # # Create the pandas DataFrame
        # df = pd.DataFrame(data, columns = ['Current Asset', 'Value', 'Liabilities & Net Worth', 'Values'])
        # # print dataframe.
        # st.write(df)


        # Approach 1
        # col1, col2 = st.columns(2)
        # with col1:
        #     col1.subheader("Current Asset")
        #     # initialize list of lists
        #     data = [['Cash', 195397.5], ['Account Receivable', 0], ['Inventory', 26122.5]]
        #     # Create the pandas DataFrame
        #     df = pd.DataFrame(data, columns = ['Current Asset', 'Value'])
        #     # print dataframe.
        #     st.write(df)
        # with col2:
        #     col2.subheader("Liabilities and Net Worth")
        #     # initialize list of lists
        #     data = [['Cash', 195397.5], ['Account Receivable', 0], ['Inventory', 26122.5]]
        #     # Create the pandas DataFrame
        #     df = pd.DataFrame(data, columns = ['Current Asset', 'Value'])
        #     # print dataframe.
        #     st.write(df)

    elif choice == "View Income Statement":
        st.subheader("View Income Statement")

        st.write("View all Income Statement records")
        # view all Income Statement
        query = conn.execute("SELECT sales_revenue, cogs, payroll, payroll_withholding, medicare, annual_expenses, date(date), time(date), date FROM plTable")
        cols = [column[0] for column in query.description]
        results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
        st.dataframe(results)

        # get time right now
        named_tuple = time.localtime()
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
        date_string = time.strftime("%Y-%m-%d", named_tuple)

        data = get_pl_nearest(time_string)
        # data = get_the_last_bs_of_that_day("2022-02-26")
        #st.write(data)

        st.write("View **latest** Income Statement")
        gross_profit = data[0][0] - data[0][1]
        total_expenses = data[0][2] + data[0][3] + data[0][4] + data[0][5]
        ebt = gross_profit - total_expenses
        data1 = [['Sales Revenue', data[0][0]],
                ['COGS', data[0][1]],
                ['Gross Profit', gross_profit],
                ['Payroll', data[0][2]],
                ['Payroll Withholding', data[0][3]],
                ['Medicare', data[0][4]],
                ['Annual Expenses', data[0][5]],
                ['Total Expenses', total_expenses],
                ['Earnings Before Taxes', ebt],
                ['Taxes', 0.20 * ebt],
                ['Net Income', ebt - 0.20*ebt]]
        d1 = pd.DataFrame(data1, columns = ['Income Statement', 'Value']).style.set_precision(2)
        st.dataframe(d1, height = 900)

    elif choice == "View Payroll History":
        st.subheader("View Payroll History")

        # TODO: """change col name of disbursement to AMOUNT PAID"""
        # View Payroll History
        query = conn.execute("SELECT date(date), employee, salary, disbursement, withholding, federal_tax, social_security_tax, medicare, total_disbursement, total_withholding FROM payrollHistoryTable")
        # cols = [column[0] for column in query.description]
        cols = ["Date", "Employee", "Salary", "Amount paid", "Withholding", "Federal Tax", "Social Security Tax", "Medicare", "Total Amount Paid", "Total Withholding"]
        results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols).style.set_precision(2)
        st.dataframe(results)

        # Additionally Display Total Disbursement (Total Amount Paid) and Total Withholding
        named_tuple = time.localtime()
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
        date_string = time.strftime("%Y-%m-%d", named_tuple)
        data = get_payroll_history_nearest(time_string)
        data1 = [[data[0][8], data[0][9]]]
        d1 = pd.DataFrame(data1, columns = ['Total Amount Paid', 'Total Withholding']).style.set_precision(2)
        st.dataframe(d1)

    elif choice == "View Inventory":
        st.subheader("View Inventory")
        result = view_all_inventory()
        st.dataframe(result.style.set_precision(2))

        # Second Table in View Inventory
        c.execute('SELECT price_per_unit, Quantity, Value FROM inventoryTable')
        data = c.fetchall()
        price_per_unit_sum = 0
        total_value_sum = 0
        quantity = 1e9
        for i in data:
            price_per_unit_sum += i[0]
            total_value_sum += i[2]
            quantity = min(quantity, i[1])

        d1 = pd.DataFrame([[total_value_sum, price_per_unit_sum, quantity]], columns = ['Total Value', 'COG/Unit', 'Total Units that can be built from current parts']).style.set_precision(2)
        st.dataframe(d1)

        # Third Table in View Inventory
        c.execute('SELECT stock_units FROM stockTable LIMIT 1')
        stock_units = c.fetchall()
        
        total_val = stock_units[0][0] * price_per_unit_sum
        d2 = pd.DataFrame([[stock_units[0][0], total_val]], columns = ['Complete Units in Stock', 'Total Value']).style.set_precision(2)
        st.dataframe(d2)

if __name__ == '__main__':
    main()
