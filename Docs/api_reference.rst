==========================
Référence API REST appDesk
==========================

Introduction
============

Cette documentation décrit les endpoints de l’API REST d’appDesk. Toutes les
requêtes utilisent le format JSON et nécessitent un token JWT.

Authentification
================

POST /auth/login
----------------

Payload :

.. code-block:: json

   {
     "username": "admin",
     "password": "pass"
   }

Réponse :

.. code-block:: json

   {
     "token": "jwt-token"
   }

Tickets
=======

GET /tickets/
-------------

Retourne la liste des tickets.

POST /tickets/
--------------

Crée un ticket.

Payload :

.. code-block:: json

   {
     "title": "Problème réseau",
     "description": "Impossible d'accéder à Internet",
     "priority": "high"
   }

Actifs
======

GET /assets/
------------

Liste des actifs.

POST /assets/
-------------

Ajout d’un actif.

Utilisateurs
============

GET /users/
-----------

Liste des utilisateurs.

Base de connaissances
=====================

GET /kb/
--------

Liste des articles.

Filtres & Pagination
====================

- ``?page=1``
- ``?search=mot``
- ``?ordering=created_at``

Codes de retour
===============

- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 404 Not Found
