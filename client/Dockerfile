# Usa la imagen base de Nginx
FROM nginx:latest

# Elimina la configuración por defecto de Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia tu configuración personalizada de Nginx (si es necesario)
COPY nginx.conf /etc/nginx/conf.d/

# Copia los archivos del cliente (HTML, JS, CSS) al directorio raíz de Nginx
COPY . /usr/share/nginx/html

# Exponer el puerto donde Nginx estará escuchando
EXPOSE 80
