import mysql.connector
from tabulate import tabulate
import sys


def x():
    db = mysql.connector.connect(host='localhost',
                                 database='BTS',
                                 user='root',
                                 port='3306',
                                 password='password')
    return db


def AdminCS():
    db = x()
    mycursor = db.cursor()
    print("1. View All Customers.\n"
          "2. Search Customer by Name.\n"
          "3. Search Customer by LoginID.\n"
          "4. EXIT.\n")

    choice01 = input("\nEnter your choice for Customer Services:(1/2/3/4)\n")
    if choice01 == '1':

        sql = "select*from customer"
        mycursor.execute(sql)

        AllRows = mycursor.fetchall()
        print('All Customers Data =', AllRows)
        if AllRows:
            table = tabulate(AllRows, headers=["LoginId", "Password", "Name", "Age", "Phone", "Email"],
                             tablefmt="pretty")
            print(table)

        AdminCS()

    elif choice01 == '2':
        nm = input("Enter the name of the customer to search :")
        try:
            sql = "select * from customer where custName='%s'"
            values = (nm)
            complete_sql = sql % values
            mycursor.execute(complete_sql)
            AllRows=mycursor.fetchall()
            print('All Customers Data =', AllRows)
            if AllRows:
                table = tabulate(AllRows, headers=["LoginId", "Password", "Name", "Age", "Phone", "Email"],
                                 tablefmt="pretty")
                print(table)

            if mycursor.rowcount == 0:
                    print("Invalid name ,Try again")
        except:
            print("Wrong information entered")
        AdminCS()

    elif choice01 == '3':
        userid = input("Enter the UserId of the customer to search :")
        try:
            sql = "select * from customer where custLoginId='%s'"
            values = (userid)
            complete_sql = sql % values
            mycursor.execute(complete_sql)
            AllRows = mycursor.fetchall()
            print('All Customers Data =', AllRows)
            if AllRows:
                table = tabulate(AllRows, headers=["LoginId", "Password", "Name", "Age", "Phone", "Email"],
                                 tablefmt="pretty")
                print(table)

            if mycursor.rowcount == 0:
                    print("Invalid UserId ,Try again")

        except IndexError:
            print("Invalid UserLoginID,Retry.")

        db.close()
        AdminCS()


    elif choice01 == '4':
        CodeForLogin()


