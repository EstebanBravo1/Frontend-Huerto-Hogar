# 📋 DOCUMENTACIÓN CONCEPTUAL - HUERTO HOGAR

## 📄 Documentos Generados

Se han generado **3 documentos Word** con análisis conceptual completo del proyecto Huerto Hogar. Cada uno ofrece un nivel diferente de detalle y enfoque:

---

### 1️⃣ **ANALISIS_CONCEPTUAL_HUERTO_HOGAR.docx** (45 KB)
**Versión Base - Recomendado para comenzar**

Contenido:
- ✅ Descripción general del proyecto
- ✅ Stack tecnológico completo
- ✅ Arquitectura de microservicios
- ✅ Explicación de los 3 microservicios (Productos, Usuarios, Ventas)
- ✅ Componentes React principales
- ✅ Gestión de estado con Contextos
- ✅ Tabla de base de datos
- ✅ Flujos de procesos principales
- ✅ Métodos detallados de servicios
- ✅ Seguridad y autenticación
- ✅ Consideraciones técnicas

**Ideal para:** Primera lectura, entender estructura general

---

### 2️⃣ **ANALISIS_CONCEPTUAL_HUERTO_HOGAR_EXTENDIDO.docx** (42 KB)
**Versión Extendida - Análisis profundo de componentes**

Contenido incluye todo lo del documento 1, MÁS:
- ✅ Diagramas detallados de arquitectura
- ✅ Análisis profundo de cada página React
- ✅ Componentes individuales explicados
- ✅ Servicios Frontend (transbank.js, api.js)
- ✅ Loaders de datos con React Router
- ✅ Flujo completo de compra paso a paso
- ✅ Integración con Transbank (3 pasos)
- ✅ Testing (Jasmine + Karma)
- ✅ Deployment en AWS

**Ideal para:** Desarrolladores que necesitan entender componentes específicos

---

### 3️⃣ **ANALISIS_CONCEPTUAL_COMPLETO_HUERTO_HOGAR.docx** (40 KB)
**Versión Final - Completa y técnica**

Contenido:
- ✅ Resumen ejecutivo
- ✅ Tecnologías utilizadas
- ✅ **Diagramas ASCII de arquitectura**
- ✅ **Diagramas de flujo de datos**
- ✅ **Modelo relacional de BD completo**
- ✅ **Ejemplos de código Java y React**
- ✅ **Código ProductService.updateStock()**
- ✅ **Código CartContext.addToCart()**
- ✅ **Código SaleService.iniciarVenta()**
- ✅ Buenas prácticas implementadas
- ✅ Conclusiones finales

**Ideal para:** Ingenieros de software, code review, documentación técnica

---

## 🎯 Recomendaciones de Lectura

**Si eres estudiante/principiante:** 
→ Lee primero el documento **#1** para entender la estructura general

**Si eres desarrollador:**
→ Lee el documento **#2** para ver componentes y servicios específicos

**Si necesitas referencia técnica completa:**
→ Usa el documento **#3** con diagramas y ejemplos de código

---

## 📊 Comparativa de Documentos

| Aspecto | Doc 1 | Doc 2 | Doc 3 |
|--------|-------|-------|-------|
| Introducción | ✅ | ✅ | ✅ |
| Arquitectura | ✅ | ✅✅ | ✅✅✅ |
| Componentes React | ✅ | ✅✅✅ | ✅✅ |
| Código fuente | - | - | ✅✅✅ |
| Diagramas | - | ✅ | ✅✅ |
| Flujos detallados | ✅ | ✅✅ | ✅✅ |
| Integración Transbank | ✅ | ✅✅ | ✅ |
| Testing | - | ✅ | ✅ |
| Deployment | - | ✅ | ✅ |

---

## 📝 Qué Explican los Documentos

### **Backend - Microservicio de Productos**
```
ProductService.findAll()     → Obtiene todos los productos con paginación
ProductService.findByCodigo() → Busca por código único
ProductService.updateStock()  → Actualiza stock después de venta
```

### **Backend - Microservicio de Usuarios**
```
UserService.register()      → Registra nuevo usuario (encripta contraseña)
UserService.login()         → Autentica y emite JWT
UserService.updateProfile() → Actualiza perfil del usuario
JwtUtil.generateToken()     → Crea tokens JWT seguros
```

### **Backend - Microservicio de Ventas**
```
SaleService.iniciarVenta()  → Crea venta, valida stock, contacta Transbank
SaleService.confirmarVenta() → Confirma pago, actualiza stock
ProductApiService          → Comunicación con servicio de Productos
```

### **Frontend - React Context API**
```
AuthContext.login()         → Login de usuario
AuthContext.register()      → Registro de usuario
CartContext.addToCart()     → Agrega producto al carrito
CartContext.getTotal()      → Calcula total de compra
```

### **Frontend - Componentes**
```
CheckoutForm               → Captura datos de envío
productsLoader()           → Carga productos para página /productos
productDetailLoader()      → Carga detalles de un producto
TransbankSuccess           → Maneja respuesta de pago
```

---

## 🔍 Buscar en los Documentos

Para encontrar información específica, busca por:

**Backend:**
- "ProductService"
- "UserService"
- "SaleService"
- "@PostMapping"
- "@GetMapping"

**Frontend:**
- "AuthContext"
- "CartContext"
- "useCart()"
- "useAuth()"
- "CheckoutForm"

**Flujos:**
- "Flujo de"
- "Paso"
- "Usuario"

**Seguridad:**
- "JWT"
- "Encriptación"
- "Validación"

---

## 💡 Conceptos Clave Explicados

### ✅ Microservicios
Explicación de por qué se dividió en 3 servicios independientes, ventajas de escalabilidad.

### ✅ Context API
Cómo React maneja estado global sin props drilling.

### ✅ JWT (JSON Web Tokens)
Sistema de autenticación seguro sin sesiones de servidor.

### ✅ DTOs (Data Transfer Objects)
Por qué se usan para separar modelo de BD de lo que expone la API.

### ✅ Repository Pattern
Abstracción de acceso a datos con Spring Data JPA.

### ✅ Transbank Integration
Flujo completo de pago: crear transacción → usuario paga → confirmar en backend.

### ✅ React Router
Sistema de rutas, loaders de datos, navegación SPA.

### ✅ PostgreSQL Relaciones
Cómo se relacionan las tablas: products ↔ saledetail ↔ sales ↔ users.

---

## 🎓 Usar estos Documentos para

- **Estudios académicos** → Entender arquitectura de e-commerce
- **Entrevistas de trabajo** → Explicar componentes del proyecto
- **Code review** → Verificar que código sigue prácticas documentadas
- **Onboarding de nuevos desarrolladores** → Guía completa del proyecto
- **Documentación** → Base para documentación más formal
- **Presentaciones** → Usar diagramas como base

---

## 📞 Notas Técnicas

**Tecnologías:**
- Frontend: React 19, Vite, React Router 7, Bootstrap 5, Context API
- Backend: Spring Boot 4, Java 17, PostgreSQL
- Pagos: Transbank WebPay Plus
- Infraestructura: AWS EC2, Docker (opcional)

**Puertos:**
- Productos: 8080
- Ventas: 8081
- Usuarios: 8082
- Frontend: 3000 (desarrollo)

**URLs Base:**
- Frontend: http://localhost:5173 (Vite dev)
- Productos: http://localhost:8080/api/products
- Usuarios: http://localhost:8082/api/auth
- Ventas: http://localhost:8081/api/sales

---

**Generado:** Diciembre 2024
**Versión:** Completa y Exhaustiva
**Formato:** Microsoft Word (.docx)
