# Importation des librairies python.
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
import time
import mysql
import mysql.connector
import string
import unicodedata



# Fonction principale, elle va éxecuter le script du Chatbot.
def start():
        
        # Récupére la réponse de l'utilisateur dans une variable:
        #"reponse_utilisateur"
        reponse_utilisateur = input("Taper votre réponse : \n")
        # On passe le résultat "reponse_utilisateur" dans une fonction pour enlever
        # les majuscules et les accents.
        resultat_minuscule = minuscule(reponse_utilisateur)
        # demande à l'utilisateur son probléme si il salut le Chatbot
        accroche(resultat_minuscule)
        fctvector()
        postrecherche()
        
        
def minuscule(reponse_utilisateur):
        
        # on utilise la fonction native python "lower"
        resultat_minuscule = reponse_utilisateur.lower()
        # on enléve ensuite les accents  (à rajouter...)          
        #print(resultat_minuscule)
        return resultat_minuscule

def accroche(resultat_minuscule):
        
        # on split le resultat avec la fonction native python "split"
        tokenize=resultat_minuscule.split(" ")
        #print(str(test))

        keyword = ["bonjour","salut","hey","hi","yo","hello"] 
        #print (keyword)
        #print ("traitement en cours, veuillez patienter")
        #time.sleep(2)
        
        # on compare les mots de l'utilisateur avec la liste des mots "keyword"
        # si il trouve une redondance il le place dans une liste
        same_values = set(keyword) & set(tokenize)
        finaltable = list(same_values)
        
        if len(finaltable) != 0 :
                print ("Quel est votre probléme ?") 

        else :
                print ("Un, petit bonjour ? dommage...")
                #time.sleep(3)
                print ("Quel est votre probléme ?:")
                
def fctvector():
        
        reponse_vector = input("Taper votre réponse : \n")
        # On passe le résultat "reponse_utilisateur" dans une fonction pour enlever
        # les majuscules et les accents.
        reponse_vector = minuscule(reponse_vector)        
        # Algorithme pour supprimer "les mots vides" avec une liste "stop_words"
        # Passage d'un tableau à une chaine de caractére
        # Passage sous le format nlp
        
        #Liste de la base de donnée dans un tableau
        # Base de donnée provisoir 
        text1=nlp(u"ordinateur qui ne s'allume plus")
        text2=nlp(u"ecran noir sur mon pc")
        text3=nlp(u"j'ai perdue mon cable video")
        text4=nlp(u"mon clavier ne repond plus")
        text5=nlp(u"ma sourie ne repond plus")
        text6=nlp(u"je n'ai plus internet")
        text7=nlp(u"j'ai pas acces à ma messagerie")
        text8=nlp(u"j'ai pas d'adresse ip")
        
        t=[text1,text2,text3,text4,text5,text6,text7,text8]  
        postt=[]
        
        for i in t:
                print(i)
                i2 = [token.text for token in i if not token.is_stop]
                print(i2)
                i2 = " ".join(i2)
                i = nlp(i2)
                postt.append(i)
                print(i)
        
        #for index, i in postt:
                #i = i + index
        
        #Phrase de référence
        phrase=nlp(reponse_vector)
        t2=[phrase]
        postt2=[]
        
        for i in t2:
                i2 = [token.text for token in i if not token.is_stop]
                print(i2)
                i2 = " ".join(i2)
                i = nlp(i2)
                postt2.append(i)
                print(i)        
                
        
        print(t)
        print(postt)
        print(t2)
        print(postt2)
        
        #Tableau qui va retenir la phrase qui va matcher + son vecteur
        t3 = []
        
        #Algorithme qui comparer la phrase de référence et la base de données pour trouver la 
        #meilleur similarité
        a=0
        i=-1
        for token1 in postt:
                for token2 in postt2:
                        print(token1.text, token2.text, token1.similarity(token2))
                        if(token1.similarity(token2) > a):
                                i= postt.index(token1)
                                a = token1.similarity(token2) 
                                b = token1.text
        
        #Ajout dans le tableau des résultats
        t3.append(a)
        t3.append(b)
        
        #Affichage des information t3 et "stop word"
        print(t3)
        #print(STOP_WORDS)
        #print(len(STOP_WORDS))    
        
        rep1=nlp(u"verifier le cable d'alimentation")
        rep2=nlp(u"verifier le cable video")
        rep3=nlp(u"contacter le service apres vente")
        rep4=nlp(u"contacter le service apres vente")
        rep5=nlp(u"debrancher et rebrancher votre sourie")
        rep6=nlp(u"verifier votre cable réseau")
        rep7=nlp(u"vérifier votre connexion internet et réésayer")
        rep8=nlp(u"vérifier que vous etes en client dhcp")
        
        rep=[rep1,rep2,rep3,rep4,rep5,rep6,rep7,rep8]
        
        #tablefinal = zip(postt,rep)
        #resulttablefinal = set(tablefinal)
                              
        print(rep[i])      
        
        #return(t,rep)

def ajout():
        
        print("Ajouter la phrase à ajouter dans la liste de donnée ?")
        ajoutq =input("")
        print("Ajouter la réponse à ajouter dans la liste de donnée ?")
        ajoutr =input("")
        
        textbonus = ajoutq
        repbonus = ajoutr
        
        t.append(textbonus)
        rep.append(repbonus)
        
        
        
def postrecherche():

        #print(abcd)
        #print([abcd])
        print("Avez-vous trouver la réponse à votre probléme ?")
        print("Taper '1' Réalisez une nouvelle recherche\nTaper '2' Afficher L'adresse Email d'un technicien support SAV réseau\nTaper '3' Quitter la conversation avec votre assistant virtuel\nTaper '4' pour ajouter des informations dans la BDD")

        variable=input("")

        while variable != '1' or variable != '2' or variable != '3' or variable != '4':

                if variable == "1" :

                        #print ("1")
                        print ("Quel est votre probléme ?")
                        fctvector()
                        postrecherche()

                if variable == "3" :

                        #print ("3")
                        print("vous avez quitté le processus")
                        print ("Bonjour, je m'appelle Eliza votre agent Conversationnelle")
                        start()

                if variable == "2" :

                        print ("Email : supporttechnicienSAV@gmail.com")
                        print ("Vous quitter le service")
                        print ("Bonjour, je m'appelle Eliza votre agent Conversationnelle")
                        start()
                        
                if variable == "4" :
        
                        ajout()
                        start()
                                        

                else :  
                        print ("Veuillez réessayer")
                        variable=input("")
        
# on charge l'intélligence artificiel "vecteurs francais"
nlp = spacy.load("fr_core_news_md")
print ("Bonjour, je m'appelle Eliza votre agent Conversationnelle")
start()