def AdminES():
    db = x()
    mycursor = db.cursor()
    print("1. Add New Employee(Admin/Expert).\n"
          "2. View All Employee Data.\n"
          "3. Search Employee by Name.\n"
          "4. Search Employee by LoginID.\n"
          "5. Search Employee by Type(Admin/Expert).\n"
          "6. Activate or Deactivate Employee.\n"
          "7. Change Password\n"
          "8. EXIT.\n")

    print(
        "\n <<=========================================================================================================>> \n")

    choice = input("Enter Your Choice:(1/2/3/4/5/6/7/8)")

    if choice == '1':
        eid = input("Enter the LoginID:")
        epass = input("Enter the Password:")
        etype = input("Enter Type of Employee(ADMIN/EXPERT):")
        ename = input("Enter the name of Employee:")
        eph = int(input("Enter the PhoneNo. of Employee:"))
        email = input("Enter the Email ID of Employee:")
        estatus = input("Enter the status of Employee:")

        sql = "insert into employee(empLoginId,empPassword,empType,empName,empPhone,empEmail,empStatus) values('%s','%s','%s','%s',%d,'%s','%s')"
        values = (eid, epass, etype, ename, eph, email, estatus)
        print(sql % values)
        mycursor.execute(sql % values)

        print("\nEmployee added successfully.\n")
        mycursor.close()
        db.commit()
        AdminES()

    elif choice == '2':
        sql = "select*from employee"
        mycursor.execute(sql)
        AllRows = mycursor.fetchall()
        print('All Employees Data =\n\n', AllRows)

        if AllRows:
            table = tabulate(AllRows, headers=["empLoginId", "Password", "Type", "Name", "Phone", "Email", "Status"],
                             tablefmt="pretty")
            print(table)
        else:
            print("Employee Not Found.")
        db.commit()
        AdminES()


    elif choice == '3':
        name = input("Enter the employee name: ")
        query = "SELECT * FROM employee WHERE empName LIKE %s"
        mycursor.execute(query, ('%' + name + '%',))
        results = mycursor.fetchall()

        if results:
            table = tabulate(results, headers=["empLoginId", "empPassword", "Type", "empName", "Phone", "Email",
                                               "Status"], tablefmt="pretty")
            print(table)

        else:
            print("\nNO EMPLOYEE FOUND WITH THE NAME:", name)
        AdminES()


    elif choice == '4':
        eid = input("Enter the UserId of the Employee to search :")
        try:
            sql = "select * from employee where empLoginId='%s'"
            values = (eid)
            complete_sql = sql % values
            mycursor.execute(complete_sql)
            AllRows = mycursor.fetchall()
            print('All Employees Data =\n\n', AllRows)

            if AllRows:
                table = tabulate(AllRows,
                                 headers=["empLoginId", "Password", "Type", "Name", "Phone", "Email", "Status"],
                                 tablefmt="pretty")
                print(table)
            else:
                print("Employee Not Found.")
            db.commit()
        except IndexError:
            print("Invalid Employee LoginID,Retry.")
        AdminES()


    elif choice == '5':
        etype = input("Enter the Type of the Employee to search :")
        try:
            sql = "select * from employee where empType='%s'"
            values = (etype)
            complete_sql = sql % values
            mycursor.execute(complete_sql)
            AllRows = mycursor.fetchall()
            print('All Employees Data =\n\n', AllRows)

            if AllRows:
                table = tabulate(AllRows,
                                 headers=["empLoginId", "Password", "Type", "Name", "Phone", "Email", "Status"],
                                 tablefmt="pretty")
                print(table)
            db.commit()

        except IndexError:
            print("Invalid Employee Type,Retry.")
        AdminES()


    elif choice == '6':
        Status = input("Change the Status:")
        LoginId = input("Enter LoginId of Employee :")

        sql = "update employee set empStatus='%s' where empLoginId='%s'"

        values = (Status, LoginId)
        complete_sql = sql % values
        print("complete_sql = ", complete_sql)
        mycursor.execute(complete_sql)
        db.commit()
        if mycursor.rowcount == 1:
            print("Type updated successfully")
        else:
            print("Record update failed")
        AdminES()


    elif choice == '7':
        print()
        Password = input("Enter the new Password:")
        LoginId = input("Enter LoginId of Employee for Password update:")

        sql = "update employee set empPassword='%s' where empLoginId='%s'"

        values = (Password, LoginId)
        mycursor.execute(sql % values)
        db.commit()

        if mycursor.rowcount == 1:
            print("Password updated successfully")
        else:
            print("Record update failed")
        AdminES()



    elif choice=='8':
        CodeForLogin()

    db.commit()
    db.close()


