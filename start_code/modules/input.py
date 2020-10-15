from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

def opt_one():
    print_list(tasks)

def opt_two():
    print_list(get_uncompleted_tasks(tasks))

def opt_three():
        print_list(get_completed_tasks(tasks))

def opt_four():
        description = input("Enter task description to search for: ")
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)

def opt_five():
        time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_longer_than(tasks, time))

def opt_six():
        description = input("Enter task description to search for: ")
        print(get_task_with_description(tasks, description))

def opt_seven():
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)


