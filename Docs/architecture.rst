===============================
Architecture Technique appDesk
===============================

Introduction
============

appDesk est une plateforme de gestion de tickets, d’actifs, d’utilisateurs et de
connaissances. L’architecture est conçue pour être modulaire, scalable et facile
à maintenir. Elle repose sur un backend Django, un frontend React/Vite, une base
PostgreSQL, Redis pour les tâches asynchrones, et Docker pour l’orchestration.

Vue d’ensemble
==============

L’architecture se compose de plusieurs modules :

- Backend Django + DRF
- Frontend React/Vite
- Base de données PostgreSQL
- Redis pour Celery
- Worker Celery + Celery Beat
- Flower pour le monitoring
- Docker Compose pour l’orchestration

Backend
=======

Technologies :

- Django 5
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- JWT Authentication

Modules internes :

- Gestion des tickets
- Gestion des actifs
- Gestion des utilisateurs et rôles
- Base de connaissances
- Notifications
- API REST

Frontend
========

Technologies :

- React 18
- Vite
- TailwindCSS
- Axios
- React Router

Fonctionnalités :

- Tableau de bord
- Gestion des tickets
- Inventaire
- Base de connaissances
- Administration

Base de données
===============

Modèle relationnel basé sur PostgreSQL :

- Tickets
- Actifs
- Utilisateurs
- Rôles
- Articles de connaissance
- Logs

Infrastructure
==============

Docker Compose orchestre :

- backend
- frontend
- postgres
- redis
- celery
- celery beat
- flower

Flux internes
=============

1. L’utilisateur interagit avec le frontend.
2. Le frontend communique avec l’API REST.
3. Le backend traite la requête.
4. Les tâches longues sont déléguées à Celery.
5. Les données sont stockées dans PostgreSQL.
6. Redis gère les files de tâches.
7. Flower permet le monitoring.

Sécurité
========

- JWT
- Permissions DRF
- Validation Pydantic
- Séparation des services
- Variables d’environnement