def AdminBS():
    db = x()
    mycursor = db.cursor()
    print(
        "\n\n======================================================== WELCOME TO BUG SERVICES =======================================================\n\n")
    print("1. View All Bugs.")
    print("2. Search Bug by Bug Id.")
    print("3. Search Bug by Bug Status.")
    print("4. Search Bug by Customer Login Id.")
    print("5. Assign the Bug to Expert.")
    print("6. Logout.\n")

    choice = input("Enter Your Choice:(1/2/3/4/5/6)")

    if choice == '1':
        print("THIS IS TO VIEW ALL BUGS.")
        query = "SELECT * FROM bug"
        mycursor.execute(query)
        results = mycursor.fetchall()

        if results:
            table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                               "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                               "Feedback"],
                             tablefmt="pretty")
            print(table)
        else:
            print("NO BUGS FOUND")
        db.close()
        AdminBS()

    elif choice == '2':
        print("YOU CAN SEARCH BUG BY BUG ID.")
        BugId = input("Enter the LoginID of the BUG")
        sql = "select*from bug where bugId='%s'"
        value = (BugId)
        mycursor.execute(sql % value)

        try:
            print("Viewing Data of:", BugId)

            results = mycursor.fetchall()

            if results:
                table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                                   "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                                   "Feedback"],
                                 tablefmt="pretty")
                print(table)
            else:
                print("NO BUGS FOUND")
        except IndexError:
            print("Invalid BugId,Retry.")
        db.close()
        AdminBS()

    elif choice == '3':
        print("YOU CAN SEARCH BUG BY STATUS.")
        Status = input("Enter the Status of the Bug:")
        sql = "select*from bug where bugStatus='%s'"
        value = (Status)
        mycursor.execute(sql % value)

        try:
            results = mycursor.fetchall()

            if results:
                table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                                   "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                                   "Feedback"],
                                 tablefmt="pretty")
                print(table)
            else:
                print("NO BUGS FOUND")
        except IndexError:
            print("Invalid BUG Type, Retry.")
        db.close()
        AdminBS()

    elif choice == '4':
        print("YOU CAN SEARCH BUG BY CUSTOMER LOGIN ID.")
        cid = input("Enter the Customer Id:")
        sql = "select*from bug where custLoginId='%s'"
        value = (cid)
        mycursor.execute(sql % value)

        try:
            results = mycursor.fetchall()

            if results:
                table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                                   "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                                   "Feedback"],
                                 tablefmt="pretty")
                print(table)
            else:
                print("NO BUGS FOUND")
        except IndexError:
            print("Invalid Customer Id, Retry.")
        AdminBS()

    elif choice == '5':
        print("")
        print("5.Assign to Expert")

        expert_login_id = input("Enter the expert login ID: ")
        bug_id = int(input("Enter the bug ID: "))

        query = "update bug set expertLoginId = %s, bugStatus = 'Assigned', expertAssignedDate = NOW() " \
                "where bugId = %s"
        mycursor.execute(query, (expert_login_id, bug_id))
        db.commit()

        print("Bug assigned to expert successfully.")
        AdminBS()

    elif choice == '6':
        CodeForLogin()


def CustomerMod():
    db = x()
    mycursor = db.cursor()
    print(
        "\n\n**************************************************************  WELCOME TO CUSTOMER SERVICE  *****************************************************************\n\n")
    print("1. Update Account.")
    print("2. Post New Bug.")
    print("3. View all Bugs.")
    print("4. Search Bugs based on Status.")
    print("5. View Bug Solution.")
    print("6. Change Password.")
    print("7. EXIT.")

    print("\n=======================================================================\n")

    choice = input("Please Enter Your Choice Customer:(1/2/3/4/5/6/7)")

    if choice == '1':
        print()
        cust_name = input("Enter the updated customer name: ")
        cust_age = int(input("Enter the updated customer age: "))
        cust_phone = input("Enter the updated customer phone number: ")
        cust_email = input("Enter the updated customer email: ")
        cid=input("Enter the Login Id:")

        query = "UPDATE customer SET custName = %s, custAge = %s, custPhone = %s, custEmail = %s " \
                "WHERE custLoginId = %s"
        values = (cust_name, cust_age, cust_phone, cust_email, cid)
        mycursor.execute(query, values)
        db.commit()

        print(" YOUR ACCOUNT HAS BEEN UPDATES SUCCESSFULLY.")
        CustomerMod()

    elif choice == '2':
        print()
        cust_login_id = input("Enter your login ID: ")
        product_name = input("Enter the product name: ")
        bug_desc = input("Enter the bug description: ")

        query = "INSERT INTO bug (custLoginId, productName, bugDesc) VALUES (%s, %s, %s)"
        values = (cust_login_id, product_name, bug_desc)
        mycursor.execute(query, values)
        db.commit()

        print("YOUR BUG HAS BEEN POSTED SUCCESSFULLY.")
        CustomerMod()

    elif choice == '3':
        print()
        print("THIS IS TO VIEW ALL BUGS.")
        sql = "select*from bug"
        mycursor.execute(sql)

        results = mycursor.fetchall()

        if results:
            table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                               "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                               "Feedback"],
                             tablefmt="pretty")
            print(table)
        else:
            print("NO BUGS FOUND")

        CustomerMod()

    elif choice == '4':
        print()
        status = input("Enter the Status of Bug:")
        sql = "select*from bug where bugStatus='%s'"
        value = (status)
        mycursor.execute(sql % value)

        try:
            results = mycursor.fetchall()

            if results:
                table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                                   "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                                   "Feedback"],
                                 tablefmt="pretty")
                print(table)
            else:
                print("NO BUGS FOUND")
        except IndexError:
            print("Invalid Status, Retry.")

        CustomerMod()

    elif choice == '5':
        print()
        bid = input("Enter the Id of Bug:")
        sql = "select*from bug where bugId='%s'"
        value = (bid)
        mycursor.execute(sql % value)

        try:
            results = mycursor.fetchall()

            if results:
                table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                                   "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                                   "Feedback"],
                                 tablefmt="pretty")
                print(table)
            else:
                print("NO BUGS FOUND")
        except IndexError:
            print("Invalid BugId, Retry.")
        CustomerMod()

    elif choice == '6':
        print("\n")
        login_id = input("Enter your login ID: ")
        current_password = input("Enter your current password: ")
        new_password = input("Enter your new password: ")

        query = "SELECT custLoginId FROM customer WHERE custLoginId = %s AND custPassword = %s"
        mycursor.execute(query, (login_id, current_password))
        result = mycursor.fetchone()

        if result:

            query = "UPDATE customer SET custPassword = %s WHERE custLoginId = %s"
            mycursor.execute(query, (new_password, login_id))
            db.commit()
            print("Password changed successfully.")
        else:
            print("Invalid login ID or current password.")
        CustomerMod()

    elif choice=='7':
        CodeForLogin()


