#
# File: esercizio1.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/14
#
# Version: 1.0
#
# Description: Laboratorio di programmazione in Python - Esercizio 1 - Funzioni
#

def is_pari(n) : 
    """Ritorna True se n è pari, False altrimenti"""
    if(n %  2 == 0) : 
        return True
    else : 
        return False

def is_int_positive() :
    """Chiede all'utente un numero intero positivo diverso da 0 e lo ritorna""" 
    n = int(input('\nInserisci un numero intero positivo diverso da 0: '))
    while(n <= 0 ) : 
        n = int(input('Inserisci un numero valido (intero positivo diverso da 0: )'))
    return n

def genera_lista(n) : 
    """Genera una particolare sequenza a partire da n e la ritorna sotto forma di lista"""
    lista = [n]
    while(n != 1 and len(lista) < 100) : 
        if(is_pari(n)) : 
            n = n //  2
        else :
            n = n * 3 + 1
        lista.append(n)
    return lista    

def analizza_sequenza(lista) : 
    """Data una lista ritorna il valore del massimo elemento, la lunghezza e la somma degli elementi della lista"""
    massimo = lista[0]
    somma = 0
    for i in lista : 
        if(i > massimo) : 
            massimo = i
        somma = somma + i
    return(massimo, len(lista), somma)   

def ricerca(lista) :
    "Data una lista stampa gli elementi divisibili per 5" 
    trovato = False
    for i in lista : 
        if(i % 5 == 0) : 
            print(i)
            trovato = True
    if(trovato == False) : 
        print('Nella lista non ci sono elementi divisibili per 5.')
        

# programma principale (main)
num = int(input("Inserire quanti numeri si vogliono testare: "))
max_len_seq = 0
num_seq_lunga = 0
for i in range(num) : 
    n = is_int_positive()
    print('\nNumero da analizzare: ', n)
    lista = genera_lista(n)
    print('Lista generata da ', n, ': ', lista)
    (massimo, lunghezza, somma) = analizza_sequenza(lista)
    print('Massimo: ', massimo)
    print('Lunghezza: ', lunghezza)
    print('Somma: ', somma)
    print('Numeri divisibili per 5: ')
    ricerca(lista)
    if(lunghezza > max_len_seq) : 
        max_len_seq = lunghezza
        num_seq_lunga = n
print('\nIl numero che ha generato la sequenza più lunga è ', num_seq_lunga, 'e la lunghezza della sequenza è ', max_len_seq)
