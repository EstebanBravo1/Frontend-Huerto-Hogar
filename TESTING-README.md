# 🧪 Testing - Pruebas Unitarias

Este proyecto incluye pruebas unitarias desarrolladas con **Jasmine** y **Karma** según los requerimientos académicos.

## 📋 Dependencias Instaladas

- **jasmine**: Framework de testing para JavaScript
- **karma**: Test runner para ejecutar pruebas en navegadores
- **karma-jasmine**: Adaptador de Jasmine para Karma
- **karma-chrome-launcher**: Launcher para ejecutar tests en Chrome
- **karma-coverage**: Generador de reportes de cobertura
- **karma-spec-reporter**: Reporter detallado para resultados

## 🚀 Comandos de Testing

```bash
# Ejecutar tests una vez
npm run test:single

# Ejecutar tests en modo watch (observa cambios)
npm run test:watch

# Ejecutar tests con reporte de cobertura
npm run test:coverage

# Ejecutar tests (default en modo watch)
npm test
```

## 📁 Estructura de Tests

```
src/test/
├── setup.js          # Configuración global de tests
├── test-arrays.js     # Tests básicos con arrays
├── mocks.js          # Tests con mocks y spies
└── proyecto.test.js   # Tests específicos del proyecto
```

## 🎯 Tipos de Tests Incluidos

### 1. **Tests de Arrays** (`test-arrays.js`)
- ✅ Contar elementos
- ✅ Buscar elementos
- ✅ Filtrar elementos
- ✅ Sumar arrays

### 2. **Tests con Mocks** (`mocks.js`)
- ✅ Simulación de funciones
- ✅ Spies y contadores
- ✅ Mock de localStorage
- ✅ Tests asíncronos

### 3. **Tests del Proyecto** (`proyecto.test.js`)
- ✅ Formateo de precios
- ✅ Creación de productos
- ✅ Cálculo de carrito
- ✅ Búsqueda de productos
- ✅ Validación de usuarios

## 🔧 Configuración

- **karma.conf.js**: Configuración principal de Karma
- **spec/support/jasmine.json**: Configuración de Jasmine
- **src/test/setup.js**: Setup global para tests

## 📊 Reportes

Los tests generan reportes en:
- **Consola**: Resultados detallados durante ejecución
- **coverage/**: Reportes HTML de cobertura de código

## ⚡ Comandos Rápidos

```bash
# Instalar dependencias (ya están instaladas)
npm install

# Ejecutar tests una vez
npm run test:single

# Ver cobertura de código
npm run test:coverage
# Luego abrir: coverage/index.html
```

## 📝 Notas para el Profesor

- Tests implementados según requerimientos de IE2.2.1 y IE2.3.1
- Incluye mocks, spies y simulaciones
- Cobertura de código configurada
- Tests tanto básicos como específicos del proyecto e-commerce
- Documentación completa incluida