
import json

json_file_path = "message_1.json"


with open(json_file_path,'r') as j: #permet d'ouvrir le fichier
     contents = json.loads(j.read())

Membres = {}
Liste_Membres=(contents["participants"])  # recupere la liste des membres
for elements in Liste_Membres:
    for key, val in dict.items(elements):
            Membres[val] = 0 
        
Liste_Messages=contents["messages" ]  #recupere la liste des messages
sender_name=""
n=0
for elements in Liste_Messages: #associe chaque a chaque membres le nombre de message qu'il a envoyé
    if "sender_name" in elements:
        sender_name=(elements["sender_name"])
        Membres[sender_name]=Membres[sender_name]+1

print("Il y a ",len(Membres)," membres")
print("Il y a ",len(Liste_Messages)," messages")

#definitions des fonctions

def fonctions():
    print("Liste des fonctions : ")
    print("")
    print("graph(title,xlabel,x,ylabel,y,) / fonction utilisable")
    print("total_Membre(Membre) / fonction utilisable")
    print("graph_total_Membre / fonction complete ")
    print("Fonction / fonction utilisable")
    print("pick1 / fonction interne")
    print("pick2 / fonction interne")
    print("correct / fonction interne")
    print("")


def graph(title,xlabel,x,ylabel,y,): 
    '''Trace un graphique selon respectivement :  
    (Le titre du graphique,Le titre de l'abscisse,La valeur de l'abscisse,Le titre de l'ordonnée,La valeur de l'ordonnée)'''
    plt.plot(x, y) 
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def total_Membre(Membre):
    ''' renvoie 2 list contenant respectivement la liste des jours ou un message a été envoyé et la liste du nombre total de message envoyé a cette date
        utiliser  la fonction graph_total_Membre pour avoir un graphique''' 
    timestamp=[]
    List_timestamp=[]
    nb=[]
    for elements in Liste_Messages:
        if "sender_name" in elements:
            if elements["sender_name"]== Membre:
                temp= elements["timestamp_ms"]
                temp= temp // 1000
                dt_object = datetime.fromtimestamp(temp) #transforme les timestamps en differents info
                timestamp.append( dt_object.strftime("%j"))
    nb=[0 for i in range(0,len(timestamp))]
    n=0 # quelqun lis ça ?
    for i in  range (0,len(timestamp)):
        if timestamp[i] not in List_timestamp:
            List_timestamp.append(timestamp[i])
            nb[n]=nb[n]+1
            n=n+1
        else:
            nb[n]=nb[n]+1
    List_nb=[]
    for i in nb:
        if i != 0:
            List_nb.append(i)
     # si on cut ici ça donne le nombre de message envoyé par jour (que par jour ou il y a des message envoyé)
    for i in range (0,len(List_timestamp)):
        List_timestamp[i]=int(List_timestamp[i])
    List_timestamp_temp=[]
    List_nb_temp=[]
    while List_timestamp[0] < 249:
        List_timestamp_temp.append(List_timestamp[0])
        List_nb_temp.append(List_nb[0])
        List_timestamp.pop(0)
        List_nb.pop(0)
    List_timestamp.reverse()
    List_nb.reverse()
    List_timestamp_temp.reverse()
    List_nb_temp.reverse()
    for i in List_timestamp_temp:
        i=i+365
        List_timestamp.append(i)
    for i in  List_nb_temp:
        List_nb.append(i)
    
    # si on cut ici ça donne le nombre de message envoyé par jour (que par jour ou il y a des message envoyé)
    #return (List_timestamp,List_nb)
    
    for i in range (1,len(List_nb)):
        List_nb[i]=List_nb[i-1]+List_nb[i]
    List_nb[-2]=List_nb[-2]+1
    List_nb.pop(-1)


    return (List_timestamp,List_nb)
    
    
def pick1(L):
    """return l'element d'indice [0] d'une liste """
    return L[0]
def pick2(L):
    """return l'element d'indice [1] d'une liste """
    return L[1]

def correct(L1,L2):
    """Verifie que les 2 liste on la meme longueur , si non retire les elements de L1 jusqu'a ce que ce soit vrai """
    if len(L1) != len (L2):
            while  len(L1) != len (L2):
                L1.pop(0)
    return(L1,L2)

def graph_total_Membre(Membre):
    """ pareil que total_Membre mais avec un graphique"""
    List_timestamp=pick1(total_Membre(Membre))
    List_nb=pick2(total_Membre(Membre))
    
    correct(List_timestamp,List_nb)
    plt.plot(List_timestamp, List_nb) 
    
    plt.xlabel("Jour")
    plt.ylabel("Nombre de message ")
    plt.title("Nombre de message en fonction du temps")
    plt.show()
    print("Qui ? :", Membre)
    print("Quand ? :", List_timestamp)
    print("Combien ? :", List_nb)



fonctions() #print toute les fonctions (normalement)



from collections import OrderedDict #met les membres par ordre croissant en fonction de leur nombre de messages envoyé
Membres_tri = dict(sorted(Membres.items(), key=lambda item:item[1]))
print("Liste des membres par ordre croissant :")
print(Membres_tri)

from datetime import datetime
Liste_timestamp_ms=[]
Liste_timestamp_dt=[]
Liste_timestamp_jour=[]
Liste_timestamp_nom_jour=[]
Liste_timestamp_semaine=[]
Liste_timestamp_mois=[]
Liste_timestamp_heure=[]
for elements in Liste_Messages:
    if "timestamp_ms" in elements:
        timestamp_ms=(elements["timestamp_ms"]) #recupere les timestamps
        timestamp_ms = timestamp_ms // 1000  #retire les 3 dernier chiffre pour les remettres en seconde
        Liste_timestamp_ms.append(timestamp_ms)
        dt_object = datetime.fromtimestamp(timestamp_ms) #transforme les timestamps en differents info
        Liste_timestamp_dt.append(dt_object)
        Liste_timestamp_jour.append( dt_object.strftime("%j"))
        Liste_timestamp_semaine.append(dt_object.strftime("%W"))
        Liste_timestamp_mois.append(dt_object.strftime("%B"))
        Liste_timestamp_heure.append(dt_object.strftime("%H"))
        Liste_timestamp_nom_jour.append(dt_object.strftime("%w"))


