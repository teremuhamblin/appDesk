###### README.md >> markdown 
# appDesk
> Documentation Technique & Fonctionnelle

Ce dossier contient l’ensemble de la documentation officielle du projet **appDesk**, 
un système open source de gestion de tickets, d’actifs, d’utilisateurs et de 
connaissances, inspiré de GLPI mais conçu pour être plus moderne, modulaire et léger.

La documentation est organisée pour couvrir tous les aspects du projet :
```md
architecture, installation, API, développement, exploitation et maintenance.
```

---

### 📁 Structure du dossier
> `Docs/`
   - **architecture.md**  
```text
***Description complète de l’architecture backend, frontend, base de données, services Docker, flux internes, modules, et logique métier.***
```

   - **install_guide.md**  
```text
***Guide d’installation détaillé : prérequis, configuration, variables d’environnement, lancement via Docker Compose, initialisation de la base, création du superuser.***
```

   - **api_reference.md**  
***Documentation de l’API REST : endpoints, méthodes, schémas JSON, codes de retour, authentification, pagination, filtres, exemples de requêtes.***

   - **user_guide.rst**  
***Manuel utilisateur : création de tickets, consultation du parc, recherche, notifications, base de connaissances.***

   - **operator_manual.rst**  
***Manuel opérateur / technicien : gestion des tickets, assignation, suivi, actions rapides, outils internes.***

   - **rust_dev_guide.rst**  
***Guide de développement Rust (si modules Rust intégrés) : structure, compilation, intégration, bonnes pratiques.***

   - **internal_compilation.rst**  
***Documentation interne pour la compilation, le packaging, les workflows CI/CD, les environnements de build.***

```text
docs/
├─ architecture.rst
├─ install_guide.rst
├─ api_reference.rst
├─ user_guide.rst
├─ operator_manual.rst
└─ internal_compilation.rst
```

---

### 🎯 Objectifs de la documentation
```md
- Fournir une vision claire et complète du fonctionnement d’appDesk  
- Faciliter l’installation et le déploiement pour les administrateurs  
- Guider les développeurs dans l’extension du projet  
- Documenter l’API pour les intégrations externes  
- Offrir des guides simples pour les utilisateurs et techniciens  
- Assurer une maintenance durable du projet
```

---

### 🛠️ Technologies documentées
- **Backend :** Django 5, DRF, Celery, Redis, PostgreSQL  
- **Frontend :** React/Vue + Vite  
- **Infrastructure :** Docker, Docker Compose  
- **CI/CD :** GitHub Actions  
- **Documentation :** Markdown + ReStructuredText (Sphinx/MkDocs)

---

## 📄 Formats utilisés

- `.md` pour la documentation générale  
- `.rst` pour les guides techniques avancés (compatibles Sphinx)  
- Possibilité d’étendre vers MkDocs ou ReadTheDocs

---

## 🔗 Contribution

Toute amélioration de la documentation est bienvenue.  
Les contributions doivent respecter la structure existante et maintenir une 
cohérence technique et stylistique.

---

## 📜 Licence

La documentation appDesk est distribuée sous licence **MIT**, comme le projet principal.
