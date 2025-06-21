users:list=[
]


def add_user(users_data: list)->None:

         new_user_name=input('Podaj imię nowego znajomego: ')
         new_location=input('Podaj miasto pochodzenia nowego znajomego: ')
         new_posts=int(input('Podaj ilość postów nowego znajomego: '))
         users_data.append({'name':new_user_name,'location':new_location,'posts:':new_posts})
add_user(users)

print(users)
