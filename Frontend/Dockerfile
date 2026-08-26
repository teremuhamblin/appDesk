# ============================
#   appDesk Frontend - Dockerfile
#   Vite + React + Nginx
# ============================

# --- Build stage ---
FROM node:20-slim AS build

WORKDIR /app

# Installer dépendances
COPY package.json .
COPY package-lock.json .
RUN npm install

# Copier le code
COPY . .

# Build Vite
RUN npm run build

# --- Production stage ---
FROM nginx:1.25-alpine

# Copier le build dans nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copier config nginx si besoin
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
