#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'L:\Program Files\Tesseract-OCR\tesseract.exe'
import pyautogui
import time

from DataQuizz import DataQuizz
import Fonctions
from difflib import SequenceMatcher
import threading
import time 


# In[2]:


dq = DataQuizz("data_quiz")

CooRx = (200,25) #Echantillon couleur

#Coordonnées smurf / main
#Smurf
th1xyxys = (1050, 410),(1840, 520) #Theme 1
th2xyxys = (1050, 580),(1840, 690) #Theme 2
th3xyxys = (1050, 750),(1840, 860) #Theme 3
th1xys = (1440, 410) #Theme 1 1 click
th2xys = (1440, 580) #Theme 2 1 click
th3xys = (1440, 750) #Theme 3 1 click
qxyxys = (992, 291),(1870, 371) #Question
r1xyxys = (1010, 410),(1400, 645) #Réponse 1
r2xyxys = (1460, 420),(1840, 650) #Réponse 2
r3xyxys = (1020, 700),(1400, 925) #Réponse 3
r4xyxys = (1460, 710),(1840, 920) #Réponse 4
r1xys = (1045, 410) #Réponse 1 click
r2xys = (1460, 420) #Réponse 2 click
r3xys = (1045, 700) #Réponse 3 click
r4xys = (1460, 710) #Réponse 4 click
lvlupxys = (1440,705) #Level up click
ctxys = (1370,520) #Continuer click
lvxys = (1050,450) #leave fail click

#Main
th1xyxym = (70,405),(890,530) #Theme 1
th2xyxym = (70,575),(890,700) #Theme 2
th3xyxym = (70,750),(890,870) #Theme 3
th1xym = (480,405) #Theme 1 click
th2xym = (480,575) #Theme 2 click
th3xym = (480,750) #Theme 3 click
qxyxym = (30,315),(920,370) #Question
r1xyxym = (60,390),(455,630) #Réponse 1
r2xyxym = (500,390),(900,640) #Réponse 2
r3xyxym = (50,680),(455,930) #Réponse 3
r4xyxym = (500,680),(900,935) #Réponse 4
r1xym = (85,445) #Réponse 1 click 390 to 445
r2xym = (500,445) #Réponse 2 click 390 to 445
r3xym = (85,735) #Réponse 3 click 680 to 735
r4xym = (500,735) #Réponse 4 click 680 to 735
lvlupxym = (480,705) #Level up click
ctxym = (370,520) #Continuer click
lvxym = (120,405) #leave fail click


#Main : Retour aux parties en cours et suite manche click
pxl_11xym = (375,750)
pxl_12xym = (480,750)
pxl_13xym = (580,750)
pxl_21xym = (375,780)
pxl_22xym = (480,780)
pxl_23xym = (580,780)
pxl_31xym = (375,830)
pxl_32xym = (480,830)
pxl_33xym = (580,830)

#Smurf : Retour aux parties en cours et suite manche click
pxl_11xys = (1335,750)
pxl_12xys = (1435,750)
pxl_13xys = (1545,750)
pxl_21xys = (1335,780)
pxl_22xys = (1435,780)
pxl_23xys = (1545,780)
pxl_31xys = (1335,828)
pxl_32xys = (1435,828)
pxl_33xys = (1545,828)


# # Core

# In[4]:


