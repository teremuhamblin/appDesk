###### README.md >> markdown 
- Logiciel simple similaire a GLPI

# appDesk
appDesk est un logiciel open source de gestion de parc et de tickets,
inspiré de GLPI, conçu pour être simple à déployer et à étendre.

### Structure du projet
```text
appDesk/
├─ .github/ . /
├─ Backend/
│  ├─ src/
│  ├─ tests/
│  ├─ requirements.txt  # si Python/Django
│  └─ Dockerfile
├─ Frontend/
│  ├─ src/
│  ├─ public/
│  ├─ package.json      # si React/Vue
│  └─ Dockerfile
├─ Docs/
│  ├─ architecture.md
│  ├─ api_reference.md
│  └─ install_guide.md
├─ docker-compose.yml
├─ LICENSE
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
