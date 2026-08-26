=========================================
Compilation Interne & Workflows CI/CD
=========================================

Introduction
============

Ce document décrit les processus internes de compilation, packaging et CI/CD
pour appDesk.

Compilation Backend
===================

.. code-block:: bash

   docker build -t appdesk-backend ./backend

Compilation Frontend
====================

.. code-block:: bash

   npm install
   npm run build

Workflows CI/CD
===============

- lint backend
- tests backend
- build docker backend
- build docker frontend
- release automatique via tags

Packaging
=========

Les artefacts générés :

- images Docker
- archives de release
- documentation HTML (Sphinx/MkDocs)

Environnements de build
=======================

- GitHub Actions
- Docker local
- Environnement isolé via containers
