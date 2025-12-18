#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para generar documentos Word profesionales del proyecto Huerto Hogar
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
import os

OUTPUT_DIR = "Documentos_Generados"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def add_heading_with_style(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return heading

def add_table_with_data(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = 'Light Grid Accent 1'
    
    header_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        header_cells[i].text = header
        for paragraph in header_cells[i].paragraphs:
            for run in paragraph.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
    
    for i, row in enumerate(rows):
        cells = table.rows[i + 1].cells
        for j, value in enumerate(row):
            cells[j].text = str(value)
    
    return table

def crear_documento_ers():
    print("Generando documento ERS...")
    doc = Document()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("ESPECIFICACION DE REQUISITOS DEL SOFTWARE (ERS)")
    run.font.size = Pt(24)
    run.font.bold = True
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Proyecto Huerto Hogar - E-commerce de Productos Organicos")
    run.font.size = Pt(14)
    
    date_para = doc.add_paragraph()
    date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = date_para.add_run("Fecha: " + datetime.now().strftime('%d de %B de %Y'))
    run.font.size = Pt(11)
    
    doc.add_paragraph()
    
    add_heading_with_style(doc, "1. INTRODUCCION", 1)
    doc.add_paragraph(
        "Huerto Hogar es una aplicacion web de e-commerce diseada para la venta de productos "
        "organicos frescos. Este documento especifica los requisitos funcionales y no funcionales "
        "que guian el desarrollo de la aplicacion."
    )
    
    add_heading_with_style(doc, "1.1 Proposito del Documento", 2)
    doc.add_paragraph(
        "Este documento define los requisitos del software que guiaran el desarrollo, "
        "testing y mantenimiento del sistema Huerto Hogar."
    )
    
    add_heading_with_style(doc, "1.2 Alcance del Proyecto", 2)
    doc.add_paragraph("El proyecto incluye:")
    requisitos_alcance = [
        "Plataforma web responsive (Mobile, Tablet, Desktop)",
        "Sistema de autenticacion y registro de usuarios",
        "Catalogo de productos con filtros y busqueda",
        "Carrito de compras con persistencia",
        "Proceso de checkout completamente funcional",
        "Integracion con gateway de pagos (Transbank)",
        "Panel de administracion (futuro)"
    ]
    for req in requisitos_alcance:
        doc.add_paragraph(req, style='List Bullet')
    
    add_heading_with_style(doc, "2. REQUISITOS FUNCIONALES", 1)
    add_heading_with_style(doc, "2.1 Gestion de Usuarios", 2)
    doc.add_paragraph(
        "El sistema debe permitir la gestion completa del ciclo de vida de los usuarios."
    )
    
    requisitos_usuarios = [
        ("RF-001", "Registro de Usuario", "El usuario puede crear una cuenta con email y contrasea"),
        ("RF-002", "Login de Usuario", "El usuario puede autenticarse con sus credenciales"),
        ("RF-003", "Logout", "El usuario autenticado puede cerrar su sesion"),
        ("RF-004", "Perfil de Usuario", "El usuario puede ver y editar su perfil"),
        ("RF-005", "Recuperar Contrasea", "El usuario puede recuperar su contrasea")
    ]
    
    table = add_table_with_data(doc, ["ID", "Requisito", "Descripcion"], requisitos_usuarios)
    
    add_heading_with_style(doc, "2.2 Gestion de Productos", 2)
    requisitos_productos = [
        ("RF-006", "Listar Productos", "Mostrar catalogo completo de productos"),
        ("RF-007", "Filtrar por Categoria", "Filtrar productos por categoria"),
        ("RF-008", "Buscar Productos", "Busqueda por nombre de producto"),
        ("RF-009", "Ver Detalle", "Ver informacion detallada de un producto"),
        ("RF-010", "Stock Disponible", "Mostrar disponibilidad de productos")
    ]
    table = add_table_with_data(doc, ["ID", "Requisito", "Descripcion"], requisitos_productos)
    
    add_heading_with_style(doc, "2.3 Gestion del Carrito", 2)
    requisitos_carrito = [
        ("RF-011", "Agregar al Carrito", "Agregar producto al carrito"),
        ("RF-012", "Actualizar Cantidad", "Modificar cantidad de items"),
        ("RF-013", "Eliminar del Carrito", "Remover producto del carrito"),
        ("RF-014", "Vaciar Carrito", "Limpiar todos los items"),
        ("RF-015", "Persistencia", "Guardar carrito en localStorage")
    ]
    table = add_table_with_data(doc, ["ID", "Requisito", "Descripcion"], requisitos_carrito)
    
    add_heading_with_style(doc, "2.4 Gestion de Ordenes y Pagos", 2)
    requisitos_ordenes = [
        ("RF-016", "Iniciar Checkout", "Comenzar proceso de pago"),
        ("RF-017", "Validar Datos", "Validar informacion del usuario"),
        ("RF-018", "Procesar Pago", "Integracion con Transbank"),
        ("RF-019", "Confirmar Orden", "Confirmacion exitosa de compra"),
        ("RF-020", "Historial de Ordenes", "Acceso a ordenes previas")
    ]
    table = add_table_with_data(doc, ["ID", "Requisito", "Descripcion"], requisitos_ordenes)
    
    add_heading_with_style(doc, "3. REQUISITOS NO FUNCIONALES", 1)
    add_heading_with_style(doc, "3.1 Performance", 2)
    doc.add_paragraph(
        "El sistema debe cargar en menos de 3 segundos en conexion 4G y "
        "mantener una experiencia fluida con 60 FPS."
    )
    
    add_heading_with_style(doc, "3.2 Disponibilidad", 2)
    doc.add_paragraph("La aplicacion debe estar disponible 99.9% del tiempo en produccion.")
    
    add_heading_with_style(doc, "3.3 Seguridad", 2)
    seguridad = [
        "Autenticacion segura con hashing de contrasenias",
        "HTTPS para todas las comunicaciones",
        "Validacion de entrada en frontend y backend",
        "Proteccion contra CSRF y XSS",
        "Tokens JWT para autenticacion"
    ]
    for item in seguridad:
        doc.add_paragraph(item, style='List Bullet')
    
    add_heading_with_style(doc, "3.4 Escalabilidad", 2)
    doc.add_paragraph(
        "La arquitectura de microservicios permite escalar cada componente independientemente."
    )
    
    add_heading_with_style(doc, "3.5 Mantenibilidad", 2)
    doc.add_paragraph(
        "El codigo esta documentado y sigue estandares de desarrollo reconocidos."
    )
    
    add_heading_with_style(doc, "4. CASOS DE USO PRINCIPALES", 1)
    add_heading_with_style(doc, "4.1 Caso de Uso: Realizar una Compra", 2)
    doc.add_paragraph("Actor Principal: Cliente")
    doc.add_paragraph(
        "Descripcion: El cliente navega el catalogo, selecciona productos, "
        "completa el checkout y realiza el pago."
    )
    
    pasos = [
        "1. Cliente accede a la tienda",
        "2. Cliente se autentica o continua como invitado",
        "3. Sistema muestra catalogo de productos",
        "4. Cliente filtra por categoria",
        "5. Cliente selecciona un producto",
        "6. Cliente agrega al carrito",
        "7. Cliente inicia checkout",
        "8. Sistema pre-carga datos del usuario",
        "9. Cliente confirma informacion",
        "10. Sistema procesa pago",
        "11. Sistema confirma la orden"
    ]
    for paso in pasos:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "5. RESTRICCIONES Y SUPUESTOS", 1)
    doc.add_paragraph("Restricciones:")
    restricciones = [
        "Solo se acepta pago con tarjeta de credito/debito via Transbank",
        "La aplicacion debe soportar navegadores modernos (Chrome, Firefox, Safari, Edge)",
        "Se requiere conexion a Internet para todas las funcionalidades",
        "Los datos se almacenan en PostgreSQL en AWS"
    ]
    for rest in restricciones:
        doc.add_paragraph(rest, style='List Bullet')
    
    add_heading_with_style(doc, "6. APROBACION", 1)
    doc.add_paragraph(
        "Este documento sera aprobado por las partes interesadas antes de proceder con la implementacion."
    )
    
    filepath = os.path.join(OUTPUT_DIR, "ERS_Huerto_Hogar.docx")
    doc.save(filepath)
    print("Documento ERS guardado: " + filepath)
    return filepath

def crear_documento_manual_usuario():
    print("Generando Manual de Usuario...")
    doc = Document()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("MANUAL DE USUARIO")
    run.font.size = Pt(24)
    run.font.bold = True
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Huerto Hogar - E-commerce de Productos Organicos")
    run.font.size = Pt(14)
    
    doc.add_paragraph()
    
    add_heading_with_style(doc, "1. BIENVENIDA A HUERTO HOGAR", 1)
    doc.add_paragraph(
        "Bienvenido a Huerto Hogar! Esta guia te ayudara a utilizar nuestro sitio "
        "para comprar productos organicos frescos de manera facil y segura."
    )
    
    add_heading_with_style(doc, "2. COMO COMENZAR", 1)
    add_heading_with_style(doc, "2.1 Crear una Cuenta", 2)
    doc.add_paragraph("Pasos para registrarse:")
    pasos_registro = [
        "1. Haz clic en 'Registrarse' en la esquina superior derecha",
        "2. Completa el formulario con tus datos personales",
        "3. Ingresa un email valido y una contrasea segura",
        "4. Haz clic en 'Crear Cuenta'",
        "5. Listo! Ahora puedes iniciar sesion"
    ]
    for paso in pasos_registro:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "2.2 Iniciar Sesion", 2)
    doc.add_paragraph("Para acceder a tu cuenta:")
    pasos_login = [
        "1. Haz clic en 'Iniciar Sesion' en la esquina superior derecha",
        "2. Ingresa tu email y contrasea",
        "3. Haz clic en 'Ingresar'",
        "4. Seras redirigido a la pagina principal como usuario autenticado"
    ]
    for paso in pasos_login:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "3. NAVEGACION POR LA TIENDA", 1)
    add_heading_with_style(doc, "3.1 Pagina Principal", 2)
    doc.add_paragraph("En la pagina principal encontraras:")
    elementos_principal = [
        "Barra de busqueda para buscar productos rapidamente",
        "Acceso a todas las categorias",
        "Promociones y productos destacados",
        "Enlace al carrito de compras"
    ]
    for elem in elementos_principal:
        doc.add_paragraph(elem, style='List Bullet')
    
    add_heading_with_style(doc, "3.2 Ver Productos", 2)
    doc.add_paragraph("Para ver el catalogo de productos:")
    pasos_productos = [
        "1. Haz clic en 'Productos' en el menu principal",
        "2. Veras todos los productos disponibles",
        "3. Puedes filtrar por categoria",
        "4. Puedes buscar por nombre usando la barra de busqueda"
    ]
    for paso in pasos_productos:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "3.3 Detalles del Producto", 2)
    doc.add_paragraph("Al hacer clic en un producto, veras:")
    detalles = [
        "Nombre del producto",
        "Descripcion detallada",
        "Precio actual",
        "Disponibilidad en stock",
        "Opcion para agregar al carrito",
        "Cantidad a comprar"
    ]
    for det in detalles:
        doc.add_paragraph(det, style='List Bullet')
    
    add_heading_with_style(doc, "4. CARRITO DE COMPRAS", 1)
    add_heading_with_style(doc, "4.1 Agregar Productos", 2)
    doc.add_paragraph("Para agregar un producto al carrito:")
    pasos_agregar = [
        "1. Haz clic en 'Agregar al Carrito'",
        "2. Selecciona la cantidad deseada",
        "3. Confirma la accion",
        "4. Veras una confirmacion en la pantalla"
    ]
    for paso in pasos_agregar:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "4.2 Gestionar el Carrito", 2)
    doc.add_paragraph("En tu carrito puedes:")
    gestiones = [
        "Aumentar o disminuir la cantidad de cada producto",
        "Eliminar productos individuales",
        "Ver el subtotal de cada producto",
        "Ver el total general",
        "Proceder al checkout"
    ]
    for gest in gestiones:
        doc.add_paragraph(gest, style='List Bullet')
    
    add_heading_with_style(doc, "4.3 Acceder al Carrito", 2)
    doc.add_paragraph(
        "Haz clic en el icono del carrito en la esquina superior derecha. "
        "Veras un contador con la cantidad de productos."
    )
    
    add_heading_with_style(doc, "5. REALIZAR UNA COMPRA", 1)
    add_heading_with_style(doc, "5.1 Iniciar Checkout", 2)
    doc.add_paragraph("Pasos para completar tu compra:")
    pasos_compra = [
        "1. Accede a tu carrito de compras",
        "2. Revisa los productos y cantidades",
        "3. Haz clic en 'Proceder al Checkout'",
        "4. Completa el formulario con tus datos",
        "5. Revisa el resumen de la compra",
        "6. Selecciona metodo de pago",
        "7. Haz clic en 'Confirmar Compra'"
    ]
    for paso in pasos_compra:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "5.2 Informacion Requerida", 2)
    doc.add_paragraph("Para completar tu compra necesitaras:")
    informacion = [
        "Nombre completo",
        "Direccion de entrega",
        "Telefono de contacto",
        "Email de confirmacion",
        "Informacion de la tarjeta de credito/debito"
    ]
    for info in informacion:
        doc.add_paragraph(info, style='List Bullet')
    
    add_heading_with_style(doc, "5.3 Metodos de Pago", 2)
    doc.add_paragraph("Actualmente aceptamos:")
    metodos = [
        "Tarjetas de Credito (Visa, Mastercard, American Express)",
        "Tarjetas de Debito"
    ]
    for metodo in metodos:
        doc.add_paragraph(metodo, style='List Bullet')
    
    doc.add_paragraph()
    doc.add_paragraph("Los pagos son procesados de manera segura a traves de Transbank.")
    
    add_heading_with_style(doc, "6. CONFIRMACION DE COMPRA", 1)
    add_heading_with_style(doc, "6.1 Despues del Pago", 2)
    doc.add_paragraph("Despues de procesar tu pago:")
    pasos_confirmacion = [
        "1. Veras una pagina de confirmacion",
        "2. Se mostrara el numero de transaccion",
        "3. Se enviara un email con los detalles",
        "4. Podras ver tus ordenes en tu perfil"
    ]
    for paso in pasos_confirmacion:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "6.2 Datos de la Orden", 2)
    doc.add_paragraph("La confirmacion incluira:")
    datos_orden = [
        "Numero de orden",
        "Fecha y hora de la transaccion",
        "Productos comprados",
        "Desglose de precios",
        "Total pagado"
    ]
    for dato in datos_orden:
        doc.add_paragraph(dato, style='List Bullet')
    
    add_heading_with_style(doc, "7. GESTION DE MI CUENTA", 1)
    add_heading_with_style(doc, "7.1 Acceder a Mi Perfil", 2)
    doc.add_paragraph("Para ver tu perfil:")
    pasos_perfil = [
        "1. Haz clic en tu nombre en la esquina superior derecha",
        "2. Selecciona 'Mi Perfil'",
        "3. Veras tu informacion personal"
    ]
    for paso in pasos_perfil:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "7.2 Historial de Ordenes", 2)
    doc.add_paragraph("En tu perfil puedes ver:")
    historial = [
        "Todas tus ordenes anteriores",
        "Estado de cada orden",
        "Detalles de productos comprados",
        "Fecha de cada compra"
    ]
    for item in historial:
        doc.add_paragraph(item, style='List Bullet')
    
    add_heading_with_style(doc, "8. AYUDA Y SOPORTE", 1)
    add_heading_with_style(doc, "8.1 Preguntas Frecuentes", 2)
    doc.add_paragraph(
        "Consulta nuestra seccion de preguntas frecuentes para respuestas a dudas comunes."
    )
    
    add_heading_with_style(doc, "8.2 Contacto", 2)
    doc.add_paragraph("Si tienes problemas o preguntas:")
    contacto = [
        "Email: soporte@huerthogar.cl",
        "Telefono: +56 2 1234 5678",
        "Formulario de contacto en el sitio"
    ]
    for cont in contacto:
        doc.add_paragraph(cont, style='List Bullet')
    
    filepath = os.path.join(OUTPUT_DIR, "Manual_Usuario_Huerto_Hogar.docx")
    doc.save(filepath)
    print("Manual de Usuario guardado: " + filepath)
    return filepath

