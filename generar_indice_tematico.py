#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar un documento Word con índice temático y glosario
"""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def agregar_titulo(doc, titulo, nivel=1):
    p = doc.add_heading(titulo, level=nivel)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)

def agregar_parrafo(doc, texto, bold=False, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(texto)
    run.bold = bold
    run.italic = italic
    p.paragraph_format.space_after = Pt(6)

def crear_indice_tematico():
    doc = Document()
    
    agregar_titulo(doc, "ÍNDICE TEMÁTICO Y GLOSARIO", 0)
    doc.add_paragraph("Referencia rápida para navegar los documentos generados").alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_page_break()
    
    # ========== CONCEPTOS FUNDAMENTALES ==========
    agregar_titulo(doc, "CONCEPTOS FUNDAMENTALES")
    
    conceptos = {
        "Microservicios": 
            "Arquitectura donde la aplicación se divide en servicios independientes pequeños que trabajan juntos. "
            "En este proyecto hay 3: Productos, Usuarios, Ventas.",
        
        "API REST": 
            "Interfaz que permite comunicación entre cliente y servidor usando HTTP. "
            "Cada microservicio expone endpoints REST.",
        
        "JWT (JSON Web Token)":
            "Sistema de autenticación donde el servidor emite un token firmado que contiene la identidad del usuario. "
            "Se usa para mantener sesiones seguras sin almacenar estado en servidor.",
        
        "Context API":
            "Sistema de React para compartir estado global entre componentes sin pasar props manualmente a través "
            "de múltiples niveles (prop drilling).",
        
        "React Router":
            "Librería para manejar rutas en aplicaciones SPA (Single Page Application). Permite navegación sin recargar página.",
        
        "DTOs (Data Transfer Objects)":
            "Objetos que se usan SOLO para transferir datos entre capas. Separan el modelo de BD del API.",
        
        "Repository Pattern":
            "Patrón que abstrae la lógica de acceso a datos. En lugar de escribir SQL, usamos métodos intuitivos.",
        
        "Spring Boot":
            "Framework Java que facilita crear aplicaciones web. Incluye servidor embebido, configuración automática, etc.",
        
        "PostgreSQL":
            "Base de datos relacional de código abierto. Almacena todos los datos del proyecto.",
        
        "Transbank":
            "Plataforma chilena que procesa pagos con tarjeta de crédito. Integrada para procesar compras.",
    }
    
    for concepto, explicacion in conceptos.items():
        agregar_parrafo(doc, concepto, bold=True)
        agregar_parrafo(doc, f"→ {explicacion}")
    
    doc.add_page_break()
    
    # ========== MICROSERVICIOS ==========
    agregar_titulo(doc, "MICROSERVICIOS EXPLICADOS")
    
    microservicios = {
        "PRODUCTOS (Puerto 8080)": {
            "Responsabilidad": "Gestionar catálogo de productos e inventario",
            "Clases Principales": "ProductService, ProductController, ProductRepository",
            "Métodos Clave": "findAll(), findByCodigo(), updateStock()",
            "BD": "Tabla 'products' con campos: id, codigo, nombre, precio, stock, etc.",
            "Endpoints": "GET /api/products, GET /api/products/{id}, PATCH /api/products/{id}/stock",
        },
        
        "USUARIOS (Puerto 8082)": {
            "Responsabilidad": "Autenticación, registro y gestión de perfil de usuarios",
            "Clases Principales": "UserService, AuthController, JwtUtil, SecurityConfig",
            "Métodos Clave": "login(), register(), updateProfile(), generateToken()",
            "BD": "Tabla 'users' con email, password (encriptado), nombre, apellido, etc.",
            "Endpoints": "POST /api/auth/register, POST /api/auth/login, PATCH /api/auth/profile/{id}",
        },
        
        "VENTAS (Puerto 8081)": {
            "Responsabilidad": "Procesar órdenes de compra, validar stock, integrar con Transbank",
            "Clases Principales": "SaleService, SaleController, ProductApiService",
            "Métodos Clave": "iniciarVenta(), confirmarVenta()",
            "BD": "Tablas 'sales' y 'saledetail' para guardar ordenes e items",
            "Endpoints": "POST /api/sales/init, POST /api/sales/commit, GET /api/sales/products",
        },
    }
    
    for servicio, detalles in microservicios.items():
        agregar_parrafo(doc, servicio, bold=True)
        for key, value in detalles.items():
            agregar_parrafo(doc, f"{key}: {value}")
        doc.add_paragraph()
    
    doc.add_page_break()
    
    # ========== FLUJOS PRINCIPALES ==========
    agregar_titulo(doc, "FLUJOS PRINCIPALES DEL SISTEMA")
    
    flujos = {
        "Login": [
            "1. Usuario accede a /login",
            "2. Ingresa email y contraseña",
            "3. POST /api/auth/login",
            "4. Backend valida credenciales",
            "5. Emite JWT token",
            "6. Frontend guarda token en localStorage",
            "7. Usuario accede a funciones protegidas",
        ],
        
        "Agregar al Carrito": [
            "1. Usuario navega a /productos",
            "2. Ve lista de productos con botón 'Agregar'",
            "3. Clica 'Agregar al carrito'",
            "4. useCart().addToCart() ejecuta",
            "5. CartContext actualiza estado",
            "6. Carrito se guarda en localStorage",
            "7. Contador en header actualiza",
        ],
        
        "Compra Completa": [
            "1. Usuario clica 'Proceder al pago'",
            "2. CheckoutForm modal se abre",
            "3. Usuario completa datos de envío",
            "4. Clica 'Confirmar compra'",
            "5. Frontend envía SaleRequest a /api/sales/init",
            "6. Backend valida stock",
            "7. Backend contacta Transbank",
            "8. Frontend redirige a formulario de Transbank",
            "9. Usuario ingresa datos de tarjeta",
            "10. Transbank procesa y redirige a /checkout-success",
            "11. Frontend confirma con /api/sales/commit",
            "12. Backend actualiza estado a PAGADO",
            "13. Stock se reduce automáticamente",
        ],
    }
    
    for flujo, pasos in flujos.items():
        agregar_parrafo(doc, f"Flujo: {flujo}", bold=True)
        for paso in pasos:
            doc.add_paragraph(paso, style='List Number')
        doc.add_paragraph()
    
    doc.add_page_break()
    
    # ========== COMPONENTES REACT ==========
    agregar_titulo(doc, "COMPONENTES REACT PRINCIPALES")
    
    componentes = {
        "AuthContext.jsx": "Gestiona autenticación global. Métodos: login(), register(), logout().",
        "CartContext.jsx": "Gestiona carrito global. Métodos: addToCart(), removeFromCart(), getTotal().",
        "CheckoutForm.jsx": "Modal para completar compra. Valida datos y envía a /api/sales/init.",
        "Productos.jsx": "Página /productos. Muestra catálogo con paginación y filtros.",
        "DetalleProducto.jsx": "Página /productos/{codigo}. Muestra detalles completos del producto.",
        "Carrito.jsx": "Página /carrito. Muestra items, permite editar cantidades y proceder al pago.",
        "Login.jsx": "Página /login. Formulario para iniciar sesión.",
        "Register.jsx": "Página /register. Formulario para registrar nuevo usuario.",
        "Header.jsx": "Componente superior. Navegación, búsqueda, contador carrito, menú usuario.",
        "Footer.jsx": "Componente inferior. Links, información de contacto.",
    }
    
    for componente, descripcion in componentes.items():
        agregar_parrafo(doc, componente, bold=True)
        agregar_parrafo(doc, descripcion)
    
    doc.add_page_break()
    
    # ========== SERVICIOS JAVA ==========
    agregar_titulo(doc, "SERVICIOS JAVA (@Service)")
    
    servicios = {
        "ProductService": {
            "findAll(categoria, page, size, sortBy)": "Obtiene productos con paginación y filtros",
            "findByCodigo(codigo)": "Busca un producto por código",
            "findById(id)": "Busca un producto por ID",
            "save(product)": "Guarda un nuevo producto",
            "updateStock(id, cantidadVendida)": "Resta cantidad vendida del stock",
        },
        
        "UserService": {
            "register(RegisterRequest)": "Registra nuevo usuario (encripta contraseña)",
            "login(LoginRequest)": "Autentica usuario y emite JWT",
            "updateProfile(id, RegisterRequest)": "Actualiza datos del usuario",
        },
        
        "SaleService": {
            "iniciarVenta(Sale, ProductItems)": "Crea venta, valida stock, contacta Transbank",
            "confirmarVenta(token)": "Confirma pago, actualiza estado y stock",
        },
    }
    
    for servicio, metodos in servicios.items():
        agregar_parrafo(doc, servicio, bold=True)
        for metodo, descripcion in metodos.items():
            agregar_parrafo(doc, f"• {metodo}: {descripcion}")
        doc.add_paragraph()
    
    doc.add_page_break()
    
    # ========== ENDPOINTS API ==========
    agregar_titulo(doc, "ENDPOINTS REST")
    
    endpoints = [
        ("GET", "/api/products", "Obtiene lista de productos con paginación"),
        ("GET", "/api/products/{id}", "Obtiene detalles de un producto por ID"),
        ("GET", "/api/products/codigo/{codigo}", "Obtiene detalles de un producto por código"),
        ("POST", "/api/products", "Crea nuevo producto"),
        ("PATCH", "/api/products/{id}/stock", "Actualiza stock de producto"),
        
        ("POST", "/api/auth/register", "Registra nuevo usuario"),
        ("POST", "/api/auth/login", "Autentica usuario"),
        ("PATCH", "/api/auth/profile/{id}", "Actualiza perfil de usuario"),
        
        ("POST", "/api/sales/init", "Inicia nueva venta y obtiene token de Transbank"),
        ("POST", "/api/sales/commit", "Confirma venta con token de Transbank"),
        ("GET", "/api/sales/products", "Obtiene lista de productos desde ventas"),
    ]
    
    for metodo, endpoint, descripcion in endpoints:
        agregar_parrafo(doc, f"{metodo:6} {endpoint}", bold=True)
        agregar_parrafo(doc, f"→ {descripcion}")
    
    doc.add_page_break()
    
    # ========== TABLAS DATABASE ==========
    agregar_titulo(doc, "ESTRUCTURA BASE DE DATOS")
    
    tablas = {
        "products": {
            "id": "BIGINT PRIMARY KEY AUTO_INCREMENT",
            "codigo": "VARCHAR(50) UNIQUE - Ej: FR001",
            "nombre": "VARCHAR(255) - Nombre del producto",
            "categoria": "VARCHAR(50) - FR (frutas), VR (verduras), ORG (orgánico)",
            "precio": "INTEGER - Precio en pesos chilenos",
            "stock": "INTEGER - Cantidad disponible",
            "origen": "VARCHAR(255) - Lugar procedencia",
            "descripcion": "VARCHAR(1000) - Descripción larga",
            "imagen": "VARCHAR(255) - Ruta imagen",
        },
        
        "users": {
            "id": "BIGINT PRIMARY KEY AUTO_INCREMENT",
            "email": "VARCHAR(255) UNIQUE - Email para login",
            "password": "VARCHAR(255) - Hash BCrypt (ENCRIPTADA)",
            "nombre": "VARCHAR(255)",
            "apellido": "VARCHAR(255)",
            "rut": "VARCHAR(12) - RUT chileno",
            "telefono": "VARCHAR(20)",
            "role": "VARCHAR(50) - CLIENTE",
        },
        
        "sales": {
            "id": "BIGINT PRIMARY KEY AUTO_INCREMENT",
            "fecha": "TIMESTAMP - Fecha creación",
            "total": "INTEGER - Total en pesos",
            "estado": "VARCHAR(50) - PENDIENTE, PAGADO, RECHAZADO",
            "tokenWs": "VARCHAR(255) - Token de Transbank",
            "clienteNombre": "VARCHAR(255) - Nombre cliente",
            "clienteEmail": "VARCHAR(255) - Email cliente",
        },
        
        "saledetail": {
            "id": "BIGINT PRIMARY KEY AUTO_INCREMENT",
            "sale_id": "BIGINT FOREIGN KEY → sales(id)",
            "product_id": "BIGINT FOREIGN KEY → products(id)",
            "cantidad": "INTEGER - Unidades vendidas",
            "precio": "INTEGER - Precio unitario en ese momento",
        },
    }
    
    for tabla, campos in tablas.items():
        agregar_parrafo(doc, f"Tabla: {tabla}", bold=True)
        for campo, tipo in campos.items():
            agregar_parrafo(doc, f"  {campo}: {tipo}")
        doc.add_paragraph()
    
    doc.add_page_break()
    
    # ========== VALIDACIONES ==========
    agregar_titulo(doc, "VALIDACIONES IMPLEMENTADAS")
    
    validaciones = {
        "Frontend - Formulario": [
            "Email debe tener formato válido (@)",
            "Contraseña mínimo 8 caracteres",
            "Contraseña y confirmación deben coincidir",
            "RUT chileno debe ser válido (módulo 11)",
            "Campos requeridos no pueden estar vacíos",
            "Cantidades no pueden ser negativas",
        ],
        
        "Backend - Lógica": [
            "Email debe ser único (sin duplicados)",
            "Stock debe ser suficiente para venta",
            "Contraseña debe coincidir para login",
            "Usuario solo puede acceder sus propios datos",
            "Venta debe estar en estado correcto para confirmar",
            "Token de Transbank debe ser válido",
        ],
        
        "Base de Datos": [
            "Campos NOT NULL tienen restricciones",
            "UNIQUE constraints en email y codigo",
            "FOREIGN KEYs validan referencias",
            "DEFAULT values para fechas automáticas",
        ],
    }
    
    for tipo, items in validaciones.items():
        agregar_parrafo(doc, tipo, bold=True)
        for item in items:
            doc.add_paragraph(f"• {item}", style='List Bullet')
        doc.add_paragraph()
    
    doc.add_page_break()
    
    # ========== SEGURIDAD ==========
    agregar_titulo(doc, "MEDIDAS DE SEGURIDAD")
    
    seguridad = {
        "Encriptación de Contraseñas": 
            "Usamos BCrypt para encriptar. Nunca se guardan en texto plano.",
        
        "JWT Tokens": 
            "Tokens firmados digitalmente que expiran después de 24 horas.",
        
        "Validación en Capas": 
            "Frontend valida para UX. Backend valida por seguridad (nunca confiar en cliente).",
        
        "CORS Configurado": 
            "Solo ciertos orígenes pueden hacer requests (en prod, restringir a dominio específico).",
        
        "Sin Datos Sensibles": 
            "localStorage solo guarda token, no datos sensibles.",
        
        "HTTP/HTTPS": 
            "En producción usar HTTPS obligatorio para todas las comunicaciones.",
    }
    
    for medida, explicacion in seguridad.items():
        agregar_parrafo(doc, medida, bold=True)
        agregar_parrafo(doc, f"→ {explicacion}")
    
    doc.add_page_break()
    
    # ========== CARACTERÍSTICAS ==========
    agregar_titulo(doc, "CARACTERÍSTICAS DEL SISTEMA")
    
    agregar_parrafo(doc, "✅ Catálogo de Productos", bold=True)
    agregar_parrafo(doc, "Productos con paginación (10 por página), filtros por categoría, búsqueda, imágenes.")
    
    agregar_parrafo(doc, "✅ Carrito de Compras", bold=True)
    agregar_parrafo(doc, "Agregar/quitar items, modificar cantidades, cálculo automático de totales con envío y descuentos.")
    
    agregar_parrafo(doc, "✅ Autenticación", bold=True)
    agregar_parrafo(doc, "Registro e login con JWT, perfil de usuario, logout, sesiones persistentes.")
    
    agregar_parrafo(doc, "✅ Checkout", bold=True)
    agregar_parrafo(doc, "Formulario de datos de envío, validación, cálculo de costos.")
    
    agregar_parrafo(doc, "✅ Pagos", bold=True)
    agregar_parrafo(doc, "Integración Transbank, procesamiento seguro, confirmación de pago.")
    
    agregar_parrafo(doc, "✅ Inventario", bold=True)
    agregar_parrafo(doc, "Stock actualiza automáticamente cuando se completa compra.")
    
    agregar_parrafo(doc, "✅ Testing", bold=True)
    agregar_parrafo(doc, "Tests unitarios e integración con Jasmine + Karma.")
    
    # Guardar
    output_path = "INDICE_TEMATICO_Y_GLOSARIO.docx"
    doc.save(output_path)
    print(f"✅ Índice temático generado: {output_path}")
    return output_path

if __name__ == "__main__":
    crear_indice_tematico()
