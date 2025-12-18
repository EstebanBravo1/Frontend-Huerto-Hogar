// karma.conf.js
export default function(config) {
  config.set({
    // Framework de testing
    frameworks: ['jasmine'],

    // Archivos a incluir en las pruebas
    files: [
      'src/test/setup.js',
      'src/test/**/*.js'
      // Excluimos src/data por conflictos con ES modules
    ],

    // Navegadores donde ejecutar las pruebas
    browsers: ['Chrome'],

    // Reporter para mostrar resultados
    reporters: ['spec', 'coverage'],

    // Configuración de cobertura
    coverageReporter: {
      type: 'html',
      dir: 'coverage/'
    },

    // Preprocesadores
    preprocessors: {
      'src/test/**/*.js': ['coverage']
    },

    // Puerto del servidor
    port: 9876,

    // Colores en la consola
    colors: true,

    // Nivel de log
    logLevel: config.LOG_INFO,

    // Watch de archivos
    autoWatch: true,

    // Salir después de ejecutar
    singleRun: false,

    // Tiempo límite para las pruebas
    browserNoActivityTimeout: 60000,

    // Cliente configuration
    client: {
      clearContext: false // leave Jasmine Spec Runner output visible in browser
    }
  });
};