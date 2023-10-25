

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