import tkinter
from random import randint

#################################################################################
#
#  Parametres du jeu

canvas = None   # zone de dessin

#Grille[0][0] désigne la case en haut à gauche
#Grille[2][0] désigne la case en haut à droite
#Grille[0][2] désigne la case en bas à gauche


Grille = [ [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0] ]  # attention les lignes représentent les colonnes de la grille

Scores = [0,0]   # score du joueur 1 (Humain) et 2 (IA)

#################################################################################
#
# gestion du joueur humain et de l'IA
# VOTRE CODE ICI

def Reset_Grille():
    for i in range(len(Grille)):
        for j in range(len(Grille[i])):
            Grille[i][j] = 0

def checkAlignement(joueur):
    alignement = False
    for i in range(len(Grille)):
        for j in range(len(Grille[i])):
            if Grille[i][j] == joueur:
                if (j+3<=len(Grille[i])-1):
                    if Grille[i][j+1]==joueur and Grille[i][j+2]==joueur and Grille[i][j+3]==joueur:
                        alignement = True
                if (i+3<=len(Grille)-1):
                    if Grille[i+1][j]==joueur and Grille[i+2][j]==joueur and Grille[i+3][j]==joueur:
                        alignement = True
                if (i+3<=len(Grille)-1 and j+3<=len(Grille[i])-1):
                    if Grille[i+1][j+1]==joueur and Grille[i+2][j+2]==joueur and Grille[i+3][j+3]==joueur:
                        alignement = True
                if (i+3<=len(Grille)-1 and j-3>=0):
                    if Grille[i+1][j-1]==joueur and Grille[i+2][j-2]==joueur and Grille[i+3][j-3]==joueur:
                        alignement = True
    return alignement

def check100(x,y, joueur):
    result = False
    Grille[x][y] = joueur
    if checkAlignement(joueur):
        result = True
    Grille[x][y] = 0
    return result

def check50(x,y, joueur):
    if joueur == 2:
        joueur =1
    elif joueur ==1:
        joueur = 2
    result = False
    Grille[x][y] = joueur
    if checkAlignement(joueur):
        result = True
    Grille[x][y] = 0
    return result

def check30(x,y, joueur):
    alignement = False
    Grille[x][y] = joueur

    alignement = False
    if (y+2<=len(Grille[x])-1):
        if Grille[x][y+1]==joueur and Grille[x][y+2]==joueur:
            alignement = True
    if (x+2<=len(Grille)-1):
        if Grille[x+1][y]==joueur and Grille[x+2][y]==joueur:
            alignement = True
    if (x+2<=len(Grille)-1 and y+2<=len(Grille[x])-1):
        if Grille[x+1][y+1]==joueur and Grille[x+2][y+2]==joueur:
            alignement = True
    if (x+2<=len(Grille)-1 and y-2>=0):
        if Grille[x+1][y-1]==joueur and Grille[x+2][y-2]==joueur:
            alignement = True

    Grille[x][y] = 0
    return alignement


def check15(x,y, joueur):
    alignement = False
    if joueur == 2:
        joueur = 1
    elif joueur == 1:
        joueur= 2
    Grille[x][y] = joueur

    alignement = False
    if (y+2<=len(Grille[x])-1):
        if Grille[x][y+1]==joueur and Grille[x][y+2]==joueur:
            alignement = True
    if (x+2<=len(Grille)-1):
        if Grille[x+1][y]==joueur and Grille[x+2][y]==joueur:
            alignement = True
    if (x+2<=len(Grille)-1 and y+2<=len(Grille[x])-1):
        if Grille[x+1][y+1]==joueur and Grille[x+2][y+2]==joueur:
            alignement = True
    if (x+2<=len(Grille)-1 and y-2>=0):
        if Grille[x+1][y-1]==joueur and Grille[x+2][y-2]==joueur:
            alignement = True

    Grille[x][y] = 0
    return alignement

def check10(x,y, joueur):
    alignement = False
    Grille[x][y] = joueur

    alignement = False
    if (y+1<=len(Grille[x])-1):
        if Grille[x][y+1]==joueur:
            alignement = True
    if (x+1<=len(Grille)-1):
        if Grille[x+1][y]==joueur:
            alignement = True
    if (x+1<=len(Grille)-1 and y+1<=len(Grille[x])-1):
        if Grille[x+1][y+1]==joueur:
            alignement = True
    if (x+1<=len(Grille)-1 and y-1>=0):
        if Grille[x+1][y-1]==joueur:
            alignement = True

    Grille[x][y] = 0
    return alignement

def scores_coup(coups_possibles, joueur):
    simulated_scores = []
    for i in range(len(coups_possibles)):
        if check100(coups_possibles[i][0],coups_possibles[i][1], joueur):
            simulated_scores.append(100)
        elif check50(coups_possibles[i][0],coups_possibles[i][1], joueur):
            simulated_scores.append(50)
        elif check30(coups_possibles[i][0],coups_possibles[i][1], joueur):
            simulated_scores.append(30)
        elif check15(coups_possibles[i][0],coups_possibles[i][1], joueur):
            simulated_scores.append(15)
        elif check10(coups_possibles[i][0],coups_possibles[i][1], joueur):
            simulated_scores.append(10)
        else:
            simulated_scores.append(0)
    return simulated_scores

