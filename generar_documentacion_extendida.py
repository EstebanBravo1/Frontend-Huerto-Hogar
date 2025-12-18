#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script versión mejorada para generar documento Word con análisis conceptual completo
Incluye más detalles de componentes, servicios y flujos técnicos
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

def agregar_codigo_block(doc, codigo, lenguaje=""):
    """Agregar bloque de código"""
    p = doc.add_paragraph(codigo, style='List Paragraph')
    for run in p.runs:
        run.font.name = 'Courier New'
        run.font.size = Pt(9)
    p.paragraph_format.left_indent = Inches(0.5)

def crear_documento_extendido():
    """Crear el documento Word extendido con más contenido"""
    doc = Document()
    
    # Portada
    title = doc.add_heading('ANÁLISIS CONCEPTUAL COMPLETO', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    subtitle = doc.add_heading('PROYECTO E-COMMERCE "HUERTO HOGAR"', 1)
    subtitle.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph()
    
    fecha = doc.add_paragraph(f'Versión Extendida | Generado: {datetime.now().strftime("%d de %B de %Y")}')
    fecha.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph()
    resumen = doc.add_paragraph(
        "Este documento proporciona una guía conceptual exhaustiva del proyecto Huerto Hogar, "
        "explicando todos los métodos, funciones, arquitectura y cómo cada componente trabaja en conjunto "
        "para crear una plataforma de e-commerce moderna y escalable."
    )
    resumen.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    resumen_format = resumen.paragraph_format
    resumen_format.space_before = Pt(12)
    resumen_format.space_after = Pt(12)
    
    doc.add_page_break()
    
    # Tabla de contenidos ampliada
    agregar_titulo_seccion(doc, "TABLA DE CONTENIDOS")
    contenidos = [
        "1. Descripción General del Proyecto",
        "2. Stack Tecnológico y Justificación",
        "3. Arquitectura de Microservicios",
        "4. Microservicio de Productos (Backend)",
        "5. Microservicio de Usuarios (Backend)",
        "6. Microservicio de Ventas (Backend)",
        "7. Frontend: Arquitectura React",
        "8. Gestión de Estado: Contextos",
        "9. Rutas y Navegación",
        "10. Componentes React Principales",
        "11. Servicios Frontend",
        "12. Loaders de Datos",
        "13. Flujos de Procesos Completos",
        "14. Base de Datos y Relaciones",
        "15. Seguridad y Autenticación",
        "16. Integración con Transbank",
        "17. Gestión de Errores",
        "18. Performance y Optimizaciones",
        "19. Testing",
        "20. Deployment y Producción",
        "21. Consideraciones Futuras",
    ]
    for contenido in contenidos:
        doc.add_paragraph(contenido, style='List Number')
    
    doc.add_page_break()
    
    # SECCIÓN EXPANDIDA: Conceptos clave
    agresar_titulo_seccion = agregar_titulo_seccion
    
    agresar_titulo_seccion(doc, "CONCEPTOS CLAVE DEL PROYECTO")
    
    agregar_subtitulo_seccion(doc, "Pattern: Microservicios")
    agregar_parrafo(doc, 
        "En lugar de una aplicación monolítica, el proyecto está dividido en servicios independientes. "
        "Cada microservicio:\n"
        "• Tiene su propia base de datos\n"
        "• Escala independientemente\n"
        "• Se comunica vía HTTP/REST\n"
        "• Puede actualizar sin afectar otros servicios\n"
        "• Tiene lógica de negocio específica")
    
    agregar_subtitulo_seccion(doc, "Pattern: DTO (Data Transfer Objects)")
    agregar_parrafo(doc, 
        "Los DTOs son objetos utilizados para transferir datos entre capas. Ventajas:\n"
        "• Separación entre modelo BD y API\n"
        "• Control de qué datos se exponen\n"
        "• Validación centralizada\n"
        "• Evolución independiente del modelo y API")
    
    agregar_parrafo(doc, "Ejemplo: ProductDetailDTO", bold=True)
    agregar_parrafo(doc, 
        "Frontend recibe ProductDetailDTO (no la entidad Product de BD) para mostrar detalles. "
        "Si más adelante queremos agregar campo a Product sin exponerlo en API, podemos hacerlo "
        "sin afectar clientes.")
    
    agregar_subtitulo_seccion(doc, "Pattern: Repository Pattern")
    agregar_parrafo(doc, 
        "Repositories abstraen la lógica de acceso a datos. En lugar de escribir queries SQL, "
        "usamos métodos intuitivos. Spring Data JPA genera SQL automáticamente.")
    
    doc.add_page_break()
    
    # SECCIÓN: Componentes React detallados
    agresar_titulo_seccion(doc, "10. COMPONENTES REACT PRINCIPALES")
    
    agregar_subtitulo_seccion(doc, "Root Component (pages/root.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Componente raíz que envuelve toda la aplicación. Contiene:\n"
        "• Header (navegación principal)\n"
        "• Outlet (donde se renderiza la página actual)\n"
        "• Footer")
    
    agregar_parrafo(doc, "Características:", bold=True)
    agregar_parrafo(doc, 
        "• Layout consistente para todas las páginas\n"
        "• Header reactivo (muestra usuario si está logueado, icono carrito con contador)\n"
        "• Footer con información y links")
    
    agregar_subtitulo_seccion(doc, "Página Productos (pages/productos/Productos.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Mostrar catálogo de productos con paginación, filtros y búsqueda")
    
    agregar_parrafo(doc, "Flujo:", bold=True)
    flujo_productos_jsx = [
        "1. useLoaderData() obtiene productos del productsLoader",
        "2. productosLoader() hace GET a /api/products",
        "3. Se renderiza grid de ProductCard por cada producto",
        "4. Cada ProductCard muestra: imagen, nombre, precio, stock",
        "5. Botón 'Ver Detalles' navega a /productos/{codigo}",
        "6. Botón 'Agregar al Carrito' llama addToCart() del CartContext",
        "7. Contador en Header actualiza automáticamente via useCart()",
    ]
    agregar_lista_bullets(doc, flujo_productos_jsx)
    
    agregar_subtitulo_seccion(doc, "Página Detalle Producto (pages/detalleproducto/DetalleProducto.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Mostrar información completa de un producto específico")
    
    agregar_parrafo(doc, "Datos mostrados:", bold=True)
    datos_detalle = [
        "Nombre y código del producto",
        "Imagen grande",
        "Descripción completa",
        "Precio unitario",
        "Stock disponible",
        "Origen/procedencia",
        "Categoría",
        "Input para seleccionar cantidad",
        "Botón agregar al carrito",
    ]
    agregar_lista_bullets(doc, datos_detalle)
    
    agregar_subtitulo_seccion(doc, "Página Carrito (pages/carrito/Carrito.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Mostrar items agregados al carrito, permitir modificar cantidades y proceder al pago")
    
    agregar_parrafo(doc, "Elementos:", bold=True)
    elementos_carrito = [
        "Tabla/lista de items con: nombre, precio, cantidad, subtotal",
        "Botones para aumentar/disminuir cantidad",
        "Botones para eliminar item",
        "Cálculo de subtotal",
        "Estimación de envío",
        "Descuentos aplicados",
        "Total final",
        "Botón 'Proceder al Pago' que abre CheckoutForm modal",
        "Botón 'Seguir Comprando' para volver a productos",
    ]
    agregar_lista_bullets(doc, elementos_carrito)
    
    agregar_subtitulo_seccion(doc, "Componente CheckoutForm (components/checkout/CheckoutForm.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Modal que captura información de envío y completa la compra")
    
    agregar_parrafo(doc, "Campos de formulario:", bold=True)
    campos_checkout = [
        "Nombre",
        "Apellidos",
        "RUT (con validación)",
        "Teléfono",
        "Email",
        "Calle y número",
        "Departamento (opcional)",
        "Comuna",
        "Región",
        "Código postal",
        "Indicaciones de entrega",
    ]
    agregar_lista_bullets(doc, campos_checkout)
    
    agregar_parrafo(doc, "Validaciones:", bold=True)
    validaciones_checkout = [
        "Todos campos requeridos están completos",
        "Email tiene formato válido",
        "RUT es válido (dígito verificador correcto)",
        "Teléfono contiene solo números",
    ]
    agregar_lista_bullets(doc, validaciones_checkout)
    
    agregar_parrafo(doc, "Al hacer click 'Confirmar Compra':", bold=True)
    confirmacion_checkout = [
        "1. Se valida el formulario localmente",
        "2. Se prepara SaleRequest con datos del carrito",
        "3. Se envía POST a /api/sales/init",
        "4. Backend retorna token y URL de Transbank",
        "5. Se crea form HTML invisible con token",
        "6. Se hace submit automático (redirige a Transbank)",
        "7. Usuario ve formulario de pago de Transbank",
        "8. Usuario ingresa datos de tarjeta",
        "9. Transbank procesa y redirige a /checkout-success",
    ]
    agregar_lista_bullets(doc, confirmacion_checkout)
    
    agregar_subtitulo_seccion(doc, "Página Login (pages/login/Login.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Permitir que usuarios existentes inicien sesión")
    
    agregar_parrafo(doc, "Flujo:", bold=True)
    flujo_login_jsx = [
        "1. Usuario ingresa email y contraseña",
        "2. Se valida localmente (email válido, password no vacía)",
        "3. Se llama useAuth().login(email, password)",
        "4. Se envía POST a /api/auth/login",
        "5. Backend verifica credenciales",
        "6. Si válidas, retorna token JWT y datos usuario",
        "7. Frontend guarda en localStorage",
        "8. AuthContext se actualiza (isLoggedIn=true, usuario=data)",
        "9. Usuario es redirigido a home",
    ]
    agregar_lista_bullets(doc, flujo_login_jsx)
    
    agregar_subtitulo_seccion(doc, "Página Register (pages/register/Register.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Permitir que nuevos usuarios se registren en el sistema")
    
    agregar_parrafo(doc, "Campos:", bold=True)
    campos_register = [
        "Email",
        "Contraseña",
        "Confirmar contraseña",
        "Nombre",
        "Apellido",
        "RUT",
        "Teléfono (opcional)",
    ]
    agregar_lista_bullets(doc, campos_register)
    
    agregar_parrafo(doc, "Validaciones:", bold=True)
    validaciones_register = [
        "Email no está ya registrado",
        "Contraseña tiene mínimo 8 caracteres",
        "Contraseña y confirmación coinciden",
        "RUT es válido",
    ]
    agregar_lista_bullets(doc, validaciones_register)
    
    agregar_subtitulo_seccion(doc, "Componente Header (components/Header.jsx)")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Barra de navegación principal")
    
    agregar_parrafo(doc, "Elementos:", bold=True)
    elementos_header = [
        "Logo/nombre de la tienda",
        "Barra de búsqueda",
        "Links de navegación (Home, Productos, Blog, Contacto)",
        "Si NO está logueado: botones Login/Register",
        "Si está logueado: nombre usuario, botón Perfil, botón Logout",
        "Icono carrito con contador de items",
    ]
    agregar_lista_bullets(doc, elementos_header)
    
    doc.add_page_break()
    
    # SECCIÓN: Servicios Frontend
    agresar_titulo_seccion(doc, "11. SERVICIOS FRONTEND")
    
    agregar_subtitulo_seccion(doc, "services/transbank.js")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Contiene utilidades relacionadas con pagos y validaciones")
    
    agregar_parrafo(doc, "Funciones:", bold=True)
    funciones_transbank = [
        {
            "nombre": "validarRutChileno(rut)",
            "descripcion": "Valida que un RUT chileno sea correcto usando módulo 11",
        },
        {
            "nombre": "formatearRut(rut)",
            "descripcion": "Formatea RUT agregando puntos y guion (ej: 12.345.678-9)",
        },
        {
            "nombre": "procesarPago(token)",
            "descripcion": "Envía token a backend para confirmar pago con Transbank",
        },
    ]
    
    for func in funciones_transbank:
        agregar_parrafo(doc, f"• {func['nombre']}: {func['descripcion']}")
    
    agregar_subtitulo_seccion(doc, "config/api.js")
    agregar_parrafo(doc, "Propósito:", bold=True)
    agregar_parrafo(doc, 
        "Centralizar configuración de URLs de los microservicios")
    
    agregar_parrafo(doc, "Variables principales:", bold=True)
    agregar_parrafo(doc, "PRODUCTS_API_URL: URL del servicio de productos")
    agregar_parrafo(doc, "SALES_API_URL: URL del servicio de ventas")
    agregar_parrafo(doc, "USERS_API_URL: URL del servicio de usuarios")
    
    agregar_parrafo(doc, "Ventajas:", bold=True)
    ventajas_api_js = [
        "Cambiar URLs sin editar componentes",
        "Fácil cambiar entre desarrollo local y producción",
        "Función fetchWithTimeout() para evitar requests colgadas",
        "Función checkServiceHealth() para verificar disponibilidad",
    ]
    agregar_lista_bullets(doc, ventajas_api_js)
    
    doc.add_page_break()
    
    # SECCIÓN: Loaders
    agresar_titulo_seccion(doc, "12. LOADERS DE DATOS")
    
    agregar_subtitulo_seccion(doc, "¿Qué son los Loaders?")
    agregar_parrafo(doc, 
        "En React Router 6+, los loaders permiten cargar datos ANTES de renderizar la página. "
        "Esto evita el problema de 'loading' en pantalla mientras se obtienen datos.")
    
    agregar_subtitulo_seccion(doc, "loaders/products.js")
    agregar_parrafo(doc, "Función: productsLoader()", bold=True)
    
    agregar_parrafo(doc, "Pasos:", bold=True)
    pasos_productsloader = [
        "1. Se ejecuta cuando usuario navega a /productos",
        "2. Extrae parámetro 'categoria' de URL si existe",
        "3. Construye URL para llamada a API",
        "4. Hace GET request a PRODUCTS_API_URL",
        "5. Verifica que response sea OK (status 200)",
        "6. Convierte response a JSON",
        "7. Extrae array de productos del objeto Page",
        "8. Retorna { productos } que React Router pasa al componente",
        "9. Componente recibe datos via useLoaderData() hook",
    ]
    agregar_lista_bullets(doc, pasos_productsloader)
    
    agregar_subtitulo_seccion(doc, "loaders/productDetail.js")
    agregar_parrafo(doc, "Función: productDetailLoader()", bold=True)
    
    agregar_parrafo(doc, "Pasos:", bold=True)
    pasos_productdetail = [
        "1. Se ejecuta cuando usuario navega a /productos/FR001",
        "2. Extrae código de producto del params (params.id)",
        "3. Hace GET request a ${PRODUCTS_API_URL}/codigo/FR001",
        "4. Si producto no existe, lanza Response con error 404",
        "5. Si existe, convierte a JSON",
        "6. Retorna { producto }",
        "7. Componente recibe datos via useLoaderData()",
    ]
    agregar_lista_bullets(doc, pasos_productdetail)
    
    doc.add_page_break()
    
    # SECCIÓN: Flujos completos ampliados
    agresar_titulo_seccion(doc, "13. FLUJOS DE PROCESOS COMPLETOS")
    
    agregar_subtitulo_seccion(doc, "Flujo Completo: Compra desde Cero")
    agregar_parrafo(doc, "Situación: Usuario nuevo sin cuenta, navega a /productos y compra un item", bold=True)
    
    flujo_compra_completa = [
        "PASO 1: Usuario accede a home",
        "  → React renderiza página home",
        "  → AuthProvider carga token de localStorage (no existe, es nuevo usuario)",
        "  → isLoggedIn = false",
        "",
        "PASO 2: Usuario navega a /productos",
        "  → productsLoader() ejecuta GET /api/products",
        "  → Backend retorna Page con 10 productos",
        "  → Componente Productos renderiza grid de ProductCard",
        "",
        "PASO 3: Usuario clica en un producto",
        "  → Navega a /productos/FR001",
        "  → productDetailLoader() ejecuta GET /api/products/codigo/FR001",
        "  → Componente DetalleProducto muestra información completa",
        "",
        "PASO 4: Usuario selecciona cantidad y clica 'Agregar al Carrito'",
        "  → useCart().addToCart(producto, cantidad) ejecuta",
        "  → CartContext.setCartItems() agrega/actualiza item",
        "  → localStorage.setItem('cart', JSON.stringify(cartItems))",
        "  → Header renderiza y muestra contador = 1",
        "",
        "PASO 5: Usuario navega a /carrito",
        "  → Carrito.jsx obtiene cartItems de useCart()",
        "  → Renderiza tabla con items, cantidades, precios",
        "  → Calcula totales",
        "",
        "PASO 6: Usuario clica 'Proceder al Pago' (sin haber registrado cuenta)",
        "  → CheckoutForm modal se abre",
        "  → Como isLoggedIn=false, formulario no se pre-llena",
        "  → Usuario completa todos los datos manualmente",
        "",
        "PASO 7: Usuario completa datos y clica 'Confirmar Compra'",
        "  → CheckoutForm.handleSubmit() valida campos",
        "  → Prepara SaleRequest",
        "  → POST a /api/sales/init",
        "",
        "PASO 8: Backend recibe SaleRequest",
        "  → Para cada producto en la orden:",
        "    - Consulta ProductApiService",
        "    - Obtiene detalles del producto",
        "    - Valida stock suficiente",
        "  → Si todo OK: crea Sale (estado=PENDIENTE)",
        "  → Crea SaleDetail para cada item",
        "  → Contacta Transbank con monto total",
        "  → Guarda token de Transbank en Sale",
        "  → Retorna token y URL de formulario de pago",
        "",
        "PASO 9: Frontend recibe token y URL",
        "  → Crea form HTML invisible",
        "  → Agrega input oculto con token",
        "  → Hace submit del form",
        "  → Navegador redirige a Transbank",
        "",
        "PASO 10: Usuario en formulario de Transbank",
        "  → Ve monto total y confirma",
        "  → Ingresa datos de tarjeta",
        "  → Selecciona cuotas",
        "  → Clica confirmar",
        "",
        "PASO 11: Transbank procesa pago",
        "  → Valida tarjeta",
        "  → Si OK: aprueba transacción",
        "  → Redirige a /checkout-success con token en URL",
        "",
        "PASO 12: Frontend en /checkout-success",
        "  → TransbankSuccess.jsx extrae token de URL",
        "  → POST a /api/sales/commit con token",
        "",
        "PASO 13: Backend en commit",
        "  → Busca Sale por token",
        "  → Confirma con Transbank que pago fue procesado",
        "  → Si OK: estado=PAGADO",
        "  → Para cada item en venta:",
        "    - Calcula nuevo stock",
        "    - PATCH a /api/products/{id}/stock",
        "    - ProductService actualiza stock en BD",
        "  → Retorna Sale actualizada",
        "",
        "PASO 14: Frontend muestra confirmación",
        "  → Mensaje 'Compra exitosa'",
        "  → Número de pedido",
        "  → Detalles de envío",
        "  → useCart().clearCart() vacía carrito",
        "  → localStorage.setItem('cart', '[]')",
        "",
        "PASO 15: Base de datos",
        "  → products: stock reducido",
        "  → sales: nuevo registro con estado PAGADO",
        "  → saledetail: nuevos registros con items de la venta",
    ]
    agregar_lista_bullets(doc, flujo_compra_completa)
    
    doc.add_page_break()
    
    # SECCIÓN: Integración Transbank
    agresar_titulo_seccion(doc, "16. INTEGRACIÓN CON TRANSBANK")
    
    agregar_subtitulo_seccion(doc, "¿Qué es Transbank?")
    agregar_parrafo(doc, 
        "Transbank es la plataforma de pagos chilena que procesa transacciones con tarjetas de crédito. "
        "En desarrollo, se usa Integración (ambiente de pruebas). En producción, se usa ambiente real.")
    
    agregar_subtitulo_seccion(doc, "Flujo de Transbank en el Proyecto")
    agregar_parrafo(doc, "Paso 1: Crear Transacción", bold=True)
    agregar_parrafo(doc, 
        "Cuando usuario confirma compra, backend llama:\n"
        "WebpayPlus.Transaction().create(buyOrder, sessionId, amount, returnUrl)\n"
        "• buyOrder: ID único de la orden (ej: O-12345)\n"
        "• sessionId: ID de sesión (ej: S-1702000000)\n"
        "• amount: Monto total en pesos\n"
        "• returnUrl: Donde redirigir tras pago (ej: /checkout-success)")
    
    agregar_parrafo(doc, "Respuesta de Transbank:", bold=True)
    agregar_parrafo(doc, 
        "{\n"
        "  \"token\": \"abc123xyz...\",\n"
        "  \"url\": \"https://webpay.transbank.cl/form?token=abc123xyz...\"\n"
        "}")
    
    agregar_parrafo(doc, "Paso 2: Redirigir Usuario", bold=True)
    agregar_parrafo(doc, 
        "Frontend recibe URL y token. Crea form HTML invisible con:\n"
        "<input type=\"hidden\" name=\"token_ws\" value=\"abc123xyz...\">\n"
        "Luego hace submit del form hacia URL de Transbank.\n"
        "Usuario ve formulario de Transbank en navegador.")
    
    agregar_parrafo(doc, "Paso 3: Usuario Completa Pago", bold=True)
    agregar_parrafo(doc, 
        "Usuario ingresa datos de tarjeta en formulario de Transbank.\n"
        "Transbank valida y procesa pago.\n"
        "Si OK: redirige a returnUrl con token en parámetro.\n"
        "Si falla: redirige a returnUrl con código de error.")
    
    agregar_parrafo(doc, "Paso 4: Confirmar Transacción", bold=True)
    agregar_parrafo(doc, 
        "Frontend ejecuta:\n"
        "POST /api/sales/commit con { token }\n"
        "Backend llama:\n"
        "WebpayPlus.Transaction().commit(token)\n"
        "Transbank retorna:\n"
        "{\n"
        "  \"responseCode\": 0,  // 0 = aprobado\n"
        "  \"transactionDate\": \"...\",\n"
        "  \"vci\": \"...\",\n"
        "  ...\n"
        "}\n"
        "Si responseCode = 0: pago aprobado\n"
        "Backend actualiza estado a PAGADO y descuenta stock")
    
    doc.add_page_break()
    
    # SECCIÓN: Testing
    agresar_titulo_seccion(doc, "19. TESTING")
    
    agregar_subtitulo_seccion(doc, "Testing Frontend - Jasmine + Karma")
    agregar_parrafo(doc, 
        "Jasmine: Framework de testing para JavaScript\n"
        "Karma: Test runner (ejecuta tests en navegador)")
    
    agregar_parrafo(doc, "Tipos de Tests:", bold=True)
    tipos_tests = [
        "Unit Tests: Probar funciones individuales (ej: formatearRut)",
        "Component Tests: Probar componentes React renderan correctamente",
        "Service Tests: Probar servicios hacen llamadas correctas",
        "Integration Tests: Probar múltiples componentes juntos",
    ]
    agregar_lista_bullets(doc, tipos_tests)
    
    agregar_parrafo(doc, "Comandos:", bold=True)
    agregar_parrafo(doc, "npm test: Ejecuta tests en watch mode")
    agregar_parrafo(doc, "npm run test:single: Ejecuta tests una sola vez")
    agregar_parrafo(doc, "npm run test:coverage: Genera reporte de cobertura")
    
    doc.add_page_break()
    
    # SECCIÓN: Deployment
    agresar_titulo_seccion(doc, "20. DEPLOYMENT Y PRODUCCIÓN")
    
    agregar_subtitulo_seccion(doc, "Arquitectura en AWS")
    
    arquitectura_aws = [
        "Frontend:",
        "  • React app buildea con vite build → carpeta dist/",
        "  • dist/ se sube a S3 (almacenamiento)",
        "  • CloudFront (CDN) distribuye archivos",
        "  • URL: https://huerthogar.com",
        "",
        "Backend - 3 Instancias EC2:",
        "  • Instancia 1: Microservicio Productos (puerto 8080)",
        "  • Instancia 2: Microservicio Usuarios (puerto 8082)",
        "  • Instancia 3: Microservicio Ventas (puerto 8081)",
        "  • Cada una corre: java -jar application.jar",
        "",
        "Base de Datos:",
        "  • PostgreSQL en AWS RDS",
        "  • Acceso desde todas las instancias EC2",
        "  • Backups automáticos",
        "  • Multi-AZ para alta disponibilidad",
        "",
        "DNS:",
        "  • Route 53 mapea huerthogar.com a CloudFront",
        "  • SSL/TLS certificado automático",
    ]
    agregar_lista_bullets(doc, arquitectura_aws)
    
    agregar_subtitulo_seccion(doc, "Proceso de Deployment")
    
    proceso_deploy = [
        "1. Commit código a repositorio GitHub",
        "2. Para Frontend:",
        "   a. Checkout código",
        "   b. npm install",
        "   c. npm run build (genera dist/)",
        "   d. aws s3 sync dist/ s3://bucket/ (sube a S3)",
        "   e. Invalidar CloudFront cache",
        "",
        "3. Para Backend:",
        "   a. Checkout código",
        "   b. mvn clean package (genera .jar)",
        "   c. SSH a EC2",
        "   d. Descargar .jar",
        "   e. Kill proceso anterior (kill -9 PID)",
        "   f. java -jar application.jar (inicia nuevo)",
        "",
        "4. Pruebas post-deployment",
    ]
    agregar_lista_bullets(doc, proceso_deploy)
    
    doc.add_page_break()
    
    # Conclusión final
    agresar_titulo_seccion(doc, "CONCLUSIÓN Y RESUMEN FINAL")
    
    agregar_parrafo(doc, 
        "El proyecto Huerto Hogar es un ejemplo completo de arquitectura moderna de e-commerce. "
        "Demuestra conceptos clave como:\n"
        "• Arquitectura de microservicios\n"
        "• Frontend reactivo con React y Context API\n"
        "• Backend robusto con Spring Boot\n"
        "• Integración con pasarela de pagos\n"
        "• Seguridad con JWT y encriptación\n"
        "• Testing y deployment en producción")
    
    agregar_parrafo(doc, 
        "Cada componente tiene una responsabilidad clara y bien definida. La comunicación entre "
        "servicios es a través de APIs REST, lo que permite evolucionar cada uno independientemente. "
        "El frontend maneja la presentación y experiencia del usuario, mientras que el backend "
        "maneja lógica de negocio y persistencia de datos.")
    
    agregar_parrafo(doc, 
        "Este documento proporciona una guía conceptual exhaustiva para entender cómo funciona cada "
        "pieza del proyecto y cómo trabajan en conjunto para crear una plataforma funcional y escalable.")
    
    # Guardar documento
    output_path = "ANALISIS_CONCEPTUAL_HUERTO_HOGAR_EXTENDIDO.docx"
    doc.save(output_path)
    print(f"✅ Documento extendido generado exitosamente: {output_path}")
    print(f"📄 Ubicación: {os.path.abspath(output_path)}")
    return output_path

if __name__ == "__main__":
    crear_documento_extendido()
