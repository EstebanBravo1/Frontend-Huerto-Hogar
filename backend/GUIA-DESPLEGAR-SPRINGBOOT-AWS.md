# 📦 Guía Completa: Desplegar Spring Boot en AWS EC2

Esta guía te ayudará a desplegar cualquier proyecto Spring Boot en AWS EC2 con IP fija (Elastic IP) y arranque automático.

---

## 🎯 **PASO 1: Preparar el proyecto localmente**

### 1.1 Configurar `application.properties`

Edita `src/main/resources/application.properties`:

```properties
spring.application.name=tu-proyecto

# Conexión a Base de Datos (PostgreSQL en AWS)
spring.datasource.url=jdbc:postgresql://${DB_HOST:TU_ELASTIC_IP}:5432/nombre_base_datos
spring.datasource.username=${DB_USERNAME:usuario}
spring.datasource.password=${DB_PASSWORD:password}

# Configuración de JPA / Hibernate
spring.jpa.show-sql=true
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect

# Puerto del servidor
server.port=8080
```

**Importante:** Reemplaza `TU_ELASTIC_IP`, `nombre_base_datos`, `usuario` y `password` con tus valores reales.

### 1.2 Empaquetar el proyecto

Abre PowerShell en la carpeta raíz de tu proyecto y ejecuta:

```powershell
.\mvnw clean package -DskipTests
```

Esto generará el archivo JAR en: `target/nombre-proyecto-0.0.1-SNAPSHOT.jar`

---

## 🌐 **PASO 2: Configurar AWS EC2**

### 2.1 Asignar una Elastic IP (IP fija)

1. Ve a **AWS Console** → **EC2 Dashboard**
2. En el menú lateral: **Network & Security** → **Elastic IPs**
3. Click en **"Allocate Elastic IP address"**
4. Click en **"Allocate"**
5. **Copia la IP** que te asigna (ej: `34.201.115.114`)
6. Selecciona la IP → **Actions** → **"Associate Elastic IP address"**
7. Selecciona tu instancia EC2
8. Click en **"Associate"**

### 2.2 Configurar Security Group (Firewall)

1. Ve a **EC2** → **Instances**
2. Selecciona tu instancia
3. Pestaña **"Security"** → Click en el **Security Group**
4. **"Inbound rules"** → **"Edit inbound rules"**
5. Agrega estas reglas:

| Type       | Port | Source      | Description          |
|------------|------|-------------|----------------------|
| SSH        | 22   | 0.0.0.0/0   | Acceso SSH           |
| Custom TCP | 8080 | 0.0.0.0/0   | Spring Boot API      |
| Custom TCP | 5432 | 0.0.0.0/0   | PostgreSQL (opcional)|

6. Click en **"Save rules"**

---

## 📤 **PASO 3: Subir el JAR a EC2**

Desde PowerShell, ejecuta:

```powershell
scp -i "RUTA\A\TU\CLAVE.pem" "RUTA\AL\PROYECTO\target\nombre-proyecto-0.0.1-SNAPSHOT.jar" ubuntu@TU_ELASTIC_IP:/home/ubuntu/
```

**Ejemplo real:**
```powershell
scp -i "C:\Users\alvar\Desktop\react\ecommerce-key.pem" "C:\Users\alvar\Desktop\ACTUAL\backend\target\backend-0.0.1-SNAPSHOT.jar" ubuntu@34.201.115.114:/home/ubuntu/
```

**Si da error de permisos:**
```powershell
icacls "RUTA\A\TU\CLAVE.pem" /inheritance:r
icacls "RUTA\A\TU\CLAVE.pem" /grant:r "${env:USERNAME}:R"
```

---

## 🔧 **PASO 4: Instalar Java en EC2**

### 4.1 Conectarse a EC2

```powershell
ssh -i "RUTA\A\TU\CLAVE.pem" ubuntu@TU_ELASTIC_IP
```

### 4.2 Instalar Java 17

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
java -version
```

---

## 🚀 **PASO 5: Configurar inicio automático (systemd)**

### 5.1 Crear el archivo de servicio

```bash
sudo nano /etc/systemd/system/tu-proyecto.service
```

### 5.2 Pegar esta configuración

```ini
[Unit]
Description=Spring Boot Backend - Tu Proyecto
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu
ExecStart=/usr/bin/java -jar /home/ubuntu/nombre-proyecto-0.0.1-SNAPSHOT.jar
SuccessExitStatus=143
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Importante:** Reemplaza `nombre-proyecto-0.0.1-SNAPSHOT.jar` con el nombre real de tu JAR.

### 5.3 Guardar el archivo

- `Ctrl + O` (guardar)
- `Enter` (confirmar)
- `Ctrl + X` (salir)

### 5.4 Activar e iniciar el servicio

```bash
# Recargar systemd
sudo systemctl daemon-reload

# Habilitar inicio automático
sudo systemctl enable tu-proyecto

# Iniciar el servicio
sudo systemctl start tu-proyecto

# Verificar estado
sudo systemctl status tu-proyecto
```

