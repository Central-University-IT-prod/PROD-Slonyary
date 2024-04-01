FROM node:alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN echo $'export const THEME_KEY: string = "appTheme"\n\
          export const BACKEND_HOST = "${DOMAIN}"' > /app/src/constants.ts ski

RUN npm run build

FROM nginx:alpine

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
