# Guía de Despliegue en AWS - Microservicio de Ventas

## Opción 1: Despliegue en la misma instancia que Products (RECOMENDADO)

Si ya tienes el microservicio de productos corriendo en AWS, puedes desplegar este servicio en la misma instancia.

### Pasos:

1. **Conectarse a tu instancia EC2:**
   ```bash
   ssh -i tu-key.pem ec2-user@34.201.115.114
   ```

2. **Crear directorio para el servicio:**
   ```bash
   sudo mkdir -p /opt/sales-service
   sudo chown -R ec2-user:ec2-user /opt/sales-service
   ```

3. **Subir el proyecto desde tu PC a AWS:**
   
   Desde tu PC (PowerShell), ejecuta:
   ```powershell
   # Comprimir el proyecto
   Compress-Archive -Path .\* -DestinationPath sales.zip
   
   # Subir a AWS
   scp -i tu-key.pem sales.zip ec2-user@34.201.115.114:/home/ec2-user/
   ```

4. **En AWS, descomprimir y compilar:**
   ```bash
   cd /home/ec2-user
   unzip sales.zip -d /opt/sales-service
   cd /opt/sales-service
   
   # Usar el perfil de producción
   cp application-prod.properties src/main/resources/application-prod.properties
   
   # Compilar
   ./mvnw clean package -DskipTests
   ```

5. **Crear servicio systemd:**
   ```bash
   sudo nano /etc/systemd/system/sales-service.service
   ```
   
   Pegar este contenido:
   ```ini
   [Unit]
   Description=Sales Service
   After=network.target

   [Service]
   Type=simple
   User=ec2-user
   WorkingDirectory=/opt/sales-service
   ExecStart=/usr/bin/java -jar -Dspring.profiles.active=prod /opt/sales-service/target/sales-0.0.1-SNAPSHOT.jar
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

6. **Iniciar el servicio:**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable sales-service
   sudo systemctl start sales-service
   sudo systemctl status sales-service
   ```

7. **Configurar Security Group en AWS Console:**
   - Ir a EC2 → Security Groups
   - Agregar regla de entrada:
     - Tipo: Custom TCP
     - Puerto: 8081
     - Origen: 0.0.0.0/0 (o tu IP específica)

8. **Verificar que funciona:**
   ```bash
   curl http://localhost:8081/api/sales/products
   ```
   
   Desde tu PC:
   ```
   http://34.201.115.114:8081/api/sales/products
   ```

---

## Opción 2: Despliegue en instancia separada

Si prefieres una instancia EC2 separada para el servicio de ventas:

1. Crear nueva instancia EC2 (igual que la de productos)
2. Seguir los pasos anteriores
3. Actualizar `application-prod.properties`:
   ```properties
   products.api.url=http://34.201.115.114:8080
   ```

---

## Comandos útiles

```bash
# Ver logs del servicio
sudo journalctl -u sales-service -f

# Reiniciar servicio
sudo systemctl restart sales-service

# Detener servicio
sudo systemctl stop sales-service

# Ver estado
sudo systemctl status sales-service

# Recompilar después de cambios
cd /opt/sales-service
./mvnw clean package -DskipTests
sudo systemctl restart sales-service
```

---

## Configuración de PostgreSQL (si usas BD separada)

Si quieres usar PostgreSQL en lugar de H2:

```bash
# En AWS, conectarse a PostgreSQL
sudo -u postgres psql

# Crear base de datos para ventas (opcional, puedes usar la misma)
CREATE DATABASE sales_db;

# O usar la misma base de datos que productos
# Ya tienes ecommerce_db con el usuario springuser
```

---

## Troubleshooting

### Puerto 8081 ya en uso:
```bash
sudo lsof -i :8081
sudo kill -9 <PID>
```

### Ver qué está pasando:
```bash
sudo journalctl -u sales-service --no-pager -n 100
```

### Error de conexión a productos:
```bash
# Verificar que products API está corriendo
curl http://localhost:8080/api/products

# Si no funciona, revisar el servicio de productos
sudo systemctl status products-service
```
