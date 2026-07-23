#
# File: esercizio2.py
#
# Author: Clelia Andreetta
#
# Date: 2026/07/14
#
# Version: 1.0
#
# Description: Laboratorio di programmazione in Python - Esercizio 2 - Data containers 
#
#

def conta_righe(testo) :
    '''Conta le righe non vuote nel testo'''
    n_righe_non_vuote = 0
    for riga in testo.split('\n') : 
        if(riga != "") : 
            n_righe_non_vuote += 1
    print('Numero di righe non vuote:', n_righe_non_vuote)
        
def conta_parole(testo) :
    '''Conta le parole nel testo'''
    n_parole = 0
    for parola in testo .split() : 
        n_parole += 1
    print('Numero di parole nel testo:', n_parole)
 
def conta_caratteri_alfanumerici(testo) : 
    '''Conta caratteri alfanumerici nel testo'''
    n_caratteri = 0
    for lettera in testo : 
        if (lettera.isalnum()) : 
            n_caratteri += 1
    print('Numero di caratteri alfanumerici nel testo:', n_caratteri)

def conta_lettera(testo) : 
    '''Conta quante volte compare nel testo una lettera inserita dall'utente'''
    lettera = input('Digitare una lettera: ').lower()
    cont = 0
    for i in testo.lower() : 
        if(i == lettera) : 
            cont += 1
    print('La lettera compare', cont, 'volte')

def sostituisci_parole(testo) : 
    '''Sostituisce le parole day, water e about con la parola PYTHON'''   
    testo_1 = testo.replace('day', 'PYTHON').replace('Day', 'PYTHON').replace('water', 'PYTHON').replace('Water', 'PYTHON').replace('about', 'PYTHON').replace('About', 'PYTHON')
    print(testo_1)

def scrivi_parole_dispari(testo) : 
    '''Riscrive il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
    for riga in testo.split('\n'):
        parole = riga.split()
        for i in range(len(parole)):
            if i % 2 == 0:                              #ricordo che gli indici partono da 0, se scrivessi i % 2 != sostituirei le parole in posizione pari
                parole[i] = parole[i].upper()
        nuova_riga = ""
        for parola in parole:
            nuova_riga = nuova_riga + parola + " "
        print(nuova_riga)

def inverti_frasi(testo) : 
    '''Riscrive il testo invertendo le frasi dal basso verso l'alto'''
    righe = testo.split('\n')
    for i in range(len(righe) - 1, -1, -1):
        print(righe[i])

def secondo_verso_strofa(testo) : 
    '''Riscrive il testo in modo che il secondo verso di ogni strofa sia scritto a specchio'''
    cont_verso = 0
    for riga in testo.split('\n') : 
        if(riga == "") : 
            cont_verso = 0
            print()
        else : 
            cont_verso +=1
            if(cont_verso == 2) : 
                riga_specchio = ""
                for i in range(len(riga) -1, -1, -1) : 
                    riga_specchio = riga_specchio + riga[i]
                print(riga_specchio)
            else : 
                print(riga)
            
def parole_strofe(testo) : 
    '''Trova le eventuali parole che compaiono in tutte le strofe'''
    strofe = testo.split('\n\n')
    parole_comuni = set(strofe[0].split())
    for i in range(1, len(strofe)):
        parole_comuni = parole_comuni & set(strofe[i].split())
    print(parole_comuni)

def elimina_punteggiatura(testo) : 
    '''Elimina i caratteri non alfanumerici'''
    nuovo_testo = testo
    for lettera in testo:
        if not lettera.isalnum():
            nuovo_testo = nuovo_testo.replace(lettera, " ")
    return nuovo_testo

def lista_univoca_parole(testo) : 
    '''Crea una lista univoca di tutte le parole che compaiono nel testo e la ordina per lunghezza della parola'''
    nuovo_testo = elimina_punteggiatura(testo)
    set_parole = set(nuovo_testo.split())
    lista_univoca_parole = list(set_parole)
    for i in range(len(lista_univoca_parole)):
        for j in range(i + 1, len(lista_univoca_parole)):
            if len(lista_univoca_parole[i]) > len(lista_univoca_parole[j]):
                lista_univoca_parole[i], lista_univoca_parole[j] = lista_univoca_parole[j], lista_univoca_parole[i]
    print(lista_univoca_parole)

def mappa_carattere_occorennza(testo) : 
    '''Crea un dizionario che mappa ogni carattere con la sua occorenza nel testo'''
    occorrenza_carattere = {}
    for lettera in testo : 
        if(lettera in occorrenza_carattere) : 
            occorrenza_carattere[lettera] += 1
        else : 
            occorrenza_carattere[lettera] = 1
    print(occorrenza_carattere)

def mappa_alfanumerico_occorenza(testo) : 
    '''Crea un dizionario che mappa ogni carattere alfanumerico con la sua occorenza nel testo'''
    nuovo_testo = elimina_punteggiatura(testo).lower()
    occorrenza_carattere_alfanumerico = {}
    for lettera in nuovo_testo : 
        if(lettera != " ") : 
            if(lettera in occorrenza_carattere_alfanumerico) : 
                occorrenza_carattere_alfanumerico[lettera] += 1
            else : 
                occorrenza_carattere_alfanumerico[lettera] = 1
    print(occorrenza_carattere_alfanumerico)



#programma principlae 
testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#conta_righe(testo)
#conta_parole(testo)
#conta_caratteri_alfanumerici(testo)
#conta_lettera(testo)
#sostituisci_parole(testo)
#scrivi_parole_dispari(testo)
#inverti_frasi(testo)
#secondo_verso_strofa(testo)
#parole_strofe(testo)
#lista_univoca_parole(testo)
#mappa_carattere_occorennza(testo)
mappa_alfanumerico_occorenza(testo)