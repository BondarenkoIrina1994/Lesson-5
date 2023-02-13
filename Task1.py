# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def stepen_chisla(n,m): 
    if m==0: 
           return 1 
    if m<0: 
        return stepen_chisla(n,m+1)*(1/n) 
    return stepen_chisla(n,m-1)*n 
 
a=float(input('Ввeдите число A=')) 
b=int(input('Ввeдите число B=')) 
print(F'Число {a} в степени {b} равно {round(stepen_chisla(a,b),5)}!')
