#Composition pour 20 level de difficulté
#Les objets sont convertie en 100 pts de score en sortent.
#La clé ¬ est nécéssaire pour franchir les portes.
#L'objet ¨ est devenu un soin 100% consomme automatique.
#L'objet @ est un continue si vous mourez.

#Bug génération Isométrie si les lignes n'ont pas 3 case vide a la fin
#Index out of rang classique. J'ai remplacé toute la formule par un sprite ascii
Isom_A = "                      |_       _||_       _|\         /\         /\         / \       /                       |_       _||_       _|\         /\         /\         / \       /                       |__     __||__     __|\         /\         /\         /\        / _________  _________ |_________||_________|\_________/\_________/\_________/\_________/"
Isom_B = "|_       _||_       _|| |\   /| || |\   /| ||_       _||__     __| \       /   \     /  |_       _||__     __|| |\   /| || |\   /| ||_       _||__     __| \       /   \     /  |_________||_________|| |\___/| || |\___/| ||_________||_________| \_______/  \______/ |         ||         ||         ||         ||         ||         ||         ||         |"
Isom_C = "| |_   _| || |\   /| || ||   || || | \ / | || |_   _| || |\   /| |  |_   _|     \   /   | |_____| || |\ _ /| || ||___|| || | \_/ | || |_____| || |\ _ /| |  |_____|     \ _ /   |         ||         || ||   || || ||   || ||         ||         | |       |  |      | |         ||         ||         ||         ||         ||         ||         ||         |"
Isom_D = "| |_]-[_| || | |-| | || ||]-[|| || | |-| | || |_]-[_| || | |-| | |  |_]-[_|      |-|    | |_____| || | |_| | || ||___|| || | |_| | || |_____| || | |_| | |  |_____|      |_|    |         ||         || ||   || || ||   || ||         ||         | |       |  |      | |         ||         ||         ||         ||         ||         ||         ||         |"
Isom_E = "|_|     |_||_|/   \|_|| ||   || || | / \ | ||_|     |_||_|/   \|_|  |     |     /   \   |_|     |_||_|/   \|_|| ||   || || | / \ | ||_|     |_||_|/   \|_|  |     |     /   \   |_________||_________|| ||___|| || ||___|| ||_________||_________| |_______|  |______| |         ||         ||         ||         ||         ||         ||         ||         |"
Isom_F = "|         ||         ||_|/   \|_||_|/   \|_||         ||         | /       \   /     \  |         ||         ||_|/   \|_||_|/   \|_||         ||         | /       \   /     \  |         ||         ||_|/   \|_||_|/   \|_||         ||         | /       \  /      \ |_________||_________||_________||_________||_________||_________||_________||_________|"
Isom_G = "     &          &     |    &    ||    &    |/    &    \/    &    \/    &    \ /   &   \      &          &     |    &    ||    &    |/    &    \/    &    \/    &    \ /   &   \      &          &     |    &    ||    &    |/    &    \/    &    \/    &    \/   &    \     &          &     |    &    ||    &    |/    &    \/    &    \/    &    \/    &    \\"

import copy
import random
import re
Jeu = 1
MaxX = 79 #Max resolution droite
MaxY = 15
sf = "E:\PERSONNEL\python_2\python\histoires\Temple\Temple"
#var Hero
x = 2
y = 5
Hero="&"
vie=100
Score=0
objets=[]
lv = 15
MessageTemple = ""
clip = 0
god = 0
N0 = ""
N1 = ""
N2 = ""
N3 = ""
C0 = ""
C1 = ""
C2 = ""
C3 = ""
S0 = ""
S1 = ""
S2 = ""
S3 = ""
Isom = "         "
IsomA = ""
IsomB = ""
IsomC = ""
IsomD = ""
IsomE = ""
IsomF = ""
IsomG = ""
Z = 3

print("BIENVENU DANS PYTHON TEMPLE 2.0")
print("")
print("POUR PROGRESSÉ DANS CETTE UNIVER")
print("VOUS DEVEZ UTILISER L'INVITE DE")
print("COMMANDE SUIVIE DE ENTER. MAIS")
print("VOUS POUVEZ ÉCRIR UN LONG PARCOUR")
print("D'AVAANCE.")
print("LES QUATRES DIRRECTIONS SONT:")
print("W=NORD, S=SUD, A=OUEST, D=EST")
print("Q=REGARDE HAUT, Z=REGARDE BAS")
print("LES OBJETS SONT RÉCOLTER AUTO-")
print("MATIQUEMENT SUR VOTRE PASSAGE.")
print("QUELQUE FOIS, LES CORRIDORES SE")
print("TRANSFORMENT QUAND VOUS RAMASSER")
print("UN OBJET POUR PLUS DE DIFFICULTÉ.")
print("UN CONTACTE AVEC UN OBSTACLE VOUS")
print("BLESSE ET VOTRE OBJECTIF C'EST LA")
print("LIGNE DIRECT VERRE LA SORTIE DU LV.")
print("IL Y A DES CODE DE TRICHE INSPIRÉ")
print("PAR DOOM JE VOUS LAISSE DÉCOUVRIR.")
print("")
print("Vous choisisez un level (0-20)")
key = input("Start Level=")
if (key == ""):
    lv = 0
else:
    lv = int(key)
#Chargement d'une carte
sourcefile = ""
x = 2
y = 5
if (lv <= 0):
    sourcefile = sf+".joj.txt"
if (lv == 1):
    sourcefile = sf+"1.joj.txt"
if (lv == 2):
    sourcefile = sf+"2.joj.txt"
if (lv == 3):
    sourcefile = sf+"3.joj.txt"
if (lv == 4):
    sourcefile = sf+"4.joj.txt"
if (lv == 5):
    sourcefile = sf+"5.joj.txt"
if (lv == 6):
    sourcefile = sf+"6.joj.txt"
if (lv == 7):
    sourcefile = sf+"7.joj.txt"
if (lv == 8):
    sourcefile = sf+"8.joj.txt"
if (lv == 9):
    sourcefile = sf+"9.joj.txt"
if (lv == 10):
    sourcefile = sf+"10.joj.txt"
if (lv == 11):
    sourcefile = sf+"11.joj.txt"
if (lv == 12):
    sourcefile = sf+"12.joj.txt"
if (lv == 13):
    sourcefile = sf+"13.joj.txt"
    x = 2
    y = 1
if (lv == 14):
    sourcefile = sf+"14.joj.txt"
    x = 2
    y = 1
if (lv == 15):
    sourcefile = sf+"15.joj.txt"
    x = 2
    y = 1
if (lv == 16):
    sourcefile = sf+"16.joj.txt"
    x = 2
    y = 1
if (lv == 17):
    sourcefile = sf+"17.joj.txt"
    x = 2
    y = 1
if (lv == 18):
    sourcefile = sf+"18.joj.txt"
    x = 2
    y = 1
if (lv == 19):
    sourcefile = sf+"19.joj.txt"
    x = 2
    y = 1
if (lv == 20):
    sourcefile = sf+"20.joj.txt"
    x = 2
    y = 1
if (sourcefile == ""):
    sourcefile = sf+".joj.txt"
    x = 2
    y = 5
file = open(sourcefile.upper(), "r")
ligne = 0
for line in file:
    if (ligne == 0):
        A = line[:-1]
    if (ligne == 1):
        B = line[:-1]
    if (ligne == 2):
        C = line[:-1]
    if (ligne == 3):
        D = line[:-1]
    if (ligne == 4):
        E = line[:-1]
    if (ligne == 5):
        F = line[:-1]
    if (ligne == 6):
        G = line[:-1]
    if (ligne == 7):
        H = line[:-1]
    if (ligne == 8):
        I = line[:-1]
    if (ligne == 9):
        J = line[:-1]
    if (ligne == 10):
        K = line[:-1]
    if (ligne == 11):
        L = line[:-1]
    if (ligne == 12):
        M = line[:-1]
    if (ligne == 13):
        N = line[:-1]
    if (ligne == 14):
        O = line[:-1]
    if (ligne == 15):
        P = line[:-1]
    if (ligne == 16):
        a = line[:-1]
    if (ligne == 17):
        b = line[:-1]
    if (ligne == 18):
        c = line[:-1]
    if (ligne == 19):
        d = line[:-1]
    if (ligne == 20):
        e = line[:-1]
    if (ligne == 21):
        f = line[:-1]
    if (ligne == 22):
        g = line[:-1]
    if (ligne == 23):
        h = line[:-1]
    if (ligne == 24):
        i = line[:-1]
    if (ligne == 25):
        j = line[:-1]
    if (ligne == 26):
        k = line[:-1]
    if (ligne == 27):
        l = line[:-1]
    if (ligne == 28):
        m = line[:-1]
    if (ligne == 29):
        n = line[:-1]
    if (ligne == 30):
        o = line[:-1]
    ligne = ligne + 1

String = "________________________________________________________________________________"
Isomtr = "                                                                                "

