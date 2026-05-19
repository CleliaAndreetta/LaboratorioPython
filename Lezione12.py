#su Gemini --> scrivi una funzione per il gico dell'impiccato 
#(ricordare sempre di mettere l'intestazione perchè il prof la vuole)
#prima di una funzione scrivere sempre cosa fa (mettere la doc string)



#Esercizio 8 
#Autore: Clelia Andreetta
#Data: 19/05/2026

import random

#questa funzione va bene per il primo punto ("Scrivete il programma con un approccio totalmente LBYL") perchè usa solo if ed else 
def gioco_impiccato():
    '''Documentazione di cosa fa la funzione'''
    # Lista di parole possibili per il gioco
    parole = ["python", "programmazione", "computer", "sviluppatore", "algoritmo", "funzione"]
    
    # Sceglie una parola a caso e la trasforma in lettere minuscole
    parola_segreta = random.choice(parole).lower()
    lettere_indovinate = set()
    lettere_errate = set()
    tentativi_massimi = 6

    # Rappresentazione grafica dell'impiccato per ogni errore (da 0 a 6)
    fasi_impiccato = [
        """
           --------
           |      |
           |      
           |     
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / 
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
        ---------
        """
    ]

    print("--- BENVENUTO AL GIOCO DELL'IMPICCATO! ---")

    while len(lettere_errate) < tentativi_massimi:
        # Mostra lo stato attuale dell'omino
        print(fasi_impiccato[len(lettere_errate)])
        
        # Mostra la parola con i trattini (es. p _ t h o n)
        parola_visualizzata = [lettera if lettera in lettere_indovinate else "_" for lettera in parola_segreta]
        print("Parola da indovinare: " + " ".join(parola_visualizzata))
        print(f"Lettere errate: {', '.join(lettere_errate)}")
        print(f"Tentativi rimasti: {tentativi_massimi - len(lettere_errate)}")
        print("-" * 30)

        # Controllo vittoria: se non ci sono più trattini, l'utente ha vinto
        if "_" not in parola_visualizzata:
            print(f"🎉 COMPLIMENTI! Hai indovinato la parola: '{parola_segreta}'!")
            return

        # Input dell'utente con validazione
        tentativo = input("Inserisci una lettera: ").lower().strip()

        if len(tentativo) != 1 or not tentativo.isalpha():
            print("❌ Input non valido. Inserisci una singola lettera.")
            continue

        if tentativo in lettere_indovinate or tentativo in lettere_errate:
            print("⚠️ Hai già provato questa lettera. Scegline un'altra.")
            continue

        # Verifica se la lettera è corretta o meno
        if tentativo in parola_segreta:
            print(f"✅ Ottimo! La lettera '{tentativo}' è presente.")
            lettere_indovinate.add(tentativo)
        else:
            print(f"❌ Peccato! La lettera '{tentativo}' NON è presente.")
            lettere_errate.add(tentativo)

    # Se si esce dal ciclo, i tentativi sono esauriti
    print(fasi_impiccato[tentativi_massimi])
    print(f"💥 HAI PERSO! La parola segreta era: '{parola_segreta}'.")

# Per avviare il gioco basta chiamare la funzione:
gioco_impiccato()


