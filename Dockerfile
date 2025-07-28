# Utilise une image Python officielle comme image de base
FROM python:3.12-slim

# Met à jour les paquets système pour corriger d'éventuelles failles
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de dépendances
COPY requirement.txt ./

# Installe les dépendances
RUN pip install --no-cache-dir -r requirement.txt

# Copie tout le code du projet dans le conteneur
COPY . .

# Collecte les fichiers statiques
RUN python ./journal_project/manage.py collectstatic --noinput

# Expose le port 8000
EXPOSE 8000

# Commande de démarrage
CMD ["python", "./journal_project/manage.py", "runserver", "0.0.0.0:8000"]
