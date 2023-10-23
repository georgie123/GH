
########################### Api Wikipedia exemple choix au hasard
import wikipedia
import random

wikipedia.set_lang("fr")

myWikiContent = ''

try:
    myWikiContent = wikipedia.summary("L'Ourson", sentences=3)

# Gestion des DisambiguationErrors
except wikipedia.DisambiguationError as e:
    print('\nAttention : DisambiguationError !')
    # print(str(e))
    # print(e.options)

    print(e)

    for p in e.options:
        print('p : ' + p)

        try:
            myWikiContent = wikipedia.summary(p)
        except wikipedia.DisambiguationError as e:
            print('\nAttention : DisambiguationError !')

# Vérifier la pertinence du resultat si pas de DisambiguationError
if str('Massif des Écrins').lower() in str(myWikiContent).lower():
    pass

else:
    myWikiContent = 'Pas pertinent !!!'

print('\nmyWikiContent : ' + str(myWikiContent))