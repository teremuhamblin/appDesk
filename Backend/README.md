 ###### README.md >> markdown

# 🎯 appDesk
> Backend
Le backend d’appDesk fournit l’API principale du système :
- gestion des tickets,
- inventaire,
- utilisateurs,
- rôles et base de connaissances.  
   - Il expose une **API REST** structurée, sécurisée et extensible.

Fonctionnalités

- API REST pour toutes les entités (tickets, actifs, utilisateurs, etc.)
- Authentification (JWT ou session selon configuration)
- Gestion des rôles et permissions
- Système de notifications (email / webhook)
- Structure modulaire pour ajouter facilement de nouveaux modules

Stack technique

- Python + Django + Django REST Framework  
  (ou Node.js + NestJS si choisi dans le projet)  
- PostgreSQL comme base de données
- Docker pour l’environnement de déploiement

Démarrage

`bash

Installer les dépendances
pip install -r requirements.txt

Lancer le serveur
python manage.py runserver
`

Tests
```bash
pytest
```

### Structure
```text
backend/
├─ src/
├─ tests/
├─ requirements.txt
└─ Dockerfile
```

Licence

Ce module backend est distribué sous licence MIT.
`

---
