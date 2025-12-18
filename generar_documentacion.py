#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar documento Word con análisis conceptual completo del proyecto Huerto Hogar
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os
from datetime import datetime

def agregar_titulo_seccion(doc, titulo, nivel=1):
    """Agregar un título de sección"""
    if nivel == 1:
        p = doc.add_heading(titulo, level=1)
    elif nivel == 2:
        p = doc.add_heading(titulo, level=2)
    else:
        p = doc.add_heading(titulo, level=3)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)

def agregar_subtitulo_seccion(doc, titulo):
    """Agregar un subtítulo"""
    p = doc.add_heading(titulo, level=2)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)

def agregar_parrafo(doc, texto, bold=False, italic=False):
    """Agregar un párrafo con formato opcional"""
    p = doc.add_paragraph()
    run = p.add_run(texto)
    run.bold = bold
    run.italic = italic
    p.paragraph_format.space_after = Pt(6)

def agregar_lista_bullets(doc, items):
    """Agregar una lista con bullets"""
    for item in items:
        doc.add_paragraph(item, style='List Bullet')

def agregar_tabla(doc, headers, rows):
    """Agregar una tabla"""
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = 'Light Grid Accent 1'
    
    # Headers
    header_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        header_cells[i].text = header
        # Formatear header
        for paragraph in header_cells[i].paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
        # Color de fondo
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), '366092')
        header_cells[i]._element.get_or_add_tcPr().append(shading_elm)
    
    # Contenido
    for i, row in enumerate(rows, 1):
        cells = table.rows[i].cells
        for j, cell_data in enumerate(row):
            cells[j].text = str(cell_data)

