#
# File: esercizio3.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/15
#
# Version: 1.0
#
# Description: Laboratorio di programmazione in Python - Esercizio 3 - Command Line
#

import sys
import argparse

rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

def visualizza_rubrica() :
    '''Stampa a video una stringa formattata che contiene la chiave e i valori di ciascun elemento della rubrica''' 
    for nome, dati in rubrica.items() :
        print(nome, '->')
        for chiave, valore in dati.items() :
            print('  ' + str(chiave) + ': ' +  str(valore))
        print()
    
def lista_nomi_eta() : 
    '''Costruisce la lista delle età in ordine crescenta e ritona i nomi in ordine cresecnte di età'''
    lista_eta = []
    for nome, dati in rubrica.items():
        lista_eta.append(dati['età'])
    for i in range(len(lista_eta)):
        for j in range(i + 1, len(lista_eta)):
            if lista_eta[j] < lista_eta[i]:
                lista_eta[i], lista_eta[j] = lista_eta[j], lista_eta[i]
    lista_nomi = []
    for eta in lista_eta:
        for nome, dati in rubrica.items():
            if dati['età'] == eta:
                if(nome not in lista_nomi) : 
                    lista_nomi.append(nome)
    return lista_nomi

def inverti_ordine(lista_nomi):
    '''Inverte l'ordine della lista dei nomi costruita in lista_nomi_eta()'''
    lista_nomi_invertita = []
    for i in range(len(lista_nomi)-1, -1, -1):
        lista_nomi_invertita.append(lista_nomi[i])
    return (lista_nomi_invertita)         

def messaggio(nome) : 
    '''Stampa a video un messaggio solo per il nome fornito come parametro'''
    if nome not in rubrica : 
        print('Nome non presente in rubrica')
        return
    o_a = ''
    dati = rubrica[nome]  
    if(dati['sesso'] == 'M') : 
        o_a = 'o'
    else : 
        o_a = 'a'
    template = 'Car{} {}, \nsei nat{} il {} di {} del {} e quindi a breve compirai {} anni. \nTi manderemo gli auguri a {} \n\n'
    out = template.format(o_a, nome, o_a, dati['giorno'], dati['mese'], dati['anno'], dati['età'], dati['mail'])
    print(out)

def messaggio_membri() : 
    '''Per ogni membro della rurbica scrive a video un messaggio'''
    for nome in rubrica.keys() : 
        messaggio(nome)

#def contenuto_chiave() : 
#   '''Visualizza tutti i valori relativi alla chiave passata come parametro'''
#    chiave = sys.argv[1]
#    for dati in rubrica.values() : 
#        print(dati[chiave])

def contenuto_chiave(chiave) : 
    '''Visualizza tutti i valori relativi alla chiave passata come parametro'''
    valori = []
    for dati in rubrica.values() : 
        valori.append(dati[chiave])
    return valori
        
        
        
#programma principale main (punto 7)
parser = argparse.ArgumentParser()
parser.add_argument('--visualizza_rubrica', action='store_true')
parser.add_argument('--lista_nomi_eta', action='store_true')
parser.add_argument('--inverti_ordine', action='store_true')
parser.add_argument('--messaggio_membri', action = 'store_true')
parser.add_argument('--nome')
parser.add_argument('--contenuto_chiave')

args = parser.parse_args()

if args.visualizza_rubrica:
    visualizza_rubrica()

if args.lista_nomi_eta:
    print(lista_nomi_eta())

if args.inverti_ordine:
    print(inverti_ordine(lista_nomi_eta()))

if args.contenuto_chiave:
    print(contenuto_chiave(args.contenuto_chiave))

if args.nome:
    messaggio(args.nome)
    
if args.messaggio_membri : 
    messaggio_membri()


