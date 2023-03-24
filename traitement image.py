"""
Objectif du projet
Jouer avec la notion de pixelisation des images pour produire des "oeuvres d'art"
La première partie de ce notebook à pour objectif de vous donner les éléments logiciels 
nécessaires à l'avancement du projet.On utilisera la bibliothèque PILlow spécialisée dans le traitement 
de l'image. Vous pourrez avantageusement en tirer profit en lisant la documentation lorsque cela est nécessaire."""

from PIL import Image
# on crée une structure image de 256 pixels sur 256 pixels utilisant le codage couleur RGB

monCarreBleu = Image.new("RGB", (256,256))

for x in range(256):
    for y in range(256):
        monCarreBleu.putpixel((x,y),(0,0,255)) # on colorie le pixel à la position x,y en bleu

from PIL import Image
# on crée une structure image de 256 pixels sur 256 pixels  dégradé vertical de rouge 

monDegadreRouge = Image.new("RGB", (256,256))

for x in range(256):
    for y in range(256):
        monDegadreRouge.putpixel((x,y),(x,0,0)) 

from PIL import Image
# on crée une structure image de 256 pixels sur 256 pixels  dégradé vertical de rouge 

monDegadreVert = Image.new("RGB", (256,256))

for x in range(256):
    for y in range(256):
        monDegadreVert.putpixel((x,y),(0,x,0)) 

from PIL import Image
# on crée une structure image de 256 pixels sur 256 pixels  dégradé vertical de rouge 

monDegadreBleu = Image.new("RGB", (256,256))

for x in range(256):
    for y in range(256):
        monDegadreBleu.putpixel((x,y),(0,0,x)) 

from PIL import Image
# on crée une structure image de 256 pixels sur 256 pixels  dégradé vertical de rouge 

monDegadreBleu = Image.new("RGB", (256,256))

for x in range(256):
    for y in range(256):
        monDegadreBleu.putpixel((x,y),(x,x,x)) 

from PIL import Image
# code pour charger et afficher une image
puppy = Image.open("puppy.png")

largeur, hauteur = puppy.size

"""
Voici un exemple de code pour le filtre rouge

"""

# On crée une nouvelle image aux dimensions du Puppy originale
puppy_rouge = Image.new("RGB",(largeur,hauteur))

# On balaye l'image d'origine pixel par pixel
for x in range(largeur):
    for y in range(hauteur):
        # on récupère les 3 composantes couleurs du pixel à la position x,y donnée
        composante_rouge, composante_verte, composante_bleu = puppy.getpixel((x,y)) 
        # on copie la composante rouge dans l'image de sortie et on force les 2 autres composantes verte et bleue à 0
        puppy_rouge.putpixel((x,y),(composante_rouge, 0, 0))
# on affiche la nouvelle image        
puppy_rouge

# filtre vert
puppy = Image.open("puppy.png")
largeur, hauteur = puppy.size
def filtre_vert(uneImage):
    """
    rôle : Ne garde que la composante verte d'une image passée en argument d'entrée
    entrée : uneImage, image préalablement chargée avec PIL
    sortie : une image à composante verte uniquement    
    """
    largeur, hauteur = uneImage.size
    
    # On crée une nouvelle image aux dimensions du Puppy originale
    image_en_sortie = Image.new("RGB",(largeur,hauteur))
    
    # a completer vous même
    for x in range(largeur):
        for y in range(hauteur):
            # on récupère les 3 composantes couleurs du pixel à la position x,y donnée
            composante_rouge, composante_verte, composante_bleu = puppy.getpixel((x,y)) 
            # on copie la composante rouge dans l'image de sortie et on force les 2 autres composantes verte et bleue à 0
            image_en_sortie.putpixel((x,y),(0,composante_verte ,0))

       
    return image_en_sortie

filtre_vert(puppy)

def filtre_gris(uneImage):
    """
    rôle : passe une image en couleur RGB en niveau de gris
    entrée : uneImage, image préalablement chargée avec PIL
    sortie : une image à composante en niveau de gris
    
    indications :
    Il suffit de faire la moyenne des 3 composantes et de positionner cette valeur 
    sur les 3 composantes R,G,B de l'image de sortie.
    
    exemple :
    
    niveau_de_gris = ... # calculer la moyenne des 3 composantes
    imageGrise = uneImage.putpixel((x,y),(niveau_de_gris))
    ...
    return imageGrise
    """
    largeur, hauteur = uneImage.size
   
    # On crée une nouvelle image aux dimensions du Puppy originale
    image_en_sortie = Image.new("RGB",(largeur,hauteur))
    
    for x in range(largeur):
        for y in range(hauteur):
            # on récupère les 3 composantes couleurs du pixel à la position x,y donnée
            composante_rouge, composante_verte, composante_bleu = uneImage.getpixel((x,y))
            
            niveau_de_gris=(composante_rouge+ composante_verte+ composante_bleu)//3
            image_en_sortie.putpixel((x,y),(niveau_de_gris,niveau_de_gris,niveau_de_gris))
            
    return image_en_sortie

filtre_gris(puppy)

puppy = Image.open("puppy.png")
largeur, hauteur = puppy.size


