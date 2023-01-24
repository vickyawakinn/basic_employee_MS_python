
import time
from shutil import get_terminal_size
from os import system
from getpass import getpass
from sys import platform
import csv
from getch import getch
import maskpass
# import stdiomask
import getpass


def clear():
    if platform == 'linux':
        return system('clear')
    else:
        return system('cls')


cols = get_terminal_size().columns


def First_Page():

    print('-'*cols)
    print('|', 'Welcome to Our Employee Management System'.center(cols-4), '|')
    print('-'*cols)

    print('\n\n')

    print('\t\t1.  Get the List of all working Employees.\n')
    print('\t\t2.  Enter as an Employee.\n')
    print('\t\t3.  Enter as the Administrator.\n')
    print('\t\t4.  To quit the system.\n')

    print('\n')

    selection = input('\tEnter your selected preference here.  ')

    if selection == '1':
        all_emp_details(False)
    elif selection == '2':
        while True:
            x = authenticate('Employee')
            if x == -1:
                break
    elif selection == '3':
        while True:
            x = authenticate('Admin')
            if x == -1:
                break
    elif selection == '4':
        clear()
        quit()
    else:
        print('You have given an invalid input!'.rjust(cols))


def all_emp_details(fact):

    clear()
    print('\n')
    print('-'*cols)
    print('|', 'Here is the list of all the Employees'.center(cols-4), '|')
    print('-'*cols)

    print('\n\n')

    with open('emloyee_list.csv', 'r') as f:
        employees_list = csv.reader(f)
        employees_details = list(employees_list)
        print(employees_details)
        flag = 0
        if fact == False:
            for i in employees_details:
                if len(i) == 0:
                    continue
                print('\t', i[0].ljust(15), '|  ',
                      i[1].ljust(20), '|  ', i[2].ljust(25))
                if flag == 0:
                    print('\t', '_'*60)
                print()
                flag += 1
            print()
            go_back = input('\t\tPress Enter key to go back ')

        else:
            for i in employees_details:
                print(i[0].ljust(12), '|  ', i[1].ljust(15), '|  ', i[2].ljust(23), '|  ', i[3].ljust(
                    15), '|  ', i[4].ljust(10), '|  ', i[5].ljust(18), '|  ', i[6].ljust(20),)
                if flag == 0:
                    print('_'*cols)
                flag += 1
            print()
            print("\tPress q to go back, or c to make changes ")
            go_back = getch().decode()

            if go_back.lower() == 'q':
                print("Quiting Employees Detail Page.....".rjust(cols-10))
                time.sleep(3)
                return -1
                pass
            elif go_back.lower() == 'c':
                print('\n')
                val = input(
                    '\t\tEnter the Employee Id that you want to change ')
                for i in employees_details:
                    if i[0] == val:
                        adm = Person(
                            'admin_chng', i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                        break


def authenticate(name):

    clear()

    print('\n')

    print('-'*cols)
    print('|', 'Welcome to {} Login Page'.format(name).center(cols-4), '|')
    print('-'*cols)

    print('\n\n')

    print('\tFill up your details here - ')
    print('\n')

    id_ = input("\t\tEnter {} Id here  ".format(name))
    print()
    # pwd_ = stdiomask.getpass("\t\tEnter Id password here.  ")
    pwd_ = maskpass.askpass(prompt="\t\tEnter Id password here.  ", mask="*")

    print('\n\n')

    # selection = input("\tSelect y to confirm, b to go back  ")
    print('\tPress y to enter and b to return back to main menu. ')

    selection = getch().decode()

    if selection.lower() == 'y':

        f = open('emloyee_list.csv', 'r')
        f_reader = csv.reader(f)
        details = list(f_reader)
        if name.lower() == 'employee':
            for i in details:
                if id_ == i[0]:
                    if pwd_ == i[6]:
                        flag = 0
                        emp = Person(name, i[0], i[1], i[2],
                                     i[3], i[4], i[5], i[6])
                        break
                    else:
                        flag = 0
                        print()
                        print('Invalid Password :( Try Again.'.rjust(cols))
                        time.sleep(2)
                        break
                else:
                    flag = 1
            if flag == 1:
                print('Invalid Employee Id Given!'.rjust(cols-10))
                time.sleep(2)

        elif name.lower() == 'admin':
            if details[1][0] == id_:
                if details[1][6] == pwd_:
                    admin = Person(name, details[1][0], details[1][1], details[1][2],
                                   details[1][3], details[1][4], details[1][5], details[1][6])
                else:
                    print('Invalid Credentials :( Try Again')
                    time.sleep(2)
            else:
                print('Invalid Credentials :( Try Again! '.rjust(cols))
                time.sleep(2)
    elif selection == 'b':
        print("Quitting Employee Login Menu ....".rjust(cols-10))
        time.sleep(3)
        return -1

    else:
        print("Invalid key pressed!".rjust(cols-10))
        time.sleep(3)


class Person:

    def __init__(self, name, Id, Name, Desg, Joining, Salary, Project, Password):

        self.name = name
        self.Id = Id
        self.Id_len = 6
        self.Name = Name
        self.Name_len = 12
        self.Desg = Desg
        self.Desg_len = 20
        self.Joining = Joining
        self.Joining_len = 15
        self.Salary = Salary
        self.Salary_len = 10
        self.Project = Project
        self.Project_len = 18
        self.Password = Password
        self.Password_len = 15

        if (self.name).lower() == 'admin':
            while True:
                x = self.admin_in()
                if x == -1:
                    break
        elif (self.name).lower() == 'admin_chng':
            while True:
                x = self.employee_in('adm')
                if x == -1:
                    break
        else:
            while True:
                x = self.employee_in('emp')
                if x == -1:
                    break

    def employee_in(self, kota):

        clear()

        print('\n')

        print("-"*cols)
        print("|", "welcome {}".format(self.name).upper().center(cols-4), "|")
        print("-"*cols)
        print("\n\n")
        with open('emloyee_list.csv', 'r') as f:
            f_reader = csv.reader(f)
            details = list(f_reader)

            print('\t', details[0][0].ljust(self.Id_len), '|  ', details[0][1].ljust(self.Name_len), '|  ', details[0][2].ljust(self.Desg_len), '|  ', details[0][3].ljust(
                self.Joining_len), '|  ', details[0][4].ljust(self.Salary_len), '|  ', details[0][5].ljust(self.Project_len), '|  ', details[0][6].ljust(self.Password_len))

            print('_'*cols, '\n')

            for i in range(len(details)):
                if details[i][0] == self.Id:
                    print('\t', details[i][0].ljust(self.Id_len), '|  ', details[i][1].ljust(self.Name_len), '|  ', details[i][2].ljust(self.Desg_len), '|  ', details[i][3].ljust(
                        self.Joining_len), '|  ', details[i][4].ljust(self.Salary_len), '|  ', details[i][5].ljust(self.Project_len), '|  ', details[i][6].ljust(self.Password_len))
                    break
        print('\n\n')
        time.sleep(2)
        print("Press q to return and c to append your data. ")
        y = getch().decode()

        if y.lower() == 'q':
            return -1
        elif y.lower() == 'c':
            if kota == 'emp':
                print('\n\n')
                print(
                    '\tYou Dont have the Admin permission, You can only change your Id Password and Project Working\n')
                print('\t\t1.  To change your Project working on. ')
                print('\t\t2.  To change your Id Password.')
                print('\n')
                pref = input("\tEnter your preferences over here  ")

                if pref == '1':
                    while True:
                        x = self.change(self.Project)
                        if x == -1:
                            break
                elif pref == '2':
                    while True:
                        x = self.change(self.Password)
                        if x == -1:
                            break
                else:
                    print('Invalid Input given, try again!'.rjust(cols-10))
                    time.sleep(3)
            elif kota == 'adm':
                print('\n\n')
                print('\tYou can change any value for any Employee\n')
                print('\t\t1.  To change the Name')
                print('\t\t2.  To change the Designation')
                print('\t\t3.  To change the Joining Date')
                print('\t\t4.  To change the Salary')
                print('\t\t5.  To change the Project Working on')
                print('\t\t6.  To change the Id Password')
                print('\n')

                pref = input("\tEnter your preference over here  ")

                if pref == '1':
                    while True:
                        x = self.change(self.Name)
                        if x == -1:
                            break
                elif pref == '2':
                    while True:
                        x = self.change(self.Desg)
                        if x == -1:
                            break
                elif pref == '3':
                    while True:
                        x = self.change(self.Desg)
                        if x == -1:
                            break
                elif pref == '4':
                    while True:
                        x = self.change(self.Salary)
                        if x == -1:
                            break
                elif pref == '5':
                    while True:
                        x = self.change(self.Project)
                        if x == -1:
                            break
                elif pref == '6':
                    while True:
                        x = self.change(self.Password)
                        if x == -1:
                            break
                else:
                    print('Invalid Input Given, Try Again! ....'.rjust(cols-10))

    def admin_in(self):

        clear()

        print('-'*cols)
        print('|', 'Welcome Administrator'.center(cols-4), '|')
        print('-'*cols)

        print('\n\n')

        print('\t1.  To get a list of All working Employees.\n')
        print('\t2.  To add a new Employee to the list.\n')
        print('\t3.  To delete the record of an employee.\n')
        print('\t4.  To return back to main menu.\n')
        print()
        pref = input('\t\tEnter Your selected preference over here ')

        if pref == '1':
            while True:
                x = all_emp_details(True)
                if x == -1:
                    break
        elif pref == '2':
            while True:
                x = self.add_row()
                if x == -1:
                    break
        elif pref == '3':
            while True:
                x = self.del_row()
                if x == -1:
                    break
        elif pref == '4':
            return -1
        else:
            print("Invalid Input given".rjust(cols-10))
            time.sleep(3)

    def change(self, para):

        print('\n\n')
        if para == self.Password:
            # val = stdiomask.getpass("\tEnter the New Password        ")
            val = maskpass.askpass(
                prompt="\t\tEnter Id password here.  ", mask="*")
            print()
            # valu = stdiomask.getpass("\tEnter the New Password Again  ")
            valu = maskpass.askpass(
                prompt="\t\tEnter Id password here.  ", mask="*")

            if val == valu:

                with open('emloyee_list.csv', 'r') as f:
                    f_reader = csv.reader(f)
                    details = list(f_reader)

                    for i in details:
                        if i[0] == self.Id:
                            for j in range(len(i)):
                                if i[j] == para:
                                    i[j] = val
                                    break
                            break

                    with open('emloyee_list.csv', 'w', newline='') as f:
                        f_writer = csv.writer(f)
                        f_writer.writerows(details)

                    print('\n\n')
                    a = input(
                        "Id Password has been Changed !          (Press Enter to Continue)".center(cols))

            else:
                print('\n')
                print('Id Password did not Matched!'.rjust(cols-5))
                time.sleep(2)

            return -1

        else:
            val = input('\tEnter the New Value  ')

            with open('emloyee_list.csv', 'r') as f:
                f_reader = csv.reader(f)
                details = list(f_reader)

                for i in details:
                    if i[0] == self.Id:
                        for j in range(len(i)):
                            if i[j] == para:
                                i[j] = val
                                break
                        break

                with open('emloyee_list.csv', 'w', newline="") as f:
                    f_writer = csv.writer(f)
                    f_writer.writerows(details)

                print('\n\n')
                a = input(
                    "New Data has been Updated!                Press Enter to Continue.".center(cols))

            return -1

    def add_row(self):

        clear()

        print('-'*cols)
        print('|', 'Welcome Administrator'.center(cols-4), '|')
        print('-'*cols)

        print('\n\n')

        print('\tEnter the information of the New Employee \n')

        with open('emloyee_list.csv', 'r') as f:
            f_reader = csv.reader(f)
            detail = list(f_reader)

            last = detail[-1][0]
            l = list()
            l.append(int(last)+1)
            l.append(input("\t\tEnter the Name  ".rjust(30)))
            print()
            l.append(input("\t\tEnter the Designation  ".rjust(30)))
            print()
            l.append(input("\t\tEnter the Joining Date  ".rjust(30)))
            print()
            l.append(input("\t\tEnter the Salary  ".rjust(30)))
            print()
            l.append(input("\t\tEnter the Project Working  ".rjust(30)))
            print()
            l.append(input("\t\tEnter the Password  ".rjust(30)))

            with open('emloyee_list.csv', 'a', newline="") as j:
                j_apped = csv.writer(j)
                j_apped.writerow(l)

        print('\n')
        print("Information Updated Successfully!!".center(cols))
        time.sleep(3)
        return -1

    def del_row(self):

        clear()
        print('\n\n')

        print('-'*cols)
        print('|', 'Welcome Administrator to the Employee Record Delete Wizard'.center(
            cols-4), '|')
        print('-'*cols)

        print('\n\n')

        inf = input('\tEnter the Employee Id that you want to delete  ')

        print('\n\n')
        print('Are you sure you want to delete the Record of Employee with the Id {}'.format(
            inf).center(cols))
        print('\n')
        print('Press y to continue and N to exit '.center(cols))

        key = getch().decode()

        if key.lower() == 'y':

            with open('emloyee_list.csv', 'r') as f:
                f_reader = csv.reader(f)
                det = list(f_reader)

                for i in range(len(det)):
                    if det[i][0] == inf.strip():
                        st = i
                        break
                else:
                    print('\n')
                    print('Sorry No Record Found!'.ljust(cols))
                    time.sleep(3)
                    return 1
                with open('emloyee_list.csv', 'w', newline="") as j:
                    j_writer = csv.writer(j)

                    for i in range(len(det)):
                        if i == st:
                            continue
                        j_writer.writerow(det[i])

            print('\n\n')
            print('Employee Record Deleted Successfully!'.center(cols))
            time.sleep(3)
            return -1

        else:
            return -1


while True:
    clear()
    First_Page()

# admin = Person(Id, Name, Desg, Joining, Salary, Project, Password)
# employee = Person(Id, Name, Desg, Joining, Salary, Project, Password)
