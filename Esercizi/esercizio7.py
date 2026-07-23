#
# File: esercizio7.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/18
#
# Version: 1.0
#
# Description: Laboratorio di programmazione in Python - Esercizio 7 - Unpacking, Decoratori, Generatori, Lambda
#

def tabellina(num) : 
    '''Generatore che dato un numero genera la tabellina corrispondente'''
    for i in range(11) : 
        yield i, i * num


n = int(input('Quale tabellina si vuole verificare?'))
for moltiplicatore, risultato_corretto in tabellina(n) :
    risposta = input(f"Quanto fa {moltiplicatore} x {n}? (scrivere fine per terminare il programma)")
    if(risposta.lower() == 'fine') : 
        break
    if risposta == str(risultato_corretto) :
        print("Corretto!")
    else:
        print(f"Sbagliato! La risposta corretta è {risultato_corretto}")