def ExpertMod():
    db = x()
    mycursor = db.cursor()
    print("\nTHIS IS EXPERT MODULE.\n")
    print("\nWELCOME EXPERT\n")
    print("1. View Assigned Bug.")
    print("2. Filter Assigned Bugs based on status.")
    print("3. Solve the Bug.")
    print("4. Change Password.\n")

    choice = input("Please Enter your Choice Expert:(1/2/3/4)")

    if choice == '1':
        print(" 1] View Assigned Bug")
        expert_login_id = input("Enter your login ID: ")
        query = "SELECT * FROM bug WHERE expertLoginId = %s"
        mycursor.execute(query, (expert_login_id,))
        results = mycursor.fetchall()

        if results:
            table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                               "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                               "Feedback"],
                             tablefmt="pretty")
            print(table)
        else:
            print("NO ASSIGNED BUGS FOUND FOR ID:", expert_login_id)

        ExpertMod()


    elif choice == '2':
        print("2] Filter Assigned Bugs based on status")
        expert_login_id = input("Enter your login ID: ")
        status = input("Enter the bug status: ")
        query = "SELECT * FROM bug WHERE expertLoginId = %s AND bugStatus = %s"
        mycursor.execute(query, (expert_login_id, status))
        results = mycursor.fetchall()

        if results:
            table = tabulate(results, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                               "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                               "Feedback"],
                             tablefmt="pretty")
            print(table)
        else:
            print("NO BUGS FOUND WITH SPECIFIED STATUS:", status)
        ExpertMod()

    elif choice == '3':
        print("3] Solve the Bug")
        bug_id = int(input("Enter the bug ID: "))
        query = "SELECT * FROM bug WHERE bugId = %s"
        mycursor.execute(query, (bug_id,))
        result = mycursor.fetchall()

        if result:
            table = tabulate(result, headers=["BugId", "BugEntered Date", "CustomerId", "BugStatus", "DeviceType",
                                              "BugDesc", "BugAssignedDate", "ExpertId", "BugSolvedDate", "BugSoln",
                                              "Feedback"],
                             tablefmt="pretty")
            print(table)

            solution = input("Enter the bug solution: ")
            query = "UPDATE bug SET bugStatus = 'Solved', bugSolvedDate = NOW(), solution = %s WHERE bugId = %s"
            mycursor.execute(query, (solution, bug_id))
            db.commit()

            print("BUG SOLUTION SUBMITTED SUCCESSFULLY ")
        ExpertMod()

    elif choice == '4':
        print("4] change password")
        eps = input("Enter the new password: ")
        eid = input("Enter empLoginId of employee for password update: ")

        sql = "update employee set empPassword ='%s' where empLoginId='%s'"

        values = (eps, eid)
        mycursor.execute(sql % values)
        db.commit()
        if mycursor.rowcount == 1:
            print("Record Updated successfully")
        else:
            print("Record update failed ")
        db.close()
        ExpertMod()

    elif choice == '5':
        print("5]exit")
        pass

def exit_program():
    print("Exiting the program.")
    sys.exit()


