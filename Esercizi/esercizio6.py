#
# File: esercizio6.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/18
#
# Version: 1.0
#
# Description: Laboratorio di Programmazione in Python - Esercizio 6- OOP
#

import json

class Rubrica :
    '''Classe che rappresenta una rubrica di contatti''' 
    def __init__(self, rubrica = None) :
        '''Inizializzazione di un oggetto Rubrica'''
        self.rubrica = rubrica
       
    @classmethod
    def rubrica_JSON(cls, file_json) : 
        '''Inizializzazione di una ribrica leggendo i dati da un file JSON'''
        with open(file_json, 'r') as read_file_json : 
            rubrica = json.load(read_file_json)
        return cls(rubrica)
     
    @classmethod
    def rubrica_txt(cls, file_txt) : 
        '''Inizializzazione di una ribrica leggendo i dati da un file txt'''
        rubrica = {}
        read_file_txt = open(file_txt, 'r')
        while True : 
            linea = read_file_txt.readline()
            if(len(linea) == 0 or linea == '\n') : 
                break 
            dati = linea.split(', ')
            rubrica[dati[0]] = {'giorno' : int(dati[1]), 'mese': dati[2], 'anno' : int(dati[3]), 'età' : int(dati[4]), 'sesso' : dati[5], 'mail' : dati[6]}
        return cls(rubrica)
         
    def aggiungi(self, nome, giorno, mese, anno, eta, sesso, mail) : 
        '''Aggiunge un elemento in rubrica'''
        if (self.rubrica is None) : 
            print('Prima apri una rubrica!')
            return
        self.rubrica[nome] = {'giorno' : int(giorno), 'mese': mese, 'anno' : int(anno), 'età' : int(eta), 'sesso' : sesso, 'mail' : mail}
       
    def rimuovi(self, nome) : 
        '''Rimuove un elemento dalla rubrica'''
        if (len(self.rubrica) == 0) : 
            print('La rubrica è vuota!')
            return
        if(nome not in self.rubrica.keys()) : 
            print('Il contatto', nome, 'non esiste in rubrica')
        else : 
            del self.rubrica[nome]

    def salva(self, file) : 
        '''Salva la rubrica su un file JSON o txt'''
        if(len(self.rubrica) == 0) : 
            print('La rubrica è vuota!')
            return
        f = file.split('.')
        estensione = f[1]
        if(estensione == 'json') : 
            with open(file, 'w') as write_file : 
                json.dump(self.rubrica, write_file)
        elif(estensione == 'txt') : 
            with open(file, 'w') as write_file: 
                for nome, dati in self.rubrica.items():
                    write_file.write(nome)
                    for dato in dati.values():
                        write_file.write(', ' + str(dato))
                    write_file.write('\n')
        
    def stampa(self, nome) : 
        '''Stampa le informazioni di un contatto in rubrica'''
        if (len(self.rubrica) == 0) : 
            print('La rubrica è vuota!')
            return
        if(nome not in self.rubrica.keys()) : 
            print('Il contatto', nome, 'non esiste in rubrica')
        else : 
            print('Nome:', nome)
            for chiave, valore in self.rubrica[nome].items() : 
                print(chiave, ':', valore)
                