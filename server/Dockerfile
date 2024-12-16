# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala venv y configura el entorno virtual
RUN python -m venv venv \
    && ./venv/bin/pip install --upgrade pip \
    && ./venv/bin/pip install -r requirements.txt

# Define las variables de entorno
ENV PATH="/app/venv/bin:$PATH"

# Exponer el puerto donde se ejecutará el servicio
EXPOSE 80

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