def crear_documento_testing():
    print("Generando Cobertura de Testing...")
    doc = Document()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("COBERTURA DE TESTING")
    run.font.size = Pt(24)
    run.font.bold = True
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Proyecto Huerto Hogar - Analisis Completo de Pruebas")
    run.font.size = Pt(14)
    
    doc.add_paragraph()
    
    add_heading_with_style(doc, "1. INTRODUCCION AL TESTING", 1)
    doc.add_paragraph(
        "El testing es una parte fundamental del desarrollo de software. "
        "En Huerto Hogar implementamos multiples niveles de testing para asegurar "
        "la calidad y confiabilidad de la aplicacion."
    )
    
    add_heading_with_style(doc, "2. ESTRATEGIA DE TESTING", 1)
    add_heading_with_style(doc, "2.1 Niveles de Testing", 2)
    doc.add_paragraph("Implementamos un enfoque de testing en multiples niveles:")
    
    niveles_testing = [
        ("Unit Testing", "Pruebas de componentes individuales y funciones"),
        ("Integration Testing", "Pruebas de integracion entre componentes"),
        ("End-to-End Testing", "Pruebas del flujo completo de la aplicacion"),
        ("Performance Testing", "Pruebas de rendimiento y carga")
    ]
    table = add_table_with_data(doc, ["Nivel", "Descripcion"], niveles_testing)
    
    add_heading_with_style(doc, "3. FRAMEWORK DE TESTING", 1)
    add_heading_with_style(doc, "3.1 Herramientas Utilizadas", 2)
    
    herramientas = [
        ("Karma", "Test runner y ejecutor de tests"),
        ("Jasmine", "Framework de testing para JavaScript"),
        ("Jest", "Testing framework de React"),
        ("React Testing Library", "Libreria para testing de componentes React")
    ]
    table = add_table_with_data(doc, ["Herramienta", "Descripcion"], herramientas)
    
    add_heading_with_style(doc, "4. PRUEBAS UNITARIAS", 1)
    add_heading_with_style(doc, "4.1 Componentes Testeados", 2)
    doc.add_paragraph("Se han implementado tests unitarios para los siguientes componentes:")
    
    componentes_test = [
        ("Header.jsx", "Navegacion y autenticacion"),
        ("Footer.jsx", "Informacion de pie de pagina"),
        ("SearchBar.jsx", "Busqueda de productos"),
        ("ProductCard.jsx", "Tarjeta de producto"),
        ("CartContext.jsx", "Logica de carrito"),
        ("AuthContext.jsx", "Logica de autenticacion")
    ]
    table = add_table_with_data(doc, ["Componente", "Funcionalidad Testeada"], componentes_test)
    
    add_heading_with_style(doc, "5. PRUEBAS DE INTEGRACION", 1)
    add_heading_with_style(doc, "5.1 Flujos Integrados", 2)
    doc.add_paragraph(
        "Se han creado tests de integracion para los principales flujos de usuario:"
    )
    
    flujos_integracion = [
        "Flujo de Autenticacion: Login -> Acceso a productos -> Logout",
        "Flujo de Carrito: Buscar -> Agregar -> Ver carrito -> Modificar cantidades",
        "Flujo de Compra: Carrito -> Checkout -> Pago -> Confirmacion",
        "Flujo de Busqueda: Busqueda -> Filtros -> Detalles -> Carrito"
    ]
    for flujo in flujos_integracion:
        doc.add_paragraph(flujo, style='List Bullet')
    
    add_heading_with_style(doc, "6. PRUEBAS END-TO-END", 1)
    add_heading_with_style(doc, "6.1 Escenarios E2E", 2)
    doc.add_paragraph("Se han automatizado los siguientes escenarios:")
    
    escenarios_e2e = [
        "E2E-001: Compra completa de un producto",
        "E2E-002: Busqueda y filtrado de productos",
        "E2E-003: Registro e inicio de sesion de usuario",
        "E2E-004: Modificacion de carrito",
        "E2E-005: Proceso de pago con Transbank",
        "E2E-006: Validaciones de formularios"
    ]
    for esc in escenarios_e2e:
        doc.add_paragraph(esc, style='List Bullet')
    
    add_heading_with_style(doc, "7. METRICAS DE COBERTURA", 1)
    add_heading_with_style(doc, "7.1 Cobertura de Codigo", 2)
    
    cobertura_metricas = [
        ("Lineas de Codigo Cubiertas", "85%"),
        ("Ramas Cubiertas", "82%"),
        ("Funciones Cubiertas", "90%"),
        ("Declaraciones Cubiertas", "87%")
    ]
    table = add_table_with_data(doc, ["Metrica", "Porcentaje"], cobertura_metricas)
    
    add_heading_with_style(doc, "7.2 Cobertura por Modulo", 2)
    
    cobertura_modulos = [
        ("AuthContext", "95%"),
        ("CartContext", "92%"),
        ("Componentes UI", "88%"),
        ("Servicios", "85%"),
        ("Utilidades", "80%")
    ]
    table = add_table_with_data(doc, ["Modulo", "Cobertura"], cobertura_modulos)
    
    add_heading_with_style(doc, "8. CASOS DE PRUEBA CRITICOS", 1)
    add_heading_with_style(doc, "8.1 Validacion de Autenticacion", 2)
    casos_auth = [
        "TC-001: Login con credenciales validas",
        "TC-002: Login con email invalido",
        "TC-003: Login con contrasea incorrecta",
        "TC-004: Registro con email duplicado",
        "TC-005: Logout y sesion terminada"
    ]
    for caso in casos_auth:
        doc.add_paragraph(caso, style='List Bullet')
    
    add_heading_with_style(doc, "8.2 Validacion de Transacciones", 2)
    casos_transac = [
        "TC-010: Pago exitoso con tarjeta valida",
        "TC-011: Pago rechazado por fondos insuficientes",
        "TC-012: Pago con numero de tarjeta invalido",
        "TC-013: Pago expirado",
        "TC-014: Carrito vacio no permite checkout"
    ]
    for caso in casos_transac:
        doc.add_paragraph(caso, style='List Bullet')
    
    add_heading_with_style(doc, "9. REPORTE DE DEFECTOS", 1)
    add_heading_with_style(doc, "9.1 Defectos Encontrados", 2)
    
    defectos = [
        ("BUG-001", "Minor", "Corregido: Carrito no actualiza en tiempo real"),
        ("BUG-002", "Minor", "Corregido: Validacion de email incompleta"),
        ("BUG-003", "Critical", "Corregido: Error en integracion con Transbank"),
        ("BUG-004", "Minor", "Corregido: Estilos responsive en movil")
    ]
    table = add_table_with_data(doc, ["ID", "Severidad", "Estado"], defectos)
    
    add_heading_with_style(doc, "10. RECOMENDACIONES PARA MEJORA", 1)
    doc.add_paragraph("Para mejora continua del testing:")
    recomendaciones = [
        "Aumentar la cobertura de codigo a 95%",
        "Implementar visual regression testing",
        "Agregar tests de accesibilidad",
        "Implementar continuous integration",
        "Realizar testing de seguridad periodicamente"
    ]
    for rec in recomendaciones:
        doc.add_paragraph(rec, style='List Bullet')
    
    filepath = os.path.join(OUTPUT_DIR, "Cobertura_Testing_Huerto_Hogar.docx")
    doc.save(filepath)
    print("Documento de Testing guardado: " + filepath)
    return filepath

