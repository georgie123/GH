import wikipedia
import requests
import warnings
import re

warnings.catch_warnings()
warnings.simplefilter('ignore')

wikipedia.set_lang('fr')

# On précise ici la chaîne à chercher car on l'utilisera sans doute plusieurs fois
chercherMot = "l'ourson"

# Chaîne pour aider à trouver l'article
aide = ''

# Chaîne pour vérification du résultat
# On la précise ici car on l'utilisera sans doute plusieurs fois
chaineTemoin = 'Massif des Écrins'

# Nombre de phrases à récupérer
# On le précise ici car on l'utilisera sans doute plusieurs fois
numberPhrase = 10

# Nombre de lettres à récupérer
numberLetter = 500

myWikiContent = 'Pas pertinent'

if chercherMot != '' and chercherMot != None :
    chercher = aide + ' ' + chercherMot
    print('\nChercher :', chercher)

    try:
        myWikiContent = wikipedia.summary(chercher, sentences=numberPhrase)

        # Vérifier la pertinence du résultat
        if str(chaineTemoin).lower() in str(myWikiContent).lower():
            pass

        else:
            myWikiContent = 'Pas pertinent'

    except wikipedia.exceptions.PageError as e:
        myWikiContent = 'Pas pertinent'

    except requests.exceptions.ConnectionError as e:
        myWikiContent = 'Pas pertinent'

    # Gestion des DisambiguationErrors
    except wikipedia.DisambiguationError as e:
        for p in e.options:
            print('Option testée : ' + p)

            try:
                myWikiContent = wikipedia.summary(p, sentences=numberPhrase)

                # Vérifier la pertinence du résultat
                if str(chaineTemoin).lower() in str(myWikiContent).lower():
                    break

                if not str(chaineTemoin).lower() in str(myWikiContent).lower():
                    myWikiContent = 'Pas pertinent'

            except wikipedia.DisambiguationError as e:
                myWikiContent = 'Pas pertinent'

            except wikipedia.exceptions.PageError as e:
                myWikiContent = 'Pas pertinent'

            except requests.exceptions.ConnectionError as e:
                myWikiContent = 'Pas pertinent'

    # Mise en forme du résultat
    myWikiContent = re.sub('==(.+)==', '', myWikiContent)
    myWikiContent = re.sub('\n\n', '\n', myWikiContent)
    myWikiContent = re.sub('\n\n', '\n', myWikiContent)

    myWikiContent = re.sub('\. ', '.\n', myWikiContent)
    myWikiContent = re.sub('\[réf\.\n', ' [réf. ', myWikiContent)

    # Raccourcissement du résultat
    if len(myWikiContent) > numberLetter:
        myWikiContent = myWikiContent[:numberLetter] + '...'

        print('\n' + str(myWikiContent))

    if len(myWikiContent) < numberLetter:
        print('\n' + str(myWikiContent))