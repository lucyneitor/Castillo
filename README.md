# 🚀 EcoTech Solutions - Sistema de Gestión Empresarial

Repositorio oficial para la **Evaluación Sumativa 2 (Unidad 2)** de la asignatura **Programación Orientada a Objeto Seguro** (INACAP Sede Chillán). 

Desarrollado íntegramente en **Python**, este repositorio implementa el modelo de clases de EcoTech Solutions estructurado bajo el patrón **MVC** y **DAO**. El sistema aplica los principios de la Programación Orientada a Objetos, asegura la persistencia de datos mediante librerías oficiales, garantiza la estabilidad operativa con manejo de errores y contempla una evaluación crítica de las prácticas de codificación asistidas por IA.

---

## 📋 Tabla de Contenidos
- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Modelo de Clases (UML)](#-modelo-de-clases-uml)
- [Arquitectura del Sistema (MVC + DAO)](#-arquitectura-del-sistema-mvc--dao)
- [Estructura del Proyecto](#-estructura-del-proyecto)

---

## 📌 Descripción del Proyecto
El sistema **EcoTech Solutions** responde a la necesidad de gestionar de forma integral los recursos corporativos de la empresa, abarcando entidades clave como **Empleados**, **Departamentos**, **Proyectos**, **Tiempos**, **Usuarios** e **Informes**. El diseño cumple estrictamente con el diagrama UML de clases validado, aplicando los principios de encapsulamiento, herencia y modularidad en Python.

---

## 📐 Modelo de Clases (UML)
El sistema modela las siguientes entidades de negocio principales:
* **Usuario:** Gestiona credenciales de acceso (`user`, `contrasena`), autenticación y control de permisos.
* **Empleado:** Entidad que hereda de Usuario, con atributos propios (`id_empleado`, `nombre`, `direccion`, `telefono`, `correo`, `sueldo`, etc.) y relaciones con proyectos y departamentos.
* **Departamento:** Agrupa empleados bajo la dirección de un gerente, permitiendo búsquedas y reasignaciones de personal.
* **Proyecto y Tiempo:** Controlan la asignación de tareas, cronogramas y horas trabajadas por los colaboradores.
* **Informe:** Permite generar reportes operativos y administrativos de la empresa.

---

## 🏛️ Arquitectura del Sistema (MVC + DAO)
El repositorio se encuentra estructurado bajo un enfoque desacoplado y profesional:
* **`config/`**: Gestiona la conexión centralizada a la base de datos relacional.
* **`models/`**: Contiene las clases de entidad (POO) y las clases DAO encargadas exclusivamente de la persistencia y ejecución de operaciones SQL.
* **`controllers/`**: Administran la lógica de negocio, sirviendo de puente entre las vistas y los modelos.
* **`views/`**: Manejan la interacción con el usuario (interfaz de consola o menús interactivos).

---

## 📂 Estructura del Proyecto

```text
ecotech-gestion-empresarial/
│
├── config/
│   ├── __init__.py
│   └── database.py          
├── controllers/
│   ├── __init__.py
│   ├── departamento_controller.py
│   ├── empleado_controller.py
│   ├── proyecto_controller.py
│   ├── usuario_controller.py
│   ├── tiempo_controller.py
│   ├── administrador_controller.py
│   ├── informe_controller.py
│   └── main_controller.py
├── models/
│   ├── departamento.py      
│   ├── departamento_dao.py  
│   ├── empleado.py          
│   ├── empleado_dao.py      
│   └── proyecto.py
│   ├── proyecto_dao.py
│   ├── usuario.py
│   ├── usuario_dao.py
│   ├── tiempo.py
│   ├── tiempo_dao.py
│   ├── administrador.py
│   ├── administrador_dao.py
│   ├── informe.py
│   └── informe_dao.py
├── views/
│   ├── __init__.py
│   ├── departamento_view.py
│   ├── empleado_view.py
│   ├── proyecto_view.py
│   ├── usuario_view.py
│   ├── tiempo_view.py
│   ├── administrador_view.py
│   ├── informe_view.py
│   └── main_view.py 
├── imagenes/               
├── ecotech.db               
├── main.py                  
├── requirements.txt
└── README.md