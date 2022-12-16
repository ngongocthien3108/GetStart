User_name = input().split()

if len(User_name) == 3:
    print(f'{User_name[2]}, {User_name[0][0]}.{User_name[1][0]}.')

elif len(User_name) == 2:
    print(f'{User_name[1]}, {User_name[0][0]}.')
    
