Major Hamblin, voici un README.md simple, propre et professionnel pour ton dossier src/ du backend appDesk.  
Format minimal, clair, prêt à coller dans ton repo.

---

📁 src/ — Backend appDesk

Le dossier src/ contient l’ensemble du code source du backend d’appDesk.  
Il regroupe les modules principaux de l’API, la configuration du projet, les modèles, les vues, les routes et la logique métier.

📦 Contenu

- config/ — configuration Django (settings, urls, wsgi/asgi)  
- core/ — utilitaires communs, helpers, exceptions, middleware  
- tickets/ — gestion des tickets (modèles, vues, serializers, routes)  
- inventory/ — gestion des actifs et ressources  
- users/ — gestion des utilisateurs, rôles, permissions  
- knowledge/ — base de connaissances  
- notifications/ — système d’envoi (email, webhook)  
- tests/ — tests unitaires et d’intégration liés au code source

🎯 Rôle du dossier

Ce dossier constitue le cœur du backend :  
- définition des modèles de données,  
- logique métier,  
- endpoints REST,  
- authentification et permissions,  
- intégration des modules internes.

🚀 Démarrage (depuis la racine backend)

`bash
python manage.py runserver
`

🧪 Tests

`bash
pytest
`

📜 Licence

Le code source du dossier src/ est distribué sous licence MIT, comme le projet principal.

---