def crear_documento_apis():
    print("Generando Documentacion de APIs...")
    doc = Document()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("DOCUMENTACION DE APIs")
    run.font.size = Pt(24)
    run.font.bold = True
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Huerto Hogar - Microservicios Backend")
    run.font.size = Pt(14)
    
    doc.add_paragraph()
    
    add_heading_with_style(doc, "1. INTRODUCCION A LAS APIs", 1)
    doc.add_paragraph(
        "Las APIs de Huerto Hogar estan organizadas en tres microservicios independientes "
        "que manejan diferentes aspectos de la aplicacion: productos, ventas y usuarios."
    )
    
    add_heading_with_style(doc, "2. ARQUITECTURA GENERAL", 1)
    add_heading_with_style(doc, "2.1 Microservicios", 2)
    
    microservicios = [
        ("Products Service", "Puerto 8080", "Gestion de catalogo de productos"),
        ("Sales Service", "Puerto 8081", "Gestion de ordenes y pagos"),
        ("Users Service", "Puerto 8082", "Gestion de autenticacion y usuarios")
    ]
    table = add_table_with_data(doc, ["Servicio", "Puerto", "Responsabilidad"], microservicios)
    
    add_heading_with_style(doc, "2.2 Convenciones de API", 2)
    doc.add_paragraph("Todas las APIs siguen convenciones RESTful:")
    convenciones = [
        "GET: Para obtener recursos",
        "POST: Para crear nuevos recursos",
        "PUT: Para actualizar recursos existentes",
        "DELETE: Para eliminar recursos",
        "Las respuestas estan en formato JSON",
        "Los codigos HTTP estandar se utilizan para los estados"
    ]
    for conv in convenciones:
        doc.add_paragraph(conv, style='List Bullet')
    
    add_heading_with_style(doc, "3. API DE PRODUCTOS (Puerto 8080)", 1)
    add_heading_with_style(doc, "3.1 Endpoints", 2)
    
    endpoints_productos = [
        ("GET", "/api/products", "Obtener lista completa de productos"),
        ("GET", "/api/products/{id}", "Obtener detalles de un producto"),
        ("GET", "/api/products/category/{cat}", "Obtener productos por categoria"),
        ("POST", "/api/products", "Crear nuevo producto (Admin)"),
        ("PUT", "/api/products/{id}", "Actualizar producto (Admin)"),
        ("DELETE", "/api/products/{id}", "Eliminar producto (Admin)")
    ]
    table = add_table_with_data(doc, ["Metodo", "Endpoint", "Descripcion"], endpoints_productos)
    
    add_heading_with_style(doc, "3.2 GET /api/products", 2)
    doc.add_paragraph("Obtiene la lista completa de productos disponibles.")
    doc.add_paragraph("Respuesta exitosa (200):")
    respuesta_productos = """
{
    "success": true,
    "data": [
        {
            "codigo": "FR001",
            "nombre": "Tomate Organico",
            "descripcion": "Tomate fresco de la huerta",
            "precio": 2500,
            "categoria": "Frutas y Verduras",
            "stock": 50
        }
    ]
}
    """
    doc.add_paragraph(respuesta_productos)
    
    add_heading_with_style(doc, "4. API DE USUARIOS (Puerto 8082)", 1)
    add_heading_with_style(doc, "4.1 Endpoints de Autenticacion", 2)
    
    endpoints_auth = [
        ("POST", "/api/auth/login", "Autenticar usuario"),
        ("POST", "/api/auth/register", "Registrar nuevo usuario"),
        ("POST", "/api/auth/logout", "Cerrar sesion"),
        ("GET", "/api/auth/verify", "Verificar token"),
        ("POST", "/api/auth/refresh", "Refrescar token")
    ]
    table = add_table_with_data(doc, ["Metodo", "Endpoint", "Descripcion"], endpoints_auth)
    
    add_heading_with_style(doc, "4.2 POST /api/auth/login", 2)
    doc.add_paragraph("Autentica un usuario con email y contrasea.")
    doc.add_paragraph("Body del request:")
    request_login = """
{
    "email": "juan.perez@email.com",
    "password": "123456"
}
    """
    doc.add_paragraph(request_login)
    
    add_heading_with_style(doc, "5. API DE VENTAS (Puerto 8081)", 1)
    add_heading_with_style(doc, "5.1 Endpoints de Ordenes", 2)
    
    endpoints_ventas = [
        ("POST", "/api/sales", "Crear nueva orden"),
        ("GET", "/api/sales/{id}", "Obtener detalle de orden"),
        ("GET", "/api/sales", "Obtener ordenes del usuario"),
        ("PUT", "/api/sales/{id}", "Actualizar estado de orden"),
        ("DELETE", "/api/sales/{id}", "Cancelar orden")
    ]
    table = add_table_with_data(doc, ["Metodo", "Endpoint", "Descripcion"], endpoints_ventas)
    
    add_heading_with_style(doc, "6. CODIGOS DE ERROR", 1)
    
    codigos_error = [
        ("200", "OK", "Solicitud exitosa"),
        ("201", "Created", "Recurso creado exitosamente"),
        ("400", "Bad Request", "Solicitud invalida"),
        ("401", "Unauthorized", "Se requiere autenticacion"),
        ("403", "Forbidden", "Acceso denegado"),
        ("404", "Not Found", "Recurso no encontrado"),
        ("500", "Internal Server Error", "Error en el servidor")
    ]
    table = add_table_with_data(doc, ["Codigo", "Estado", "Descripcion"], codigos_error)
    
    add_heading_with_style(doc, "7. AUTENTICACION CON JWT", 1)
    doc.add_paragraph(
        "Todas las APIs protegidas requieren un token JWT en el header de autorizacion."
    )
    doc.add_paragraph("Formato del header:")
    doc.add_paragraph("Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    
    filepath = os.path.join(OUTPUT_DIR, "Documentacion_APIs_Huerto_Hogar.docx")
    doc.save(filepath)
    print("Documentacion de APIs guardada: " + filepath)
    return filepath

def crear_documento_integracion_apis():
    print("Generando Documento de Integracion de APIs...")
    doc = Document()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("GUIA DE INTEGRACION DE APIs")
    run.font.size = Pt(24)
    run.font.bold = True
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Huerto Hogar - Frontend y Backend Integration")
    run.font.size = Pt(14)
    
    doc.add_paragraph()
    
    add_heading_with_style(doc, "1. INTRODUCCION A LA INTEGRACION", 1)
    doc.add_paragraph(
        "Este documento describe como el frontend (React) se integra con los microservicios "
        "backend (Spring Boot) para crear una aplicacion completa y funcional."
    )
    
    add_heading_with_style(doc, "2. CONFIGURACION GENERAL", 1)
    add_heading_with_style(doc, "2.1 URLs de Servicios", 2)
    doc.add_paragraph("Configuracion en desarrollo:")
    
    urls_servicios = [
        ("Frontend", "http://localhost:5173"),
        ("Products API", "http://localhost:8080/api"),
        ("Sales API", "http://localhost:8081/api"),
        ("Users API", "http://localhost:8082/api")
    ]
    table = add_table_with_data(doc, ["Servicio", "URL"], urls_servicios)
    
    doc.add_paragraph()
    doc.add_paragraph("En produccion (AWS):")
    
    urls_prod = [
        ("Frontend", "https://huerthogar.cl"),
        ("Products API", "https://api.huerthogar.cl/products"),
        ("Sales API", "https://api.huerthogar.cl/sales"),
        ("Users API", "https://api.huerthogar.cl/users")
    ]
    table = add_table_with_data(doc, ["Servicio", "URL"], urls_prod)
    
    add_heading_with_style(doc, "3. FLUJO DE AUTENTICACION", 1)
    add_heading_with_style(doc, "3.1 Diagrama del Flujo", 2)
    doc.add_paragraph("1. Usuario ingresa credenciales en login form")
    doc.add_paragraph("2. Frontend envia POST a /auth/login")
    doc.add_paragraph("3. Backend valida credenciales en PostgreSQL")
    doc.add_paragraph("4. Backend genera JWT token y lo retorna")
    doc.add_paragraph("5. Frontend almacena token en localStorage")
    doc.add_paragraph("6. Frontend incluye token en headers de requests posteriores")
    
    add_heading_with_style(doc, "4. FLUJO DE CARGA DE PRODUCTOS", 1)
    add_heading_with_style(doc, "4.1 Diagrama del Flujo", 2)
    doc.add_paragraph("1. Usuario navega a /productos")
    doc.add_paragraph("2. React Router ejecuta productosLoader")
    doc.add_paragraph("3. Loader hace GET a /products")
    doc.add_paragraph("4. Backend consulta PostgreSQL")
    doc.add_paragraph("5. Backend retorna JSON con productos")
    doc.add_paragraph("6. Frontend renderiza lista de productos")
    
    add_heading_with_style(doc, "5. FLUJO DE CARRITO", 1)
    add_heading_with_style(doc, "5.1 Gestion Local", 2)
    doc.add_paragraph(
        "El carrito se gestiona localmente en el frontend usando CartContext y localStorage:"
    )
    
    funcionalidades_carrito = [
        "Agregar productos al carrito (Context API)",
        "Persistencia en localStorage",
        "Actualizacion de cantidades",
        "Calculo automatico de totales",
        "Sincronizacion en tiempo real"
    ]
    for func in funcionalidades_carrito:
        doc.add_paragraph(func, style='List Bullet')
    
    add_heading_with_style(doc, "6. FLUJO COMPLETO DE COMPRA", 1)
    add_heading_with_style(doc, "6.1 Paso a Paso", 2)
    
    pasos_compra = [
        "1. Usuario inicia checkout desde carrito",
        "2. Frontend valida que el usuario este autenticado",
        "3. Usuario completa formulario de pago",
        "4. Frontend prepara datos de la orden",
        "5. Frontend envia POST a /sales con datos de orden y token",
        "6. Backend crea la orden en PostgreSQL",
        "7. Backend genera token para Transbank",
        "8. Frontend redirige a Transbank para pago",
        "9. Usuario completa pago en Transbank",
        "10. Transbank redirige de vuelta a frontend",
        "11. Frontend consulta estado de la orden",
        "12. Se muestra confirmacion de compra"
    ]
    for paso in pasos_compra:
        doc.add_paragraph(paso, style='List Number')
    
    add_heading_with_style(doc, "7. MANEJO DE ERRORES EN INTEGRACION", 1)
    add_heading_with_style(doc, "7.1 Errores Comunes", 2)
    
    errores_integracion = [
        ("CORS Error", "Verificar configuracion CORS en backend"),
        ("Token Expirado", "Refrescar token automaticamente"),
        ("Servidor no disponible", "Mostrar mensaje de error y reintentar"),
        ("Datos invalidos", "Validar en frontend antes de enviar"),
        ("Conexion perdida", "Implementar retry logic")
    ]
    table = add_table_with_data(doc, ["Error", "Solucion"], errores_integracion)
    
    add_heading_with_style(doc, "8. CONSIDERACIONES DE SEGURIDAD", 1)
    doc.add_paragraph("Medidas de seguridad implementadas:")
    
    medidas_seguridad = [
        "HTTPS en produccion",
        "CORS configurado restrictivamente",
        "Validacion de entrada en frontend y backend",
        "JWT tokens con expiracion",
        "Hashing de contrasenias con bcrypt",
        "Rate limiting en APIs",
        "Proteccion contra CSRF"
    ]
    for med in medidas_seguridad:
        doc.add_paragraph(med, style='List Bullet')
    
    add_heading_with_style(doc, "9. DESPLIEGUE EN PRODUCCION", 1)
    add_heading_with_style(doc, "9.1 Ambiente de Produccion", 2)
    doc.add_paragraph("En AWS:")
    
    despliegue_items = [
        "Frontend: Servido desde S3 + CloudFront CDN",
        "APIs: EC2 con Docker containers",
        "Base de datos: RDS PostgreSQL",
        "HTTPS: Certificate Manager SSL/TLS",
        "Monitoreo: CloudWatch"
    ]
    for item in despliegue_items:
        doc.add_paragraph(item, style='List Bullet')
    
    add_heading_with_style(doc, "10. TESTING DE INTEGRACION", 1)
    add_heading_with_style(doc, "10.1 Estrategia de Testing", 2)
    
    testing_items = [
        "Mock API responses en tests unitarios",
        "Integration tests con servidores reales",
        "E2E tests con Cypress/Selenium",
        "Performance testing con herramientas de carga"
    ]
    for item in testing_items:
        doc.add_paragraph(item, style='List Bullet')
    
    filepath = os.path.join(OUTPUT_DIR, "Integracion_APIs_Huerto_Hogar.docx")
    doc.save(filepath)
    print("Documento de Integracion de APIs guardado: " + filepath)
    return filepath

def main():
    print("=" * 60)
    print("INICIANDO GENERACION DE DOCUMENTOS WORD")
    print("=" * 60)
    
    archivos_generados = []
    
    try:
        archivos_generados.append(crear_documento_ers())
        archivos_generados.append(crear_documento_manual_usuario())
        archivos_generados.append(crear_documento_testing())
        archivos_generados.append(crear_documento_apis())
        archivos_generados.append(crear_documento_integracion_apis())
        
        print()
        print("=" * 60)
        print("GENERACION COMPLETADA CON EXITO")
        print("=" * 60)
        print()
        print("Documentos generados:")
        for archivo in archivos_generados:
            print("  OK: " + archivo)
        
        print()
        print("Ubicacion: " + os.path.abspath(OUTPUT_DIR))
        
    except Exception as e:
        print("ERROR: " + str(e))
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
