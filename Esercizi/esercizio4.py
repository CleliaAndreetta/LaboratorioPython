#
# File: esercizio4.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/16
#
# Version: 1.0
#
# Description: Laboratorio di programmazione in Python - Esercizio 4 - Input/Outpu
#

import json

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

'''Genera un file di testo contenente tutti gli elementi della rubrica'''
with open('file.txt', 'w') as write_file_txt : 
    for nome, dati in rubrica.items():
        write_file_txt.write(nome)
        for dato in dati.values():
            write_file_txt.write(', ' + str(dato))
        write_file_txt.write('\n')

'''Genera un file JSON contenente la rubrica con la stessa struttura del dizionario interno al programma'''
with open('file_json.json', 'w') as write_file : 
    json.dump(rubrica, write_file)
    

'''Legge la rubrica salvata in un file formato JSON e visualizza tutto il contenuto'''
with open('file_json.json', 'r') as read_file:
    nuova_rubrica = json.load(read_file)
print(nuova_rubrica)
