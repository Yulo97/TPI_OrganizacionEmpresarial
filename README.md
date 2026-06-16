# tpi-vacaciones

Proyecto simple en Python para simular el proceso de solicitud de vacaciones desde la consola.

## Requisitos

- Python 3.9 o superior
- Dependencias mínimas (solo se usa la librería estándar de Python)

## Instalación

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd tpi-vacaciones
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el programa:

```bash
python main.py
```

## Estructura del proyecto

- `main.py`: archivo principal que inicia la aplicación.
- `bot.py`: contiene la lógica del flujo del chatbot y la interacción con el usuario.
- `database.py`: carga y guarda los datos de los empleados, además de actualizar el saldo disponible.
- `utils.py`: funciones auxiliares para validación de fechas, mensajes de error y confirmaciones.
- `data/empleados.csv`: archivo con datos ficticios de empleados y saldo de vacaciones.
- `requirements.txt`: lista de dependencias del proyecto.

## Flujo del sistema

1. El usuario ingresa el ID del empleado.
2. El sistema muestra el nombre del empleado y su saldo disponible.
3. Se solicitan las fechas de inicio y fin de vacaciones.
4. El programa valida que las fechas sean correctas.
5. Se verifica si el empleado tiene saldo suficiente.
6. El usuario confirma o cancela la solicitud.
7. Si se confirma, el saldo se actualiza en el archivo CSV.

## Funcionalidades principales

- Buscar un empleado por ID.
- Validar formato de fechas.
- Calcular la cantidad de días solicitados.
- Verificar si hay saldo suficiente.
- Confirmar o cancelar una solicitud.
- Actualizar el saldo de vacaciones en la base de datos simulada.

## Cómo probar el sistema

- Puedes usar los datos del archivo CSV para seleccionar un empleado.
- El programa funciona completamente desde la consola.
- No necesitas configurar APIs ni servicios externos.

## Nota para docentes o evaluadores

Este proyecto está pensado como una versión simple y didáctica del manejo de solicitudes de vacaciones, con lógica básica y archivos simulados para facilitar la comprensión del flujo del proceso.
