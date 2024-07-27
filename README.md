# Phone_checker
# Phone Number Checker

Este proyecto es una herramienta simple en Python para verificar información sobre números telefónicos usando la biblioteca `phonenumbers`. El script permite obtener la descripción y el nombre del proveedor del número de teléfono ingresado.

## Requisitos

- Python 3.x
- `phonenumbers` (se instalará automáticamente)

## Instalación

1. **Clona el repositorio (si corresponde):**

   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd <DIRECTORIO_DEL_PROYECTO>


2. **Crea y activa un entorno virtual:
   
   ```sh
    Copiar código
    python3 -m venv venv
    source venv/bin/activate

3.**Instala las dependencias:

    ```sh
    Copiar código
    pip install phonenumbers

##Uso

1.**Ejecuta el script:
Asegúrate de que tu entorno virtual esté activado y ejecuta el script:

    ```sh
    Copiar código
    python main.py
2.**Sigue las instrucciones:
El script te pedirá que ingreses un número de teléfono. Ingresa el número en formato internacional (por ejemplo, +14155552671) y presiona Enter.

El script devolverá la descripción del número y el nombre del proveedor en español.

##Ejemplo de salida

    ```sh
    Copiar código
    Digite su número telefónico: +14155552671
    ['Estados Unidos', 'Verizon']
