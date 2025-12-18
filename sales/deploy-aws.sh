#!/bin/bash

# Script de despliegue para el microservicio de ventas en AWS Ubuntu
# Ejecutar este script en tu instancia EC2 de AWS

echo "=== Desplegando Microservicio de Ventas en AWS Ubuntu ==="

# 1. Actualizar el sistema
echo "Actualizando sistema..."
sudo apt update
sudo apt upgrade -y

# 2. Instalar Java 17
echo "Instalando Java 17..."
sudo apt install openjdk-17-jdk -y

# 3. Instalar Maven
echo "Instalando Maven..."
sudo apt install maven -y

# 4. Verificar instalaciones
echo "Verificando instalaciones..."
java -version
mvn -version

# 5. Crear directorio para la aplicación
echo "Creando directorio de aplicación..."
sudo mkdir -p /opt/sales-service
sudo chown -R ubuntu:ubuntu /opt/sales-service

# 6. Copiar archivos (debes subir el proyecto primero)
echo "Copiando archivos..."
cp -r ~/sales/* /opt/sales-service/

# 7. Compilar la aplicación
echo "Compilando aplicación..."
cd /opt/sales-service
./mvnw clean package -DskipTests

# 8. Crear servicio systemd
echo "Creando servicio systemd..."
sudo tee /etc/systemd/system/sales-service.service > /dev/null <<EOF
[Unit]
Description=Sales Service
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/opt/sales-service
ExecStart=/usr/bin/java -jar /opt/sales-service/target/sales-0.0.1-SNAPSHOT.jar
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 9. Habilitar e iniciar el servicio
echo "Habilitando servicio..."
sudo systemctl daemon-reload
sudo systemctl enable sales-service
sudo systemctl start sales-service

# 10. Verificar estado
echo "Verificando estado del servicio..."
sudo systemctl status sales-service

# 11. Configurar UFW (firewall de Ubuntu)
echo "Configurando firewall..."
sudo ufw allow 8081/tcp 2>/dev/null || echo "UFW no configurado"

echo "=== Despliegue completado ==="
echo "El servicio está corriendo en el puerto 8081"
echo "Verifica con: curl http://localhost:8081/api/sales/products"