#message par jour de l'année
nb_Liste_timestamp_jour=[0 for k in range (0,len( Liste_timestamp_jour))]
Liste_timestamp_jour_one=[]
n=-1
for i in  Liste_timestamp_jour:
    if i not in Liste_timestamp_jour_one:
        Liste_timestamp_jour_one.append(i)
        n+=1
        nb_Liste_timestamp_jour[n]=1
 
    else:
        nb_Liste_timestamp_jour[n]=nb_Liste_timestamp_jour[n]+1

nb_Liste_timestamp_jour=nb_Liste_timestamp_jour[:n+1]

for i in range (0,len(Liste_timestamp_jour_one)):
    Liste_timestamp_jour_one[i]=int(Liste_timestamp_jour_one[i])

#graphique

import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars 
left =Liste_timestamp_jour_one
# heights of bars
height=nb_Liste_timestamp_jour


# plotting a bar chart
plt.bar(left, height, width = 0.8, color = ['red'])
 
# naming the x-axis
plt.xlabel('Jour')
# naming the y axis
plt.ylabel('Nombre de messages ')
 
# giving a title to my graph
plt.title('Nombre de messages par jour de l année sur le groupe classe')
 
# function to show the plot
plt.show()

#Nombre de messages total par heure sur le groupe classe
Liste_timestamp_heure_one=[]
nb_timestamp_heure=[]
Liste_timestamp_heure=sorted(Liste_timestamp_heure)

for i in range (0,len(Liste_timestamp_heure)):
    Liste_timestamp_heure[i]=int(Liste_timestamp_heure[i])
    
Liste_timestamp_heure

nb_heure=[0 for l in range (0,24)]
heure=[]
for i in Liste_timestamp_heure:
    if i not in heure:
        heure.append(i)
        nb_heure[i]=1
    else:
        nb_heure[i]=nb_heure[i]+1

Tab_nb_heure=[]
for i in nb_heure:
    if i!=0:
        Tab_nb_heure.append(i)

 
left =heure
height=Tab_nb_heure
plt.bar(left, height, width = 0.8, color = ['red'])
 
plt.xlabel('Heure')
plt.ylabel('Nombre de messages ')
 
plt.title('Nombre de messages total par heure sur le groupe classe')
plt.show()

#Pourcentage de message par jour sur le groupe classe

Liste_nom_jour_one=[]
nb_nom_jour=[]
Liste_nom_jour=sorted(Liste_timestamp_nom_jour)

for i in range (0,len(Liste_nom_jour)):
    Liste_nom_jour[i]=int(Liste_nom_jour[i])
    
Liste_nom_jour

nb_nom_jour=[0 for l in range (0,24)]
nom_jour=[]
for i in Liste_nom_jour:
    if i not in nom_jour:
        nom_jour.append(i)
        nb_nom_jour[i]=1
    else:
       nb_nom_jour[i]=nb_nom_jour[i]+1

Tab_nb_nom_jour=[]
for i in nb_nom_jour:
    if i!=0:
       Tab_nb_nom_jour.append(i)
        

total=len(Liste_Messages)



for i in range(0,(len(Tab_nb_nom_jour))):
    Tab_nb_nom_jour[i]=Tab_nb_nom_jour[i]/ len(Liste_Messages) 

#renonmez les jours de la semaine :)
nom_jour[0]="Lundi"
nom_jour[1]="Mardi"
nom_jour[2]="Mercredi"
nom_jour[3]="Jeudi"
nom_jour[4]="Vendredi"
nom_jour[5]="Samedi"
nom_jour[6]="Dimanche"

            
left =nom_jour
height=Tab_nb_nom_jour
plt.bar(left, height, width = 0.8, color = ['red'])
 
plt.xlabel('')
plt.ylabel('Nombre de messages ')
plt.title('Pourcentage de message par jour sur le groupe classe')
plt.show()

#Nombre de messages total par heure sur le groupe classe
Liste_timestamp_heure_one=[]
nb_timestamp_heure=[]
Liste_timestamp_heure=sorted(Liste_timestamp_heure)

for i in range (0,len(Liste_timestamp_heure)):
    Liste_timestamp_heure[i]=int(Liste_timestamp_heure[i])
    
Liste_timestamp_heure

nb_heure=[0 for l in range (0,24)]
heure=[]
for i in Liste_timestamp_heure:
    if i not in heure:
        heure.append(i)
        nb_heure[i]=1
    else:
        nb_heure[i]=nb_heure[i]+1

Tab_nb_heure=[]
for i in nb_heure:
    if i!=0:
        Tab_nb_heure.append(i)


Liste_timestamp_jour_one.reverse()
nb_Liste_timestamp_jour.reverse()




for i in range(1,len(nb_Liste_timestamp_jour)):
    nb_Liste_timestamp_jour[i]=nb_Liste_timestamp_jour[i-1]+nb_Liste_timestamp_jour[i]


for i in range (0,len(Liste_timestamp_jour_one)):
    if Liste_timestamp_jour_one[i] < 249 :
        Liste_timestamp_jour_one[i]=Liste_timestamp_jour_one[i]+365
graph('Evolution nombre total de message','Jour',Liste_timestamp_jour_one,'Nb de msg ',nb_Liste_timestamp_jour)

