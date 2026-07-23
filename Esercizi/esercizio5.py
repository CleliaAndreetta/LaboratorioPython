#
# File: esercizio5.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/17
#
# Version: 1.0
#
# Description: Problema delle 8 regine con permutazioni casuali
#

import random
import time


def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0) 

    # distanza lungo x
    dx = abs(x1 - x0)   
    
    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def tentativi_per_soluzione(n_lato):
    '''Trova una soluzione valida e conta tutti i tentativi'''
    random_generator = random.Random()
    tentativi = 0
    while True:
        tentativi += 1
        lista_soluzione = list(range(n_lato))
        random_generator.shuffle(lista_soluzione)
        soluzione_valida = True
        for col in range(n_lato):
            if incrocia_colonne(lista_soluzione, col):
                soluzione_valida = False
        if soluzione_valida:
            return (lista_soluzione, tentativi)


def trova_n_soluzioni_uniche(n_lato, n_soluzioni):
    '''Genera un numero fissato di soluzioni uniche'''
    totale_tentativi = 0
    soluzioni = []
    soluzioni_ripetute = {}
    inizio = time.time()
    while len(soluzioni) < n_soluzioni:
        soluzione, tentativi = tentativi_per_soluzione(n_lato)
        soluzione_tupla = tuple(soluzione)
        if (soluzione not in soluzioni):
            soluzioni.append(soluzione)
            totale_tentativi += tentativi
            soluzioni_ripetute[soluzione_tupla] = 1
            print("Soluzione", len(soluzioni), soluzione)
            print("Tentativi:", tentativi)
            print()
        else : 
            soluzioni_ripetute[soluzione_tupla] += 1 
    fine = time.time()
    print(soluzioni_ripetute)
    print("Tempo totale:", fine - inizio)
    print("Tempo medio per soluzione:", (fine - inizio) / n_soluzioni)
    print("Tentativi medi:", totale_tentativi / n_soluzioni)
    return soluzioni
    

def cerca_soluzione(n_lato, tempo_max) : 
    '''Cerca una solizione entro un limite di tempo'''
    random_generator = random.Random()
    soluzione_trovata = False
    inizio = time.time()
    while(soluzione_trovata == False and time.time() - inizio < tempo_max) : 
        lista_soluzione = list(range(n_lato))
        random_generator.shuffle(lista_soluzione)
        soluzione_trovata = True
        for col in range(n_lato):
            if incrocia_colonne(lista_soluzione, col):
                soluzione_trovata = False
        fine = time.time()
        if soluzione_trovata : 
            print('La soluzione', lista_soluzione, 'per una schacchiera di dimensione', n_lato, 'x', n_lato, 'è stata trovata in', fine - inizio, '<', tempo_max)
    return soluzione_trovata

def trova_n_max():
    '''Trova la massima dimensione di una scacchiera risolvibile entro 15 secondi'''
    n_lato = 8
    n_lato_max = 0
    while True:
        if cerca_soluzione(n_lato, 15):
            n_lato_max = n_lato
            n_lato += 1
        else:
            print("La scacchiera", n_lato, "x", n_lato, "non è stata risolta entro 15 secondi")
            return n_lato_max 
    
def rotazione_90(soluzione) : 
    '''Restituisce la soluzione ruotata di 90 gradi'''
    nuova_soluzione = [0, 0, 0, 0, 0, 0, 0, 0]
    for riga in range(len(soluzione)) : 
        colonna = soluzione[riga]
        nuova_riga = colonna
        nuova_colonna = len(soluzione) - riga - 1
        nuova_soluzione[nuova_riga] = nuova_colonna
    return nuova_soluzione
    

def rotazione_180(soluzione) : 
    '''Restituisce la soluzione ruotata di 180 gradi'''
    return rotazione_90(rotazione_90(soluzione))

def rotazione_270(soluzione) : 
    '''Restituisce la soluzione ruotata di 270 gradi'''
    return rotazione_90(rotazione_180(soluzione))

def soluzioni_simmetriche(n_lato, n_sol) : 
    '''Mostra le rotazioni delle soluzioni trovate'''
    soluzioni = trova_n_soluzioni_uniche(n_lato, n_sol)
    for soluzione in soluzioni : 
        print('Le 4 soluzione simmetriche a', soluzione, 'sono:')
        print(soluzione)
        print(rotazione_90(soluzione))
        print(rotazione_180(soluzione))
        print(rotazione_270(soluzione))


#programma principale(main)
trova_n_soluzioni_uniche(8, 6)
trova_n_max()
soluzioni_simmetriche(8, 5)