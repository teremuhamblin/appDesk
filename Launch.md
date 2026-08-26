###### Launch.md >> markdown
- (Backend, Frontend, Dockerfile, docker-compose, override, plugin system, plugin-store, PostgreSQL, Redis, Celery, Flower, Nginx ...)
- Le projet appDesk est peu être lancé en DEV ou en PROD.

   - **Voici le guide clair et direct**

### 🟦 1. Structure finale de ton projet appDesk

---

### 🟩 2. Lancer le projet
👉 **En développement DEV :**
- Lancer le fichier :
```yaml
docker-compose.override.yml
```
   - **Il est automatiquement chargé en mode dev.**

👉 **En commande DEV :**
```bash
docker-compose up --build
```

>***Ce que ça lance :***
```md
| Service | Mode | Port |
|--------|------|------|
| backend Django | hot‑reload | 8000 |
| frontend Vite | hot‑reload | 5173 |
| PostgreSQL | exposé | 5432 |
| Redis | exposé | 6379 |
| Celery worker | debug | — |
| Celery beat | debug | — |
| Flower | monitoring | 5555 |
```
>URLs DEV :
- Frontend :
```md
http://localhost:5173
```
- Backend API :
```md
http://localhost:8000
```
- Plugin API :
```md
http://localhost:8000/api/plugins/
```
- Flower :
```md
http://localhost:5555
```
   - **Le plugin-store fonctionne immédiatement.**

---

### 🟦 3. Lancer le projet
👉 **En production PROD :**
- Lancer le fichier :
```yaml
docker-compose.yml
```

   - **Lance la version optimisée :**

- frontend → build Vite → Nginx
- backend → Django
- DB → PostgreSQL
- Redis
- Celery
- Flower

👉 **En commande PROD :**
```bash
docker-compose -f docker-compose.yml up --build -d
```

>URLs PROD :
- Frontend (Nginx) :
```md
http://localhost
```
- Backend API :
```md
http://localhost:8000
```
- Plugin API :
```md
http://localhost/api/plugins/
```
- Flower :
```md
http://localhost:5555
```

---

### 🟩 4. Comment lancer ton backend seul (hors Docker)
- Si tu veux tester Django sans Docker :
```text
cd backend
pip install -r requirements.txt
python src/manage.py migrate
python src/manage.py runserver
```

---

### 🟦 5. Comment lancer ton frontend seul (hors Docker)
```text
cd frontend
npm install
npm run dev
```

- Frontend accessible sur :
```text
http://localhost:5173
```

---

### 🟩 6. Comment vérifier que tout fonctionne

✔ Backend OK
```bash
curl http://localhost:8000/api/plugins/list/
```

✔ Frontend OK
Ouvre :  
```text
http://localhost:5173
```
- Tu dois voir ton Plugin Store.

✔ Plugin install OK
- Dans ton UI plugin-store, mets une URL ZIP de plugin.

✔ Celery OK
```bash
docker logs appdesk-celery
```

✔ Flower OK
```text
http://localhost:5555
```

---

### 🟦 7. Workflow militaire pour appDesk
- DEV :
```text
docker-compose up --build
```

- PROD :
```text
docker-compose -f docker-compose.yml up --build -d
```

- Stop :
```text
docker-compose down
```

- Reset DB :
```text
docker volume rm appdeskpostgresdata
```

---

### 🟩 **Pret pour le deploiement**
