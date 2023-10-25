"""
API WIKIPEDIA COMPLET :
- On aide la recherche
- On teste son résultat
- On récupère les homonymes selon Wikipédia
- On lance la recherche sur les homonymes
- On teste les résultats
"""

import wikipedia
import requests
import warnings
warnings.catch_warnings()
warnings.simplefilter('ignore')

wikipedia.set_lang('fr')

# On précise ici la chaîne à chercher car on l'utilisera sans doute plusieurs fois
chercherMot = 'meije'

# Chaîne pour aider à trouver l'article
aide = 'montagne'

# Chaîne pour vérification du résultat
# On la précise ici car on l'utilisera sans doute plusieurs fois
chaineTemoin = 'Massif des Écrins'

# Nombre de phrases à récupérer
# On le précise ici car on l'utilisera sans doute plusieurs fois
numberPhrase = 3

myWikiContent = 'Pas pertinent 0 !'

if chercherMot != '' and chercherMot != None :

    chercher = aide + ' ' + chercherMot

    print('\nChercher :', chercher)
    try:
        myWikiContent = wikipedia.summary(chercher, sentences=numberPhrase)

        # Vérifier la pertinence du résultat
        if str(chaineTemoin).lower() in str(myWikiContent).lower():
            pass

        else:
            myWikiContent = 'Pas pertinent 1 !'

    except wikipedia.exceptions.PageError as e:
        myWikiContent = 'Pas trouvé 1 !'

    except requests.exceptions.ConnectionError as e:
        myWikiContent = 'Pas trouvé 3 !'

    # Gestion des DisambiguationErrors
    except wikipedia.DisambiguationError as e:
        for p in e.options:
            # print('Option testée : ' + p)
            try:
                myWikiContent = wikipedia.summary(p, sentences=numberPhrase)
                # Vérifier la pertinence du résultat
                if str(chaineTemoin).lower() in str(myWikiContent).lower():
                    pass
                if not str(chaineTemoin).lower() in str(myWikiContent).lower():
                    myWikiContent = 'Pas pertinent 2 !'

            except wikipedia.DisambiguationError as e:
                myWikiContent = 'Pas pertinent 3 !'

            except wikipedia.exceptions.PageError as e:
                myWikiContent = 'Pas trouvé 2 !'

            except requests.exceptions.ConnectionError as e:
                myWikiContent = 'Pas trouvé 4 !'

    import re

    myWikiContent = myWikiContent.split('==')[0]

    myWikiContent = myWikiContent.replace('\n\n', '')

    myWikiContent = myWikiContent.replace('. ', '\n')

    print('\n' + str(myWikiContent))
    print('fin')