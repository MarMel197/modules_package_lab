from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

while (True):
    print_menu()
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        opt_one()
    elif option == '2':
        opt_two()
       
    elif option == '3':
        opt_three()
        
    elif option == '4':
        opt_four()
        
    elif option == '5':
        opt_five()
    
    elif option == '6':
        opt_six()
        
    elif option == '7':
        opt_seven()
        
    else:
        print("Invalid Input - choose another option")
