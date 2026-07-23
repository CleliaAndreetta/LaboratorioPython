#
# File: gestione_torneo.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/18
#
# Version: 1.0
#
# Description: Programma per la gestione di un torneo di giochi (Morra cinese, Pari o dispari, Indovina numero)
#

from giocatore import Giocatore 
import random
import json

giocatori = {}

def aggiungi_giocatore() : 
    '''Aggiunge un nuovo giocatore al torneo verificando che l'ID scelto non si già in uso'''
    nome = input('Nome giocatore: ')
    id_giocatore = input('ID giocatore: ')
    while(id_giocatore in giocatori) : 
        print('ID già in uso.')
        id_giocatore = input('ID giocatore: ')
    nuovo_giocatore = Giocatore(nome, id_giocatore)
    giocatori[id_giocatore] = nuovo_giocatore
    print('Benvenuto', id_giocatore)
    
def mostra_giocatori():
    '''Stampa a video i nomi e i corrispettivi ID di tutti i giocatori che partecipano al torneo'''
    if len(giocatori) == 0:
        print("Nessun giocatore registrato")
        return
    for giocatore in giocatori.values():
        print(giocatore)
        
def carica_giocatori_json() : 
    '''Carica dal file JSON i giocatori precedentemente salvati e ricostruisce il dizionario dei giocatori.'''
    try : 
        with open('giocatori.json', 'r') as read_file_giocatori : 
            dati = json.load(read_file_giocatori)
            for id_giocatore, dati_giocatore in dati.items() : 
                giocatore = Giocatore(dati_giocatore['nome'], id_giocatore)
                giocatore.statistiche = dati_giocatore['statistiche']
                giocatori[id_giocatore] = giocatore
    except FileNotFoundError: 
        print('Nessun file di salvataggio trovato')

def salva_giocatori_json() : 
    '''Salva sul file JSON tutti i giocatori e le relative statistiche'''
    dati = {}
    for id_giocatore, giocatore in giocatori.items() : 
        dati[id_giocatore] = giocatore.to_dict()
    with open('giocatori.json', 'w') as write_file_giocatori : 
        json.dump(dati, write_file_giocatori)
        
def seleziona_giocatore() : 
    '''Seleziona un giocatore tramite ID e se non è presente nel dizionario è possibile aggiungerlo'''
    while True:
            id_giocatore = input('ID giocatore: ')
            if id_giocatore in giocatori:
                giocatore = giocatori[id_giocatore]
                break
            risposta = input('Giocatore non trovato. Vuoi aggiungerlo? (si/no): ')
            if risposta.lower() == "si":
                aggiungi_giocatore()
    return giocatore

def seleziona_due_giocatori():
    '''Seleziona due giocatori tramite ID e se non sono presenti nel dizionario è possibile aggiungerli'''
    while True:
        id_giocatore = input('ID giocatore 1: ')
        if id_giocatore in giocatori:
            giocatore1 = giocatori[id_giocatore]
            break
        risposta = input('Giocatore non trovato. Vuoi aggiungerlo? (si/no): ')
        if risposta.lower() == "si":
            aggiungi_giocatore()
    while True:
        id_giocatore = input('ID giocatore 2: ')
        if id_giocatore in giocatori:
            giocatore2 = giocatori[id_giocatore]
            break
        risposta = input('Giocatore non trovato. Vuoi aggiungerlo? (si/no): ')
        if risposta.lower() == "si":
            aggiungi_giocatore()
    return (giocatore1, giocatore2)

def mostra_statistiche_giocatore():
    '''Stampa a video le statistiche dei giocatori'''
    id_giocatore = input('ID giocatore: ')
    if id_giocatore not in giocatori:
        print('Giocatore non trovato')
        return
    giocatore = giocatori[id_giocatore]
    print('ID:', giocatore.id_giocatore)
    for gioco, statistiche in giocatore.statistiche.items():
        print(f'\n{gioco}')
        print('Vittorie:', statistiche['vittorie'])
        print('Sconfitte:', statistiche['sconfitte'])
        print('Pareggi:', statistiche['pareggi'])

