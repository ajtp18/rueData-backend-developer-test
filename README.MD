Documentación del Endpoint

El endpoint /api/upload/keylog.txt permite subir un archivo keylog.txt que contiene intentos de inicio de sesión en la banca electrónica. 

El archivo debe tener el formato correcto, donde cada intento de inicio de sesión consiste en tres caracteres.

Instalar requirements.txt para obtener las librerias necesarias:
    pip install -r requirements.txt


Método
PUT

URL
http://localhost:8000/api/upload/keylog.txt

Parámetros de entrada
* file (archivo): El archivo keylog.txt que se desea subir.
Respuesta exitosa
Si el archivo se sube correctamente y cumple con el formato esperado, el endpoint retornará un JSON con el código secreto más corto posible.

- Ejemplo de respuesta exitosa:
    {
    "secret_code": "38029716"
    }

* Errores posibles
Código de estado: 400 Bad Request

Detalle: "El archivo debe tener el nombre 'keylog.txt'."

- Posible causa: El archivo subido no se llama keylog.txt.

- Código de estado: 400 Bad Request

- Detalle: "Formato incorrecto del archivo. Cada intento debe tener 3 caracteres."

Posible causa: El archivo subido no cumple con el formato esperado.

- Documentación del Script de Solución
- El script de solución implementa un servidor FastAPI que maneja el endpoint /api/upload/keylog.txt para subir y procesar el archivo keylog.txt.

Requerimientos
   - Python 3.7 o superior
   - FastAPI
   - Ejecución
   - Asegúrate de tener los requerimientos instalados.
Guarda el script en un archivo con extensión .py (por ejemplo, keylog_api.py).
Desde la línea de comandos, ejecuta el siguiente comando para iniciar el servidor:
uvicorn keylog_api:app --host 0.0.0.0 --port 8000

Diagrama de Flujo
El diagrama de flujo muestra el flujo de ejecución del script de solución:

Inicio
    ├─ Definir función validate_format()
    │   ├─ Separar intentos de inicio de sesión en una lista
    │   ├─ Para cada intento:
    │   │      Si el intento no está vacío y no tiene 3 caracteres:
    │   │          Lanzar excepción HTTP (400 Bad Request)
    │   ├─ Fin Para
    │   ├─ Retornar sin errores
    ├─ Definir función upload_keylog()
    │   ├─ Decodificar el archivo en una cadena de texto
    │   ├─ Validar el formato del contenido del archivo
    │   ├─ Dividir los intentos de inicio de sesión en una lista
    │   ├─ Crear conjuntos para almacenar caracteres únicos y un diccionario para contar la frecuencia de aparición de cada carácter
    │   ├─ Para cada intento:
    │   │      Si el intento está vacío, continuar al siguiente
    │   │      Agregar los caracteres del intento al conjunto de caracteres únicos
    │   │      Actualizar la frecuencia de aparición de cada carácter
    │   ├─ Ordenar los caracteres por su frecuencia de aparición
    │   ├─ Construir el código secreto más corto uniéndolos en orden de frecuencia
    │   ├─ Imprimir el código secreto más corto
    │   ├─ Retornar el código secreto más corto en un JSON de respuesta exitosa
    ├─ Definir el endpoint /api/upload/keylog.txt (Método PUT)
    │   ├─ Recibir el archivo keylog.txt como parámetro
    │   ├─ Decodificar el contenido del archivo en una cadena de texto
    │   ├─ Validar el formato del contenido del archivo
    │   ├─ Procesar el archivo y encontrar el código secreto más corto
    │   ├─ Retornar el código secreto más corto en un JSON de respuesta exitosa
    ├─ Iniciar el servidor FastAPI en el puerto 8000
Fin

