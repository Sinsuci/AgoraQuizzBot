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


dq = DataQuizz("data_quiz")


def defie() :
    pyautogui.click(1330, 370)
    pyautogui.press('F5')
    time.sleep(2)
    pyautogui.click(1330, 370)
    time.sleep(0.2)
    pyautogui.write('krioro-guagangh')
    time.sleep(0.2)
    pyautogui.click(1580, 370)
    time.sleep(0.2)

def ScanTXT(pos_origin,pos_end):
    pos_diff = tuple(map(lambda i, j: i - j, pos_end, pos_origin))
    k = pyautogui.screenshot(region=(pos_origin + pos_diff))
    k = pytesseract.image_to_string(k)
    return k.replace('\n','')

def ImReponse(pos_origin,pos_end):   
    pos_diff = tuple(map(lambda i, j: i - j, pos_end, pos_origin))
    return pyautogui.screenshot(region=(pos_origin + pos_diff))

def choixtheme(th1,th2,th3,th1xy,th2xy,th3xy) :
    ThmB1 = "Machines thermiques avec changements de phase"
    ThmB2 = "Second principe"
    ThmB3 = "Machines thermiques"
    ThmB4 = "Enthalpie"
    TXTth1 = Fonctions.ScanTXT(th1[0],th1[1])
    TXTth2 = Fonctions.ScanTXT(th2[0],th2[1])
    TXTth3 = Fonctions.ScanTXT(th3[0],th3[1])
    
    #Theme 1 :
    if TXTth1 == ThmB1 :
        pyautogui.click(th1xy) #Click theme 1
    elif TXTth2 == ThmB1 :
        pyautogui.click(th2xy) #Click theme 2
    elif TXTth3 == ThmB1 :
        pyautogui.click(th3xy) #Click theme 3

    elif TXTth1 == ThmB2 :
        pyautogui.click(th1xy)
    elif TXTth2 == ThmB2 :
        pyautogui.click(th2xy)
    elif TXTth3 == ThmB2 :
        pyautogui.click(th3xy)

    elif TXTth1 == ThmB3 :
        pyautogui.click(th1xy)
    elif TXTth2 == ThmB3 :
        pyautogui.click(th2xy)
    elif TXTth3 == ThmB3 :
        pyautogui.click(th3xy)

    elif TXTth1 == ThmB4 :
        pyautogui.click(th1xy)
    elif TXTth2 == ThmB4 :
        pyautogui.click(th2xy)
    elif TXTth3 == ThmB4 :
        pyautogui.click(th3xy)

    else :
        pyautogui.click(th1xy) #Click theme 1 puis F5
        time.sleep(1)
        pyautogui.press('F5')
        return 1
    
    return 0

def answerLearningIntingSmurf(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy):
    CooRx = (200,25)

    TXTq = Fonctions.ScanTXT(qxyxy[0],qxyxy[1])
    TXTr1 = Fonctions.ScanTXT(r1xyxy[0],r1xyxy[1])
    TXTr2 = Fonctions.ScanTXT(r2xyxy[0],r2xyxy[1])
    TXTr3 = Fonctions.ScanTXT(r3xyxy[0],r3xyxy[1])
    TXTr4 = Fonctions.ScanTXT(r4xyxy[0],r4xyxy[1])

    if dq.getAnswer(TXTq) != False : #Possede la réponse
        pyautogui.click(r1xy)
    
    else : #Ne possede pas la réponse

        pyautogui.click(r1xy)
        time.sleep(0.2)
        IMr1 = Fonctions.ImReponse(r1xyxy[0],r1xyxy[1])
        IMr2 = Fonctions.ImReponse(r2xyxy[0],r2xyxy[1])
        IMr3 = Fonctions.ImReponse(r3xyxy[0],r3xyxy[1])
        IMr4 = Fonctions.ImReponse(r4xyxy[0],r4xyxy[1])

        r1,g1,b1 = IMr1.getpixel(CooRx)
        r2,g2,b2 = IMr2.getpixel(CooRx)
        r3,g3,b3 = IMr3.getpixel(CooRx)
        r4,g4,b4 = IMr4.getpixel(CooRx)

        if r1 < 200 :
            answer = TXTr1
            dq.addQuestion(TXTq,answer)
        elif r2 < 200 :
            answer = TXTr2
            dq.addQuestion(TXTq,answer)
        elif r3 < 200 :
            answer = TXTr3
            dq.addQuestion(TXTq,answer)
        elif r4 < 200 :
            answer = TXTr4
            dq.addQuestion(TXTq,answer)

