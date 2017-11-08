FROM node

RUN apt-get update && apt-get install -y nginx
COPY ./nginx/ /etc/nginx/sites-enabled/

RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /ui
COPY ./package.json /ui/package.json
RUN npm install --warn
COPY ./ /ui
RUN npm run build

RUN chmod 755 -R /ui/dist

EXPOSE 5000
CMD ["nginx", "-g", "daemon off;"]