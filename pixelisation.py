"""
Objectif
écrire une fonction capable de pixeliser une image d’entrée à des degrés divers. Cette fonction pourra être intégré dans une solution logiciel plus importante, un jeu par exemple.

Méthode :
La signature de la fonction est la suivante :

def pixeliser_image(uneImage, nbre_sections)

Elle prend en paramètre uneImage chargée avec la bibliothèque Image de PIL. L’image est divisée en nbre_sections colonnes sur l’axe horizontale, et nbre_sections lignes sur l’axe vertical. On obtient ainsi une image avec nbre_sections² divisions.

L'écriture de la fonction se fera en décomposant le problème en sous-fonction pour permettre une résolution et une lecture du code facilité.

Prévoir de documenter le projet par l'intermédiaire de ce notebook en donnant des explications sur la démarche adoptée.

Un découpage possible pourrait-être :

decoupe_image(uneImage, nbre_sections)
renvoie un tuple composé des limites en x et y de chaque zone

exemple :
    decoupe_image(poppy,2)
        renvoie (
                (0,largeur//2, 0, hauteur//2) ,
                (largeur//2, largeur, 0, hauteur//2),
                (0, largeur//2, hauteur//2, hauteur),
                (largeur//2, largeur, hauteur//2, hauteur)
                )
           

calculer_moyenne_zone(uneImage, valeurs_limites_zone) 

renvoie un triplet moy_r, moy_v, moy_b
correspondant à la moyenne de chaque composante des pixels présents dans la zone concernée

colorier_zone(uneAutreImage, valeurs_limites_zones, uneCouleur)
colorie les pixels dune autre image dans la zone concernée avec uneCouleur donnée.
"""
from PIL import Image

""" 
il faut créer trois fonctions 

Premiere fonction : decouper l'image en plusieurs section. Elle se nommera  decoupe_image.
Deuxieme fonction : calculer la moyenne des trois couleur bleu, vert , rouge dans chaque section . Elle se nommera composante_moyennetroisieme fonction : appliquer la couleur moyenne à chaque section. elle se nommera colorier_zone.
Troisieme fonction : appliquer la couleur moyenne à chaque section. elle se nommera colorier_zone.

Fonction finale s'appele pixeliser_image(uneImage, nbre_sections) 
"""

# creer une sous fonction decoupe_image
def decoupe_image(uneImage,nbre_sections):
    """
    Premiere fonction : decouper l'image en plusieurs section. 
    Elle se nommera  decoupe_image.
    Entrée: uneImage et un nombre qui correspond aux nombres de section de l'image 
    Sortie: des coordonner des limite des zones (nombre)
    """
    largeur, hauteur = uneImage.size# on rentre les dimensions d'une image 
    # delimite les sections 
    valeurs_limites_zone = []#crér une liste pour les limites des zones 
    # créer une boucle for ligne in range embrique dans une boucle for colonne in range pour balayer l'image d'origine pixel par pixel
    for ligne in range(nbre_sections):
        for colonne in range(nbre_sections):   
            # il faut attribuer chaque groupe de coordonée a une liste 
            valeurs_limites_zone.append([colonne*largeur//nbre_sections,(colonne+1)*largeur//nbre_sections ,ligne*hauteur//nbre_sections,(ligne+1)*hauteur//nbre_sections])
    # on retourne les valeurs des limites des zones
    return valeurs_limites_zone

    # on crée une sous-fonction composante_moyenne 
def composante_moyenne(uneImage,valeurs_limites_zone):
    """ 
    Deuxieme fonction : calculer la moyenne des trois couleur bleu, vert , rouge dans chaque section . 
    Elle se nommera composant
    Entrée: uneImage et des coordonnées des limites de la zone
    Sortie une moyenne par zone
    """
    # on initialise les moyennes des trois composantes à 0
    somme_r,somme_b,somme_v=0,0,0
    # on créer une boucle for x in range embriqué dans une boucle for y in range pour balayer la zone pixel par pixel
    for x in range(valeurs_limites_zone[0],valeurs_limites_zone[1]):
        for y in range(valeurs_limites_zone[2],valeurs_limites_zone[3]):
            # on calcule pour chaque zone les 3 sommes 
            r,v,b=uneImage.getpixel((x,y))
            somme_r = somme_r + r
            somme_v = somme_v + v
            somme_b = somme_b + b
    
    # on calcule le nombre de pixels par section 
    nombre_pixel = (valeurs_limites_zone[1]-valeurs_limites_zone[0])*(valeurs_limites_zone[3]- valeurs_limites_zone[2])
    # on calcule la moyenne des couleurs pour chaque sections 
    moy_r = somme_r// nombre_pixel
    moy_v = somme_v//nombre_pixel
    moy_b = somme_b//nombre_pixel
    # on retourne la valeur des moyennes 
    return moy_r,moy_v,moy_b
                      
# on crée une sous-fonction colorier_zone 
def colorier_zone(uneAutreImage, valeurs_limites_zone, uneCouleur):
    """
    Troisieme fonction : appliquer la couleur moyenne à chaque section. elle se nommera colorier_zone.
    Entée: une autre image ainsi que les coordonne des limites des sections et une couleur 
    Sortie: uen sections colorier dans la moyenne de la section 
    """
    #créer une boucle for x in range embriqué dans une boucle for y in range pour balayer les zones pixel par pixel
    for x in range(valeurs_limites_zone[0], valeurs_limites_zone[1]):
        for y in range(valeurs_limites_zone[2], valeurs_limites_zone[3]):
            uneAutreImage.putpixel((x,y),uneCouleur) # on applique une couleurs determiner pour chaque zones
    # on retourne une autre image         
    return uneAutreImage

    def pixeliser_image(uneImage, nbre_sections):
        """
        Cette fonction a pour but de pixelise une image donne en foction d'un nombre de sections 
        Entrée : une image quelconque et un nombre integer qui represente le nombre de section dont l'image va etre decouper 
        Sortie : une image pixelise 
        """
    
    # recuperer les dimensions uneImage
    largeur, hauteur = uneImage.size
    # creer une nouvelleImage    
    nouvelleImage = Image.new("RGB",(largeur,hauteur))
    # liste_des_zones = decoupe_image(uneImage, nbre_sections)
    liste_zones = decoupe_image(nouvelleImage,nbre_sections)
    # Pour chaque zone de liste_des_zones:
    for zone in liste_zones:
            # couleur_moy_zone = calculer_moyenne_zone(zone)
            couleur_moy = composante_moyenne(uneImage,zone)
            # colorier_zone(nouvelleImage, zone, couleur_moy_zone)
            colorier_zone(nouvelleImage,zone, couleur_moy)
    # retourner nouvelleImage
    return nouvelleImage