def answerLearningMain(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy,r2xy,r3xy,r4xy):
    CooRx = (200,25)

    TXTq = Fonctions.ScanTXT(qxyxy[0],qxyxy[1])
    TXTr1 = Fonctions.ScanTXT(r1xyxy[0],r1xyxy[1])
    TXTr2 = Fonctions.ScanTXT(r2xyxy[0],r2xyxy[1])
    TXTr3 = Fonctions.ScanTXT(r3xyxy[0],r3xyxy[1])
    TXTr4 = Fonctions.ScanTXT(r4xyxy[0],r4xyxy[1])
    
    if dq.getAnswer(TXTq) != False : #Possede la réponse
        valueAnswerRatio = Fonctions.wordspellingratio(TXTq,TXTr1,TXTr2,TXTr3,TXTr4)
        if valueAnswerRatio == 0 :
            pyautogui.click(r1xy)
        elif valueAnswerRatio == 1 :
            pyautogui.click(r2xy)
        elif valueAnswerRatio == 2 :
            pyautogui.click(r3xy)
        elif valueAnswerRatio == 3 :
            pyautogui.click(r4xy)
        else :
            print("merde, ratio sup à 4 ou False")


    else : #Ne possede pas la réponse
        pyautogui.click(r1xy)
        time.sleep(0.2)
        IMr1 = Fonctions.ImReponse(r1xyxy[0],r1xyxy[1])
        IMr2 = Fonctions.ImReponse(r2xyxy[0],r2xyxy[1])
        IMr3 = Fonctions.ImReponse(r3xyxy[0],r3xyxy[1])
        IMr4 = Fonctions.ImReponse(r4xyxy[0],r4xyxy[1])

        r1,g1,b1 = IMr1.getpixel(CooRx)
        r2,g2,b2 = IMr2.getpixel(CooRx)
        r3,g3,b3 = IMr3.getpixel(CooRx)
        r4,g4,b4 = IMr4.getpixel(CooRx)

        if r1 < 200 :
            answer = TXTr1
            dq.addQuestion(TXTq,answer)
        elif r2 < 200 :
            answer = TXTr2
            dq.addQuestion(TXTq,answer)
        elif r3 < 200 :
            answer = TXTr3
            dq.addQuestion(TXTq,answer)
        elif r4 < 200 :
            answer = TXTr4
            dq.addQuestion(TXTq,answer)


def wordspellingratio (TXTq,TXTr1,TXTr2,TXTr3,TXTr4) :
    
    answertxtratio = dq.getAnswer(TXTq)
    if answertxtratio != False :
        listvalue = []
        listvalue.append(SequenceMatcher(a=answertxtratio,b=TXTr1).ratio())
        listvalue.append(SequenceMatcher(a=answertxtratio,b=TXTr2).ratio())
        listvalue.append(SequenceMatcher(a=answertxtratio,b=TXTr3).ratio())
        listvalue.append(SequenceMatcher(a=answertxtratio,b=TXTr4).ratio())
        return listvalue.index(max(listvalue))
    else :
        return


def fctanswerSmurf (SKIP,ctxy,manche,qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,lvlupxy,pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy,lvxy,r1xy) :
    if SKIP == 1 :
        if manche == 1 or manche == 3 :
            time.sleep(1)
            pyautogui.click(ctxy)
        else :
            pyautogui.press('F5')
            time.sleep(2)
            pyautogui.click(ctxy) #Envoie
            time.sleep(1)
            pyautogui.click(ctxy) #Ouvre theme
    else : #Répond aux questions, apprend et répond 1 tout le temps
        time.sleep(8) #Transi to questions
        Fonctions.answerLearningIntingSmurf(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy)
        time.sleep(9) #Attente transi questions
        Fonctions.answerLearningIntingSmurf(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy)
        time.sleep(9)
        Fonctions.answerLearningIntingSmurf(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy)
        
        if manche == 1 or manche == 3 :
            time.sleep(4) #Attente fin questions
            pyautogui.click(lvlupxy)#Lvl Up
            time.sleep(0.2)
            Fonctions.nextDetection(pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy)

            time.sleep(1)
            pyautogui.click(lvxy) #Sortir du fail clic si il y a
            time.sleep(1)
        else :
            time.sleep(4) #Attente fin questions
            pyautogui.click(lvlupxy)#Lvl Up
            time.sleep(0.2)
            Fonctions.nextDetection(pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy)
            time.sleep(1)

