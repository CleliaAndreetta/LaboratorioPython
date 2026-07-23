#
# File: esercizio8.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/19
#
# Description: Laboratorio di Programmazione in Python - Esercizio 8 - Gestione errori 
#

import json
import random

def gioco_impiccato_lbyl() : 
    '''Gioco dell'impiccato con un approcio LBYL'''
    with open('impiccato.json', 'r') as read_json : 
        parole = json.load(read_json)   
    if(len(parole) == 0) : 
        print('Nessuna parola disponibile!')
        return
    parola_segreta = random.choice(parole)
    tentativi_massimi = 8
    lettere_indovinate = []
    while(tentativi_massimi > 0) : 
        parola_completata = True
        for lettera in parola_segreta : 
            if lettera in lettere_indovinate : 
                print(lettera, end=' ')
            else : 
                print('_', end=' ')
                parola_completata = False
        print()
        if(parola_completata) : 
            print('Hai vinto')
            return
        print('Tentativi rimasti', tentativi_massimi)
        lettera = input('Inserisci una lettera: ').lower()
        if len(lettera) != 1:
            print('Inserisci una sola lettera.')
            continue

        if not lettera.isalpha():
            print('Devi inserire una lettera.')
            continue

        if lettera in lettere_indovinate:
            print('Hai già provato questa lettera.')
            continue

        lettere_indovinate.append(lettera)

        if lettera in parola_segreta:
            print('Lettera corretta!')
        else:
            print('Lettera sbagliata!')
            tentativi_massimi -= 1  
    print('Hai perso! La parola era', parola_segreta)
        
        
def gioco_impiccato_eafp():
    '''Gioco dell'impiccato con approccio EAFP'''
    try:
        with open('impiccato.json', 'r') as read_json:
            parole = json.load(read_json)
        parola_segreta = random.choice(parole).lower()
    except FileNotFoundError:
        print('File non trovato!')
        return
    except IndexError:
        print('Nessuna parola disponibile!')
        return
    lettere_indovinate = []
    tentativi_massimi = 6
    while tentativi_massimi > 0:
        parola_completata = True
        for lettera in parola_segreta : 
            if lettera in lettere_indovinate : 
                print(lettera, end=' ')
            else : 
                print('_', end=' ')
                parola_completata = False
        print()
        if parola_completata:
            print('Hai vinto!')
            return
        print('Tentativi rimasti', tentativi_massimi)
        lettera = input('Inserisci una lettera: ').lower()
        if len(lettera) != 1:
            print('Inserisci una sola lettera.')
            continue

        if not lettera.isalpha():
            print('Devi inserire una lettera.')
            continue

        if lettera in lettere_indovinate:
            print('Hai già provato questa lettera.')
            continue

        lettere_indovinate.append(lettera)

        if lettera in parola_segreta:
            print('Lettera corretta!')
        else:
            print('Lettera sbagliata!')
            tentativi_massimi -= 1      
    print('Hai perso! La parola era', parola_segreta)


#gioco_impiccato_eafp()
gioco_impiccato_lbyl()