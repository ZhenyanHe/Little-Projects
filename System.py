
info = [{'id': '001', 'name': 'alice', 'tel': '86635312'}]

# define function
def info_print():
    print('Please Select--------------------------')
    print('1. Add user')
    print('2. Delete user')
    print('3. Edit user')
    print('4. Find user')
    print('5. Show all users')
    print('6. Exit')
    print('-'*20)


def add_info():
    """add user info"""
    new_id = input('Enter your student ID:')
    new_name = input('Enter your name:')
    new_tel = input('Enter your phone number:')
    global info
    for i in info:
        if new_name == i['name']:
            print('username exist! please try again!')
            return
    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    info.append(info_dict)
    print(info)
"""
def del_info():
    """"""
    del_name = input('Enter your name:')

    global info
    for i in info:
                if del_name == i['name']:
            info.remove(i)
            break
    else:
        print("username doesn't exist! please try again!")
"""

def modify_info():
    stu_name = input('please enter your name:')

    global info
    for i in info:
        if i['name'] == stu_name:
            change_tel = input('please enter your new telephone number:')
            i['tel'] = change_tel
            print(f'you have changed your contact into {change_tel}!')
            break
    else:
        print("username doesn't exist! please try again!")

def find_info():
    find_name = input('please enter username:')
    for i in info:
        find_name = i['name']
        print(f"your name is {i['name']}, your id is {i['id']}, your number is {i['tel']}'")
        break
    else:
        print("username doesn't exist! please try again!")

# make a loop and get user back to the home page until he/she enter 6
while True:
    info_print()
    user_num = int(input('Please select the service code:'))
    if user_num == 1:
        print('Add')
        add_info()
    elif user_num == 2:
        print('Delete')
        del_info()
    elif user_num == 3:
        print('Edit')
        modify_info()
    elif user_num == 4:
        print('Find')
        find_info()
    elif user_num == 5:
        print('Show all')
    elif user_num == 6:
        print("Exit")











