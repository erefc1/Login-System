Password = 'Erefc123'
Password_Chances = int(3)

First_Password_Try = input('Podaj hasło: ')
if First_Password_Try == Password:
    print('Zostałeś zalogowany!')
else:
    print('Nie zostałeś zalogowany!')
    Password_Chances -= 1
    print(f"Pozostały ci {Password_Chances} szanse")
Second_Password_Try = input('Podaj hasło: ')
if Second_Password_Try == Password:
    print('\nZostałeś zalogowany!')
else:
    print('Nie zostałeś zalogowany!')
    Password_Chances -= 1
    print(f"Pozostały ci {Password_Chances} szanse")
Third_Password_Try = input('Podaj hasło: ')
if Third_Password_Try == Password:
    print('\nZostałeś zalogowany!')
else:
    print('Nie zostałeś zalogowany!')
    Password_Chances -= 1
if Password_Chances == 0:
    print("Niestety ale możliwość dalszej próby zalogowania nie istnieje \nSpróbuj później")