def coupsPossibles():
    colonnes_possibles = [0, 1, 2, 3, 4, 5, 6]
    for i in range(len(Grille)):
        if all(j !=0 for j in Grille[i]):
            colonnes_possibles.remove(i)

    coups_possibles = []
    for x in colonnes_possibles:
        CaseAJouer = 0
        for i in range(len(Grille[x])):
            if Grille[x][i]==0:
                CaseAJouer=i
        coups_possibles.append([x,CaseAJouer])
    return coups_possibles

def JoueurHumainSimule(profondeur):
    profondeur += 1
    simulated_scores = []
    L = coupsPossibles()
    if profondeur>= 5 or checkAlignement(1) or checkAlignement(2) or gameover():
        return CalculScore()
    for coup in L:
        Grille[coup[0]][coup[1]] = 1
        Score = JoueurIA(profondeur)
        simulated_scores.append(Score[0])
        Grille[coup[0]][coup[1]] = 0
    return min(simulated_scores), L[simulated_scores.index(min(simulated_scores))]

def JoueurIA(profondeur):
    profondeur += 1
    simulated_scores = []
    L = coupsPossibles()
    if profondeur>= 5 or checkAlignement(1) or checkAlignement(2) or gameover():
        return CalculScore()
    for coup in L:
        Grille[coup[0]][coup[1]] = 2
        Score = JoueurHumainSimule(profondeur)
        simulated_scores.append(Score[0])
        Grille[coup[0]][coup[1]] = 0
    return max(simulated_scores), L[simulated_scores.index(max(simulated_scores))]

def Note():
    coups_possibles = coupsPossibles()
    LIA = scores_coup(coups_possibles, 2)
    LH = scores_coup(coups_possibles, 1)
    return max(LIA)-max(LH)

def CalculScore():
    if checkAlignement(2):
        return 500, [0,0]
    elif checkAlignement(1):
        return -500, [0,0]
    else:
        return Note(), [0,0]

def gameover():
    colonnes_possibles = [0, 1, 2, 3, 4, 5, 6]
    for i in range(len(Grille)):
        if all(j !=0 for j in Grille[i]):
            colonnes_possibles.remove(i)
    if not(colonnes_possibles):
        return True
    return False

def Play(x,y):
    less = True
    while y<len(Grille[x])-1 and less:
        if Grille[x][y+1]==0:
            y += 1
        else:
            less = False
    Grille[x][y] = 1
    if checkAlignement(1):
        Scores[0]+=1
        #input('Gagné! Appuyez sur une touche pour rejouer...')
        Reset_Grille()
    elif gameover():
        #input('Match nul! Appuyez sur une touche pour rejouer...')
        Reset_Grille()
    profondeur = 0
    _, CoupAJouer = JoueurIA(profondeur)
    Grille[CoupAJouer[0]][CoupAJouer[1]] = 2
    if checkAlignement(2):
        Scores[1]+=1
        #input('Perdu! Appuyez sur une touche pour rejouer...')
        Reset_Grille()
    elif gameover():
        #input('Match nul! Appuyez sur une touche pour rejouer...')
        Reset_Grille()


################################################################################
#
# Dessine la grille de jeu

def Affiche(PartieGagnee = False):
        ## DOC canvas : http://tkinter.fdex.eu/doc/caw.html
        canvas.delete("all")

        for i in range(7):
            canvas.create_line(i*43,0,i*43,300,fill="blue", width="4" )
            canvas.create_line(0,i*50,300,i*50,fill="blue", width="4" )

        for y in range(6):
            for x in range(7):
                xc = x * 43
                yc = y * 50
                if ( Grille[x][y] == 1):
                    canvas.create_oval(xc+5,yc+10,xc+35,yc+40,outline="yellow", width="4" )
                if ( Grille[x][y] == 2):
                    canvas.create_oval(xc+5,yc+10,xc+35,yc+40,outline="red", width="4" )

        msg = 'SCORES : ' + str(Scores[0]) + '-' + str(Scores[1])
        fillcoul = 'gray'
        if (PartieGagnee) : fillcoul = 'red'
        canvas.create_text(150,400, font=('Helvetica', 30), text = msg, fill=fillcoul)


        canvas.update()   #force la mise a jour de la zone de dessin


####################################################################################
#
#  fnt appelée par un clic souris sur la zone de dessin

def MouseClick(event):

    window.focus_set()
    x = event.x // 42  # convertit une coordonée pixel écran en coord grille de jeu
    y = event.y // 49
    if ( (x<0) or (x>6) or (y<0) or (y>5) ) : return


    print("clicked at", x,y)

    Play(x,y)  # gestion du joueur humain et de l'IA

    Affiche()

#####################################################################################
#
#  Mise en place de l'interface - ne pas toucher

# fenetre
window = tkinter.Tk()
window.geometry("300x500")
window.title('Mon Super Jeu')
window.protocol("WM_DELETE_WINDOW", lambda : window.destroy())
window.bind("<Button-1>", MouseClick)

#zone de dessin
WIDTH = 300
HEIGHT = 500
canvas = tkinter.Canvas(window, width=WIDTH , height=HEIGHT, bg="#000000")
canvas.place(x=0,y=0)
Affiche()

# active la fenetre
window.mainloop()











