#FROM node:latest as build
#
#WORKDIR /app
#
#COPY package.json ./
#
#RUN npm install
#
#COPY . .
#
#RUN npm create vite@latest
#
#RUN npm i
#
#EXPOSE 5173
#
#CMD ["npm", "run", "dev", "--", "--host"]


## 1. Создаем приложение Angular
#FROM node:alpine as builder
#WORKDIR /app
## Убедитесь, что файлы package.json и package-lock.json сначала копируются, чтобы использовать кэширование слоев
#COPY package.json package-lock.json ./
#ENV CI=1
#RUN npm ci
## Теперь копируем остальные файлы проекта и собираем
#COPY . .
#RUN npm run build
## 2. Развертываем приложение Angular на NGINX
#FROM nginx:alpine
## Заменяем дефолтную страницу nginx соответствующей веб-приложению
#RUN rm -rf /usr/share/nginx/html/*
## Указываем правильный путь к собранным файлам, включая имя проекта, если оно есть
#COPY --from=builder /app/dist/ /usr/share/nginx/html
## Копируем конфигурацию NGINX, если она есть
#COPY nginx/nginx.conf /etc/nginx/nginx.conf
#ENTRYPOINT ["nginx", "-g", "daemon off;"]

# Use an official Node runtime as a parent image
FROM node:alpine as build
# Set the working directory to /app
WORKDIR /app
# Copy the package.json and package-lock.json to the container
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy the rest of the application code to the container
COPY . .
# Build the React app
RUN npm run build
# Use an official Nginx runtime as a parent image
FROM nginx:alpine
# Copy the nginx.conf to the container
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
# Copy the React app build files to the container
COPY --from=build /app/dist /usr/share/nginx/html
# Expose port 80 for Nginx
EXPOSE 80
# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]