while True :

    #Début temps session
    start_time = time.time()


    # In[5]:


    #Timer reset si crash +350s

    #my_timer = Fonctions.MyTimer()
    #x = threading.Thread(target=Fonctions.thread_function, args=(my_timer,lvxym,lvxys,), daemon=True)

    #if :
    #    my_timer.reset = True #Reset timer
    #else :
    #    x.start()


    # In[6]:


    #Smurf M0 : Lancer défi + clean saisie par F5
    Fonctions.defie()
    manche = 1
    print("SM0")

    #Smurf M1 : Choix theme
    time.sleep(1)
    SKIP = 0
    SKIP = Fonctions.choixtheme(th1xyxys,th2xyxys,th3xyxys,th1xys,th2xys,th3xys)
    print("SM1")

    #Smurf M1 : Réponse / Skip
    Fonctions.fctanswerSmurf(SKIP,ctxys,manche,qxyxys,r1xyxys,r2xyxys,r3xyxys,r4xyxys,lvlupxys,pxl_11xys,pxl_12xys,pxl_13xys,pxl_21xys,pxl_22xys,pxl_23xys,pxl_31xys,pxl_32xys,pxl_33xys,lvxys,r1xys)
    print("SM1.")


    # In[7]:


    #Au Main de jouer
    time.sleep(2)
    pyautogui.click(ctxym)
    print("MM1")

    #Main M1 : Réponse / Skip
    Fonctions.fctanswerMain(SKIP,ctxym,manche,qxyxym,r1xyxym,r2xyxym,r3xyxym,r4xyxym,lvlupxym,pxl_11xym,pxl_12xym,pxl_13xym,pxl_21xym,pxl_22xym,pxl_23xym,pxl_31xym,pxl_32xym,pxl_33xym,lvxym,r1xym,r2xym,r3xym,r4xym)
    print("MM1.")

    #Main M2 : Choix theme
    manche = manche + 1
    time.sleep(1)
    SKIP = 0
    SKIP = Fonctions.choixtheme(th1xyxym,th2xyxym,th3xyxym,th1xym,th2xym,th3xym)
    print("MM2")

    #Main M2 : Réponse / Skip
    Fonctions.fctanswerMain(SKIP,ctxym,manche,qxyxym,r1xyxym,r2xyxym,r3xyxym,r4xyxym,lvlupxym,pxl_11xym,pxl_12xym,pxl_13xym,pxl_21xym,pxl_22xym,pxl_23xym,pxl_31xym,pxl_32xym,pxl_33xym,lvxym,r1xym,r2xym,r3xym,r4xym)
    print("MM2.")


    # In[8]:


    #Au Smurf de jouer
    time.sleep(2)
    pyautogui.click(ctxys)
    print("SM2")

    #Smurf M2 : Skip
    time.sleep(2)
    pyautogui.press('F5')
    time.sleep(2)
    pyautogui.click(ctxys)
    time.sleep(0.5)
    pyautogui.click(ctxys)
    print("SM2.")


    #Smurf M3 : Choix theme
    manche = manche + 1
    time.sleep(1)
    SKIP = 0
    SKIP = Fonctions.choixtheme(th1xyxys,th2xyxys,th3xyxys,th1xys,th2xys,th3xys)
    print("SM3")

    #Smurf M3 : Réponse / Skip
    Fonctions.fctanswerSmurf(SKIP,ctxys,manche,qxyxys,r1xyxys,r2xyxys,r3xyxys,r4xyxys,lvlupxys,pxl_11xys,pxl_12xys,pxl_13xys,pxl_21xys,pxl_22xys,pxl_23xys,pxl_31xys,pxl_32xys,pxl_33xys,lvxys,r1xys)
    print("SM3.")


    # In[9]:


    #Au Main de jouer
    time.sleep(2)
    pyautogui.click(ctxym)
    print("MM3")

    #Main M3 : Réponse / Skip
    Fonctions.fctanswerMain(SKIP,ctxym,manche,qxyxym,r1xyxym,r2xyxym,r3xyxym,r4xyxym,lvlupxym,pxl_11xym,pxl_12xym,pxl_13xym,pxl_21xym,pxl_22xym,pxl_23xym,pxl_31xym,pxl_32xym,pxl_33xym,lvxym,r1xym,r2xym,r3xym,r4xym)
    print("MM3.")

    #Main M4 : choix theme
    manche = manche + 1
    time.sleep(1)
    SKIP = 0
    SKIP = Fonctions.choixtheme(th1xyxym,th2xyxym,th3xyxym,th1xym,th2xym,th3xym)
    print("MM4")

    #Main M4 : Réponse / Skip
    Fonctions.fctanswerMain(SKIP,ctxym,manche,qxyxym,r1xyxym,r2xyxym,r3xyxym,r4xyxym,lvlupxym,pxl_11xym,pxl_12xym,pxl_13xym,pxl_21xym,pxl_22xym,pxl_23xym,pxl_31xym,pxl_32xym,pxl_33xym,lvxym,r1xym,r2xym,r3xym,r4xym)
    print("MM4.")


    # In[10]:


    #Au Smurf de jouer
    time.sleep(2)
    pyautogui.click(ctxys)
    print("SM4")
    time.sleep(2)
    pyautogui.press('F5')
    time.sleep(2)
    pyautogui.click(ctxys)
    print("SM4.")
    #si lvl up
    time.sleep(2)
    pyautogui.press('F5')
    print("SM4..")


    # In[11]:


    #Fin temps session for statistiques
    print("--- %s seconds ---" % (time.time() - start_time))

