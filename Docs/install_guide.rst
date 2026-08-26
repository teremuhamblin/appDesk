==========================
Guide d'installation appDesk
==========================

Introduction
============

Ce guide décrit l'installation complète d'appDesk via Docker Compose. Il couvre
les prérequis, la configuration, le lancement des services et l'initialisation
du système.

Prérequis
=========

- Docker 24+
- Docker Compose v2+
- Git
- 4 Go RAM minimum

Récupération du projet
======================

.. code-block:: bash

   git clone https://github.com/teremuhamblin/appDesk.git
   cd appDesk

Configuration
=============

Créer le fichier ``backend/.env`` :

.. code-block:: bash

   DEBUG=False
   SECRET_KEY=change_me
   DATABASE_URL=postgres://appdesk_user:appdesk_pass@postgres:5432/appdesk
   REDIS_URL=redis://redis:6379/0

Lancement des services
======================

.. code-block:: bash

   docker-compose up -d --build

Initialisation de la base
=========================

.. code-block:: bash

   docker-compose exec backend python src/manage.py migrate

Création du superuser
=====================

.. code-block:: bash

   docker-compose exec backend python src/manage.py createsuperuser

Accès à l'application
=====================

- Backend : http://localhost:8000
- Frontend : http://localhost:5173
- Flower : http://localhost:5555

Maintenance
===========

.. code-block:: bash

   docker-compose logs -f backend
   docker-compose restart backend
