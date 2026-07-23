#
# File: giocatore.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/22
#
# Version: 1.0
#
# Description: Definizione della classe Giocatore
#

class Giocatore : 
    '''
    Classe che rappresenta un giocatore del torneo.
    Ogni giocatore è identificato da un nome e da un ID univoco e mantiene le statistiche relative ai giochi disponibili (Morra Cinese, Pari o Dispari e Indovina il Numero).
    '''
    
    def __init__(self, nome, id_giocatore) : 
        '''Inizializzazione di un giocatore'''
        self.nome = nome
        self.id_giocatore = id_giocatore
        self.statistiche = {'Morra cinese' : {'vittorie' : 0, 'sconfitte' : 0, 'pareggi' : 0}, 
                            'Indovina numero' : {'vittorie' : 0, 'sconfitte' : 0, 'pareggi' : 0},
                            'Pari o dispari' : {'vittorie' : 0, 'sconfitte' : 0, 'pareggi' : 0}}
    def to_dict(self):
        '''Restituisce i dati del giocatore nella struttura dizionario per facilitare il salvataggio nel file JSON'''
        return {'nome': self.nome, 'statistiche': self.statistiche}
    
    def aggiungi_vittoria(self, gioco) :
        '''Incrementa il numero di vittorie per il gioco specificato''' 
        self.statistiche[gioco]['vittorie'] += 1
    
    def aggiungi_sconfitta(self, gioco) : 
        '''Incrementa il numero di sconfitte per il gioco specificato'''
        self.statistiche[gioco]['sconfitte'] += 1
        
    def aggiungi_pareggio(self, gioco) : 
        '''Incrementa il numero di pareggi per il gioco specfificato'''
        self.statistiche[gioco]['pareggi'] += 1
    
    def __str__(self):
        '''Restituisce una rappresentazione in stringa di ID e nome del giocatore'''
        return f'ID: {self.id_giocatore} | Nome: {self.nome}'