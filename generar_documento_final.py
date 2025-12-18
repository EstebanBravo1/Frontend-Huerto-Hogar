#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar documento Word COMPLETO y DEFINITIVO con análisis técnico exhaustivo
Incluye: Arquitectura, flujos, código de ejemplo, tablas de relaciones, y guía conceptual
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
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
    elif nivel == 2:
        p = doc.add_heading(titulo, level=2)
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(3)
    else:
        p = doc.add_heading(titulo, level=3)

def agregar_subtitulo_seccion(doc, titulo):
    """Agregar un subtítulo"""
    p = doc.add_heading(titulo, level=2)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)

def agregar_parrafo(doc, texto, bold=False, italic=False, size=11):
    """Agregar un párrafo con formato opcional"""
    p = doc.add_paragraph()
    run = p.add_run(texto)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    p.paragraph_format.space_after = Pt(6)
    return p

def agregar_lista_bullets(doc, items):
    """Agregar una lista con bullets"""
    for item in items:
        doc.add_paragraph(item, style='List Bullet')

def agregar_tabla(doc, headers, rows):
    """Agregar una tabla formateada"""
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = 'Light Grid Accent 1'
    
    header_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        header_cells[i].text = header
        for paragraph in header_cells[i].paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), '366092')
        header_cells[i]._element.get_or_add_tcPr().append(shading_elm)
    
    for i, row in enumerate(rows, 1):
        cells = table.rows[i].cells
        for j, cell_data in enumerate(row):
            cells[j].text = str(cell_data)

