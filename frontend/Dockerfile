# Step 1: Build the React application
FROM node:latest as build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm i
RUN ls -la
# Step 2: Set up Nginx to serve the React application
FROM nginx:stable-alpine as production-stage
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]