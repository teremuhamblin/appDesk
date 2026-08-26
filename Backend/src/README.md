###### README.md >> markdown
- simple, propre et professionnel pour ton dossier **src/** du ***backend appDesk.*** 
(Format minimal, clair et prêt)

---

# 📁 src/
> Backend appDesk
Le dossier `src/` contient l’ensemble du code source du backend d’appDesk.  
Il regroupe les modules principaux de l’API, la configuration du projet, les modèles, les vues, les routes et la logique métier.

### 📦 Contenu
- config/ — configuration Django (settings, urls, wsgi/asgi)  
- core/ — utilitaires communs, helpers, exceptions, middleware  
- tickets/ — gestion des tickets (modèles, vues, serializers, routes)  
- inventory/ — gestion des actifs et ressources  
- users/ — gestion des utilisateurs, rôles, permissions  
- knowledge/ — base de connaissances  
- notifications/ — système d’envoi (email, webhook)  
- tests/ — tests unitaires et d’intégration liés au code source

### 🎯 Rôle du dossier
>Ce dossier constitue le cœur du backend :  
- définition des modèles de données,  
- logique métier,  
- endpoints REST,  
- authentification et permissions,  
- intégration des modules internes.

```text
src/
├─ config/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
│
├─ core/
│  ├─ __init__.py
│  ├─ exceptions.py
│  ├─ middleware.py
│  └─ utils.py
│
├─ tickets/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  └─ urls.py
│
├─ inventory/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  └─ urls.py
│
├─ users/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  └─ urls.py
│
├─ knowledge/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  └─ urls.py
│
├─ notifications/
│  ├─ __init__.py
│  ├─ email.py
│  ├─ webhook.py
│  └─ service.py
│
└─ __init__.py
```

###🚀 Démarrage (depuis la racine backend)
```python
python manage.py runserver
```

### 🧪 Tests
```pyton
pytest
```

### 📜 Licence
Le code source du dossier src/ est distribué sous licence MIT, comme le projet principal.

---
