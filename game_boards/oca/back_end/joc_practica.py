import copy
import random

#####################
#DEF TAULELL
#####################

taulell = {}
taulell[0] = {'text': 'Sortida!', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[1] = {'text': 'Caus per un pou directament a la casella 11!', 'moviment': 10, 'vida': 0, 'objecte': ('', 0)}
taulell[2] =  {'text': 'Trobes un elixir de la vida', 'moviment': 0, 'vida': 0, 'objecte': ('Elixir', 1)}
taulell[3] = {'text': 'Et pares per culpa del stop', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[4] =  {'text': 'Surts del teletransportador a la casella 18', 'moviment': 14, 'vida': 0, 'objecte': ('', 0)}
taulell[5] = {'text': 'Trobes una espasa!', 'moviment': 0, 'vida': 0, 'objecte': ('Espasa', 1)}
taulell[6] =  {'text': 'No passa res', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[7] =  {'text': 'Ets mossegat per una serp verinosa', 'moviment': 0, 'vida': -2, 'objecte': ('', 0)}
taulell[8] =  {'text': 'Patinet', 'moviment': 0, 'vida': 0, 'objecte': ('Patinet', 1)}
taulell[9] =  {'text': 'No passa res', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[10] = {'text': 'Et disparen una fletxa', 'moviment': 0, 'vida': -1, 'objecte': ('', 0)}
taulell[11] =  {'text': 'No passa res', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[12] = {'text': 'Trobes una torxa', 'moviment': 0, 'vida': 0, 'objecte': ('Torxa', 1)}
taulell[13] =  {'text': 'No passa res', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[14] =  {'text': 'Ets mossegat per una planta carnívora, perds 3 unitats de vida', 'moviment': 0, 'vida': -3, 'objecte': ('', 0)}
taulell[15] =  {'text': 'Et perds dins la casa encantada, no podràs fer res durant dos torns', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[16] = {'text': 'Prens un verí que et fa perdre 5 punts de vida!', 'moviment': 0, 'vida': -5, 'objecte': ('Veri', 2)}
taulell[17] =  {'text': 'Ets catapultat fins la casella 9', 'moviment': -8, 'vida': 0, 'objecte': ('', 0)}
taulell[18] =  {'text': 'No passa res', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}
taulell[19] =  {'text': 'Inspecciones el coet Sputnik que et porta fins la casella de sortida', 'moviment': -19, 'vida': 0, 'objecte': ('', 0)}
taulell[20] = {'text': 'Has arribat al final del camí. Felicitats!', 'moviment': 0, 'vida': 0, 'objecte': ('', 0)}



#########################
#DEF TIRADA
#########################

def tirar_daus(jugador, taulell=taulell):

    ###A cada torn

    # 1) Tira els daus i avança posiciop
    valor = random.randint(1, 6)
    posicio_original = jugador.posicio
    nova_posicio = posicio_original + valor
    print(f"{jugador.nom} llença el dau i surt un {valor}")
    jugador.set_posicio(nova_posicio)
    print(f"El jugador {jugador.nom} es mou de la casella {posicio_original} a la casella {jugador.posicio}")
    print(f"Et trobes a la casella {jugador.posicio}: {taulell[jugador.posicio]['text']}")

    ###2) A la nova posicio actualitza objectes
    nom_objecte, numero = taulell[jugador.posicio]["objecte"]
    jugador.set_objecte(nom_objecte, numero)

    #A la nova posicio actualitza vida
    nova_vida = jugador.vida + taulell[jugador.posicio]['vida']
    jugador.set_vida(nova_vida)

    #A la nova posicio  actualitza posicio
    nova_posicio = jugador.posicio + taulell[jugador.posicio]['moviment']
    jugador.set_posicio(nova_posicio)
    

class Joc():

    def __init__(self, jugadors=[]):
        self.jugadors = jugadors

    def create_jugador(self, nom):
        jugador = Jugador(nom)
        self.jugadors.append(jugador)

    def vides(self):
        return [jugador.vida for jugador in self.jugadors]

    def posicions(self):
        return [jugador.posicio for jugador in self.jugadors]




##########################
#DEF CLASES JOC/JUGADOR
##########################

class Jugador():

    def __init__(self, nom, posicio=0, vida=10):
        self.nom = nom
        self.posicio = posicio
        self.vida = vida
        self.objectes = {}

    def set_posicio(self, posicio):
        if posicio < 20:
            self.posicio = posicio
        else: 
            self.posicio = 20

    def set_vida(self, vida):
        if vida > 0:
            self.vida = vida
        else:
            self.vida = 0
            print(f"El jugador {self.nom} s'ha quedat sense vides i per tant perd!")

    def set_objecte(self, nom_objecte, numero):
        if nom_objecte:
            if nom_objecte in jugador.objectes:
                self.objectes[nom_objecte] += numero
            else:
                self.objectes[nom_objecte] = numero


###################
#EXECUCIO PROGRAMA
###################


#Inicia joc
joc = Joc()

# Inicia jugadors
joc.create_jugador("eric")
joc.create_jugador("anna")

#Fins que no s'acaben les vides o les posicions
while (0 not in joc.vides()) and (20 not in joc.posicions()):
    #Cada jugador fa el seu torn
    for jugador in joc.jugadors:
        print("\n#######################")
        print(f"Torn jugador {jugador.nom}:")
        print("#######################\n ")
        tirar_daus(jugador, taulell=taulell)
        print("\n#######################")
        print(f"Informació del jugador {jugador.nom}:")
        print("#######################\n")
        print(f"Vida --> {jugador.vida} \nPosico --> {jugador.posicio} \nObjectes--> {jugador.objectes}\n\n")
