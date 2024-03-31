# Step 1: Build the React application
FROM node:latest as build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm create vite@latest
RUN npm i
CMD ["npm", "run", "dev", "--", "--host"]