def CodeForLogin():
    db = x()
    mycursor = db.cursor()
    print(
        '\n\n***********************************************************************************        WELCOME TO BUG TRACKING SYSTEM         *************************************************************************************************************************** \n\n')
    while True:
        print('1. Employee Login.')
        print('2. Customer Login/Signup.')
        print('3. EXIT')

        print("\n<<===========================================================================>>\n")

        choice = input('Enter your choice:(1/2/3)')

        if choice == '1':
            print('\n=====================  THIS IS LOGIN BLOCK  =======================\n')

            while True:
                print("\n")
                login = input("Enter Your LoginID:")
                password = input("Enter your Password:")

                sql = "select * from employee where empLoginId = '%s' and empPassword='%s'"
                values = (login, password)
                mycursor.execute(sql % values)

                try:
                    while True:
                        row = mycursor.fetchmany(1)[0]
                        empPassword = row[1]
                        if password == empPassword:
                            print("Login authentication Successfully.\n\n")
                        empType = row[2]
                        if empType == 'ADMIN':
                            print(
                                "\n********************************************************  WELCOME ADMIN.  ****************************************************************\n")

                            while True:
                                print("***************************************************************************************************************")
                                print("\n\n1.Customer Service.")
                                print("2.Employee Service.")
                                print("3.Bug Service.")
                                print("4.EXIT\n\n")

                                choice2 = input("Please Enter Your Choice Admin.(1/2/3/4)")
                                if choice2 == '1':
                                    AdminCS()


                                elif choice2 == '2':
                                    AdminES()


                                elif choice2 == '3':
                                    print("")
                                    AdminBS()

                                elif choice2 == '4':
                                    CodeForLogin()


                        elif empType == 'EXPERT':
                                print("*****************************************************  WELCOME EXPERT.  ***************************************************")
                                ExpertMod()
                                break
                        else:
                            print("Login Authentication failed")
                            continue
                except IndexError:
                        print("Invalid User Name .Retry...")
                        continue

        elif choice == '2':
            print("**************************************** WELCOME CUSTOMER. *********************************************")
            print("THIS IS CUSTOMER LOGIN/SIGNUP.")
            print("1. Login.")
            print("2. Signup.")

            choice3 = input("\nEnter Your Choice:(1/2)")

            if choice3 == '1':
                login = input("Enter Your LoginID:")
                password = input("Enter your Password:")
                sql = "select * from customer where custLoginId = '%s' and custPassword='%s'"
                values = (login, password)
                mycursor.execute(sql % values)
                try:
                    row = mycursor.fetchmany(1)[0]
                    customerPassword = row[1]
                    if password == customerPassword:
                        print("Login authentication Successfully.")
                        print("Welcome Customer.\n", login)
                        CustomerMod()

                    else:
                        print("Login Authentication failed")
                        continue
                except IndexError:
                    print("Invalid User ID .Retry...")
                    continue

            elif choice3 == '2':
                print(
                    "\n***********************************  WELCOME TO THE SIGNUP PART.  ************************************\n")
                cid = input("Enter Your LoginId:")
                cpassword = input("Enter Your Password:")
                cname = input("Enter Your Name:")
                cage = int(input("Enter Your Age:"))
                cph = int(input("Enter Your Phone No. :"))
                cmail = input("Enter your Email Id:")

                sql = "insert into customer(custLoginId,custPassword,custName,custAge,custPhone,custEmail) values('%s','%s','%s',%d,%d,'%s'\n\n)"
                values1 = (cid, cpassword, cname, cage, cph, cmail)
                mycursor.execute(sql % values1)

                print("Customer data inserted successfully.")
                mycursor.close()
                db.commit()

        else:
            print(
                "\n\n********************************************   THIS IS EXIT BLOCK   ********************************************\n\n")
            print("1 NO")
            print("2 YES")
            choice12 = input("ARE YOU SURE YOU WANT TO EXIT ?(1/2)")
            if choice12 == '1':
                print("\n\n\n")
                CodeForLogin()
            elif choice12 == '2':
                print("=============================================================  THANK YOU FOR CHOOSING OUR SERVICE  =============================================================================")
                print("\n=================================  BYEE!! :)  ======================================\n")
                exit_program()


CodeForLogin()