def crear_documento_final():
    """Crear documento Word COMPLETO Y DEFINITIVO"""
    doc = Document()
    
    # ============ PORTADA ============
    doc.add_heading('📋 ANÁLISIS CONCEPTUAL COMPLETO Y EXHAUSTIVO', 0).alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    doc.add_heading('PROYECTO E-COMMERCE "HUERTO HOGAR"', 1).alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph()
    p = doc.add_paragraph('Documento Técnico Definitivo')
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    p = doc.add_paragraph(f'Generado: {datetime.now().strftime("%d de %B de %Y - %H:%M")}')
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    p = doc.add_paragraph(
        'Este documento proporciona una guía exhaustiva y conceptual del proyecto Huerto Hogar. '
        'Explica en detalle cada método, función, componente y cómo trabajan juntos para crear '
        'una plataforma de e-commerce funcional, segura y escalable.'
    )
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_page_break()
    
    # ============ ÍNDICE ============
    agregar_titulo_seccion(doc, "ÍNDICE COMPLETO")
    contenidos = [
        "1. Resumen Ejecutivo",
        "2. Descripción del Proyecto",
        "3. Tecnologías Utilizadas",
        "4. Arquitectura General",
        "5. Diagramas de Sistema",
        "6. Frontend: Arquitectura React",
        "7. Backend: Microservicios Spring Boot",
        "8. Base de Datos",
        "9. Autenticación y Seguridad",
        "10. Flujo de Compra Completo",
        "11. Ejemplos de Código",
        "12. Integración con Transbank",
        "13. Buenas Prácticas Implementadas",
        "14. Conclusiones",
    ]
    for contenido in contenidos:
        doc.add_paragraph(contenido, style='List Number')
    
    doc.add_page_break()
    
    # ============ SECCIÓN 1: RESUMEN ============
    agregar_titulo_seccion(doc, "1. RESUMEN EJECUTIVO")
    
    agregar_parrafo(doc, 
        "Huerto Hogar es una plataforma de e-commerce especializada en la venta de productos agrícolas "
        "y hortícolas. El proyecto demuestra una arquitectura moderna basada en microservicios con un "
        "frontend reactivo (React) y un backend robusto (Spring Boot).")
    
    agregar_parrafo(doc, "Características principales:", bold=True)
    caracteristicas = [
        "Catálogo de productos con filtros y paginación",
        "Carrito de compras con persistencia en localStorage",
        "Sistema de autenticación con JWT",
        "Checkout integrado con Transbank para procesamiento de pagos",
        "Tres microservicios independientes (Productos, Usuarios, Ventas)",
        "Base de datos PostgreSQL centralizada",
        "Testing automatizado con Jasmine + Karma",
        "Deployment en AWS EC2",
    ]
    agregar_lista_bullets(doc, caracteristicas)
    
    doc.add_page_break()
    
    # ============ SECCIÓN 4: ARQUITECTURA ============
    agregar_titulo_seccion(doc, "4. ARQUITECTURA GENERAL")
    
    agregar_parrafo(doc, "Diagrama de Componentes:", bold=True)
    diagrama = """
    ┌─────────────────────────────────────────────────────────────────┐
    │                        USUARIO (Cliente)                        │
    │                    Navegador Web (Chrome, etc)                  │
    └────────────────────────┬─────────────────────────────────────────┘
                             │ HTTP/HTTPS
                             ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │                    FRONTEND (React + Vite)                      │
    │  • SPA (Single Page Application)                               │
    │  • Context API (Auth, Cart)                                    │
    │  • React Router (Navegación)                                   │
    │  • Bootstrap (Estilos)                                         │
    │  • localStorage (Persistencia)                                 │
    └────────────────┬──────────────────────────┬──────────────────────┘
                     │ HTTP/JSON                │ HTTP/JSON
                     │                          │
        ┌────────────▼─────────────┐  ┌────────▼──────────────┐
        │  MICROSERVICIO           │  │  MICROSERVICIO       │
        │  PRODUCTOS (8080)        │  │  USUARIOS (8082)     │
        │  • ProductService        │  │  • UserService       │
        │  • ProductController     │  │  • AuthController    │
        │  • ProductRepository     │  │  • JwtUtil           │
        └────────────┬─────────────┘  └────────┬──────────────┘
                     │                         │
        ┌────────────▼──────────────────────────▼─────────┐
        │  MICROSERVICIO VENTAS (8081)                   │
        │  • SaleService                                 │
        │  • SaleController                              │
        │  • ProductApiService (llamadas a Productos)   │
        └────────────┬──────────────────────────────────┘
                     │ HTTP/JSON
                     ▼
        ┌─────────────────────────────────────────────┐
        │  BASE DE DATOS PostgreSQL                   │
        │  • Tabla: products                          │
        │  • Tabla: users                             │
        │  • Tabla: sales                             │
        │  • Tabla: saledetail                        │
        └─────────────────────────────────────────────┘
                     │
                     ▼
        ┌─────────────────────────────────────────────┐
        │  TRANSBANK WebPay (Procesamiento Pagos)    │
        └─────────────────────────────────────────────┘
    """
    agregar_parrafo(doc, diagrama)
    
    doc.add_page_break()
    
    # ============ SECCIÓN 5: DIAGRAMAS ============
    agregar_titulo_seccion(doc, "5. DIAGRAMAS DE SISTEMA")
    
    agregar_subtitulo_seccion(doc, "Flujo de Datos: Compra de Producto")
    flujo_diagrama = """
    Usuario                Frontend              Backend             Transbank
      │                      │                    │                    │
      │  1. Navega /productos│                    │                    │
      ├────────────────────►│                    │                    │
      │                      │  2. GET /api/products                   │
      │                      ├───────────────────►│                    │
      │                      │◄─── JSON (productos)                    │
      │                      │  3. Renderiza grid  │                    │
      │  4. Clica "Agregar"  │                    │                    │
      ├────────────────────►│ addToCart()         │                    │
      │                      │ (guarda en Cart Context + localStorage)  │
      │                      │                    │                    │
      │  5. Va a /carrito    │                    │                    │
      ├────────────────────►│                    │                    │
      │  6. Clica "Pagar"   │                    │                    │
      ├────────────────────►│ CheckoutForm abre   │                    │
      │  7. Completa datos   │                    │                    │
      │  8. "Confirmar"      │                    │                    │
      ├────────────────────►│  POST /api/sales/init               │
      │                      │────────────────────►│                    │
      │                      │                    │  Valida stock      │
      │                      │                    │  Crea Sale         │
      │                      │                    │  9. Contacta Transbank
      │                      │                    ├──────────────────►│
      │                      │                    │◄─── token + URL    │
      │                      │◄─── token + URL    │                    │
      │  10. Redirige        │  (form invisible)  │                    │
      ├────────────────────►│────────────────────────────────────────►│
      │                      │                    │                    │
      │  11. Ingresa datos   │                    │                    │
      │  12. "Confirmar"     │                    │                    │
      │◄────────────────────────────────────────────────────────────┤│
      │  13. Redirige /checkout-success          │                    │
      ├────────────────────►│  POST /api/sales/commit                 │
      │                      │────────────────────►│                    │
      │                      │                    │  Confirma con TB   │
      │                      │                    ├──────────────────►│
      │                      │                    │◄─── Aprobado       │
      │                      │◄─── Status OK      │                    │
      │  ✓ Éxito             │                    │  Stock actualizado │
      │                      │                    │  Carrito vacío     │
      └                      └                    └                    └
    """
    agregar_parrafo(doc, flujo_diagrama)
    
    doc.add_page_break()
    
    # ============ SECCIÓN 8: BASE DE DATOS ============
    agregar_titulo_seccion(doc, "8. BASE DE DATOS")
    
    agregar_subtitulo_seccion(doc, "Modelo de Datos Relacional")
    
    agregar_parrafo(doc, "Tabla: products", bold=True)
    tabla_products = [
        ["id", "codigo", "nombre", "categoria", "precio", "stock", "origen", "descripcion", "imagen"],
        ["1", "FR001", "Manzana Roja", "FR", "2500", "100", "Maule", "Manzana fresca...", "img/manzana.jpg"],
        ["2", "VR001", "Lechuga", "VR", "1500", "50", "Los Andes", "Lechuga orgánica...", "img/lechuga.jpg"],
    ]
    agregar_tabla(doc, tabla_products[0], tabla_products[1:])
    
    agregar_parrafo(doc, "Tabla: users", bold=True)
    tabla_users = [
        ["id", "email", "password (hash)", "nombre", "apellido", "rut", "telefono", "role"],
        ["1", "juan@email.com", "bcrypt_hash...", "Juan", "Pérez", "12.345.678-9", "912345678", "CLIENTE"],
    ]
    agregar_tabla(doc, tabla_users[0], tabla_users[1:])
    
    agregar_parrafo(doc, "Tabla: sales", bold=True)
    tabla_sales = [
        ["id", "fecha", "total", "estado", "tokenWs", "clienteNombre", "clienteEmail"],
        ["1", "2024-01-15 10:30", "7500", "PAGADO", "abc123xyz", "Juan Pérez", "juan@email.com"],
    ]
    agregar_tabla(doc, tabla_sales[0], tabla_sales[1:])
    
    agregar_parrafo(doc, "Tabla: saledetail", bold=True)
    tabla_saledetail = [
        ["id", "sale_id", "product_id", "cantidad", "precio"],
        ["1", "1", "1", "3", "2500"],
        ["2", "1", "2", "2", "1500"],
    ]
    agregar_tabla(doc, tabla_saledetail[0], tabla_saledetail[1:])
    
    agregar_parrafo(doc, "Relaciones (ER Diagram):", bold=True)
    relaciones = """
    products ──────────┐
                       ├──── saledetail ──── sales ──── users
    (1 a muchos)       │        (1)
    """
    agregar_parrafo(doc, relaciones)
    
    doc.add_page_break()
    
    # ============ SECCIÓN 11: EJEMPLOS DE CÓDIGO ============
    agregar_titulo_seccion(doc, "11. EJEMPLOS DE CÓDIGO")
    
    agregar_subtitulo_seccion(doc, "Ejemplo 1: ProductService.java - Método updateStock()")
    
    codigo_update_stock = """
    @Service
    public class ProductService {
      
      @Autowired
      private ProductRepository productRepository;
      
      // DESCRIPCIÓN: Resta cantidad vendida del stock disponible
      // PARÁMETROS: id (ID del producto), cantidadVendida (unidades vendidas)
      // RETORNA: Optional<Product> (el producto actualizado)
      public Optional<Product> updateStock(Long id, Integer cantidadVendida) {
        return productRepository.findById(id)
          .map(product -> {
            // Restar la cantidad vendida del stock actual
            product.setStock(product.getStock() - cantidadVendida);
            // Guardar cambios en BD
            return productRepository.save(product);
          });
      }
    }
    """
    agregar_parrafo(doc, codigo_update_stock)
    
    agregar_subtitulo_seccion(doc, "Ejemplo 2: AuthContext.jsx - Hook useAuth()")
    
    codigo_useauth = """
    export const useAuth = () => {
      const context = useContext(AuthContext);
      if (!context) {
        throw new Error('useAuth debe usarse dentro de AuthProvider');
      }
      return context;
    };
    
    // USO EN COMPONENTES:
    export function Login() {
      const { login, isLoggedIn } = useAuth();
      
      const handleSubmit = async (e) => {
        const result = await login(email, password);
        if (result.success) {
          navigate('/'); // Redirigir a home
        }
      };
    }
    """
    agregar_parrafo(doc, codigo_useauth)
    
    agregar_subtitulo_seccion(doc, "Ejemplo 3: CartContext.jsx - Método addToCart()")
    
    codigo_addtocart = """
    const addToCart = (producto, cantidad = 1) => {
      setCartItems(prevItems => {
        // Buscar si producto ya existe en carrito
        const existingItem = prevItems.find(
          item => item.codigo === producto.codigo
        );
        
        if (existingItem) {
          // Si existe, incrementar cantidad
          return prevItems.map(item =>
            item.codigo === producto.codigo
              ? { ...item, cantidad: item.cantidad + cantidad }
              : item
          );
        } else {
          // Si no existe, agregar como nuevo item
          return [...prevItems, { ...producto, cantidad }];
        }
      });
    };
    """
    agregar_parrafo(doc, codigo_addtocart)
    
    agregar_subtitulo_seccion(doc, "Ejemplo 4: SaleService.java - Método iniciarVenta()")
    
    codigo_iniciar_venta = """
    @Transactional
    public Map<String, Object> iniciarVenta(
      Sale saleData, 
      List<SaleRequest.ProductItem> items) throws Exception {
      
      // 1. Guardar venta con estado PENDIENTE
      Sale nuevaVenta = saleRepository.save(saleData);
      List<SaleDetail> detalles = new ArrayList<>();
      
      // 2. Para cada item en la orden
      for (SaleRequest.ProductItem item : items) {
        // Obtener producto de BD
        Product p = productApiService.obtenerProductoPorCodigo(item.getCodigo());
        
        if (p == null) {
          throw new RuntimeException("Producto no encontrado: " + item.getCodigo());
        }
        
        // Validar stock
        if (p.getStock() < item.getCantidad()) {
          throw new RuntimeException("Sin stock para: " + p.getNombre());
        }
        
        // Crear detalle de venta
        SaleDetail d = new SaleDetail();
        d.setSale(nuevaVenta);
        d.setProduct(p);
        d.setCantidad(item.getCantidad());
        d.setPrecio(p.getPrecio());
        detalles.add(d);
      }
      
      // 3. Contactar a Transbank
      WebpayPlusTransactionCreateResponse response = 
        new WebpayPlus.Transaction().create(
          "O-" + nuevaVenta.getId(),
          "S-" + System.currentTimeMillis(),
          nuevaVenta.getTotal(),
          returnUrl
        );
      
      // 4. Guardar token y retornar
      nuevaVenta.setTokenWs(response.getToken());
      saleRepository.save(nuevaVenta);
      
      return Map.of("token", response.getToken(), "url", response.getUrl());
    }
    """
    agregar_parrafo(doc, codigo_iniciar_venta)
    
    doc.add_page_break()
    
    # ============ SECCIÓN 13: BUENAS PRÁCTICAS ============
    agregar_titulo_seccion(doc, "13. BUENAS PRÁCTICAS IMPLEMENTADAS")
    
    practicas = {
        "Separación de Responsabilidades": [
            "Cada clase tiene una única responsabilidad",
            "Controladores: exponen endpoints",
            "Servicios: contienen lógica de negocio",
            "Repositories: acceso a datos",
            "DTOs: transferencia de datos",
        ],
        "Validación en Múltiples Capas": [
            "Frontend: validación inmediata para UX",
            "Backend: validación real (seguridad)",
            "BD: constraints para integridad referencial",
        ],
        "Manejo de Errores": [
            "Try-catch en operaciones que pueden fallar",
            "Mensajes de error claros para usuario",
            "Logging de errores para debugging",
            "Respuestas HTTP apropiadas (4xx, 5xx)",
        ],
        "Seguridad": [
            "Contraseñas encriptadas con BCrypt",
            "Tokens JWT con expiración",
            "CORS configurado",
            "Validación de RUT chileno",
            "Sin datos sensibles en localStorage (solo token)",
        ],
        "Performance": [
            "Paginación de productos (10 por página)",
            "Lazy loading de imágenes",
            "Caching en localStorage",
            "Minificación y compresión en producción",
        ],
        "Testing": [
            "Unit tests para funciones críticas",
            "Integration tests para flujos",
            "Coverage reports",
        ],
    }
    
    for practica, detalles in practicas.items():
        agregar_parrafo(doc, practica, bold=True)
        agregar_lista_bullets(doc, detalles)
    
    doc.add_page_break()
    
    # ============ SECCIÓN 14: CONCLUSIONES ============
    agregar_titulo_seccion(doc, "14. CONCLUSIONES")
    
    conclusiones = [
        {
            "titulo": "Arquitectura Moderna",
            "texto": "El proyecto implementa una arquitectura de microservicios que permite escalabilidad "
                    "y mantenibilidad independiente de cada servicio."
        },
        {
            "titulo": "Separación Frontend/Backend",
            "texto": "Frontend y backend están completamente desacoplados, permitiendo evolución "
                    "independiente y uso de diferentes tecnologías."
        },
        {
            "titulo": "Seguridad",
            "texto": "Se implementan prácticas de seguridad como encriptación de contraseñas, JWT, "
                    "validación en múltiples capas y CORS configurado."
        },
        {
            "titulo": "Escalabilidad",
            "texto": "El uso de microservicios y paginación permite que el sistema escale con el crecimiento "
                    "de usuarios y productos."
        },
        {
            "titulo": "Testing",
            "texto": "Se incluye testing automatizado para asegurar calidad del código."
        },
        {
            "titulo": "Experiencia Usuario",
            "texto": "Frontend reactivo con Context API proporciona experiencia fluida sin recargas "
                    "de página."
        },
    ]
    
    for conclusion in conclusiones:
        agregar_parrafo(doc, conclusion["titulo"], bold=True)
        agregar_parrafo(doc, conclusion["texto"])
    
    agregar_parrafo(doc, 
        "En resumen, Huerto Hogar es un proyecto profesional que demuestra conocimientos sólidos "
        "en arquitectura de software, backend robusto, frontend reactivo y buenas prácticas de "
        "desarrollo. Es un excelente ejemplo educativo de cómo construir un e-commerce moderno, "
        "escalable y seguro.")
    
    # Guardar
    output_path = "ANALISIS_CONCEPTUAL_COMPLETO_HUERTO_HOGAR.docx"
    doc.save(output_path)
    print(f"✅ DOCUMENTO FINAL GENERADO: {output_path}")
    print(f"📁 Ubicación: {os.path.abspath(output_path)}")
    print(f"📊 Tamaño estimado: ~200 KB")
    return output_path

if __name__ == "__main__":
    crear_documento_final()