### 5.5 Ver logs en tiempo real

```bash
sudo journalctl -u tu-proyecto -f
```

Presiona `Ctrl + C` para salir.

---

## ✅ **PASO 6: Verificar que funciona**

### Desde el navegador:

```
http://TU_ELASTIC_IP:8080/api/tu-endpoint
```

**Ejemplo:**
```
http://34.201.115.114:8080/api/products
```

### Desde PowerShell:

```powershell
Test-NetConnection -ComputerName TU_ELASTIC_IP -Port 8080
```

---

## 🔄 **Actualizar el backend (despliegue futuro)**

Cuando hagas cambios en tu código:

### 1. Empaquetar localmente

```powershell
.\mvnw clean package -DskipTests
```

### 2. Subir el nuevo JAR

```powershell
scp -i "RUTA\A\TU\CLAVE.pem" "target\nombre-proyecto-0.0.1-SNAPSHOT.jar" ubuntu@TU_ELASTIC_IP:/home/ubuntu/
```

### 3. Reiniciar el servicio

```powershell
ssh -i "RUTA\A\TU\CLAVE.pem" ubuntu@TU_ELASTIC_IP "sudo systemctl restart tu-proyecto"
```

### 4. Verificar logs

```powershell
ssh -i "RUTA\A\TU\CLAVE.pem" ubuntu@TU_ELASTIC_IP "sudo journalctl -u tu-proyecto -f"
```

---

## 🛠️ **Comandos útiles de systemd**

| Comando | Descripción |
|---------|-------------|
| `sudo systemctl start tu-proyecto` | Iniciar servicio |
| `sudo systemctl stop tu-proyecto` | Detener servicio |
| `sudo systemctl restart tu-proyecto` | Reiniciar servicio |
| `sudo systemctl status tu-proyecto` | Ver estado |
| `sudo systemctl enable tu-proyecto` | Habilitar inicio automático |
| `sudo systemctl disable tu-proyecto` | Deshabilitar inicio automático |
| `sudo journalctl -u tu-proyecto -f` | Ver logs en tiempo real |
| `sudo journalctl -u tu-proyecto --since "10 minutes ago"` | Ver logs recientes |

---

## 📝 **Checklist de verificación**

Antes de considerar el despliegue exitoso:

- [ ] La Elastic IP está asignada a la instancia
- [ ] El Security Group tiene abierto el puerto 8080
- [ ] Java 17 está instalado en EC2
- [ ] El JAR se subió correctamente a `/home/ubuntu/`
- [ ] El servicio systemd está configurado
- [ ] El servicio está habilitado: `sudo systemctl is-enabled tu-proyecto`
- [ ] El servicio está corriendo: `sudo systemctl is-active tu-proyecto`
- [ ] La URL responde: `http://TU_ELASTIC_IP:8080/api/...`
- [ ] El frontend puede conectarse al backend

---

## ⚠️ **Solución de problemas comunes**

### El backend no inicia

```bash
# Ver logs detallados
sudo journalctl -u tu-proyecto -n 100 --no-pager

# Ver errores de Java
sudo journalctl -u tu-proyecto | grep -i error
```

### No puedo conectarme por SSH

- Verifica que el Security Group tenga el puerto 22 abierto
- Verifica que estás usando el usuario correcto (`ubuntu` o `ec2-user`)
- Verifica los permisos del archivo `.pem`

### El frontend no se conecta al backend

- Verifica que el puerto 8080 esté abierto en el Security Group
- Verifica que la URL en el frontend sea correcta
- Verifica que el backend esté corriendo: `sudo systemctl status tu-proyecto`

### La base de datos no conecta

- Verifica que la IP de la base de datos sea correcta en `application.properties`
- Verifica que el puerto 5432 esté abierto en el Security Group de la base de datos
- Verifica las credenciales de la base de datos

---

## 🎓 **Ejemplo completo para API Sales**

```powershell
# 1. Empaquetar
cd C:\Users\alvar\Desktop\sales-api
.\mvnw clean package -DskipTests

# 2. Subir a EC2
scp -i "C:\Users\alvar\Desktop\react\ecommerce-key.pem" "target\sales-api-0.0.1-SNAPSHOT.jar" ubuntu@34.201.115.114:/home/ubuntu/

# 3. Conectar y configurar
ssh -i "C:\Users\alvar\Desktop\react\ecommerce-key.pem" ubuntu@34.201.115.114

# 4. Crear servicio
sudo nano /etc/systemd/system/sales-api.service

# 5. Pegar configuración (ajustar nombre del JAR)
# 6. Activar
sudo systemctl daemon-reload
sudo systemctl enable sales-api
sudo systemctl start sales-api
sudo systemctl status sales-api

# 7. Ver logs
sudo journalctl -u sales-api -f
```

---

## 📚 **Recursos adicionales**

- [Spring Boot Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/)
- [Systemd Documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

---

**¡Listo!** Ahora puedes desplegar cualquier proyecto Spring Boot en AWS EC2 siguiendo estos pasos. 🚀
