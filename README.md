# ChatGPT3

 Réalisation d'un clonage de ChatGPT en utilisant Python, j'ai utilisé deux modules principaux : `customtkinter` et `openai`. Le module `customtkinter` permet de créer des interfaces graphiques modernes et personnalisables, tandis que le module `openai` me permet d'interagir avec l'API d'OpenAI pour exploiter les capacités de traitement du langage naturel de ChatGPT.

Avant de commencer, il est essentiel de posséder une clé API fournie par OpenAI. Cette clé est nécessaire pour authentifier les requêtes envoyées à l'API. Après avoir obtenu cette clé en m'inscrivant sur le site d'OpenAI et en créant une nouvelle API, je dois l'insérer dans l'instance de client OpenAI. Pour ce faire, j'initialise le client avec ma clé API.

Ensuite, j'installe les bibliothèques nécessaires (`customtkinter` et `openai`) et je crée une interface utilisateur simple. Cette interface inclut une zone de texte pour saisir les questions, un bouton pour envoyer les questions à l'API, et une zone de texte pour afficher les réponses générées par ChatGPT. Cela permet de construire une application basique qui peut être personnalisée et améliorée selon mes besoins.
