from functools import reduce
from client import client
from account import account
from movements import mov
import hashlib
import random


#login
print("------------Choose the type of user------------\n1) Registered user\n2) Create user")
print("------------------------------------------------")
us = int(input())
if us == 1:
    print("------------log in------------")
    user = input("Rut: ")
    v_pswrd = input("Password: ")
    #verify login
    pswrd_ci=hashlib.sha512(v_pswrd.encode('utf-8'))
    client.update_pswrd(pswrd_ci.hexdigest(), user)
    log_pswrd = (client.confirm_pswrd(user))
    cof_pswrd = (client.confirm_login(user))
    if log_pswrd == cof_pswrd:
        print("--------Access approved!--------")
        print("---------Main menu---------\n1) Manage Client\n2) Operations\n0) Exit")
        print("------------------------------------------------")
        menu = int(input())
        while menu!= 0:
            if menu == 1:
                # manage client menu
                print("-----Manage Client-----\n1) Modify data\n2) Consult Data\n3) View movement history\n0) Exit")
                print("------------------------------------------------")
                option = int(input())
                while option != 0:
                    if option == 1:
                        print("-----Manage Client-----\n1) Name\n2) Last name\n3) Rut\n4) City\n5) Direction\n6) Phone\n7) Email\n8) Password\n9) Delete Client\n0) Exit")
                        print("------------------------------------------------")
                        opc = int(input())
                        while opc != 0:
                            if opc == 1:
                                print("----Modify Client-----")
                                client.modify_name(input("Insert the new Name: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 2:
                                print("----Modify Last name-----")
                                client.modify_last_name(input("Insert the new Last name: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 3:
                                print("----Modify Rut-----")
                                client.modify_rut(input("Insert the new Rut: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 4:
                                print("----Modify City-----")
                                client.modify_city(input("Insert the new City: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 5:
                                print("----Modify Direction-----")
                                client.modify_direction(input("Insert the new Direction: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 6:
                                print("----Modify Email-----")
                                client.modify_email(input("Insert the new Email: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 7:
                                print("----Modify Phone-----")
                                client.modify_phone(input("Insert the new Phone: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 8:
                                print("----Modify Password-----")
                                client.modify_pswrd(input("Insert the new Password: "),user)
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 9:
                                print("----Delete Client-----")
                                client.delete_client(user)
                                print("---Deleted Client---")
                                print("------------Session Closed!------------")
                                quit()
                            elif opc == 0:
                                print("------------Session Closed!------------")
                                quit()
                            else:
                                print("Please type a valid option for the next one")
                                quit()
                    elif option == 2:
                        print("-----Consult Data-----")
                        client.consultation_client(user)
                        print("-------------------------")
                        account.consultation_account(user)
                        print("-------------------------")
                        print("------------Session Closed!!------------")
                        quit()

                    elif option ==3:
                        print("-----movement history-----")
                        print("-----History Deposit-----")
                        mov.set_deposit(user)
                        print("-----History Extract-----")
                        mov.set_extract(user)
                        print("------------Session Closed!------------")
                        quit()     
                                      
            elif menu == 2:
                # Operations
                print("-----What operation do you want to perform?-----\n1) Make a deposit\n2) make a turn\n3) Check the balance\n4) Exit")
                print("------------------------------------------------")
                ope = int(input())
                while ope != 0:
                    if ope == 1:
                        cash = account.cash(user)
                        acc = account.consultation_account_number(user)
                        print("--------------------------------------")
                        ingress = int(input("How much money do you want to deposit?: "))
                        cash += ingress
                        account.deposit(cash, user)
                        print("------------------------------------------------------------------------")
                        print("Deposit made successfully! Your current balance is: ",(account.cash(user)))
                        mov.register_deposit(acc,user,ingress,cash)
                        print("------------------------------------------------------------------------")
                        print("------------Session Closed!------------")
                        quit()
                    elif ope == 2:
                        cash = account.cash(user)
                        acc = account.consultation_account_number(user)
                        print("-----------------------------")
                        extract = int(input("How much money do you want to withdraw?: "))
                        if cash-extract < 0:
                            print("-------------------------------------------------------------")
                            print("your balance is insufficient, your balance is only: ",(account.cash(user)))
                            print("-------------------------------------------------------------")
                            print("------------Session Closed!------------")
                            quit()
                        else:
                            cash -= extract
                            account.extract(cash, user)
                            print("---------------------------------")
                            print("Your current balance is: ",(account.cash(user)))
                            mov.register_extract(acc,user,extract,cash)
                            print("---------------------------------")
                            print("------------Session Closed!------------")

                    elif ope == 3:
                        account.cash(user)

                    elif ope == 4:
                        print("------------Session Closed!------------")
                        quit()

                    else:
                        print("Please enter a valid option for the next")

            elif menu == 0:
                print("------------Exit!------------")

            else:
                print("Please enter a valid option for the next")

    else:
        print("--------Access denied!--------")
    
elif us == 2:
    # User register
    acc_nbr = reduce(lambda x, y: str(x) + str(y), map(lambda x: random.randint(1, 9), range(16)))
    print("-------------------User register-------------------")
    print("To create a new client enter the following data.")
    print("---------------------------------------------------------")
    client.register_client(input("Name: "),input("Last name: "),input("Rut: "),input("City: "),input("Direction: "),input("Phone: "),input("Email: "),input("Password: "),0)
    print("---------------------------------------------------------")
    rut = input("Confirm your Rut: ")
    pswrd=input("Confirm your Password: ")
    pswrd_encrypted=hashlib.sha512(pswrd.encode('utf-8'))
    client.modify_pswrd(pswrd_encrypted.hexdigest(), rut)
    account.register_account(acc_nbr,'vista',rut,0)
    print("------------Full user registration------------")

else:
    print("Please enter a valid option for the next")
