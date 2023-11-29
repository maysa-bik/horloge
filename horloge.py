# TUPLE EN LISTE 
# FONCTION AFFICHER_HEURE(TUPLE/LISTE)
#CONDITON SUR LES H,m,s
# time.sleep(1)                    # boucle infini اليه عمل مترابطة مغ / طريقة الحساب / وقت النوم bucle
#________________________________________________

import time
import threading

heure_liste = [22, 30, 45]
alarme_reglee = [22, 31, 00]
alarme_atteinte = False
mode_affichage_24h = False  # Mode 24 heures par défaut
pause_horloge = False  # Variable de contrôle pour la pause
arreter_programe = False # Variable de contrôle pour arrêter le programme


def regler_alarme(heure_alarme):
    global alarme_reglee
    alarme_reglee = heure_alarme
    print(f"Alarme réglée pour {alarme_reglee[0]:02d}:{alarme_reglee[1]:02d}:{alarme_reglee[2]:02d}")

def verifier_alarme():
    global alarme_atteinte
    heure_actuelle = tuple(heure_liste)
    if heure_actuelle == tuple(alarme_reglee):
        print("Alarme !!! L'heure de l'alarme est atteinte.")
        alarme_atteinte = True

def afficher_heure_liste():
    global alarme_atteinte, pause_horloge, arreter_programe
    while not arreter_programe:
        if not pause_horloge:
            heure_formattee = format_heure(heure_liste)
            print(heure_formattee, end='\r')
            time.sleep(1)

            heure_liste[2] += 1
            if heure_liste[2] == 60:
                heure_liste[2] = 0
                heure_liste[1] += 1
                if heure_liste[1] == 60:
                    heure_liste[1] = 0
                    heure_liste[0] += 1
                    if heure_liste[0] == 24:
                        heure_liste[0] = 0

            verifier_alarme()

    # Code à exécuter après que l'alarme a été atteinte
    print("Le programme continue après l'alarme.")   
    
def format_heure(heure):
    if mode_affichage_24h:
        return f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}"
    else:
        am_pm = "AM" if heure[0] < 12 else "PM"
        heure12 = heure[0] % 12 if heure[0] % 12 != 0 else 12
        return f"{heure12:02d}:{heure[1]:02d}:{heure[2]:02d} {am_pm}"

def mettre_en_pause():
    global pause_horloge
    pause_horloge = True
    print("L'horloge est en pause.")

def relancer_horloge():
    global pause_horloge
    pause_horloge = False
    print("L'horloge a été relancée.")

# fonction pour quitter le programme
def quitter_programme():
    global arreter_programe
    arreter_programe = True
# fonction pour delander a l'utilisateur de faire la pause et de relancé l'horloge
def entrer_utilisateur():
    global pause_horloge, arreter_programe
    while not arreter_programe:
        user_input = input("Appuyez sur 'p' et entrée pour mettre en pause, 'r' et entreé pour relancer, ou 'entrée' pour quitter :")
        if user_input == 'p':
            mettre_en_pause()
        elif user_input == 'r':
            relancer_horloge()
        elif user_input == '':
            quitter_programme()

# Création d'un thread pour l'horloge
thread_horloge = threading.Thread(target=afficher_heure_liste)

# Création d'un thread pour attendre l'entrée utilisateur
thread_entree_utilisateur = threading.Thread(target= entrer_utilisateur)

# Démarrage du thread de l'horloge
thread_horloge.start()

# Démarrage du thread d'attente de l'entrée utilisateur
thread_entree_utilisateur.start()


# Attente que le thread de l'horloge se termine (ce qui ne se produira pas dans cet exemple)
thread_horloge.join()