print("W,S,A,D,Q,Z ?>")
while Jeu == 1:
    #Computer Point de fuite
    if (y == 0):
        N0 = "-"
        N1 = "-"
        N2 = "-"
        N3 = "-"
        C0 = A[x]
        C1 = A[x+1]
        C2 = A[x+2]
        C3 = A[x+3]
        S0 = B[x]
        S1 = B[x+1]
        S2 = B[x+2]
        S3 = B[x+3]
    if (y == 1):
        N0 = A[x]
        N1 = A[x+1]
        N2 = A[x+2]
        N3 = A[x+3]
        C0 = B[x]
        C1 = B[x+1]
        C2 = B[x+2]
        C3 = B[x+3]
        S0 = C[x]
        S1 = C[x+1]
        S2 = C[x+2]
        S3 = C[x+3]
    if (y == 2):
        N0 = B[x]
        N1 = B[x+1]
        N2 = B[x+2]
        N3 = B[x+3]
        C0 = C[x]
        C1 = C[x+1]
        C2 = C[x+2]
        C3 = C[x+3]
        S0 = D[x]
        S1 = D[x+1]
        S2 = D[x+2]
        S3 = D[x+3]
    if (y == 3):
        N0 = C[x]
        N1 = C[x+1]
        N2 = C[x+2]
        N3 = C[x+3]
        C0 = D[x]
        C1 = D[x+1]
        C2 = D[x+2]
        C3 = D[x+3]
        S0 = E[x]
        S1 = E[x+1]
        S2 = E[x+2]
        S3 = E[x+3]
    if (y == 4):
        N0 = D[x]
        N1 = D[x+1]
        N2 = D[x+2]
        N3 = D[x+3]
        C0 = E[x]
        C1 = E[x+1]
        C2 = E[x+2]
        C3 = E[x+3]
        S0 = F[x]
        S1 = F[x+1]
        S2 = F[x+2]
        S3 = F[x+3]
    if (y == 5):
        N0 = E[x]
        N1 = E[x+1]
        N2 = E[x+2]
        N3 = E[x+3]
        C0 = F[x]
        C1 = F[x+1]
        C2 = F[x+2]
        C3 = F[x+3]
        S0 = G[x]
        S1 = G[x+1]
        S2 = G[x+2]
        S3 = G[x+3]
    if (y == 6):
        N0 = F[x]
        N1 = F[x+1]
        N2 = F[x+2]
        N3 = F[x+3]
        S0 = H[x]
        S1 = H[x+1]
        S2 = H[x+2]
        S3 = H[x+3]
    if (y == 7):
        N0 = G[x]
        N1 = G[x+1]
        N2 = G[x+2]
        N3 = G[x+3]
        C0 = H[x]
        C1 = H[x+1]
        C2 = H[x+2]
        C3 = H[x+3]
        S0 = I[x]
        S1 = I[x+1]
        S2 = I[x+2]
        S3 = I[x+3]
    if (y == 8):
        N0 = H[x]
        N1 = H[x+1]
        N2 = H[x+2]
        N3 = H[x+3]
        C0 = I[x]
        C1 = I[x+1]
        C2 = I[x+2]
        C3 = I[x+3]
        S0 = J[x]
        S1 = J[x+1]
        S2 = J[x+2]
        S3 = J[x+3]
    if (y == 9):
        N0 = I[x]
        N1 = I[x]
        N2 = I[x]
        N3 = I[x]
        C0 = J[x]
        C1 = J[x+1]
        C2 = J[x+2]
        C3 = J[x+3]
        S0 = K[x]
        S1 = K[x+1]
        S2 = K[x+2]
        S3 = K[x+3]
    if (y == 10):
        N0 = J[x]
        N1 = J[x+1]
        N2 = J[x+2]
        N3 = J[x+3]
        C0 = K[x]
        C1 = K[x+1]
        C2 = K[x+2]
        C3 = K[x+3]
        S0 = L[x]
        S1 = L[x+1]
        S2 = L[x+2]
        S3 = L[x+3]
    if (y == 11):
        N0 = K[x]
        N1 = K[x+1]
        N2 = K[x+2]
        N3 = K[x+3]
        C0 = L[x]
        C1 = L[x+1]
        C2 = L[x+2]
        C3 = L[x+3]
        S0 = M[x]
        S1 = M[x+1]
        S2 = M[x+2]
        S3 = M[x+3]
    if (y == 12):
        N0 = L[x]
        N1 = L[x+1]
        N2 = L[x+2]
        N3 = L[x+3]
        C0 = M[x]
        C1 = M[x+1]
        C2 = M[x+2]
        C3 = M[x+3]
        S0 = N[x]
        S1 = N[x+1]
        S2 = N[x+2]
        S3 = N[x+3]
    if (y == 13):
        N0 = M[x]
        N1 = M[x+1]
        N2 = M[x+2]
        N3 = M[x+3]
        C0 = N[x]
        C1 = N[x+1]
        C2 = N[x+2]
        C3 = N[x+3]
        S0 = O[x]
        S1 = O[x+1]
        S2 = O[x+2]
        S3 = O[x+3]
    if (y == 14):
        N0 = N[x]
        N1 = N[x+1]
        N2 = N[x+2]
        N3 = N[x+3]
        C0 = O[x]
        C1 = O[x+1]
        C2 = O[x+2]
        C3 = O[x+3]
        S0 = P[x]
        S1 = P[x+1]
        S2 = P[x+2]
        S3 = P[x+3]
    if (y == 15):
        N0 = O[x]
        N1 = O[x+1]
        N2 = O[x+2]
        N3 = O[x+3]
        C0 = P[x]
        C1 = P[x+1]
        C2 = P[x+2]
        C3 = P[x+3]
        S0 = "-"
        S1 = "-"
        S2 = "-"
        S3 = "-"
    #Scane du Map
    scaleG = 0
    if (N0 != " "):
        scaleG = scaleG + 4
    if (N1 != " "):
        scaleG = scaleG + 2
    if (N2 != " "):
        scaleG = scaleG + 1
    scaleD = 0
    if (S0 != " "):
        scaleD = scaleD + 4
    if (S1 != " "):
        scaleD = scaleD + 2
    if (S2 != " "):
        scaleD = scaleD + 1
    scaleC = 0
    if (C3 != " "):
        scaleC = 1
    if (C2 != " "):
        scaleC = 2
    if (C1 != " "):
        scaleC = 3
    if (C0 != " "):
        scaleC = 4
    #Construction Isométrie
    IsomA = Isom_A[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_A[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    IsomB = Isom_B[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_B[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    IsomC = Isom_C[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_C[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    IsomD = Isom_D[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_D[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    IsomE = Isom_E[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_E[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    IsomF = Isom_F[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_F[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    IsomG = Isom_G[0+(scaleG*11)+(scaleC*88):6+(scaleG*11)+(scaleC*88)] + Isom_G[6+(scaleD*11)+(scaleC*88):10+(scaleD*11)+(scaleC*88)]
    #Angle Regard
    if (Z == 0):
        Isom1 = Isom
        Isom2 = IsomA
        Isom3 = IsomB
        Isom4 = IsomC
    if (Z == 1):
        Isom1 = IsomA
        Isom2 = IsomB
        Isom3 = IsomC
        Isom4 = IsomD
    if (Z == 2):
        Isom1 = IsomB
        Isom2 = IsomC
        Isom3 = IsomD
        Isom4 = IsomE
    if (Z == 3):
        Isom1 = IsomC
        Isom2 = IsomD
        Isom3 = IsomE
        Isom4 = IsomF
    if (Z == 4):
        Isom1 = IsomD
        Isom2 = IsomE
        Isom3 = IsomF
        Isom4 = IsomG
    if (Z == 5):
        Isom1 = IsomE
        Isom2 = IsomF
        Isom3 = IsomG
        Isom4 = Isom
    #Santer
    if (vie <= 0):
        if "continu" in objets:
            objets.remove("continu")
            vie = 100
            MessageTemple = "Vous êtes Réssucité!"
        else:
            vie = 0
            MessageTemple = "Vous êtes Mort!"
    if (vie < 100):
        if "mush" in objets:
            objets.remove("mush")
            vie = 100
            MessageTemple = "Vous mangez les champignons."
    #Nouveau Cadrage avec le message plus bas
    centre = int((len(String) - len(MessageTemple)) / 2)
    print(String)
    print(Isom1, "Santé:",vie,"%", x, y)#Ne ramasse pas les objets avec les touches W,S, quand y = 2,4 mais pas y = 1,3
    print(Isom2, "Objet:",objets)
    print(Isom3, "Score:",Score)
    print(Isom4, "Dungeon Lair, Niveau ", lv)
    if (len(MessageTemple) == 0):
        corrige = 1#Test
    else:
        corrige = 0
    print(String[0:centre] + MessageTemple + String[0:centre - corrige])
    if (y == 0):
        print(A[:x]+Hero+A[x+1:])
    else:
        print(A)
    if (y == 1):
        print(B[:x]+Hero+B[x+1:])
    else:
        print(B)
    if (y == 2):
        print(C[:x]+Hero+C[x+1:])
    else:
        print(C)
    if (y == 3):
        print(D[:x]+Hero+D[x+1:])
    else:
        print(D)
    if (y == 4):
        print(E[:x]+Hero+E[x+1:])
    else:
        print(E)
    if (y == 5):
        print(F[:x]+Hero+F[x+1:])
    else:
        print(F)
    if (y == 6):
        print(G[:x]+Hero+G[x+1:])
    else:
        print(G)
    if (y == 7):
        print(H[:x]+Hero+H[x+1:])
    else:
        print(H)
    if (y == 8):
        print(I[:x]+Hero+I[x+1:])
    else:
        print(I)
    if (y == 9):
        print(J[:x]+Hero+J[x+1:])
    else:
        print(J)
    if (y == 10):
        print(K[:x]+Hero+K[x+1:])
    else:
        print(K)
    if (y == 11):
        print(L[:x]+Hero+L[x+1:])
    else:
        print(L)
    if (y == 12):
        print(M[:x]+Hero+M[x+1:])
    else:
        print(M)
    if (y == 13):
        print(N[:x]+Hero+N[x+1:])
    else:
        print(N)
    if (y == 14):
        print(O[:x]+Hero+O[x+1:])
    else:
        print(O)
    if (y == 15):
        print(P[:x]+Hero+P[x+1:])
    else:
        print(P)
    print("")#Correction en petite écran éxecutable
    
    #Tour a tour
    if (vie > 0):
        key = input("W,S,A,D ?>")
    else:
        key = input("VOUS ÊTES MORT!")
        break
    
    if (key.upper() == ""):
        MessageTemple = "Vous attendez...Rien ne se passe."
        if (god == 0):
            vie = vie - 1
    if (key.upper() == "FIn DE LA PARTIE" or key.upper() == "QUITTER" or key.upper() == "FIN DU JEUX" or key.upper() == "TELEPORT" or key.upper() == "EXIT" or key.upper() == "SORTIE" or key.upper() == "QUIT" or key.upper() == "FIN"):
        break
    
    #Codes de triche
    if (clip == 1 and key.upper() == "IDCLIP"):
        clip = 0
        key = ""
        MessageTemple = "Vous refermez le dematerrialisateur."
    if (clip == 0 and key.upper() == "IDCLIP"):
        clip = 1
        key = ""
        MessageTemple = "Vous utilisez le dematerrialisateur."
    if (god == 1 and key.upper() == "IDXPIXPOPD"):
        god = 0
        key = ""
        MessageTemple = "Vous fermez l'invincibilisateur."
    if (god == 0 and key.upper() == "IDXPIXPOPD"):
        god = 1
        key = ""
        MessageTemple = "Vous utilisez l'invincibilisateur."
    if (key.upper() == "IDDQD"):
        objets.append("shuricain")
        objets.append("mush")
        objets.append("roche")
        objets.append("continu")
        objets.append("boomrang")
        key = ""
        MessageTemple = "Vous avez tout les objets."
    if (key.upper() == "IDKFA"):
        vie = 100
        key = ""
        MessageTemple = "Vous êtes au sommet de la forme."
    if (key.upper() == "IDLV"):
        lv = input("level=")
        x = 2
        y = 5
        if (lv <= 0):
            sourcefile = sf+".joj.txt"
        if (lv == 1):
            sourcefile = sf+"1.joj.txt"
        if (lv == 2):
            sourcefile = sf+"2.joj.txt"
        if (lv == 3):
            sourcefile = sf+"3.joj.txt"
        if (lv == 4):
            sourcefile = sf+"4.joj.txt"
        if (lv == 5):
            sourcefile = sf+"5.joj.txt"
        if (lv == 6):
            sourcefile = sf+"6.joj.txt"
        if (lv == 7):
            sourcefile = sf+"7.joj.txt"
        if (lv == 8):
            sourcefile = sf+"8.joj.txt"
        if (lv == 9):
            sourcefile = sf+"9.joj.txt"
        if (lv == 10):
            sourcefile = sf+"10.joj.txt"
        if (lv == 11):
            sourcefile = sf+"11.joj.txt"
        if (lv == 12):
            sourcefile = sf+"12.joj.txt"
        if (lv == 13):
            sourcefile = sf+"13.joj.txt"
            x = 2
            y = 1
        if (lv == 14):
            sourcefile = sf+"14.joj.txt"
            x = 2
            y = 1
        if (lv == 15):
            sourcefile = sf+"15.joj.txt"
            x = 2
            y = 1
        if (lv == 16):
            sourcefile = sf+"16.joj.txt"
            x = 2
            y = 1
        if (lv == 17):
            sourcefile = sf+"17.joj.txt"
            x = 2
            y = 1
        if (lv == 18):
            sourcefile = sf+"18.joj.txt"
            x = 2
            y = 1
        if (lv == 19):
            sourcefile = sf+"19.joj.txt"
            x = 2
            y = 1
        if (lv == 20):
            sourcefile = sf+"20.joj.txt"
            x = 2
            y = 1
        if (sourcefile == ""):
            sourcefile = sf+".joj.txt"
            x = 2
            y = 5
        file = open(sourcefile.upper(), "r")
        ligne = 0
        for line in file:
            if (ligne == 0):
                A = line[:-1]
            if (ligne == 1):
                B = line[:-1]
            if (ligne == 2):
                C = line[:-1]
            if (ligne == 3):
                D = line[:-1]
            if (ligne == 4):
                E = line[:-1]
            if (ligne == 5):
                F = line[:-1]
            if (ligne == 6):
                G = line[:-1]
            if (ligne == 7):
                H = line[:-1]
            if (ligne == 8):
                I = line[:-1]
            if (ligne == 9):
                J = line[:-1]
            if (ligne == 10):
                K = line[:-1]
            if (ligne == 11):
                L = line[:-1]
            if (ligne == 12):
                M = line[:-1]
            if (ligne == 13):
                N = line[:-1]
            if (ligne == 14):
                O = line[:-1]
            if (ligne == 15):
                P = line[:-1]
            if (ligne == 16):
                a = line[:-1]
            if (ligne == 17):
                b = line[:-1]
            if (ligne == 18):
                c = line[:-1]
            if (ligne == 19):
                d = line[:-1]
            if (ligne == 20):
                e = line[:-1]
            if (ligne == 21):
                f = line[:-1]
            if (ligne == 22):
                g = line[:-1]
            if (ligne == 23):
                h = line[:-1]
            if (ligne == 24):
                i = line[:-1]
            if (ligne == 25):
                j = line[:-1]
            if (ligne == 26):
                k = line[:-1]
            if (ligne == 27):
                l = line[:-1]
            if (ligne == 28):
                m = line[:-1]
            if (ligne == 29):
                n = line[:-1]
            if (ligne == 30):
                o = line[:-1]
            if (ligne == 31):
                p = line[:-1]
            ligne = ligne + 1

    for z in range(len(key)):
        #Angle élévation Isométrie Q up, Z down
        if (Z>0 and key[z].upper() == "Q"):
            Z = Z - 1
        if (Z<6 and key[z].upper() == "Z"):
            Z = Z + 1
        if (y>0 and key[z].upper() == "W"):
            if (y == 1 and A[x] == " ") or (y == 2 and B[x] == " ") or (y == 3 and C[x] == " ") or (y == 4 and D[x] == " ") or (y == 5 and E[x] == " ") or (y == 6 and F[x] == " ") or (y == 7 and G[x] == " ") or (y == 8 and H[x] == " ") or (y == 9 and I[x] == " ") or (y == 10 and J[x] == " ") or (y == 11 and K[x] == " ") or (y == 12 and L[x] == " ") or (y == 13 and M[x] == " ") or (y == 14 and N[x] == " ") or (y == 15 and O[x] == " "):
                # or (y == 1 and A[x] == "*") or (y == 2 and B[x] == "*") or (y == 3 and C[x] == "*") or (y == 4 and D[x] == "*") or (y == 5 and E[x] == "*") or (y == 6 and F[x] == "*") or (y == 7 and G[x] == "*") or (y == 8 and H[x] == "*") or (y == 9 and I[x] == "*") or (y == 10 and J[x] == "*") or (y == 11 and K[x] == "*") or (y == 12 and L[x] == "*") or (y == 13 and M[x] == "*") or (y == 14 and N[x] == "*") or (y == 15 and O[x] == "*") or (y == 1 and A[x] == "^") or (y == 2 and B[x] == "^") or (y == 3 and C[x] == "^") or (y == 4 and D[x] == "^") or (y == 5 and E[x] == "^") or (y == 6 and F[x] == "^") or (y == 7 and G[x] == "^") or (y == 8 and H[x] == "^") or (y == 9 and I[x] == "^") or (y == 10 and J[x] == "^") or (y == 11 and K[x] == "^") or (y == 12 and L[x] == "^") or (y == 13 and M[x] == "^") or (y == 14 and N[x] == "^") or (y == 15 and O[x] == "^") or (y == 1 and A[x] == "¨") or (y == 2 and B[x] == "¨") or (y == 3 and C[x] == "¨") or (y == 4 and D[x] == "¨") or (y == 5 and E[x] == "¨") or (y == 6 and F[x] == "¨") or (y == 7 and G[x] == "¨") or (y == 8 and H[x] == "¨") or (y == 9 and I[x] == "¨") or (y == 10 and J[x] == "¨") or (y == 11 and K[x] == "¨") or (y == 12 and L[x] == "¨") or (y == 13 and M[x] == "¨") or (y == 14 and N[x] == "¨") or (y == 15 and O[x] == "¨") or (y == 1 and A[x] == "@") or (y == 2 and B[x] == "@") or (y == 3 and C[x] == "@") or (y == 4 and D[x] == "@") or (y == 5 and E[x] == "@") or (y == 6 and F[x] == "@") or (y == 7 and G[x] == "@") or (y == 8 and H[x] == "@") or (y == 9 and I[x] == "@") or (y == 10 and J[x] == "@") or (y == 11 and K[x] == "@") or (y == 12 and L[x] == "@") or (y == 13 and M[x] == "@") or (y == 14 and N[x] == "@") or (y == 15 and O[x] == "@") or (y == 1 and A[x] == ":") or (y == 2 and B[x] == ":") or (y == 3 and C[x] == ":") or (y == 4 and D[x] == ":") or (y == 5 and E[x] == ":") or (y == 6 and F[x] == ":") or (y == 7 and G[x] == ":") or (y == 8 and H[x] == ":") or (y == 9 and I[x] == ":") or (y == 10 and J[x] == ":") or (y == 11 and K[x] == ":") or (y == 12 and L[x] == ":") or (y == 13 and M[x] == ":") or (y == 14 and N[x] == ":") or (y == 15 and O[x] == ":") or (y == 1 and A[x] == "¬") or (y == 2 and B[x] == "¬") or (y == 3 and C[x] == "¬") or (y == 4 and D[x] == "¬") or (y == 5 and E[x] == "¬") or (y == 6 and F[x] == "¬") or (y == 7 and G[x] == "¬") or (y == 8 and H[x] == "¬") or (y == 9 and I[x] == "¬") or (y == 10 and J[x] == "¬") or (y == 11 and K[x] == "¬") or (y == 12 and L[x] == "¬") or (y == 13 and M[x] == "¬") or (y == 14 and N[x] == "¬") or (y == 15 and O[x] == "¬")
                y = y - 1
                MessageTemple = ""
            else:
                if (clip == 1):
                    y = y - 1
                    MessageTemple = "Vous passez a traver les mures."
                else:
                    MessageTemple = "Vous ne passez pas les mures."
                    if (god == 0):
                        vie = vie - 1
            for item in ["*","^","¨","@",":","¬"]:
                if (y == 1 and A[x] == item) or (y == 2 and B[x] == item) or (y == 3 and C[x] == item) or (y == 4 and D[x] == item) or (y == 5 and E[x] == item) or (y == 6 and F[x] == item) or (y == 7 and G[x] == item) or (y == 8 and H[x] == item) or (y == 9 and I[x] == item) or (y == 10 and J[x] == item) or (y == 11 and K[x] == item) or (y == 12 and L[x] == item) or (y == 13 and M[x] == item) or (y == 14 and N[x] == item) or (y == 15 and O[x] == item):
                    if (item == "*"):
                        trouver = "shurican"
                        vie = vie + 1
                        if (y == 1):
                            A = a
                        if (y == 2):
                            B = b
                        if (y == 3):
                            C = c
                        if (y == 4):
                            D = d
                        if (y == 5):
                            E = e
                        if (y == 6):
                            F = f
                        if (y == 7):
                            G = g
                        if (y == 8):
                            H = h
                        if (y == 9):
                            I = i
                        if (y == 10):
                            J = j
                        if (y == 11):
                            K = k
                        if (y == 12):
                            L = l
                        if (y == 13):
                            M = m
                        if (y == 14):
                            N = n
                        if (y == 15):
                            O = o
                    if (item == "^"):
                        vie = vie + 1
                        trouver = "boomrang"
                        if (y == 1):
                            A = a
                        if (y == 2):
                            B = b
                        if (y == 3):
                            C = c
                        if (y == 4):
                            D = d
                        if (y == 5):
                            E = e
                        if (y == 6):
                            F = f
                        if (y == 7):
                            G = g
                        if (y == 8):
                            H = h
                        if (y == 9):
                            I = i
                        if (y == 10):
                            J = j
                        if (y == 11):
                            K = k
                        if (y == 12):
                            L = l
                        if (y == 13):
                            M = m
                        if (y == 14):
                            N = n
                        if (y == 15):
                            O = o
                    if (item == "¨"):
                        vie = vie + 1
                        trouver = "mush"
                        if (y == 1):
                            A = a
                        if (y == 2):
                            B = b
                        if (y == 3):
                            C = c
                        if (y == 4):
                            D = d
                        if (y == 5):
                            E = e
                        if (y == 6):
                            F = f
                        if (y == 7):
                            G = g
                        if (y == 8):
                            H = h
                        if (y == 9):
                            I = i
                        if (y == 10):
                            J = j
                        if (y == 11):
                            K = k
                        if (y == 12):
                            L = l
                        if (y == 13):
                            M = m
                        if (y == 14):
                            N = n
                        if (y == 15):
                            O = o
                    if (item == "@"):
                        vie = vie + 1
                        trouver = "continu"
                        if (y == 1):
                            A = a
                        if (y == 2):
                            B = b
                        if (y == 3):
                            C = c
                        if (y == 4):
                            D = d
                        if (y == 5):
                            E = e
                        if (y == 6):
                            F = f
                        if (y == 7):
                            G = g
                        if (y == 8):
                            H = h
                        if (y == 9):
                            I = i
                        if (y == 10):
                            J = j
                        if (y == 11):
                            K = k
                        if (y == 12):
                            L = l
                        if (y == 13):
                            M = m
                        if (y == 14):
                            N = n
                        if (y == 15):
                            O = o
                    if (item == ":"):
                        vie = vie + 1
                        trouver = "roche"
                        if (y == 1):
                            A = a
                        if (y == 2):
                            B = b
                        if (y == 3):
                            C = c
                        if (y == 4):
                            D = d
                        if (y == 5):
                            E = e
                        if (y == 6):
                            F = f
                        if (y == 7):
                            G = g
                        if (y == 8):
                            H = h
                        if (y == 9):
                            I = i
                        if (y == 10):
                            J = j
                        if (y == 11):
                            K = k
                        if (y == 12):
                            L = l
                        if (y == 13):
                            M = m
                        if (y == 14):
                            N = n
                        if (y == 15):
                            O = o
                    if (item == "¬"):
                        vie = vie + 1
                        trouver = "clé"
                        if (y == 1):
                            A = a
                        if (y == 2):
                            B = b
                        if (y == 3):
                            C = c
                        if (y == 4):
                            D = d
                        if (y == 5):
                            E = e
                        if (y == 6):
                            F = f
                        if (y == 7):
                            G = g
                        if (y == 8):
                            H = h
                        if (y == 9):
                            I = i
                        if (y == 10):
                            J = j
                        if (y == 11):
                            K = k
                        if (y == 12):
                            L = l
                        if (y == 13):
                            M = m
                        if (y == 14):
                            N = n
                        if (y == 15):
                            O = o
                    objets.append(trouver)
                    MessageTemple = "Vous trouvez " + trouver
                    y = y - 1
            for item in ["(","[","<","{",")","]",">","}"]:
                if (y == 1 and A[x] == item) or (y == 2 and B[x] == item) or (y == 3 and C[x] == item) or (y == 4 and D[x] == item) or (y == 5 and E[x] == item) or (y == 6 and F[x] == item) or (y == 7 and G[x] == item) or (y == 8 and H[x] == item) or (y == 9 and I[x] == item) or (y == 10 and J[x] == item) or (y == 11 and K[x] == item) or (y == 12 and L[x] == item) or (y == 13 and M[x] == item) or (y == 14 and N[x] == item) or (y == 15 and O[x] == item):
                    if "clé" in objets:
                        ran = random.randint(1, 4)
                        if (ran == 1):
                            MessageTemple = "Vous quitez la pièce."
                        elif (ran == 2):
                            MessageTemple = "Vous empruntez le tunnel."
                        elif (ran == 3):
                            MessageTemple = "Vous trouvez un passage."
                        elif (ran == 4):
                            MessageTemple = "Vous passez la porte."
                        #key = input()
                        Score = Score + (len(objets) * 100)
                        objets = []
                        x = 2
                        y = 5
                        if (item == "[" or item == "]"):
                            lv = lv + 1
                        if (item == "(" or item == ")"):
                            lv = lv - 1
                        x = 2
                        y = 5
                        if (lv <= 0):
                            sourcefile = sf+".joj.txt"
                        if (lv == 1):
                            sourcefile = sf+"1.joj.txt"
                        if (lv == 2):
                            sourcefile = sf+"2.joj.txt"
                        if (lv == 3):
                            sourcefile = sf+"3.joj.txt"
                        if (lv == 4):
                            sourcefile = sf+"4.joj.txt"
                        if (lv == 5):
                            sourcefile = sf+"5.joj.txt"
                        if (lv == 6):
                            sourcefile = sf+"6.joj.txt"
                        if (lv == 7):
                            sourcefile = sf+"7.joj.txt"
                        if (lv == 8):
                            sourcefile = sf+"8.joj.txt"
                        if (lv == 9):
                            sourcefile = sf+"9.joj.txt"
                        if (lv == 10):
                            sourcefile = sf+"10.joj.txt"
                        if (lv == 11):
                            sourcefile = sf+"11.joj.txt"
                        if (lv == 12):
                            sourcefile = sf+"12.joj.txt"
                        if (lv == 13):
                            sourcefile = sf+"13.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 14):
                            sourcefile = sf+"14.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 15):
                            sourcefile = sf+"15.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 16):
                            sourcefile = sf+"16.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 17):
                            sourcefile = sf+"17.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 18):
                            sourcefile = sf+"18.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 19):
                            sourcefile = sf+"19.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 20):
                            sourcefile = sf+"20.joj.txt"
                            x = 2
                            y = 1
                        if (sourcefile == ""):
                            sourcefile = sf+".joj.txt"
                            x = 2
                            y = 5
                        file = open(sourcefile.upper(), "r")
                        ligne = 0
                        for line in file:
                            if (ligne == 0):
                                A = line[:-1]
                            if (ligne == 1):
                                B = line[:-1]
                            if (ligne == 2):
                                C = line[:-1]
                            if (ligne == 3):
                                D = line[:-1]
                            if (ligne == 4):
                                E = line[:-1]
                            if (ligne == 5):
                                F = line[:-1]
                            if (ligne == 6):
                                G = line[:-1]
                            if (ligne == 7):
                                H = line[:-1]
                            if (ligne == 8):
                                I = line[:-1]
                            if (ligne == 9):
                                J = line[:-1]
                            if (ligne == 10):
                                K = line[:-1]
                            if (ligne == 11):
                                L = line[:-1]
                            if (ligne == 12):
                                M = line[:-1]
                            if (ligne == 13):
                                N = line[:-1]
                            if (ligne == 14):
                                O = line[:-1]
                            if (ligne == 15):
                                P = line[:-1]
                            if (ligne == 16):
                                a = line[:-1]
                            if (ligne == 17):
                                b = line[:-1]
                            if (ligne == 18):
                                c = line[:-1]
                            if (ligne == 19):
                                d = line[:-1]
                            if (ligne == 20):
                                e = line[:-1]
                            if (ligne == 21):
                                f = line[:-1]
                            if (ligne == 22):
                                g = line[:-1]
                            if (ligne == 23):
                                h = line[:-1]
                            if (ligne == 24):
                                i = line[:-1]
                            if (ligne == 25):
                                j = line[:-1]
                            if (ligne == 26):
                                k = line[:-1]
                            if (ligne == 27):
                                l = line[:-1]
                            if (ligne == 28):
                                m = line[:-1]
                            if (ligne == 29):
                                n = line[:-1]
                            if (ligne == 30):
                                o = line[:-1]
                            if (ligne == 31):
                                p = line[:-1]
                            ligne = ligne + 1
                        Jeu = 1
                        break
                    else:
                        MessageTemple = "Il vous faudrai une clé pour l'ouvrir."
            #Combat
            if (y == 1 and A[x] == "&") or (y == 2 and B[x] == "&") or (y == 3 and C[x] == "&") or (y == 4 and D[x] == "&") or (y == 5 and E[x] == "&") or (y == 6 and F[x] == "&") or (y == 7 and G[x] == "&") or (y == 8 and H[x] == "&") or (y == 9 and I[x] == "&") or (y == 10 and J[x] == "&") or (y == 11 and K[x] == "&") or (y == 12 and L[x] == "&") or (y == 13 and M[x] == "&") or (y == 14 and N[x] == "&") or (y == 15 and O[x] == "&"):
                #MessageTemple = "Une créature se prépare a vous attaque!"
                
                for att in ["shurican", "boomrang", "roche"]:
                    if att in objets:
                        ran = random.randint(1, 4)
                        if (ran == 1):
                            MessageTemple = "COMBAT! Vous blockez attaque monstre."
                        if (ran == 2):
                            MessageTemple = "COMBAT! Le monstre vous griffe sauvagement."
                            if (god == 0):
                                vie = vie - random.randint(5, 15)
                        if (ran == 3):
                            MessageTemple = "COMBAT! Coup critique, vous tuez le monstre."
                            #mal = mal - random.randint(5, 15)
                            if y == 1:
                                A = a
                            if y == 2:
                                B = b
                            if y == 3:
                                C = c
                            if y == 4:
                                D = d
                            if y == 5:
                                E = e
                            if y == 6:
                                F = f
                            if y == 7:
                                G = g
                            if y == 8:
                                H = h
                            if y == 9:
                                I = i
                            if y == 10:
                                J = j
                            if y == 11:
                                K = k
                            if y == 12:
                                L = l
                            if y == 13:
                                M = m
                            if y == 14:
                                N = n
                            if y == 15:
                                O = o
                        if (ran == 4):
                            MessageTemple = "COMBAT! Le monstre bloque votre attaque."
                        #Refresh Display
                        centre = int((len(String) - len(MessageTemple)) / 2)
                        print(String)
                        print(Isom1, "Santé:",vie,"%", x, y)#Ne ramasse pas les objets avec les touches W,S, quand y = 2,4 mais pas y = 1,3
                        print(Isom2, "Objet:",objets)
                        print(Isom3, "Score:",Score)
                        print(Isom4, "Dungeon Lair, Niveau ", lv)
                        if (len(MessageTemple) == 0):
                            corrige = 1#Test
                        else:
                            corrige = 0
                        print(String[0:centre] + MessageTemple + String[0:centre - corrige])
                        if (y == 0):
                            print(A[:x]+Hero+A[x+1:])
                        else:
                            print(A)
                        if (y == 1):
                            print(B[:x]+Hero+B[x+1:])
                        else:
                            print(B)
                        if (y == 2):
                            print(C[:x]+Hero+C[x+1:])
                        else:
                            print(C)
                        if (y == 3):
                            print(D[:x]+Hero+D[x+1:])
                        else:
                            print(D)
                        if (y == 4):
                            print(E[:x]+Hero+E[x+1:])
                        else:
                            print(E)
                        if (y == 5):
                            print(F[:x]+Hero+F[x+1:])
                        else:
                            print(F)
                        if (y == 6):
                            print(G[:x]+Hero+G[x+1:])
                        else:
                            print(G)
                        if (y == 7):
                            print(H[:x]+Hero+H[x+1:])
                        else:
                            print(H)
                        if (y == 8):
                            print(I[:x]+Hero+I[x+1:])
                        else:
                            print(I)
                        if (y == 9):
                            print(J[:x]+Hero+J[x+1:])
                        else:
                            print(J)
                        if (y == 10):
                            print(K[:x]+Hero+K[x+1:])
                        else:
                            print(K)
                        if (y == 11):
                            print(L[:x]+Hero+L[x+1:])
                        else:
                            print(L)
                        if (y == 12):
                            print(M[:x]+Hero+M[x+1:])
                        else:
                            print(M)
                        if (y == 13):
                            print(N[:x]+Hero+N[x+1:])
                        else:
                            print(N)
                        if (y == 14):
                            print(O[:x]+Hero+O[x+1:])
                        else:
                            print(O)
                        if (y == 15):
                            print(P[:x]+Hero+P[x+1:])
                        else:
                            print(P)
                        print("")
                        press = input("[Press enter]")#Next
                        if "boomrang" in objets:
                            objets = objets
                            MessageTemple = "Le boomrang touche est revein en main."
                        else:
                            if "shurican" in objets:
                                objets.remove("shurican")
                                MessageTemple = "Le shurican la touche et Double dégas."
                                break
                            if "roche" in objets:
                                objets.remove("roche")
                                MessageTemple = "Le roche la frappe entre les yeux."
                                break
        if (y<15 and key[z].upper() == "S"):
            if (y == 0 and B[x] == " ") or (y == 1 and C[x] == " ") or (y == 2 and D[x] == " ") or (y == 3 and E[x] == " ") or (y == 4 and F[x] == " ") or (y == 5 and G[x] == " ") or (y == 6 and H[x] == " ") or (y == 7 and I[x] == " ") or (y == 8 and J[x] == " ") or (y == 9 and K[x] == " ") or (y == 10 and L[x] == " ") or (y == 11 and M[x] == " ") or (y == 12 and N[x] == " ") or (y == 13 and O[x] == " ") or (y == 14 and P[x] == " "):
                # or (y == 0 and B[x] == "¬") or (y == 1 and C[x] == "¬") or (y == 2 and D[x] == "¬") or (y == 3 and E[x] == "¬") or (y == 4 and F[x] == "¬") or (y == 5 and G[x] == "¬") or (y == 6 and H[x] == "¬") or (y == 7 and I[x] == "¬") or (y == 8 and J[x] == "¬") or (y == 9 and K[x] == "¬") or (y == 10 and L[x] == "¬") or (y == 11 and M[x] == "¬") or (y == 12 and N[x] == "¬") or (y == 13 and O[x] == "¬") or (y == 14 and P[x] == "¬") or (y == 0 and B[x] == ":") or (y == 1 and C[x] == ":") or (y == 2 and D[x] == ":") or (y == 3 and E[x] == ":") or (y == 4 and F[x] == ":") or (y == 5 and G[x] == ":") or (y == 6 and H[x] == ":") or (y == 7 and I[x] == ":") or (y == 8 and J[x] == ":") or (y == 9 and K[x] == ":") or (y == 10 and L[x] == ":") or (y == 11 and M[x] == ":") or (y == 12 and N[x] == ":") or (y == 13 and O[x] == ":") or (y == 14 and P[x] == ":") or (y == 0 and B[x] == "@") or (y == 1 and C[x] == "@") or (y == 2 and D[x] == "@") or (y == 3 and E[x] == "@") or (y == 4 and F[x] == "@") or (y == 5 and G[x] == "@") or (y == 6 and H[x] == "@") or (y == 7 and I[x] == "@") or (y == 8 and J[x] == "@") or (y == 9 and K[x] == "@") or (y == 10 and L[x] == "@") or (y == 11 and M[x] == "@") or (y == 12 and N[x] == "@") or (y == 13 and O[x] == "@") or (y == 14 and P[x] == "@") or (y == 0 and B[x] == "¨") or (y == 1 and C[x] == "¨") or (y == 2 and D[x] == "¨") or (y == 3 and E[x] == "¨") or (y == 4 and F[x] == "¨") or (y == 5 and G[x] == "¨") or (y == 6 and H[x] == "¨") or (y == 7 and I[x] == "¨") or (y == 8 and J[x] == "¨") or (y == 9 and K[x] == "¨") or (y == 10 and L[x] == "¨") or (y == 11 and M[x] == "¨") or (y == 12 and N[x] == "¨") or (y == 13 and O[x] == "¨") or (y == 14 and P[x] == "¨") or (y == 0 and B[x] == "^") or (y == 1 and C[x] == "^") or (y == 2 and D[x] == "^") or (y == 3 and E[x] == "^") or (y == 4 and F[x] == "^") or (y == 5 and G[x] == "^") or (y == 6 and H[x] == "^") or (y == 7 and I[x] == "^") or (y == 8 and J[x] == "^") or (y == 9 and K[x] == "^") or (y == 10 and L[x] == "^") or (y == 11 and M[x] == "^") or (y == 12 and N[x] == "^") or (y == 13 and O[x] == "^") or (y == 14 and P[x] == "^") or (y == 0 and B[x] == "*") or (y == 1 and C[x] == "*") or (y == 2 and D[x] == "*") or (y == 3 and E[x] == "*") or (y == 4 and F[x] == "*") or (y == 5 and G[x] == "*") or (y == 6 and H[x] == "*") or (y == 7 and I[x] == "*") or (y == 8 and J[x] == "*") or (y == 9 and K[x] == "*") or (y == 10 and L[x] == "*") or (y == 11 and M[x] == "*") or (y == 12 and N[x] == "*") or (y == 13 and O[x] == "*") or (y == 14 and P[x] == "*")
                y = y + 1
                MessageTemple = ""
            else:
                if (clip == 1):
                    y = y + 1
                    MessageTemple = "Vous passez a traver les mures."
                else:
                    MessageTemple = "Vous ne passez pas les mures."
                    if (god == 0):
                        vie = vie - 1
            for item in ["*","^","¨","@",":","¬"]:
                if (y == 0 and B[x] == item) or (y == 1 and C[x] == item) or (y == 2 and D[x] == item) or (y == 3 and E[x] == item) or (y == 4 and F[x] == item) or (y == 5 and G[x] == item) or (y == 6 and H[x] == item) or (y == 7 and I[x] == item) or (y == 8 and J[x] == item) or (y == 9 and K[x] == item) or (y == 10 and L[x] == item) or (y == 11 and M[x] == item) or (y == 12 and N[x] == item) or (y == 13 and O[x] == item) or (y == 14 and P[x] == item):
                    if (item == "*"):
                        vie = vie + 1
                        trouver = "shurican"
                        if (y == 0):
                            B = b
                        if (y == 1):
                            C = c
                        if (y == 2):
                            D = d
                        if (y == 3):
                            E = e
                        if (y == 4):
                            F = f
                        if (y == 5):
                            G = g
                        if (y == 6):
                            H = h
                        if (y == 7):
                            I = i
                        if (y == 8):
                            J = j
                        if (y == 9):
                            K = k
                        if (y == 10):
                            L = l
                        if (y == 11):
                            M = m
                        if (y == 12):
                            N = n
                        if (y == 13):
                            O = o
                        if (y == 14):
                            P = p
                    if (item == "^"):
                        vie = vie + 1
                        trouver = "boomrang"
                        if (y == 0):
                            B = b
                        if (y == 1):
                            C = c
                        if (y == 2):
                            D = d
                        if (y == 3):
                            E = e
                        if (y == 4):
                            F = f
                        if (y == 5):
                            G = g
                        if (y == 6):
                            H = h
                        if (y == 7):
                            I = i
                        if (y == 8):
                            J = j
                        if (y == 9):
                            K = k
                        if (y == 10):
                            L = l
                        if (y == 11):
                            M = m
                        if (y == 12):
                            N = n
                        if (y == 13):
                            O = o
                        if (y == 14):
                            P = p
                    if (item == "¨"):
                        vie = vie + 1
                        trouver = "mush"
                        if (y == 0):
                            B = b
                        if (y == 1):
                            C = c
                        if (y == 2):
                            D = d
                        if (y == 3):
                            E = e
                        if (y == 4):
                            F = f
                        if (y == 5):
                            G = g
                        if (y == 6):
                            H = h
                        if (y == 7):
                            I = i
                        if (y == 8):
                            J = j
                        if (y == 9):
                            K = k
                        if (y == 10):
                            L = l
                        if (y == 11):
                            M = m
                        if (y == 12):
                            N = n
                        if (y == 13):
                            O = o
                        if (y == 14):
                            P = p
                    if (item == "@"):
                        vie = vie + 1
                        trouver = "continu"
                        if (y == 0):
                            B = b
                        if (y == 1):
                            C = c
                        if (y == 2):
                            D = d
                        if (y == 3):
                            E = e
                        if (y == 4):
                            F = f
                        if (y == 5):
                            G = g
                        if (y == 6):
                            H = h
                        if (y == 7):
                            I = i
                        if (y == 8):
                            J = j
                        if (y == 9):
                            K = k
                        if (y == 10):
                            L = l
                        if (y == 11):
                            M = m
                        if (y == 12):
                            N = n
                        if (y == 13):
                            O = o
                        if (y == 14):
                            P = p
                    if (item == "¬"):
                        vie = vie + 1
                        trouver = "clé"
                        if (y == 0):
                            B = b
                        if (y == 1):
                            C = c
                        if (y == 2):
                            D = d
                        if (y == 3):
                            E = e
                        if (y == 4):
                            F = f
                        if (y == 5):
                            G = g
                        if (y == 6):
                            H = h
                        if (y == 7):
                            I = i
                        if (y == 8):
                            J = j
                        if (y == 9):
                            K = k
                        if (y == 10):
                            L = l
                        if (y == 11):
                            M = m
                        if (y == 12):
                            N = n
                        if (y == 13):
                            O = o
                        if (y == 14):
                            P = p
                    if (item == ":"):
                        vie = vie + 1
                        trouver = "roche"
                        if (y == 0):
                            B = b
                        if (y == 1):
                            C = c
                        if (y == 2):
                            D = d
                        if (y == 3):
                            E = e
                        if (y == 4):
                            F = f
                        if (y == 5):
                            G = g
                        if (y == 6):
                            H = h
                        if (y == 7):
                            I = i
                        if (y == 8):
                            J = j
                        if (y == 9):
                            K = k
                        if (y == 10):
                            L = l
                        if (y == 11):
                            M = m
                        if (y == 12):
                            N = n
                        if (y == 13):
                            O = o
                        if (y == 14):
                            P = p
                    objets.append(trouver)
                    MessageTemple = "Vous trouvez " + trouver
                    y = y + 1
            for item in ["(","[","<","{",")","]",">","}"]:
                if (y == 0 and B[x] == item) or (y == 1 and C[x] == item) or (y == 2 and D[x] == item) or (y == 3 and E[x] == item) or (y == 4 and F[x] == item) or (y == 5 and G[x] == item) or (y == 6 and H[x] == item) or (y == 7 and I[x] == item) or (y == 8 and J[x] == item) or (y == 9 and K[x] == item) or (y == 10 and L[x] == item) or (y == 11 and M[x] == item) or (y == 12 and N[x] == item) or (y == 13 and O[x] == item) or (y == 14 and P[x] == item):
                    if "clé" in objets:
                        ran = random.randint(1, 4)
                        if (ran == 1):
                            MessageTemple = "Vous quitez la pièce."
                        if (ran == 2):
                            MessageTemple = "Vous empruntez le tunnel."
                        if (ran == 3):
                            MessageTemple = "Vous trouvez un passage."
                        if (ran == 4):
                            MessageTemple = "Vous passez la porte."
                        #key = input()
                        Score = Score + (len(objets) * 100)
                        objets = []
                        x = 2
                        y = 5
                        if (item == "[" or item == "]"):
                            lv = lv + 1
                        if (item == "(" or item == ")"):
                            lv = lv - 1
                        x = 2
                        y = 5
                        if (lv <= 0):
                            sourcefile = sf+".joj.txt"
                        if (lv == 1):
                            sourcefile = sf+"1.joj.txt"
                        if (lv == 2):
                            sourcefile = sf+"2.joj.txt"
                        if (lv == 3):
                            sourcefile = sf+"3.joj.txt"
                        if (lv == 4):
                            sourcefile = sf+"4.joj.txt"
                        if (lv == 5):
                            sourcefile = sf+"5.joj.txt"
                        if (lv == 6):
                            sourcefile = sf+"6.joj.txt"
                        if (lv == 7):
                            sourcefile = sf+"7.joj.txt"
                        if (lv == 8):
                            sourcefile = sf+"8.joj.txt"
                        if (lv == 9):
                            sourcefile = sf+"9.joj.txt"
                        if (lv == 10):
                            sourcefile = sf+"10.joj.txt"
                        if (lv == 11):
                            sourcefile = sf+"11.joj.txt"
                        if (lv == 12):
                            sourcefile = sf+"12.joj.txt"
                        if (lv == 13):
                            sourcefile = sf+"13.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 14):
                            sourcefile = sf+"14.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 15):
                            sourcefile = sf+"15.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 16):
                            sourcefile = sf+"16.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 17):
                            sourcefile = sf+"17.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 18):
                            sourcefile = sf+"18.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 19):
                            sourcefile = sf+"19.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 20):
                            sourcefile = sf+"20.joj.txt"
                            x = 2
                            y = 1
                        if (sourcefile == ""):
                            sourcefile = sf+".joj.txt"
                            x = 2
                            y = 5
                        file = open(sourcefile.upper(), "r")
                        ligne = 0
                        for line in file:
                            if (ligne == 0):
                                A = line[:-1]
                            if (ligne == 1):
                                B = line[:-1]
                            if (ligne == 2):
                                C = line[:-1]
                            if (ligne == 3):
                                D = line[:-1]
                            if (ligne == 4):
                                E = line[:-1]
                            if (ligne == 5):
                                F = line[:-1]
                            if (ligne == 6):
                                G = line[:-1]
                            if (ligne == 7):
                                H = line[:-1]
                            if (ligne == 8):
                                I = line[:-1]
                            if (ligne == 9):
                                J = line[:-1]
                            if (ligne == 10):
                                K = line[:-1]
                            if (ligne == 11):
                                L = line[:-1]
                            if (ligne == 12):
                                M = line[:-1]
                            if (ligne == 13):
                                N = line[:-1]
                            if (ligne == 14):
                                O = line[:-1]
                            if (ligne == 15):
                                P = line[:-1]
                            if (ligne == 16):
                                a = line[:-1]
                            if (ligne == 17):
                                b = line[:-1]
                            if (ligne == 18):
                                c = line[:-1]
                            if (ligne == 19):
                                d = line[:-1]
                            if (ligne == 20):
                                e = line[:-1]
                            if (ligne == 21):
                                f = line[:-1]
                            if (ligne == 22):
                                g = line[:-1]
                            if (ligne == 23):
                                h = line[:-1]
                            if (ligne == 24):
                                i = line[:-1]
                            if (ligne == 25):
                                j = line[:-1]
                            if (ligne == 26):
                                k = line[:-1]
                            if (ligne == 27):
                                l = line[:-1]
                            if (ligne == 28):
                                m = line[:-1]
                            if (ligne == 29):
                                n = line[:-1]
                            if (ligne == 30):
                                o = line[:-1]
                            if (ligne == 31):
                                p = line[:-1]
                            ligne = ligne + 1
                        Jeu = 1
                        break
                    else:
                        MessageTemple = "Il vous faudrai une clé pour l'ouvrir."
        if (x>0 and key[z].upper() == "A"):
            if (y == 0 and A[x-1] == " ") or (y == 1 and B[x-1] == " ") or (y == 2 and C[x-1] == " ") or (y == 3 and D[x-1] == " ") or (y == 4 and E[x-1] == " ") or (y == 5 and F[x-1] == " ") or (y == 6 and G[x-1] == " ") or (y == 7 and H[x] == " ") or (y == 8 and I[x] == " ") or (y == 9 and J[x] == " ") or (y == 10 and K[x] == " ") or (y == 11 and L[x] == " ") or (y == 12 and M[x] == " ") or (y == 13 and N[x] == " ") or (y == 14 and O[x] == " ") or (y == 15 and P[x] == " ") or (y == 0 and A[x-1] == "*") or (y == 1 and B[x-1] == "*") or (y == 2 and C[x-1] == "*") or (y == 3 and D[x-1] == "*") or (y == 4 and E[x-1] == "*") or (y == 5 and F[x-1] == "*") or (y == 6 and G[x-1] == "*") or (y == 7 and H[x] == "*") or (y == 8 and I[x] == "*") or (y == 9 and J[x] == "*") or (y == 10 and K[x] == "*") or (y == 11 and L[x] == "*") or (y == 12 and M[x] == "*") or (y == 13 and N[x] == "*") or (y == 14 and O[x] == "*") or (y == 15 and P[x] == "*") or (y == 0 and A[x-1] == "^") or (y == 1 and B[x-1] == "^") or (y == 2 and C[x-1] == "^") or (y == 3 and D[x-1] == "^") or (y == 4 and E[x-1] == "^") or (y == 5 and F[x-1] == "^") or (y == 6 and G[x-1] == "^") or (y == 7 and H[x] == "^") or (y == 8 and I[x] == "^") or (y == 9 and J[x] == "^") or (y == 10 and K[x] == "^") or (y == 11 and L[x] == "^") or (y == 12 and M[x] == "^") or (y == 13 and N[x] == "^") or (y == 14 and O[x] == "^") or (y == 15 and P[x] == "^") or (y == 0 and A[x-1] == "¨") or (y == 1 and B[x-1] == "¨") or (y == 2 and C[x-1] == "¨") or (y == 3 and D[x-1] == "¨") or (y == 4 and E[x-1] == "¨") or (y == 5 and F[x-1] == "¨") or (y == 6 and G[x-1] == "¨") or (y == 7 and H[x] == "¨") or (y == 8 and I[x] == "¨") or (y == 9 and J[x] == "¨") or (y == 10 and K[x] == "¨") or (y == 11 and L[x] == "¨") or (y == 12 and M[x] == "¨") or (y == 13 and N[x] == "¨") or (y == 14 and O[x] == "¨") or (y == 15 and P[x] == "¨") or (y == 0 and A[x-1] == "@") or (y == 1 and B[x-1] == "@") or (y == 2 and C[x-1] == "@") or (y == 3 and D[x-1] == "@") or (y == 4 and E[x-1] == "@") or (y == 5 and F[x-1] == "@") or (y == 6 and G[x-1] == "@") or (y == 7 and H[x] == "@") or (y == 8 and I[x] == "@") or (y == 9 and J[x] == "@") or (y == 10 and K[x] == "@") or (y == 11 and L[x] == "@") or (y == 12 and M[x] == "@") or (y == 13 and N[x] == "@") or (y == 14 and O[x] == "@") or (y == 15 and P[x] == "@") or (y == 0 and A[x-1] == ":") or (y == 1 and B[x-1] == ":") or (y == 2 and C[x-1] == ":") or (y == 3 and D[x-1] == ":") or (y == 4 and E[x-1] == ":") or (y == 5 and F[x-1] == ":") or (y == 6 and G[x-1] == ":") or (y == 7 and H[x] == ":") or (y == 8 and I[x] == ":") or (y == 9 and J[x] == ":") or (y == 10 and K[x] == ":") or (y == 11 and L[x] == ":") or (y == 12 and M[x] == ":") or (y == 13 and N[x] == ":") or (y == 14 and O[x] == ":") or (y == 15 and P[x] == ":") or (y == 0 and A[x-1] == "¬") or (y == 1 and B[x-1] == "¬") or (y == 2 and C[x-1] == "¬") or (y == 3 and D[x-1] == "¬") or (y == 4 and E[x-1] == "¬") or (y == 5 and F[x-1] == "¬") or (y == 6 and G[x-1] == "¬") or (y == 7 and H[x] == "¬") or (y == 8 and I[x] == "¬") or (y == 9 and J[x] == "¬") or (y == 10 and K[x] == "¬") or (y == 11 and L[x] == "¬") or (y == 12 and M[x] == "¬") or (y == 13 and N[x] == "¬") or (y == 14 and O[x] == "¬") or (y == 15 and P[x] == "¬"):
                x = x - 1
                MessageTemple = ""
            else:
                if (clip == 1):
                    x = x - 1
                    MessageTemple = "Vous passez a traver les mures."
                else:
                    MessageTemple = "Vous ne passez pas les mures."
                    if (god == 0):
                        vie = vie - 1
            for item in ["*","^","¨","@",":","¬"]:
                if (y == 0 and A[x-1] == item) or (y == 1 and B[x-1] == item) or (y == 2 and C[x-1] == item) or (y == 3 and D[x-1] == item) or (y == 4 and E[x-1] == item) or (y == 5 and F[x-1] == item) or (y == 6 and G[x-1] == item) or (y == 7 and H[x] == item) or (y == 8 and I[x] == item) or (y == 9 and J[x] == item) or (y == 10 and K[x] == item) or (y == 11 and L[x] == item) or (y == 12 and M[x] == item) or (y == 13 and N[x] == item) or (y == 14 and O[x] == item) or (y == 15 and P[x] == item):
                    if (item == "*"):
                        #vie = vie + 1
                        trouver = "shurican"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "^"):
                        #vie = vie + 1
                        trouver = "boomrang"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "¨"):
                        #vie = vie + 1
                        trouver = "mush"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "@"):
                        #vie = vie + 1
                        trouver = "continu"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == ":"):
                        #vie = vie + 1
                        trouver = "roche"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "¬"):
                        #vie = vie + 1
                        trouver = "clé"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    objets.append(trouver)
                    MessageTemple = "Vous trouvez " + trouver
                    #x = x - 1
            for item in ["(","[","<","{",")","]",">","}"]:
                if (y == 0 and A[x-1] == item) or (y == 1 and B[x-1] == item) or (y == 2 and C[x-1] == item) or (y == 3 and D[x-1] == item) or (y == 4 and E[x-1] == item) or (y == 5 and F[x-1] == item) or (y == 6 and G[x-1] == item) or (y == 7 and H[x] == item) or (y == 8 and I[x] == item) or (y == 9 and J[x] == item) or (y == 10 and K[x] == item) or (y == 11 and L[x] == item) or (y == 12 and M[x] == item) or (y == 13 and N[x] == item) or (y == 14 and O[x] == item) or (y == 15 and P[x] == item):
                    if "clé" in objets:
                        x = 2
                        y = 5
                        if (item == "[" or item == "]"):
                            lv = lv + 1
                        if (item == "(" or item == ")"):
                            lv = lv - 1
                        ran = random.randint(1, 4)
                        if (ran == 1):
                            MessageTemple = "Vous quitez la pièce."
                        if (ran == 2):
                            MessageTemple = "Vous empruntez le tunnel."
                        if (ran == 3):
                            MessageTemple = "Vous trouvez un passage."
                        if (ran == 4):
                            MessageTemple = "Vous passez la porte."
                        #key = input()
                        Score = Score + (len(objets) * 100)
                        objets = []
                        x = 2
                        y = 5
                        if (lv <= 0):
                            lv=0
                            sourcefile = sf+".joj.txt"
                        if (lv == 1):
                            sourcefile = sf+"1.joj.txt"
                        if (lv == 2):
                            sourcefile = sf+"2.joj.txt"
                        if (lv == 3):
                            sourcefile = sf+"3.joj.txt"
                        if (lv == 4):
                            sourcefile = sf+"4.joj.txt"
                        if (lv == 5):
                            sourcefile = sf+"5.joj.txt"
                        if (lv == 6):
                            sourcefile = sf+"6.joj.txt"
                        if (lv == 7):
                            sourcefile = sf+"7.joj.txt"
                        if (lv == 8):
                            sourcefile = sf+"8.joj.txt"
                        if (lv == 9):
                            sourcefile = sf+"9.joj.txt"
                        if (lv == 10):
                            sourcefile = sf+"10.joj.txt"
                        if (lv == 11):
                            sourcefile = sf+"11.joj.txt"
                        if (lv == 12):
                            sourcefile = sf+"12.joj.txt"
                        if (lv == 13):
                            sourcefile = sf+"13.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 14):
                            sourcefile = sf+"14.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 15):
                            sourcefile = sf+"15.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 16):
                            sourcefile = sf+"16.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 17):
                            sourcefile = sf+"17.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 18):
                            sourcefile = sf+"18.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 19):
                            sourcefile = sf+"19.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 20):
                            sourcefile = sf+"20.joj.txt"
                            x = 2
                            y = 1
                        if (sourcefile == ""):
                            sourcefile = sf+".joj.txt"
                            x = 2
                            y = 5
                        file = open(sourcefile.upper(), "r")
                        ligne = 0
                        for line in file:
                            if (ligne == 0):
                                A = line[:-1]
                            if (ligne == 1):
                                B = line[:-1]
                            if (ligne == 2):
                                C = line[:-1]
                            if (ligne == 3):
                                D = line[:-1]
                            if (ligne == 4):
                                E = line[:-1]
                            if (ligne == 5):
                                F = line[:-1]
                            if (ligne == 6):
                                G = line[:-1]
                            if (ligne == 7):
                                H = line[:-1]
                            if (ligne == 8):
                                I = line[:-1]
                            if (ligne == 9):
                                J = line[:-1]
                            if (ligne == 10):
                                K = line[:-1]
                            if (ligne == 11):
                                L = line[:-1]
                            if (ligne == 12):
                                M = line[:-1]
                            if (ligne == 13):
                                N = line[:-1]
                            if (ligne == 14):
                                O = line[:-1]
                            if (ligne == 15):
                                P = line[:-1]
                            if (ligne == 16):
                                a = line[:-1]
                            if (ligne == 17):
                                b = line[:-1]
                            if (ligne == 18):
                                c = line[:-1]
                            if (ligne == 19):
                                d = line[:-1]
                            if (ligne == 20):
                                e = line[:-1]
                            if (ligne == 21):
                                f = line[:-1]
                            if (ligne == 22):
                                g = line[:-1]
                            if (ligne == 23):
                                h = line[:-1]
                            if (ligne == 24):
                                i = line[:-1]
                            if (ligne == 25):
                                j = line[:-1]
                            if (ligne == 26):
                                k = line[:-1]
                            if (ligne == 27):
                                l = line[:-1]
                            if (ligne == 28):
                                m = line[:-1]
                            if (ligne == 29):
                                n = line[:-1]
                            if (ligne == 30):
                                o = line[:-1]
                            if (ligne == 31):
                                p = line[:-1]
                            ligne = ligne + 1
                        Jeu = 1
                        break
                    else:
                        MessageTemple = "Il vous faudrai une clé pour l'ouvrir."
        if (x < MaxX and key[z].upper() == "D"):
            if ((y == 0 and A[x+1] == "¬") or (y == 1 and B[x+1] == "¬") or (y == 2 and C[x+1] == "¬") or (y == 3 and D[x+1] == "¬") or (y == 4 and E[x+1] == "¬") or (y == 5 and F[x+1] == "¬") or (y == 6 and G[x+1] == "¬") or (y == 7 and H[x] == "¬") or (y == 8 and I[x] == "¬") or (y == 9 and J[x] == "¬") or (y == 10 and K[x] == "¬") or (y == 11 and L[x] == "¬") or (y == 12 and M[x] == "¬") or (y == 13 and N[x] == "¬") or (y == 14 and O[x] == "¬") or (y == 15 and P[x] == "¬") or (y == 0 and A[x+1] == "*") or (y == 1 and B[x+1] == "*") or (y == 2 and C[x+1] == "*") or (y == 3 and D[x+1] == "*") or (y == 4 and E[x+1] == "*") or (y == 5 and F[x+1] == "*") or (y == 6 and G[x+1] == "*") or (y == 7 and H[x] == "*") or (y == 8 and I[x] == "*") or (y == 9 and J[x] == "*") or (y == 10 and K[x] == "*") or (y == 11 and L[x] == "*") or (y == 12 and M[x] == "*") or (y == 13 and N[x] == "*") or (y == 14 and O[x] == "*") or (y == 15 and P[x] == "*") or (y == 0 and A[x+1] == "@") or (y == 1 and B[x+1] == "@") or (y == 2 and C[x+1] == "@") or (y == 3 and D[x+1] == "@") or (y == 4 and E[x+1] == "@") or (y == 5 and F[x+1] == "@") or (y == 6 and G[x+1] == "@") or (y == 7 and H[x] == "@") or (y == 8 and I[x] == "@") or (y == 9 and J[x] == "@") or (y == 10 and K[x] == "@") or (y == 11 and L[x] == "@") or (y == 12 and M[x] == "@") or (y == 13 and N[x] == "@") or (y == 14 and O[x] == "@") or (y == 15 and P[x] == "@") or (y == 0 and A[x+1] == " ") or (y == 1 and B[x+1] == " ") or (y == 2 and C[x+1] == " ") or (y == 3 and D[x+1] == " ") or (y == 4 and E[x+1] == " ") or (y == 5 and F[x+1] == " ") or (y == 6 and G[x+1] == " ") or (y == 7 and H[x] == " ") or (y == 8 and I[x] == " ") or (y == 9 and J[x] == " ") or (y == 10 and K[x] == " ") or (y == 11 and L[x] == " ") or (y == 12 and M[x] == " ") or (y == 13 and N[x] == " ") or (y == 14 and O[x] == " ") or (y == 15 and P[x] == " ") or (y == 0 and A[x+1] == "^") or (y == 1 and B[x+1] == "^") or (y == 2 and C[x+1] == "^") or (y == 3 and D[x+1] == "^") or (y == 4 and E[x+1] == "^") or (y == 5 and F[x+1] == "^") or (y == 6 and G[x+1] == "^") or (y == 7 and H[x] == "^") or (y == 8 and I[x] == "^") or (y == 9 and J[x] == "^") or (y == 10 and K[x] == "^") or (y == 11 and L[x] == "^") or (y == 12 and M[x] == "^") or (y == 13 and N[x] == "^") or (y == 14 and O[x] == "^") or (y == 15 and P[x] == "^") or (y == 0 and A[x+1] == ":") or (y == 1 and B[x+1] == ":") or (y == 2 and C[x+1] == ":") or (y == 3 and D[x+1] == ":") or (y == 4 and E[x+1] == ":") or (y == 5 and F[x+1] == ":") or (y == 6 and G[x+1] == ":") or (y == 7 and H[x] == ":") or (y == 8 and I[x] == ":") or (y == 9 and J[x] == ":") or (y == 10 and K[x] == ":") or (y == 11 and L[x] == ":") or (y == 12 and M[x] == ":") or (y == 13 and N[x] == ":") or (y == 14 and O[x] == ":") or (y == 15 and P[x] == ":") or (y == 0 and A[x+1] == "¨") or (y == 1 and B[x+1] == "¨") or (y == 2 and C[x+1] == "¨") or (y == 3 and D[x+1] == "¨") or (y == 4 and E[x+1] == "¨") or (y == 5 and F[x+1] == "¨") or (y == 6 and G[x+1] == "¨") or (y == 7 and H[x] == "¨") or (y == 8 and I[x] == "¨") or (y == 9 and J[x] == "¨") or (y == 10 and K[x] == "¨") or (y == 11 and L[x] == "¨") or (y == 12 and M[x] == "¨") or (y == 13 and N[x] == "¨") or (y == 14 and O[x] == "¨") or (y == 15 and P[x] == "¨")):
                x = x + 1
                MessageTemple = ""
            else:
                if (clip == 1):
                    x = x + 1
                    MessageTemple = "Vous passez a traver les mures."
                else:
                    MessageTemple = "Vous ne passez pas les mures."
                    if (god == 0):
                        vie = vie - 1
            for item in ["*","^","¨","@",":","¬"]:
                if (y == 0 and A[x+1] == item) or (y == 1 and B[x+1] == item) or (y == 2 and C[x+1] == item) or (y == 3 and D[x+1] == item) or (y == 4 and E[x+1] == item) or (y == 5 and F[x+1] == item) or (y == 6 and G[x+1] == item) or (y == 7 and H[x] == item) or (y == 8 and I[x] == item) or (y == 9 and J[x] == item) or (y == 10 and K[x] == item) or (y == 11 and L[x] == item) or (y == 12 and M[x] == item) or (y == 13 and N[x] == item) or (y == 14 and O[x] == item) or (y == 15 and P[x] == item):
                    if (item == "*"):
                        #vie = vie + 1
                        trouver = "shurican"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "^"):
                        #vie = vie + 1
                        trouver = "boomrang"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "¨"):
                        #vie = vie + 1
                        trouver = "mush"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "@"):
                        #vie = vie + 1
                        trouver = "continu"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == ":"):
                        #vie = vie + 1
                        trouver = "roche"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    if (item == "¬"):
                        #vie = vie + 1
                        trouver = "clé"
                        if (y == 0):
                            A = a
                        if (y == 1):
                            B = b
                        if (y == 2):
                            C = c
                        if (y == 3):
                            D = d
                        if (y == 4):
                            E = e
                        if (y == 5):
                            F = f
                        if (y == 6):
                            G = g
                        if (y == 7):
                            H = h
                        if (y == 8):
                            I = i
                        if (y == 9):
                            J = j
                        if (y == 10):
                            K = k
                        if (y == 11):
                            L = l
                        if (y == 12):
                            M = m
                        if (y == 13):
                            N = n
                        if (y == 14):
                            O = o
                    objets.append(trouver)
                    MessageTemple = "Vous trouvez " + trouver
            for item in ["(","[","<","{",")","]",">","}"]:
                if (y == 0 and A[x+1] == item) or (y == 1 and B[x+1] == item) or (y == 2 and C[x+1] == item) or (y == 3 and D[x+1] == item) or (y == 4 and E[x+1] == item) or (y == 5 and F[x+1] == item) or (y == 6 and G[x+1] == item) or (y == 7 and H[x] == item) or (y == 8 and I[x] == item) or (y == 9 and J[x] == item) or (y == 10 and K[x] == item) or (y == 11 and L[x] == item) or (y == 12 and M[x] == item) or (y == 13 and N[x] == item) or (y == 14 and O[x] == item) or (y == 15 and P[x] == item):
                    if "clé" in objets:
                        x = 2
                        y = 5
                        if (item == "[" or item == "]"):
                            lv = lv + 1
                        if (item == "(" or item == ")"):
                            lv = lv - 1
                        ran = random.randint(1, 4)
                        if (ran == 1):
                            MessageTemple = "Vous quitez la pièce."
                        if (ran == 2):
                            MessageTemple = "Vous empruntez le tunnel."
                        if (ran == 3):
                            MessageTemple = "Vous trouvez un passage."
                        if (ran == 4):
                            MessageTemple = "Vous passez la porte."
                        #key = input()
                        Score = Score + (len(objets) * 100)
                        objets = []
                        x = 2
                        y = 5
                        if (lv <= 0):
                            lv=0
                            sourcefile = sf+".joj.txt"
                        if (lv == 1):
                            sourcefile = sf+"1.joj.txt"
                        if (lv == 2):
                            sourcefile = sf+"2.joj.txt"
                        if (lv == 3):
                            sourcefile = sf+"3.joj.txt"
                        if (lv == 4):
                            sourcefile = sf+"4.joj.txt"
                        if (lv == 5):
                            sourcefile = sf+"5.joj.txt"
                        if (lv == 6):
                            sourcefile = sf+"6.joj.txt"
                        if (lv == 7):
                            sourcefile = sf+"7.joj.txt"
                        if (lv == 8):
                            sourcefile = sf+"8.joj.txt"
                        if (lv == 9):
                            sourcefile = sf+"9.joj.txt"
                        if (lv == 10):
                            sourcefile = sf+"10.joj.txt"
                        if (lv == 11):
                            sourcefile = sf+"11.joj.txt"
                        if (lv == 12):
                            sourcefile = sf+"12.joj.txt"
                        if (lv == 13):
                            sourcefile = sf+"13.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 14):
                            sourcefile = sf+"14.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 15):
                            sourcefile = sf+"15.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 16):
                            sourcefile = sf+"16.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 17):
                            sourcefile = sf+"17.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 18):
                            sourcefile = sf+"18.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 19):
                            sourcefile = sf+"19.joj.txt"
                            x = 2
                            y = 1
                        if (lv == 20):
                            sourcefile = sf+"20.joj.txt"
                            x = 2
                            y = 1
                        if (sourcefile == ""):
                            sourcefile = sf+".joj.txt"
                            x = 2
                            y = 5
                        file = open(sourcefile.upper(), "r")
                        ligne = 0
                        for line in file:
                            if (ligne == 0):
                                A = line[:-1]
                            if (ligne == 1):
                                B = line[:-1]
                            if (ligne == 2):
                                C = line[:-1]
                            if (ligne == 3):
                                D = line[:-1]
                            if (ligne == 4):
                                E = line[:-1]
                            if (ligne == 5):
                                F = line[:-1]
                            if (ligne == 6):
                                G = line[:-1]
                            if (ligne == 7):
                                H = line[:-1]
                            if (ligne == 8):
                                I = line[:-1]
                            if (ligne == 9):
                                J = line[:-1]
                            if (ligne == 10):
                                K = line[:-1]
                            if (ligne == 11):
                                L = line[:-1]
                            if (ligne == 12):
                                M = line[:-1]
                            if (ligne == 13):
                                N = line[:-1]
                            if (ligne == 14):
                                O = line[:-1]
                            if (ligne == 15):
                                P = line[:-1]
                            if (ligne == 16):
                                a = line[:-1]
                            if (ligne == 17):
                                b = line[:-1]
                            if (ligne == 18):
                                c = line[:-1]
                            if (ligne == 19):
                                d = line[:-1]
                            if (ligne == 20):
                                e = line[:-1]
                            if (ligne == 21):
                                f = line[:-1]
                            if (ligne == 22):
                                g = line[:-1]
                            if (ligne == 23):
                                h = line[:-1]
                            if (ligne == 24):
                                i = line[:-1]
                            if (ligne == 25):
                                j = line[:-1]
                            if (ligne == 26):
                                k = line[:-1]
                            if (ligne == 27):
                                l = line[:-1]
                            if (ligne == 28):
                                m = line[:-1]
                            if (ligne == 29):
                                n = line[:-1]
                            if (ligne == 30):
                                o = line[:-1]
                            if (ligne == 31):
                                p = line[:-1]
                            ligne = ligne + 1
                        Jeu = 1
                        break
                    else:
                        MessageTemple = "Il vous faudrai une clé pour l'ouvrir."
