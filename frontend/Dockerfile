FROM node:latest as build

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

RUN npm create vite@latest

RUN npm i

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]

