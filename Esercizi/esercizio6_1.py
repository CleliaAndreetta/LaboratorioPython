#
# File: esercizio6_1.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/22
#
# Version: 1.0
#
# Description: Laboratorio di programmazione in Python - Esercizio 6 - OOP
#

from esercizio6 import Rubrica

lista_operazioni = ['APRI', 'AGGIUNGI', 'RIMUOVI', 'SALVA', 'STAMPA']
rubrica = None

while True:
    operazione = input('Operazione -> APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA, EXIT: ').upper()
    if (operazione == 'EXIT') :
        break
    if operazione not in lista_operazioni :
        print('operazione non valida!')
        continue
    if (operazione == 'APRI') :
        file = input('Nome file: ')
        f = file.split('.')
        estensione = f[1]
        if(estensione == 'json') : 
            rubrica = Rubrica.rubrica_JSON(file)
        elif(estensione == 'txt') : 
            rubrica = Rubrica.rubrica_txt(file)
        else : 
            print('Formato non supportato')
    elif (operazione == 'AGGIUNGI') :
        nome = input('Nome: ')
        giorno = input('Giorno: ')
        mese = input('Mese: ')
        anno = input('Anno: ')
        eta = input('Età: ')
        sesso = input('Sesso: ')
        mail = input('Mail: ')
        rubrica.aggiungi(nome, giorno, mese, anno, eta, sesso, mail)
    elif (operazione == 'RIMUOVI') :
        nome = input('Nome del contatto da rimuovere: ')
        rubrica.rimuovi(nome)
    elif (operazione == 'SALVA') :
        file = input('Nome file in cui salvare la rubrica: ')
        rubrica.salva(file)
    elif (operazione == 'STAMPA') :
        nome = input('Nome del contatto da stampare: ')
        rubrica.stampa(nome)
            
        
    
    