def crear_documento_analisis():
    """Crear el documento Word completo"""
    doc = Document()
    
    # Portada
    title = doc.add_heading('ANÁLISIS CONCEPTUAL COMPLETO', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    subtitle = doc.add_heading('PROYECTO E-COMMERCE "HUERTO HOGAR"', 1)
    subtitle.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph()
    
    fecha = doc.add_paragraph(f'Generado: {datetime.now().strftime("%d de %B de %Y")}')
    fecha.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_page_break()
    
    # Tabla de contenidos
    agregar_titulo_seccion(doc, "TABLA DE CONTENIDOS")
    contenidos = [
        "1. Descripción General del Proyecto",
        "2. Arquitectura del Sistema",
        "3. Microservicios y Componentes",
        "4. Backend - Microservicio de Productos",
        "5. Backend - Microservicio de Usuarios",
        "6. Backend - Microservicio de Ventas",
        "7. Frontend - React y Vite",
        "8. Gestión de Estado y Contextos",
        "9. Flujos de Procesos Principales",
        "10. Métodos y Funciones Detalladas",
        "11. Base de Datos",
        "12. Seguridad y Autenticación",
        "13. Consideraciones Técnicas",
    ]
    for contenido in contenidos:
        doc.add_paragraph(contenido, style='List Number')
    
    doc.add_page_break()
    
    # ========== SECCIÓN 1: DESCRIPCIÓN GENERAL ==========
    agregar_titulo_seccion(doc, "1. DESCRIPCIÓN GENERAL DEL PROYECTO")
    
    agregar_subtitulo_seccion(doc, "¿Qué es Huerto Hogar?")
    agregar_parrafo(doc, 
        "Huerto Hogar es una plataforma e-commerce especializada en la venta de productos agrícolas y "
        "hortícolas de calidad. Funciona como intermediario entre productores locales y consumidores finales, "
        "permitiendo la compra y venta de frutas, verduras y productos orgánicos.")
    
    agregar_subtitulo_seccion(doc, "Objetivos del Proyecto")
    objetivos = [
        "Proporcionar una plataforma accesible para comprar productos de huerto",
        "Conectar productores locales con consumidores finales",
        "Implementar un sistema robusto y escalable con microservicios",
        "Demostrar conocimientos de arquitectura moderna y prácticas de ingeniería de software",
        "Integrar sistemas de pago seguros (Transbank)",
    ]
    agregar_lista_bullets(doc, objetivos)
    
    agregar_subtitulo_seccion(doc, "Stack Tecnológico")
    agregar_parrafo(doc, "Frontend:", bold=True)
    tech_frontend = ["React 19.1.1", "Vite 7.1", "React Router 7.9", "Bootstrap 5.3", "Context API"]
    agregar_lista_bullets(doc, tech_frontend)
    
    agregar_parrafo(doc, "Backend:", bold=True)
    tech_backend = [
        "Spring Boot 4.0.0 (3 microservicios)",
        "Java 17",
        "PostgreSQL (Base de datos)",
        "Transbank WebPay Plus (Pagos)",
        "Maven (Gestión de dependencias)",
    ]
    agregar_lista_bullets(doc, tech_backend)
    
    agregar_parrafo(doc, "Infraestructura:", bold=True)
    tech_infra = ["AWS EC2", "Docker (opcional)", "Nginx/Apache"]
    agregar_lista_bullets(doc, tech_infra)
    
    doc.add_page_break()
    
    # ========== SECCIÓN 2: ARQUITECTURA ==========
    agregar_titulo_seccion(doc, "2. ARQUITECTURA DEL SISTEMA")
    
    agregar_subtitulo_seccion(doc, "Visión General")
    agregar_parrafo(doc, 
        "El proyecto utiliza una arquitectura de MICROSERVICIOS, donde cada función principal se ejecuta "
        "en un servicio independiente que se comunica con otros a través de APIs REST HTTP/JSON.")
    
    agregar_subtitulo_seccion(doc, "Componentes Principales")
    
    agregar_parrafo(doc, "1. Frontend (React + Vite)", bold=True)
    agregar_parrafo(doc, 
        "Aplicación SPA (Single Page Application) que corre en el navegador del usuario. Responsable de "
        "la interfaz de usuario y la experiencia del cliente.")
    
    agregar_parrafo(doc, "2. Microservicio de Productos (Puerto 8080)", bold=True)
    agregar_parrafo(doc, 
        "Gestiona el catálogo de productos, inventario y stock. Responde a consultas sobre productos disponibles.")
    
    agregar_parrafo(doc, "3. Microservicio de Usuarios (Puerto 8082)", bold=True)
    agregar_parrafo(doc, 
        "Maneja autenticación, registro y perfiles de usuarios. Emite tokens JWT para sesiones seguras.")
    
    agregar_parrafo(doc, "4. Microservicio de Ventas (Puerto 8081)", bold=True)
    agregar_parrafo(doc, 
        "Procesa órdenes de compra, coordina con Transbank para pagos, y actualiza inventario.")
    
    agregar_parrafo(doc, "5. Base de Datos PostgreSQL", bold=True)
    agregar_parrafo(doc, 
        "Almacena toda la información persistente del sistema: productos, usuarios y ventas.")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 3: MICROSERVICIOS ==========
    agregar_titulo_seccion(doc, "3. MICROSERVICIOS Y COMPONENTES")
    
    agregar_subtitulo_seccion(doc, "¿Por qué Microservicios?")
    ventajas = [
        "Escalabilidad: Cada servicio puede escalar independientemente según su demanda",
        "Mantenibilidad: Código separado y organizado por dominio de negocio",
        "Flexibilidad: Actualizar un servicio sin afectar a otros",
        "Resiliencia: Si un servicio falla, los otros continúan funcionando",
        "Despliegue independiente: Cada equipo puede desplegar su servicio por separado",
    ]
    agregar_lista_bullets(doc, ventajas)
    
    agregar_subtitulo_seccion(doc, "Comunicación entre Microservicios")
    agregar_parrafo(doc, 
        "Los microservicios se comunican mediante APIs REST HTTP/JSON. Por ejemplo, el microservicio de "
        "ventas necesita consultar productos disponibles, por lo que hace una llamada HTTP GET al "
        "microservicio de productos para validar que haya stock antes de crear la venta.")
    
    agregar_subtitulo_seccion(doc, "URLs de los Microservicios")
    urls = [
        ["Microservicio", "Puerto", "URL"],
        ["Productos", "8080", "http://localhost:8080/api/products"],
        ["Usuarios", "8082", "http://localhost:8082/api/auth"],
        ["Ventas", "8081", "http://localhost:8081/api/sales"],
    ]
    agregar_tabla(doc, urls[0], urls[1:])
    
    doc.add_page_break()
    
    # ========== SECCIÓN 4: BACKEND - PRODUCTOS ==========
    agregar_titulo_seccion(doc, "4. BACKEND - MICROSERVICIO DE PRODUCTOS")
    
    agregar_subtitulo_seccion(doc, "Propósito")
    agregar_parrafo(doc, 
        "Este microservicio es responsable de gestionar el catálogo de productos, disponibilidad de stock "
        "y detalles de cada artículo vendido en Huerto Hogar.")
    
    agregar_subtitulo_seccion(doc, "Modelo de Datos: Entidad Product")
    agregar_parrafo(doc, "La entidad Product representa cada artículo disponible en la tienda:", italic=True)
    
    propiedades_product = [
        ["Propiedad", "Tipo", "Descripción"],
        ["id", "Long", "Identificador único (generado automáticamente)"],
        ["codigo", "String", "Código único del producto (ej: FR001 para Frutas)"],
        ["nombre", "String", "Nombre del producto (ej: Manzana Roja)"],
        ["categoria", "String", "Categoría (FR=Frutas, VR=Verduras, ORG=Orgánicos)"],
        ["precio", "Integer", "Precio en pesos chilenos"],
        ["stock", "Integer", "Cantidad disponible en inventario"],
        ["origen", "String", "Lugar de procedencia del producto"],
        ["descripcion", "String", "Descripción larga del producto"],
        ["imagen", "String", "Ruta de la imagen del producto"],
    ]
    agregar_tabla(doc, propiedades_product[0], propiedades_product[1:])
    
    agregar_subtitulo_seccion(doc, "Clase ProductService - Métodos Principales")
    
    metodos_product_service = [
        {
            "nombre": "findAll()",
            "parametros": "categoria (opcional), page, size, sortBy",
            "retorna": "Page<Product>",
            "descripcion": "Obtiene todos los productos con paginación y filtros. Permite filtrar por categoría y ordenar por diferentes campos.",
        },
        {
            "nombre": "findByCodigo()",
            "parametros": "codigo: String",
            "retorna": "Optional<Product>",
            "descripcion": "Busca un producto específico por su código único.",
        },
        {
            "nombre": "findById()",
            "parametros": "id: Long",
            "retorna": "Optional<Product>",
            "descripcion": "Busca un producto por su ID de base de datos.",
        },
        {
            "nombre": "save()",
            "parametros": "product: Product",
            "retorna": "Product",
            "descripcion": "Guarda un nuevo producto o actualiza uno existente en la BD.",
        },
        {
            "nombre": "updateStock()",
            "parametros": "id: Long, cantidadVendida: Integer",
            "retorna": "Optional<Product>",
            "descripcion": "Resta la cantidad vendida del stock disponible. Se llama después de una compra exitosa.",
        },
    ]
    
    for metodo in metodos_product_service:
        agregar_parrafo(doc, f"• {metodo['nombre']}", bold=True)
        agregar_parrafo(doc, f"Parámetros: {metodo['parametros']}")
        agregar_parrafo(doc, f"Retorna: {metodo['retorna']}")
        agregar_parrafo(doc, f"Descripción: {metodo['descripcion']}")
    
    agregar_subtitulo_seccion(doc, "Clase ProductController - Endpoints REST")
    agregar_parrafo(doc, "El controlador expone los siguientes endpoints HTTP:")
    
    endpoints_products = [
        {
            "metodo": "GET",
            "endpoint": "/api/products",
            "parametros": "?categoria=FR&page=0&size=10&sortBy=nombre",
            "descripcion": "Obtiene lista de productos con paginación y filtros",
        },
        {
            "metodo": "GET",
            "endpoint": "/api/products/codigo/{codigo}",
            "parametros": "ej: /api/products/codigo/FR001",
            "descripcion": "Obtiene detalle completo de un producto por código",
        },
        {
            "metodo": "GET",
            "endpoint": "/api/products/{id}",
            "parametros": "ej: /api/products/1",
            "descripcion": "Obtiene detalle de un producto por ID",
        },
        {
            "metodo": "POST",
            "endpoint": "/api/products",
            "parametros": "Body JSON con datos del producto",
            "descripcion": "Crea un nuevo producto (uso administrativo)",
        },
        {
            "metodo": "PATCH",
            "endpoint": "/api/products/{id}/stock",
            "parametros": "Body: {\"cantidadVendida\": 5}",
            "descripcion": "Actualiza el stock después de una venta",
        },
    ]
    
    for ep in endpoints_products:
        agregar_parrafo(doc, f"{ep['metodo']} {ep['endpoint']}", bold=True)
        agregar_parrafo(doc, f"Parámetros: {ep['parametros']}")
        agregar_parrafo(doc, f"Descripción: {ep['descripcion']}")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 5: BACKEND - USUARIOS ==========
    agregar_titulo_seccion(doc, "5. BACKEND - MICROSERVICIO DE USUARIOS")
    
    agregar_subtitulo_seccion(doc, "Propósito")
    agregar_parrafo(doc, 
        "Gestiona la autenticación de usuarios, registro, perfiles y emisión de tokens JWT para "
        "mantener sesiones seguras.")
    
    agregar_subtitulo_seccion(doc, "Modelo de Datos: Entidad User")
    
    propiedades_user = [
        ["Propiedad", "Tipo", "Descripción"],
        ["id", "Long", "Identificador único"],
        ["email", "String", "Email único para login"],
        ["password", "String", "Contraseña encriptada (hash)"],
        ["nombre", "String", "Nombre del usuario"],
        ["apellido", "String", "Apellido del usuario"],
        ["rut", "String", "RUT chileno del usuario"],
        ["telefono", "String", "Teléfono de contacto"],
        ["role", "String", "Rol del usuario (CLIENTE)"],
    ]
    agregar_tabla(doc, propiedades_user[0], propiedades_user[1:])
    
    agregar_subtitulo_seccion(doc, "Clase UserService - Métodos Principales")
    
    metodos_user_service = [
        {
            "nombre": "register()",
            "parametros": "RegisterRequest (email, password, nombre, apellido, rut)",
            "retorna": "UserResponse con token JWT",
            "descripcion": "Registra un nuevo usuario. Encripta la contraseña antes de guardar en BD. Emite token JWT automáticamente.",
        },
        {
            "nombre": "login()",
            "parametros": "LoginRequest (email, password)",
            "retorna": "UserResponse con token JWT",
            "descripcion": "Autentica un usuario existente comparando la contraseña con el hash guardado. Emite token JWT.",
        },
        {
            "nombre": "updateProfile()",
            "parametros": "id: Long, RegisterRequest con campos a actualizar",
            "retorna": "UserResponse con token JWT",
            "descripcion": "Actualiza perfil del usuario (nombre, apellido, contraseña, etc).",
        },
    ]
    
    for metodo in metodos_user_service:
        agregar_parrafo(doc, f"• {metodo['nombre']}", bold=True)
        agregar_parrafo(doc, f"Parámetros: {metodo['parametros']}")
        agregar_parrafo(doc, f"Retorna: {metodo['retorna']}")
        agregar_parrafo(doc, f"Descripción: {metodo['descripcion']}")
    
    agregar_subtitulo_seccion(doc, "Seguridad: JWT (JSON Web Tokens)")
    agregar_parrafo(doc, 
        "JWT es un estándar de seguridad que permite crear tokens firmados digitalmente. Cuando un usuario "
        "se registra o loguea, el backend emite un token único que contiene su identidad encriptada. "
        "Este token se guarda en el cliente (localStorage) y se envía en cada solicitud que requiere autenticación.")
    
    agregar_subtitulo_seccion(doc, "Clase JwtUtil - Generación de Tokens")
    agregar_parrafo(doc, "Método: generateToken(email: String)")
    agregar_parrafo(doc, 
        "Crea un token JWT firmado con HMAC-SHA512. El token contiene: el email del usuario, "
        "fecha de emisión, fecha de expiración (generalmente 24 horas) y una firma digital que "
        "verifica la autenticidad.")
    
    agregar_subtitulo_seccion(doc, "Endpoints de Autenticación")
    
    endpoints_auth = [
        {
            "metodo": "POST",
            "endpoint": "/api/auth/register",
            "body": "{ email, password, nombre, apellido, rut }",
            "descripcion": "Registra nuevo usuario",
        },
        {
            "metodo": "POST",
            "endpoint": "/api/auth/login",
            "body": "{ email, password }",
            "descripcion": "Autentica usuario existente",
        },
        {
            "metodo": "PATCH",
            "endpoint": "/api/auth/profile/{id}",
            "body": "{ nombre, apellido, password, rut }",
            "descripcion": "Actualiza perfil del usuario",
        },
    ]
    
    for ep in endpoints_auth:
        agregar_parrafo(doc, f"{ep['metodo']} {ep['endpoint']}", bold=True)
        agregar_parrafo(doc, f"Body JSON: {ep['body']}")
        agregar_parrafo(doc, f"Descripción: {ep['descripcion']}")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 6: BACKEND - VENTAS ==========
    agregar_titulo_seccion(doc, "6. BACKEND - MICROSERVICIO DE VENTAS")
    
    agregar_subtitulo_seccion(doc, "Propósito")
    agregar_parrafo(doc, 
        "Gestiona el proceso completo de compra: recibe órdenes, coordina con el servicio de productos "
        "para verificar stock, integra con Transbank para procesar pagos y actualiza el inventario.")
    
    agregar_subtitulo_seccion(doc, "Modelos de Datos")
    
    agregar_parrafo(doc, "1. Entidad Sale (Venta)", bold=True)
    propiedades_sale = [
        ["Propiedad", "Tipo", "Descripción"],
        ["id", "Long", "ID único de la venta"],
        ["fecha", "LocalDateTime", "Fecha y hora de creación"],
        ["total", "Integer", "Total de la compra en pesos"],
        ["estado", "String", "Estado: PENDIENTE, PAGADO, RECHAZADO"],
        ["tokenWs", "String", "Token de Transbank para el pago"],
        ["clienteNombre", "String", "Nombre del cliente"],
        ["clienteEmail", "String", "Email del cliente"],
        ["detalles", "List<SaleDetail>", "Items de la venta (relación 1:N)"],
    ]
    agregar_tabla(doc, propiedades_sale[0], propiedades_sale[1:])
    
    agregar_parrafo(doc, "2. Entidad SaleDetail (Detalle de Venta)", bold=True)
    propiedades_saledetail = [
        ["Propiedad", "Tipo", "Descripción"],
        ["id", "Long", "ID único"],
        ["sale", "Sale", "Referencia a la venta principal"],
        ["product", "Product", "Referencia al producto"],
        ["cantidad", "Integer", "Cantidad de unidades"],
        ["precio", "Integer", "Precio unitario al momento de la compra"],
    ]
    agregar_tabla(doc, propiedades_saledetail[0], propiedades_saledetail[1:])
    
    agregar_subtitulo_seccion(doc, "Clase SaleService - Métodos Principales")
    
    metodos_sale_service = [
        {
            "nombre": "iniciarVenta()",
            "parametros": "Sale, List<ProductItem>",
            "retorna": "Map con token y URL de Transbank",
            "descripcion": "Inicia una nueva venta. Valida stock, crea registro en BD, contacta a Transbank para obtener URL de pago y retorna token para redirigir al cliente.",
        },
        {
            "nombre": "confirmarVenta()",
            "parametros": "token: String (token de Transbank)",
            "retorna": "Sale actualizada con estado",
            "descripcion": "Confirma que el pago fue procesado exitosamente. Cambia estado de venta a PAGADO/RECHAZADO y actualiza stock de productos.",
        },
    ]
    
    for metodo in metodos_sale_service:
        agregar_parrafo(doc, f"• {metodo['nombre']}", bold=True)
        agregar_parrafo(doc, f"Parámetros: {metodo['parametros']}")
        agregar_parrafo(doc, f"Retorna: {metodo['retorna']}")
        agregar_parrafo(doc, f"Descripción: {metodo['descripcion']}")
    
    agregar_subtitulo_seccion(doc, "Clase ProductApiService - Comunicación con Microservicio de Productos")
    agregar_parrafo(doc, 
        "Este servicio hace llamadas HTTP REST al microservicio de Productos para verificar stock "
        "y actualizar el inventario cuando se completa una venta.")
    
    metodos_product_api = [
        "obtenerProductoPorCodigo(codigo): Obtiene detalles de un producto",
        "obtenerTodosLosProductos(): Obtiene lista completa de productos",
        "actualizarStock(codigo, nuevoStock): Actualiza el stock disponible",
    ]
    agregar_lista_bullets(doc, metodos_product_api)
    
    agregar_subtitulo_seccion(doc, "Endpoints de Ventas")
    
    endpoints_sales = [
        {
            "metodo": "POST",
            "endpoint": "/api/sales/init",
            "descripcion": "Inicia una nueva venta. Retorna token y URL de Transbank.",
        },
        {
            "metodo": "POST",
            "endpoint": "/api/sales/commit",
            "descripcion": "Confirma que el pago fue procesado exitosamente.",
        },
        {
            "metodo": "GET",
            "endpoint": "/api/sales/products",
            "descripcion": "Lista todos los productos disponibles.",
        },
    ]
    
    for ep in endpoints_sales:
        agregar_parrafo(doc, f"{ep['metodo']} {ep['endpoint']}", bold=True)
        agregar_parrafo(doc, f"Descripción: {ep['descripcion']}")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 7: FRONTEND - REACT ==========
    agregar_titulo_seccion(doc, "7. FRONTEND - REACT Y VITE")
    
    agregar_subtitulo_seccion(doc, "¿Qué es React?")
    agregar_parrafo(doc, 
        "React es una librería de JavaScript que permite construir interfaces de usuario interactivas "
        "de forma eficiente. Utiliza el concepto de 'componentes' reutilizables y manejo reactivo de estado.")
    
    agregar_subtitulo_seccion(doc, "¿Qué es Vite?")
    agregar_parrafo(doc, 
        "Vite es un bundler y servidor de desarrollo moderno que ofrece:\n"
        "• Inicio rápido del servidor de desarrollo\n"
        "• Hot Module Replacement (HMR) para actualizaciones en tiempo real\n"
        "• Bundling optimizado para producción\n"
        "• Carga rápida de módulos ES6")
    
    agregar_subtitulo_seccion(doc, "Estructura del Frontend")
    estructura_frontend = [
        "src/main.jsx: Punto de entrada de la aplicación",
        "src/routes.jsx: Definición de rutas con React Router",
        "src/context/: Contextos para estado global (Auth, Cart)",
        "src/pages/: Páginas principales de la aplicación",
        "src/components/: Componentes reutilizables",
        "src/services/: Servicios para llamadas a APIs",
        "src/loaders/: Funciones de carga de datos para rutas",
        "src/config/api.js: Configuración centralizada de URLs de microservicios",
        "src/utils/: Utilidades y funciones auxiliares",
    ]
    agregar_lista_bullets(doc, estructura_frontend)
    
    agregar_subtitulo_seccion(doc, "Páginas Principales")
    
    paginas = [
        {
            "nombre": "Home",
            "ruta": "/",
            "descripcion": "Página inicial con banner, productos destacados y información general.",
        },
        {
            "nombre": "Productos",
            "ruta": "/productos",
            "descripcion": "Catálogo completo con paginación, filtros por categoría y búsqueda.",
        },
        {
            "nombre": "Detalle Producto",
            "ruta": "/productos/:id",
            "descripcion": "Página detallada de un producto con descripción completa, precio y botón agregar al carrito.",
        },
        {
            "nombre": "Carrito",
            "ruta": "/carrito",
            "descripcion": "Vista del carrito de compras con listado de items, cantidades y totales.",
        },
        {
            "nombre": "Checkout",
            "ruta": "Modal dentro de /carrito",
            "descripcion": "Formulario para completar compra, dirección de envío e información de pago.",
        },
        {
            "nombre": "Login",
            "ruta": "/login",
            "descripcion": "Formulario para iniciar sesión con email y contraseña.",
        },
        {
            "nombre": "Register",
            "ruta": "/register",
            "descripcion": "Formulario para registrar nuevo usuario.",
        },
        {
            "nombre": "Blog",
            "ruta": "/blog",
            "descripcion": "Artículos y consejos sobre productos y jardinería.",
        },
        {
            "nombre": "Contacto",
            "ruta": "/contacto",
            "descripcion": "Formulario para contactar al equipo de soporte.",
        },
    ]
    
    for pagina in paginas:
        agregar_parrafo(doc, f"• {pagina['nombre']}", bold=True)
        agregar_parrafo(doc, f"Ruta: {pagina['ruta']}")
        agregar_parrafo(doc, f"Descripción: {pagina['descripcion']}")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 8: GESTIÓN DE ESTADO ==========
    agregar_titulo_seccion(doc, "8. GESTIÓN DE ESTADO Y CONTEXTOS")
    
    agregar_subtitulo_seccion(doc, "¿Por qué Contextos?")
    agregar_parrafo(doc, 
        "React proporciona Context API para compartir estado global sin tener que pasar props a través "
        "de múltiples niveles de componentes. Usamos dos contextos principales: AuthContext y CartContext.")
    
    agregar_subtitulo_seccion(doc, "AuthContext - Gestión de Autenticación")
    agregar_parrafo(doc, "Responsabilidades:", bold=True)
    auth_responsabilidades = [
        "Mantener estado del usuario autenticado",
        "Gestionar token JWT",
        "Proporcionar métodos login(), register(), logout()",
        "Persistir sesión en localStorage",
        "Validar autenticación en rutas protegidas",
    ]
    agregar_lista_bullets(doc, auth_responsabilidades)
    
    agregar_parrafo(doc, "Métodos principales:", bold=True)
    metodos_auth = [
        {
            "nombre": "register(datosRegistro)",
            "descripcion": "Registra nuevo usuario llamando a /api/auth/register, guarda token en localStorage",
        },
        {
            "nombre": "login(email, password)",
            "descripcion": "Autentica usuario llamando a /api/auth/login, guarda token y datos en localStorage",
        },
        {
            "nombre": "logout()",
            "descripcion": "Limpia localStorage, cierra sesión del usuario",
        },
        {
            "nombre": "getDatosCheckout()",
            "descripcion": "Retorna datos del usuario para pre-llenar formulario de checkout",
        },
    ]
    
    for metodo in metodos_auth:
        agregar_parrafo(doc, f"• {metodo['nombre']}")
        agregar_parrafo(doc, f"  {metodo['descripcion']}")
    
    agregar_subtitulo_seccion(doc, "CartContext - Gestión del Carrito")
    agregar_parrafo(doc, "Responsabilidades:", bold=True)
    cart_responsabilidades = [
        "Mantener lista de items en el carrito",
        "Persistir carrito en localStorage",
        "Calcular totales y cantidades",
        "Agregar/quitar/actualizar items",
    ]
    agregar_lista_bullets(doc, cart_responsabilidades)
    
    agregar_parrafo(doc, "Métodos principales:", bold=True)
    metodos_cart = [
        {
            "nombre": "addToCart(producto, cantidad)",
            "descripcion": "Agrega un producto al carrito o incrementa su cantidad si ya existe",
        },
        {
            "nombre": "removeFromCart(codigo)",
            "descripcion": "Remueve un producto del carrito completamente",
        },
        {
            "nombre": "updateQuantity(codigo, cantidad)",
            "descripcion": "Actualiza la cantidad de un producto",
        },
        {
            "nombre": "clearCart()",
            "descripcion": "Vacía completamente el carrito",
        },
        {
            "nombre": "getTotal()",
            "descripcion": "Calcula el total de la compra",
        },
        {
            "nombre": "getItemCount()",
            "descripcion": "Calcula la cantidad total de items",
        },
    ]
    
    for metodo in metodos_cart:
        agregar_parrafo(doc, f"• {metodo['nombre']}")
        agregar_parrafo(doc, f"  {metodo['descripcion']}")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 9: FLUJOS DE PROCESOS ==========
    agregar_titulo_seccion(doc, "9. FLUJOS DE PROCESOS PRINCIPALES")
    
    agregar_subtitulo_seccion(doc, "Flujo 1: Registro de Usuario")
    agregar_parrafo(doc, "Paso a Paso:", bold=True)
    flujo_registro = [
        "1. Usuario completa formulario de registro en página /register",
        "2. Frontend valida datos localmente (email, contraseña fuerte, etc)",
        "3. Se envía POST request a /api/auth/register con datos",
        "4. Backend valida que email no exista, encripta contraseña",
        "5. Backend guarda usuario en BD PostgreSQL",
        "6. Backend emite token JWT y lo retorna",
        "7. Frontend guarda token y datos de usuario en localStorage",
        "8. Usuario es redirigido a página principal (autenticado)",
    ]
    agregar_lista_bullets(doc, flujo_registro)
    
    agregar_subtitulo_seccion(doc, "Flujo 2: Login de Usuario")
    agregar_parrafo(doc, "Paso a Paso:", bold=True)
    flujo_login = [
        "1. Usuario ingresa email y contraseña en página /login",
        "2. Se envía POST request a /api/auth/login",
        "3. Backend busca usuario por email",
        "4. Backend compara contraseña ingresada con hash guardado",
        "5. Si coincide, emite token JWT",
        "6. Frontend guarda token en localStorage",
        "7. Usuario accede a todas las funciones autenticadas",
    ]
    agregar_lista_bullets(doc, flujo_login)
    
    agregar_subtitulo_seccion(doc, "Flujo 3: Navegación de Productos")
    agregar_parrafo(doc, "Paso a Paso:", bold=True)
    flujo_productos = [
        "1. Usuario accede a página /productos",
        "2. React Router ejecuta productsLoader() del route",
        "3. productsLoader() hace GET request a /api/products",
        "4. Backend retorna objeto Page con productos paginados",
        "5. Frontend extrae array de productos del objeto Page",
        "6. Componente Producto renderiza lista con grid de items",
        "7. Usuario puede filtrar por categoría (parámetro query)",
        "8. Clicando en producto, navega a /productos/{codigo}",
    ]
    agregar_lista_bullets(doc, flujo_productos)
    
    agregar_subtitulo_seccion(doc, "Flujo 4: Compra Completa (Frontend)")
    agregar_parrafo(doc, "Paso a Paso:", bold=True)
    flujo_compra = [
        "1. Usuario ve productos y clica 'Agregar al carrito'",
        "2. addToCart() agrega item a CartContext",
        "3. CartContext guarda cambios en localStorage",
        "4. Contador en header se actualiza automáticamente",
        "5. Usuario navega a /carrito para revisar items",
        "6. Usuario clica 'Proceder al Pago'",
        "7. Se abre CheckoutForm modal",
        "8. Si está autenticado, formulario se pre-llena con sus datos",
        "9. Usuario revisa dirección, totales (subtotal, descuentos, envío)",
        "10. Usuario clica 'Confirmar Compra'",
    ]
    agregar_lista_bullets(doc, flujo_compra)
    
    agregar_subtitulo_seccion(doc, "Flujo 5: Compra Completa (Backend + Pago)")
    agregar_parrafo(doc, "Paso a Paso:", bold=True)
    flujo_compra_backend = [
        "1. CheckoutForm envía SaleRequest a /api/sales/init",
        "2. Microservicio de Ventas recibe la orden",
        "3. Para cada producto en la orden:",
        "   a. Consulta ProductApiService para obtener detalles",
        "   b. Verifica que haya stock suficiente",
        "   c. Si falta stock, retorna error",
        "4. Si todo valida, crea registro Sale en BD (estado=PENDIENTE)",
        "5. Crea registros SaleDetail para cada item",
        "6. Contacta a Transbank API con monto total",
        "7. Transbank retorna token y URL de formulario de pago",
        "8. Backend retorna token y URL al frontend",
        "9. Frontend crea form HTML con token oculto",
        "10. Frontend redirige automáticamente a Transbank",
        "11. Usuario ingresa datos de tarjeta en formulario de Transbank",
        "12. Transbank procesa pago y redirige a /checkout-success",
        "13. CheckoutSuccess extrae token de URL",
        "14. Llama a /api/sales/commit con token",
        "15. Backend confirma pago con Transbank",
        "16. Si aprobado: actualiza estado=PAGADO, descuenta stock",
        "17. Frontend muestra mensaje de éxito",
        "18. Carrito se vacía automáticamente",
    ]
    agregar_lista_bullets(doc, flujo_compra_backend)
    
    doc.add_page_break()
    
    # ========== SECCIÓN 10: MÉTODOS Y FUNCIONES DETALLADAS ==========
    agregar_titulo_seccion(doc, "10. MÉTODOS Y FUNCIONES DETALLADAS")
    
    agregar_subtitulo_seccion(doc, "Components/Checkout/CheckoutForm.jsx - Función handleSubmit()")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Valida todos los datos del formulario de checkout, prepara la solicitud de venta "
        "y la envía al microservicio de ventas para iniciar el proceso de pago con Transbank.")
    
    agregar_parrafo(doc, "Pasos de ejecución:", bold=True)
    pasos_handlesubmit = [
        "1. Prevenir envío predeterminado del formulario (preventDefault)",
        "2. Validar que todos los campos requeridos estén completos",
        "3. Si hay errores, mostrarlos en el formulario y retornar",
        "4. Establecer isProcessing=true para desactivar botón",
        "5. Preparar objeto SaleRequest con:",
        "   - Nombre cliente concatenado",
        "   - Email del cliente",
        "   - Total final (con envío y descuentos)",
        "   - Array de ProductItem con código, cantidad, precio",
        "6. Hacer POST request a ${SALES_API_URL}/init",
        "7. Si error, mostrar alert y retornar",
        "8. Si exitoso, recibir token y URL de Transbank",
        "9. Crear form HTML invisible con token como campo oculto",
        "10. Hacer submit del form (redirige a Transbank automáticamente)",
    ]
    agregar_lista_bullets(doc, pasos_handlesubmit)
    
    agregar_subtitulo_seccion(doc, "Loaders/products.js - productsLoader()")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Carga la lista de productos desde el backend cuando el usuario navega a /productos. "
        "React Router ejecuta esta función automáticamente y pasa los datos al componente.")
    
    agregar_parrafo(doc, "Pasos de ejecución:", bold=True)
    pasos_productloader = [
        "1. Obtener URL de la solicitud del parámetro request",
        "2. Extraer parámetro 'categoria' de query string si existe",
        "3. Construir URL de fetch con base PRODUCTS_API_URL",
        "4. Si hay categoría seleccionada, agregar ?categoria=XX",
        "5. Hacer GET request al backend",
        "6. Si no es exitoso (response.ok false), lanzar error",
        "7. Convertir respuesta a JSON",
        "8. Extraer array content del objeto Page retornado",
        "9. Retornar objeto { productos } para que React Router lo pase como loader data",
        "10. El componente Producto accede a data via useLoaderData()",
    ]
    agregar_lista_bullets(doc, pasos_productloader)
    
    agregar_subtitulo_seccion(doc, "Services/transbank.js - validarRutChileno()")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Valida que un RUT chileno sea correcto usando el algoritmo de dígito verificador.")
    
    agregar_parrafo(doc, "Lógica:", bold=True)
    agregar_parrafo(doc, 
        "1. Extraer dígito verificador (último dígito)\n"
        "2. Extraer número base (todos excepto último)\n"
        "3. Aplicar algoritmo de módulo 11 al número base\n"
        "4. Calcular dígito verificador esperado\n"
        "5. Comparar con dígito ingresado\n"
        "6. Si coinciden, RUT es válido; si no, es inválido")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 11: BASE DE DATOS ==========
    agregar_titulo_seccion(doc, "11. BASE DE DATOS")
    
    agregar_subtitulo_seccion(doc, "Tipo de Base de Datos")
    agregar_parrafo(doc, 
        "Se utiliza PostgreSQL, una base de datos relacional de código abierto conocida por su "
        "confiabilidad, escalabilidad y cumplimiento de estándares SQL.")
    
    agregar_subtitulo_seccion(doc, "Tablas Principales")
    
    agregar_parrafo(doc, "1. Tabla products", bold=True)
    agregar_parrafo(doc, 
        "Almacena el catálogo de productos. Cada row representa un artículo disponible para comprar. "
        "Incluye campos como código, nombre, precio, stock actual, etc.")
    
    agregar_parrafo(doc, "2. Tabla users", bold=True)
    agregar_parrafo(doc, 
        "Almacena información de usuarios registrados. Incluye email (único), contraseña encriptada, "
        "nombre, apellido, RUT, teléfono y rol.")
    
    agregar_parrafo(doc, "3. Tabla sales", bold=True)
    agregar_parrafo(doc, 
        "Almacena cada compra realizada. Incluye fecha, total, estado (PENDIENTE/PAGADO/RECHAZADO), "
        "token de Transbank, nombre y email del cliente.")
    
    agregar_parrafo(doc, "4. Tabla saledetail", bold=True)
    agregar_parrafo(doc, 
        "Almacena cada línea/item de una venta. Relación muchos-a-uno con sales. "
        "Incluye cantidad, precio unitario, y referencias a sale y product.")
    
    agregar_subtitulo_seccion(doc, "Relaciones entre Tablas")
    
    relaciones = [
        "users (1) ---- (*) sales: Un usuario puede hacer muchas compras",
        "sales (1) ---- (*) saledetail: Una venta tiene muchos items",
        "products (1) ---- (*) saledetail: Un producto puede estar en muchos sales_detail",
    ]
    agregar_lista_bullets(doc, relaciones)
    
    agregar_subtitulo_seccion(doc, "Persistencia de Datos - Spring Data JPA")
    agregar_parrafo(doc, 
        "Los microservicios usan Spring Data JPA para interactuar con PostgreSQL de forma orientada a objetos. "
        "Esto significa que NO escribimos SQL directamente, sino que usamos Repositories que generan las "
        "consultas automáticamente basado en nombres de métodos.")
    
    ejemplo_jpa = [
        "findByCodigo(codigo): Genera SELECT * FROM products WHERE codigo = ?",
        "findByEmail(email): Genera SELECT * FROM users WHERE email = ?",
        "findByEstado(estado): Genera SELECT * FROM sales WHERE estado = ?",
    ]
    agregar_lista_bullets(doc, ejemplo_jpa)
    
    doc.add_page_break()
    
    # ========== SECCIÓN 12: SEGURIDAD ==========
    agregar_titulo_seccion(doc, "12. SEGURIDAD Y AUTENTICACIÓN")
    
    agregar_subtitulo_seccion(doc, "Encriptación de Contraseñas")
    agregar_parrafo(doc, 
        "Las contraseñas NUNCA se guardan en texto plano en la base de datos. Se usan algoritmos "
        "hash criptográficos (BCrypt) para encriptarlas. Cuando un usuario se loguea, la contraseña "
        "ingresada se encripta y se compara con el hash guardado.")
    
    agregar_subtitulo_seccion(doc, "JSON Web Tokens (JWT)")
    agregar_parrafo(doc, 
        "JWT es el mecanismo de autenticación usado. Funciona así:\n"
        "1. Usuario se loguea exitosamente\n"
        "2. Backend emite un JWT firmado digitalmente\n"
        "3. Cliente guarda JWT en localStorage\n"
        "4. En cada solicitud autenticada, cliente envía JWT en header Authorization\n"
        "5. Backend verifica la firma del JWT\n"
        "6. Si es válido y no expiró, acceso permitido")
    
    agregar_subtitulo_seccion(doc, "CORS (Cross-Origin Resource Sharing)")
    agregar_parrafo(doc, 
        "Todos los endpoints Backend tienen @CrossOrigin(origins = \"*\") para permitir solicitudes "
        "desde cualquier origen. En producción, deberías restringir esto a tu dominio específico.")
    
    agregar_subtitulo_seccion(doc, "Validaciones en Frontend")
    agregar_parrafo(doc, 
        "El frontend valida datos antes de enviarlos al backend:\n"
        "• Email debe ser válido (contener @)\n"
        "• Contraseña debe tener mínimo 8 caracteres\n"
        "• RUT debe cumplir formato chileno\n"
        "• Campos requeridos no pueden estar vacíos\n"
        "• Cantidades no pueden ser negativas")
    
    agregar_subtitulo_seccion(doc, "Validaciones en Backend")
    agregar_parrafo(doc, 
        "El backend NO confía en el frontend y valida nuevamente:\n"
        "• Email debe ser único\n"
        "• Stock debe ser suficiente\n"
        "• Usuarios solo pueden acceder a sus propios datos\n"
        "• Transacciones de venta deben ser atómicas")
    
    doc.add_page_break()
    
    # ========== SECCIÓN 13: CONSIDERACIONES TÉCNICAS ==========
    agregar_titulo_seccion(doc, "13. CONSIDERACIONES TÉCNICAS")
    
    agregar_subtitulo_seccion(doc, "Manejo de Errores")
    agregar_parrafo(doc, "Frontend:", bold=True)
    errores_frontend = [
        "Try-catch blocks en funciones async para capturar errores de red",
        "Validación de respuestas HTTP (response.ok)",
        "Mensajes de error legibles para el usuario",
        "Fallback states (ej: loading spinners mientras se carga)",
    ]
    agregar_lista_bullets(doc, errores_frontend)
    
    agregar_parrafo(doc, "Backend:", bold=True)
    errores_backend = [
        "Validación de DTOs (Data Transfer Objects)",
        "Try-catch blocks en servicios",
        "Respuestas HTTP apropiadas (200, 400, 404, 500)",
        "Logging de errores para debugging",
    ]
    agregar_lista_bullets(doc, errores_backend)
    
    agregar_subtitulo_seccion(doc, "Performance")
    agregar_parrafo(doc, 
        "• Paginación: Los productos se cargan de 10 en 10 para evitar cargar 1000s de items\n"
        "• Lazy Loading: Las imágenes se cargan conforme se ven en pantalla\n"
        "• Caching: El carrito y usuario se guardan en localStorage\n"
        "• Compresión: Vite minifica y compresa el código en producción")
    
    agregar_subtitulo_seccion(doc, "Testing")
    agregar_parrafo(doc, 
        "Frontend se testea con Jasmine + Karma:\n"
        "• Unit tests para componentes y servicios\n"
        "• Integration tests para flujos completos\n"
        "• Coverage reports para medir cobertura de tests")
    
    agregar_subtitulo_seccion(doc, "Deployment")
    agregar_parrafo(doc, 
        "Frontend:\n"
        "• Se buildea con vite build (genera carpeta dist/)\n"
        "• Se sirve como archivos estáticos en servidor Nginx\n"
        "\n"
        "Backend:\n"
        "• Se packagea como JAR ejecutable con Maven\n"
        "• Se corre en AWS EC2 como java -jar application.jar\n"
        "• Base de datos PostgreSQL se aloja en AWS RDS")
    
    agregar_subtitulo_seccion(doc, "Mejoras Futuras Sugeridas")
    mejoras = [
        "Implementar WebSockets para notificaciones en tiempo real",
        "Agregar carrito de deseos (wishlist)",
        "Sistema de reviews y ratings de productos",
        "Historial de compras del usuario",
        "Reportes de ventas y analytics",
        "Integración con más pasarelas de pago",
        "Sistema de cupones y promociones",
        "Notificaciones por email",
        "Búsqueda full-text en productos",
        "Integración con redes sociales",
    ]
    agregar_lista_bullets(doc, mejoras)
    
    doc.add_page_break()
    
    # ========== CONCLUSIÓN ==========
    agregar_titulo_seccion(doc, "CONCLUSIÓN")
    
    agregar_parrafo(doc, 
        "Huerto Hogar es un proyecto de e-commerce profesional que demuestra arquitectura moderna con "
        "microservicios, frontend reactivo y prácticas de seguridad. Cada componente está bien organizado, "
        "escalable y mantiene separación de responsabilidades.")
    
    agregar_parrafo(doc, 
        "El flujo de datos es claro: el usuario interactúa con la interfaz React, que se comunica con "
        "tres microservicios Spring Boot independientes. La base de datos PostgreSQL persiste todos los datos, "
        "y la integración con Transbank permite procesar pagos de forma segura.")
    
    agregar_parrafo(doc, 
        "Este documento proporciona una visión conceptual completa del proyecto. Para información "
        "más técnica y específica sobre implementación, referirse al código fuente comentado en el repositorio.")
    
    # Guardar documento
    output_path = "ANALISIS_CONCEPTUAL_HUERTO_HOGAR.docx"
    doc.save(output_path)
    print(f"✅ Documento generado exitosamente: {output_path}")
    return output_path

if __name__ == "__main__":
    crear_documento_analisis()
