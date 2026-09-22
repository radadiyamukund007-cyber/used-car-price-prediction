FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
COPY car-intake.html /usr/share/nginx/html/car-intake.html
COPY about.html /usr/share/nginx/html/about.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]