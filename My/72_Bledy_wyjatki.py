try:
    print('Póbujemy podzielć')
    a = 2/'a'
    print(a)
except ZeroDivisionError:
    print('Nie można dzielić przez 0')  
except TypeError:
    print('Zmienna nie jest liczbą')

finally:
    print('Skonczono dzielenie')

