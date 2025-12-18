# 🏆 GUÍA: Implementar Filtro con Backend (Mejor Práctica)

## 📋 Cambios a Realizar en `Productos.jsx`

### **CAMBIO 1: Importar `useNavigate`**

**Línea 1 - ANTES:**
```javascript
import { Link, useLoaderData, useSearchParams } from 'react-router-dom';
```

**Línea 1 - DESPUÉS:**
```javascript
import { Link, useLoaderData, useSearchParams, useNavigate } from 'react-router-dom';
```

---

### **CAMBIO 2: Agregar `useNavigate` y leer parámetro de categoría**

**Líneas 14-17 - ANTES:**
```javascript
const { addToCart } = useCart();
const [filtroActivo, setFiltroActivo] = useState('all');
const [searchParams] = useSearchParams();
const searchQuery = searchParams.get('search') || '';
```

**Líneas 14-18 - DESPUÉS:**
```javascript
const { addToCart } = useCart();
const navigate = useNavigate(); // Para navegar con parámetros
const [searchParams] = useSearchParams();
const searchQuery = searchParams.get('search') || '';
const categoriaParam = searchParams.get('categoria') || 'all';
```

---

### **CAMBIO 3: Agregar función para cambiar categoría**

**DESPUÉS de la línea 18, AGREGA:**
```javascript
// Función para cambiar de categoría (navega a nueva URL con parámetro)
const cambiarCategoria = (categoria) => {
    if (categoria === 'all') {
        navigate('/productos');
    } else {
        navigate(`/productos?categoria=${categoria}`);
    }
};
```

---

### **CAMBIO 4: Eliminar el filtro de categoría en el frontend**

**Líneas 31-42 - ANTES:**
```javascript
// Aplicar filtros en orden: primero búsqueda, luego categoría
let productosFiltrados = productos;

// Si hay búsqueda, filtrar por búsqueda primero
if (searchQuery) {
    productosFiltrados = filtrarPorBusqueda(productos, searchQuery);
}

// Luego aplicar filtro de categoría si no es 'all'
if (filtroActivo !== 'all') {
    productosFiltrados = productosFiltrados.filter(p => p.categoria_id === filtroActivo);
}
```

**Líneas 31-37 - DESPUÉS:**
```javascript
// Aplicar solo filtro de búsqueda (el filtro de categoría ya viene del backend)
let productosFiltrados = productos;

if (searchQuery) {
    productosFiltrados = filtrarPorBusqueda(productos, searchQuery);
}
```

---

### **CAMBIO 5: Actualizar TODOS los botones de filtro**

Busca TODOS los botones (hay 10 en total: 5 para desktop y 5 para móvil)

**ANTES (ejemplo con "Todos"):**
```javascript
<Button 
    variant={filtroActivo === 'all' ? 'primary' : 'outline-primary'}
    onClick={() => setFiltroActivo('all')}
    className="filter-btn-bootstrap"
>
    Todos
</Button>
```

**DESPUÉS:**
```javascript
<Button 
    variant={categoriaParam === 'all' ? 'primary' : 'outline-primary'}
    onClick={() => cambiarCategoria('all')}
    className="filter-btn-bootstrap"
>
    Todos
</Button>
```

**Repite este cambio para TODOS los botones:**
- `'all'` → Todos
- `'FR'` → Frutas Frescas
- `'VR'` → Verduras Orgánicas
- `'PO'` → Productos Orgánicos
- `'PL'` → Lácteos

---

## ✅ RESUMEN DE CAMBIOS

1. ✅ Importar `useNavigate`
2. ✅ Agregar `navigate` y `categoriaParam`
3. ✅ Crear función `cambiarCategoria`
4. ✅ Eliminar filtro de categoría en frontend
5. ✅ Cambiar `filtroActivo` por `categoriaParam` en todos los botones
6. ✅ Cambiar `setFiltroActivo` por `cambiarCategoria` en todos los botones

---

## 🧪 CÓMO PROBAR

Después de hacer los cambios:

1. Guarda el archivo
2. El servidor de Vite debería recargar automáticamente
3. Ve a `http://localhost:5173/productos`
4. Abre la consola del navegador (F12)
5. Haz clic en "Frutas Frescas"
6. Deberías ver en la consola:
   ```
   🔗 Conectando a: http://localhost:8080/api/products?categoria=FR
   ✅ Productos recibidos: [solo frutas]
   ```

---

## 🎯 BENEFICIOS DE ESTA SOLUCIÓN

✅ El backend filtra los productos (más eficiente)
✅ La URL refleja el filtro activo (`/productos?categoria=FR`)
✅ Puedes compartir URLs con filtros
✅ El botón "atrás" del navegador funciona
✅ El historial de navegación funciona correctamente
✅ SEO amigable

---

## 🚨 SI TIENES PROBLEMAS

Si después de hacer los cambios algo no funciona:

1. Verifica que Spring Boot esté corriendo
2. Abre la consola del navegador y busca errores
3. Verifica que la URL cambie cuando haces clic en un filtro
4. Comparte el error que aparece en la consola
