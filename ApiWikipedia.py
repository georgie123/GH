
########################### Api Wikipedia exemple choix testé
import wikipedia

import warnings
warnings.catch_warnings()
warnings.simplefilter('ignore')

wikipedia.set_lang('fr')

chercher = 'dibona'
chaineTemoin = 'Massif des Écrins'
numberPhrase = 2

myWikiContent = ''

print('\nChercher :', chercher)
try:
    myWikiContent = wikipedia.summary(chercher, sentences=numberPhrase)

    # Vérifier la pertinence du résultat
    if str(chaineTemoin).lower() in str(myWikiContent).lower():
        pass

    else:
        myWikiContent = 'Pas pertinent !!!'

# Gestion des DisambiguationErrors
except wikipedia.DisambiguationError as e:
    # print('\nAttention : 1ère DisambiguationError!')
    for p in e.options:
        # print('Option testée : ' + p)
        try:
            myWikiContent = wikipedia.summary(p, sentences=numberPhrase)
            # Vérifier la pertinence du résultat
            if str(chaineTemoin).lower() in str(myWikiContent).lower():
                break

        except wikipedia.DisambiguationError as e:
            # print('\nAttention : 2ème DisambiguationError!')
            myWikiContent = 'Pas pertinent !!!'

print(str(myWikiContent))

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

    # Random
    s = random.choice(e.options)
    myWikiContent = wikipedia.summary(s)
    print('Au hasard : ' + str(myWikiContent))

# Vérifier la pertinence du resultat
if str('Massif des Écrins').lower() in str(myWikiContent).lower():
    pass

else:
    myWikiContent = 'Oooouuuuppssss 1 !!!'

print('\nmyWikiContent' + str(myWikiContent))

########################### Api Wikipedia exemple simple
print('\nApi Wikipedia exemple simple')
import wikipedia

wikipedia.set_lang("fr")

summary_fr = wikipedia.summary("Aiguille Dibona", sentences=10)
my_page = wikipedia.page("Aiguille Dibona")

print(summary_fr)
print(my_page.url)