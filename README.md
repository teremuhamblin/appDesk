###### README.md >> markdown 
- Logiciel simple similaire a GLPI

[![Deploy static content to Pages](https://github.com/teremuhamblin/appDesk/actions/workflows/static.yml/badge.svg)](https://github.com/teremuhamblin/appDesk/actions/workflows/static.yml)

# appDesk
appDesk est un logiciel open source de gestion de parc et de tickets,
inspiré de GLPI, conçu pour être simple à déployer et à étendre.

[![pages-build-deployment](https://github.com/teremuhamblin/appDesk/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/teremuhamblin/appDesk/actions/workflows/pages/pages-build-deployment)

- LANCEMENT AVEC ***Launch.md***

### Structure du projet

[![Dependency Graph](https://github.com/teremuhamblin/appDesk/actions/workflows/dependabot/update-graph/badge.svg)](https://github.com/teremuhamblin/appDesk/actions/workflows/dependabot/update-graph)

```text
appDesk/
├─ .github/ . /
├─ Backend/
│  ├─ src/
│  ├─ tests/
│  ├─ README.md 
│  ├─ requirements.txt  # si Python/Django
│  └─ Dockerfile
├─ Frontend/
│  ├─ src/
│  ├─ public/
│  ├─ README.md 
│  ├─ package.json      # si React/Vue
│  └─ Dockerfile
├─ Docs/
    ├─ README.md
    ├─ architecture.rst
    ├─ install_guide.rst
    ├─ api_reference.rst
    ├─ user_guide.rst
    ├─ operator_manual.rst
    └─ internal_compilation.rst
├─ docker-compose.yml
├─ docker-compose.override.yml
├─ LICENSE
├─ Launch.md
└─ README.md
```

### Fonctionnalités
   - Gestion des tickets (création, assignation, suivi)
   - Inventaire des actifs (machines, logiciels, contrats)
   - Base de connaissances
   - Rapports et statistiques
   - Notifications par email

## Licence
appDesk est distribué sous licence MIT.
