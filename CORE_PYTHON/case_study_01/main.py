from Empmanage import Empmanage
def login():
    em = Empmanage()
    uid = input("Enter userid:")
    password = input('Enter password:')
    if uid =='admin' and password == '1234':
        print("correct userid and password!")
        while True:
            print('\nPlease select 1 option from below:')
            print('1.AddEmployee')
            print('2.Display All Employee')
            print('3.Search Employee')
            print('4.Update Employee')
            print('5.Delete Employee')
            print('6.Exit')

            choice = int(input("Enter your choice:\n"))
            if choice == 1:
                em.AddEmp()
            elif choice == 2:
                em.DisplayEmp()
            elif choice == 3:
                em.SearchEmp()
            elif choice == 4:
                em.UpdateEmp()
            elif choice == 5:
                em.DeleteEmp()
            elif choice == 6:
                print("Thanks! come again")
                break
            else:
                print('incorrect choice !')
    else:
        print('check id and password again!')

login()