# School Management Module for Odoo

## Puntos de Aprendizaje

Durante el desarrollo de este módulo, he aprendido y adquirido varias habilidades clave relacionadas con Odoo y su entorno de desarrollo:

- **Instalación de Odoo Localmente:** Aprendí a instalar Odoo en mi PC de manera local, tanto usando el instalador oficial como a través de un repositorio de GitHub.
  
- **Estructura de Carpetas de los Módulos:** Comprendí cómo está organizada la estructura de carpetas de los módulos en Odoo y para qué sirve cada archivo que compone un módulo, como modelos, vistas, archivos de seguridad, y archivos de configuración.
  
- **Creación de Modelos y Vistas:** Aprendí a crear modelos, vistas y formularios en Odoo, definiendo campos, relaciones y ajustando las vistas para satisfacer los requisitos específicos de la aplicación.

- **Modo Desarrollador en Odoo:** Descubrí cómo activar el modo desarrollador en Odoo para poder ver y gestionar los módulos personalizados.

- **Ejecución de Odoo a través de la Terminal:** Aprendí a ejecutar Odoo y gestionar módulos a través de comandos en la terminal, lo que me permitió tener un control más directo sobre la ejecución y depuración.

- **Creación de Relaciones entre Tablas:** Aprendí cómo crear y gestionar relaciones entre diferentes tablas en Odoo utilizando tipos de campos como `Many2many`, `Many2one` y `One2many`.

## Errores Resueltos e Inconvenientes Encontrados

Durante la instalación y configuración del entorno de desarrollo, me encontré con varios errores y desafíos que logré resolver:

- **Conflicto con PostgreSQL Instalado Previamente:**
  - Al instalar Odoo usando el instalador oficial, tuve problemas porque ya tenía una versión de PostgreSQL instalada en mi PC. El servicio de PostgreSQL existente estaba causando conflictos con la versión que intentaba instalar Odoo.
  - Después de varios intentos de instalación y reinicios, decidí eliminar completamente PostgreSQL de mi PC e instalar todo desde cero utilizando el instalador de Odoo. Esta solución resolvió el conflicto y me permitió avanzar.

- **Problema con el Modo Desarrollador:**
  - Una vez instalada la base de datos y creado el módulo, no podía encontrar la opción para habilitar el modo desarrollador en la interfaz de Odoo. Esto me impedía ver y gestionar el módulo creado.
  - Opté por instalar Odoo desde un repositorio de GitHub, lo que me dio más control sobre el entorno de desarrollo.

- **Clonación del Repositorio de GitHub:**
  - Inicialmente, tuve problemas al clonar el repositorio de Odoo debido a su gran tamaño. Como alternativa, decidí descargar el repositorio como un archivo ZIP y luego descomprimirlo en mi máquina local. Aunque este proceso tomó tiempo, funcionó correctamente.

- **Errores al Instalar Requerimientos:**
  - Al intentar correr el entorno, me encontré con errores al instalar los requisitos de Odoo. Después de investigar, descubrí que el problema era causado por una versión desactualizada de Microsoft C++.
  - Solucioné este problema descargando el paquete "Build Tools for Visual Studio" desde la página oficial de Microsoft e instalando todos los módulos necesarios. Esto resolvió los errores y me permitió continuar con la instalación de los requisitos.

- **Ejecución y Visualización del Módulo:**
  - Una vez que instalé Odoo y solucioné los problemas con los requerimientos, añadí mi módulo personalizado al proyecto y lo ejecuté a través de la terminal.
  - Después, habilité el modo desarrollador en Odoo y pude ver mi módulo funcionando correctamente.

## Conclusión

Este proceso me permitió entender mejor cómo funciona Odoo, tanto desde el punto de vista del desarrollo de módulos personalizados como en la configuración del entorno de desarrollo. Pude superar varios problemas técnicos, lo que me dio una comprensión más profunda de la administración y configuración de aplicaciones en Odoo.

---

¡Gracias por leer este resumen de mi aprendizaje y experiencia desarrollando el módulo de gestión escolar para Odoo!