def fctanswerMain (SKIP,ctxy,manche,qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,lvlupxy,pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy,lvxy,r1xy,r2xy,r3xy,r4xy) :
    if SKIP == 1 :
        if manche == 2 or manche == 4 :
            time.sleep(1)
            pyautogui.click(ctxy)
        else :
            pyautogui.press('F5')
            time.sleep(2)
            pyautogui.click(ctxy) #Envoie
            time.sleep(1)
            pyautogui.click(ctxy) #Ouvre theme
    else : #Répond aux questions, apprend et répond juste tout le temps
        time.sleep(12) #Transi to questions
        Fonctions.answerLearningMain(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy,r2xy,r3xy,r4xy)
        time.sleep(9) #Attente transi questions
        Fonctions.answerLearningMain(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy,r2xy,r3xy,r4xy)
        time.sleep(9)
        Fonctions.answerLearningMain(qxyxy,r1xyxy,r2xyxy,r3xyxy,r4xyxy,r1xy,r2xy,r3xy,r4xy)
        
        if manche == 2 or manche == 4 :
            time.sleep(4) #Attente fin questions
            pyautogui.click(lvlupxy)#Lvl Up
            time.sleep(0.2)
            Fonctions.nextDetection(pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy)
            

            time.sleep(1)
            pyautogui.click(lvxy) #Sortir du fail clic si il y a
            time.sleep(1)
        else :
            time.sleep(4) #Attente fin questions
            pyautogui.click(lvlupxy)#Lvl Up
            time.sleep(0.2)
            Fonctions.nextDetection(pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy)
            time.sleep(1)





def crashReset (lvxym,lvxys) :
    pyautogui.click(lvxym)
    time.sleep(0.2)
    pyautogui.press('F5')

    pyautogui.click(lvxys)
    time.sleep(0.2)
    pyautogui.press('F5')






class MyTimer:
    def __init__(self, temps=300):
        self.temps = temps
        self.reset = False

def thread_function(my_timer: MyTimer,lvxym,lvxys):
    reste = my_timer.temps

    while reste != 0:
        time.sleep(1)
        reste -= 1
        if my_timer.reset == True:
            my_timer.reset = False
            reste = my_timer.temps
        print("reste = ", reste)

    print('Crash Reset')
    Fonctions.crashReset(lvxym,lvxys)



def nextDetection(pxl_11xy,pxl_12xy,pxl_13xy,pxl_21xy,pxl_22xy,pxl_23xy,pxl_31xy,pxl_32xy,pxl_33xy):
    im = pyautogui.screenshot()
    if im.getpixel(pxl_11xy)[2] < 200 :
        pyautogui.click(pxl_11xy)
    elif im.getpixel(pxl_12xy)[2] < 200 : 
        pyautogui.click(pxl_12xy)
    elif im.getpixel(pxl_13xy)[2] < 200 : 
        pyautogui.click(pxl_13xy)

    elif im.getpixel(pxl_21xy)[2] < 200 : 
        pyautogui.click(pxl_21xy)
    elif im.getpixel(pxl_22xy)[2] < 200 : 
        pyautogui.click(pxl_22xy)
    elif im.getpixel(pxl_23xy)[2] < 200 : 
        pyautogui.click(pxl_23xy)

    elif im.getpixel(pxl_31xy)[2] < 200 : 
        pyautogui.click(pxl_31xy)
    elif im.getpixel(pxl_32xy)[2] < 200 : 
        pyautogui.click(pxl_32xy)
    elif im.getpixel(pxl_33xy)[2] < 200 : 
        pyautogui.click(pxl_33xy)




