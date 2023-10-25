
########################### Api Wikipedia exemple choix testé
import wikipedia

import warnings
warnings.catch_warnings()
warnings.simplefilter('ignore')

wikipedia.set_lang('fr')

chercher = 'aiguille dibona'
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
                pass
            if not str(chaineTemoin).lower() in str(myWikiContent).lower():
                myWikiContent = 'Pas pertinent !!!'

        except wikipedia.DisambiguationError as e:
            # print('\nAttention : 2ème DisambiguationError!')
            myWikiContent = 'Pas pertinent !!!'

print(str(myWikiContent))