def morra_cinese() : 
    '''Gestisce una parita di morra cinese e aggiorna le statistiche'''
    giocatore_1, giocatore_2 = seleziona_due_giocatori()
    while True : 
        scelta_1 = input(f'{giocatore_1.id_giocatore} - sasso, carta, forbice: ').lower()
        if (scelta_1 in ['sasso', 'carta', 'forbice']) : 
            break
        print('Input non valido!')
    while True : 
        scelta_2 = input(f'{giocatore_2.id_giocatore} - sasso, carta, forbice: ').lower()
        if (scelta_2 in ['sasso', 'carta', 'forbice']) : 
                    break
        print('Input non valido!')
    if(scelta_1 == scelta_2) : 
        print('Pareggio!')
        giocatore_1.aggiungi_pareggio('Morra cinese')
        giocatore_2.aggiungi_pareggio('Morra cinese')
    elif ((scelta_1 == 'sasso' and scelta_2 == 'forbice') or (scelta_1 == 'forbice' and scelta_2 == 'carta') or (scelta_1 == 'carta' and scelta_2 == 'sasso')) :
        print('Vince', giocatore_1.id_giocatore)
        giocatore_1.aggiungi_vittoria('Morra cinese')
        giocatore_2.aggiungi_sconfitta('Morra cinese')
    else:
        print('Vince', giocatore_2.id_giocatore)
        giocatore_2.aggiungi_vittoria('Morra cinese')
        giocatore_1.aggiungi_sconfitta('Morra cinese')

def pari_dispari() : 
    '''Gestisce le partite di pari o dispari e aggiorna le statistiche'''
    giocatore_1, giocatore_2 = seleziona_due_giocatori()
    while True : 
        scelta_1 = input(f'{giocatore_1.id_giocatore} - pari o dispari: ').lower()
        if (scelta_1 in ['pari', 'dispari']) :
            break
        print('Input non valido!')
    if(scelta_1 == 'pari') : 
        print(giocatore_2.id_giocatore, 'gioca dispari')
    else : 
        print(giocatore_2.id_giocatore, 'gioca pari')
    while True : 
        try : 
            numero_1 = int(input(f'{giocatore_1.id_giocatore} - scegli un numero da 1 a 5: '))
            if(numero_1 in range(1, 6, 1)) : 
                break
            input('Scegli un numero da 1 a 5')
        except ValueError: 
            print('Input non valido')
    while True : 
        try : 
            numero_2 = int(input(f'{giocatore_2.id_giocatore} - scegli un numero da 1 a 5: '))
            if(numero_1 in range(1, 6, 1)) : 
                break
            input('Scegli un numero da 1 a 5')
        except ValueError: 
            print('Input non valido')
    if(scelta_1 == 'pari' and (numero_1 + numero_2) % 2 == 0) : 
        print('Vince', giocatore_1.id_giocatore) 
        giocatore_1.aggiungi_vittoria('Pari o dispari')
        giocatore_2.aggiungi_sconfitta('Pari o dispari')
    elif(scelta_1 == 'dispari' and (numero_1 + numero_2) % 2 != 0) : 
        print('Vince', giocatore_1.id_giocatore) 
        giocatore_1.aggiungi_vittoria('Pari o dispari')
        giocatore_2.aggiungi_sconfitta('Pari o dispari')
    else : 
        print('Vince', giocatore_2.id_giocatore)
        giocatore_2.aggiungi_vittoria('Pari o dispari')
        giocatore_1.aggiungi_sconfitta('Pari o dispari')
        
def indovina_numero():
    '''Gestisce una partita di indovina numero e aggiorna le statistiche'''
    giocatore = seleziona_giocatore()
    numero_da_indovinare = random.randint(1, 100)
    indovinato = False
    print('Ho pensato ad un numero da 1 a 100, hai 8 tentativi!')
    for i in range(8):
        while True : 
            try : 
                num = int(input(f'Tentativo {i + 1}: '))
                if (num in range(1, 101, 1)) : 
                    break
            except ValueError : 
                print('Input non valido!')
        if num == numero_da_indovinare:
            print('Hai indovinato!')
            giocatore.aggiungi_vittoria('Indovina numero')
            indovinato = True
            break
        elif num > numero_da_indovinare:
            print('Troppo alto')
        else:
            print('Troppo basso')
    if not indovinato:
        print('Hai perso!')
        print('Il numero era', numero_da_indovinare)
        giocatore.aggiungi_sconfitta('Indovina numero')
        
        
        

#programma principale (main)
carica_giocatori_json()
print('===== TORNEO =====')
while True:
    print('\n1. Aggiungi giocatore')
    print('2. Mostra giocatori')
    print('3. Morra cinese - 2 giocatori')
    print('4. Pari o dispari - 2 giocatori')
    print('5. Indovina numero')
    print('6. Mostra statistiche giocatore')
    print('7. Mostra giocatori')
    print('0. Esci')
    scelta = input('Scelta: ')
    if scelta == '1' :
        aggiungi_giocatore()
    elif scelta == '2' :
        mostra_giocatori()
    elif scelta == '3' :
        morra_cinese()
    elif scelta == '4' :
        pari_dispari()
    elif scelta == '5' :
        indovina_numero()
    elif scelta == '6' : 
        mostra_statistiche_giocatore()
    elif scelta == '7' : 
        mostra_giocatori()
    elif scelta == '0':
        break
    else:
        print('Scelta non valida')
salva_giocatori_json() 
    
    
