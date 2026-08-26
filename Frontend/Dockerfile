# ============================
#   appDesk Frontend - Dockerfile Optimisé
#   Vite + React + Nginx
# ============================

########## BUILD STAGE ##########
FROM node:20-slim AS build

# Réduction de taille + optimisation réseau
ENV NODE_ENV=production
ENV CI=true

WORKDIR /app

# Cache intelligent pour npm install
COPY package.json package-lock.json ./
RUN npm ci --prefer-offline --no-audit --no-fund

# Copier le code source
COPY . .

# Build Vite (sortie dans /app/dist)
RUN npm run build


########## PRODUCTION STAGE ##########
FROM nginx:1.25-alpine AS production

# Nettoyage + sécurité minimale
RUN rm -rf /var/cache/apk/* \
    && adduser -D -g '' appdesk \
    && mkdir -p /usr/share/nginx/html \
    && chown -R appdesk:appdesk /usr/share/nginx/html

# Copier le build dans nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Ajouter une config nginx optimisée pour React + API Django
COPY nginx.conf /etc/nginx/conf.d/default.conf

USER appdesk

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
