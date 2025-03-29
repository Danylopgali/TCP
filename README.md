# 🧪 TCP Server and Client in Python — Technical Test for Kosmos

This project implements a simple **TCP server and client** in Python. The communication uses the **TCP protocol over localhost**, as required in the technical test.

- The **server** listens for client connections and returns any received message in **uppercase**.
- If the message is `"DESCONEXION"` (must be in uppercase), the server closes the connection with that client.
- The **client** connects to the server, sends user input messages, and displays the server response.

---

## 📁 Project Structure

```
├── client.py
├── server.py
├── Dockerfile
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- Docker (for running the server container)
- `.env` file based on `.env.example`

---

## 🌱 Environment Variables

All configuration is done using environment variables. Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Example `.env` file:

```env
# Server (inside Docker)
TCP_SERVER_HOST=0.0.0.0
TCP_SERVER_PORT=5000

# Client (runs locally)
TCP_CLIENT_SERVER_HOST=127.0.0.1
TCP_CLIENT_SERVER_PORT=6000
```

---

## 🐍 Installing Python and Setting Up a Virtual Environment

1. **Install Python**  
    If Python is not installed on your system, download and install it from the official website:  
    [https://www.python.org/downloads/](https://www.python.org/downloads/)

    Verify the installation by running:
    ```bash
    python3 --version
    ```

2. **Create a Virtual Environment**  
    It is recommended to use a virtual environment to manage dependencies. Run the following commands:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate     # On Windows
    ```

3. **Install Required Dependencies**  
    Once the virtual environment is activated, install the necessary dependencies (if any) using:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🐳 Running the Server with Docker

> **Note:** macOS may block port 5000 due to ControlCenter. For that reason, we map the internal port 5000 to port 6000 on the host.

1. **Install Docker**  
     Download Docker Desktop:  
     [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. **Build the Docker image**  
     ```bash
     docker build -t tcp-server .
     ```

3. **Run the container**  
     ```bash
     docker run --env-file .env -p 6000:5000 tcp-server
     ```

---

## 💬 Running the Client

Make sure your environment variables are loaded:

On Linux/macOS:
```bash
export $(cat .env | grep TCP_CLIENT)
python3 client.py
```

On Windows PowerShell:
```powershell
$env:TCP_CLIENT_SERVER_HOST="127.0.0.1"
$env:TCP_CLIENT_SERVER_PORT="6000"
python client.py
```

---

## ✅ Manual Test Cases

1. **Send a normal message**  
     - Input: `hola servidor`  
     - Output: `HOLA SERVIDOR`

2. **Disconnect with "DESCONEXION"**  
     - Input: `DESCONEXION`  
     - Expected:  
        - Server disconnects the client  
        - Client prints: `Connection terminated.`

3. **Attempt lowercase disconnection**  
     - Input: `desconexion`  
     - Output: `[INFO] To disconnect, type 'DESCONEXION' in uppercase exactly.`

---

## ✍️ Author

Daniel López — Technical Test for Kosmos

---

## 🇪🇸 `README.es.md` — *Versión en español*

```markdown
# 🧪 Servidor y Cliente TCP en Python — Prueba Técnica para Kosmos

Este proyecto implementa un **servidor y cliente TCP** en Python. La comunicación se realiza usando el protocolo **TCP en localhost**, tal como lo requiere la prueba técnica.

- El **servidor** escucha conexiones de clientes y devuelve cualquier mensaje recibido en **mayúsculas**.
- Si el mensaje es `"DESCONEXION"` (debe estar en mayúsculas), el servidor cierra la conexión con ese cliente.
- El **cliente** se conecta al servidor, envía mensajes ingresados por el usuario y muestra la respuesta.

---

## 📁 Estructura del proyecto

```
├── client.py
├── server.py
├── Dockerfile
├── .env.example
├── .gitignore
└── README.md / README.es.md
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Docker (para ejecutar el servidor)
- Archivo `.env` basado en `.env.example`

---

## 🌱 Variables de entorno

Toda la configuración se gestiona con variables de entorno. Crea tu propio archivo `.env` a partir del ejemplo:

```bash
cp .env.example .env
```

Ejemplo de archivo `.env`:

```env
# Servidor (dentro del contenedor)
TCP_SERVER_HOST=0.0.0.0
TCP_SERVER_PORT=5000

# Cliente (desde tu máquina local)
TCP_CLIENT_SERVER_HOST=127.0.0.1
TCP_CLIENT_SERVER_PORT=6000
```

---

## 🐍 Instalar Python y Configurar un Entorno Virtual

1. **Instalar Python**  
    Si no tienes Python instalado, descárgalo e instálalo desde el sitio oficial:  
    [https://www.python.org/downloads/](https://www.python.org/downloads/)

    Verifica la instalación ejecutando:
    ```bash
    python3 --version
    ```

2. **Crear un Entorno Virtual**  
    Se recomienda usar un entorno virtual para gestionar las dependencias. Ejecuta los siguientes comandos:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate     # En Windows
    ```

3. **Instalar Dependencias**  
    Una vez activado el entorno virtual, instala las dependencias necesarias (si las hay) con:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🐳 Ejecutar el servidor con Docker

> **⚠️ Nota:** En macOS, el puerto 5000 puede estar ocupado por ControlCenter. Por eso, se mapea el puerto 5000 del contenedor al 6000 del host.

1. **Instalar Docker**  
     Descargar Docker Desktop:  
     [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. **Construir la imagen**  
     ```bash
     docker build -t tcp-server .
     ```

3. **Ejecutar el contenedor**  
     ```bash
     docker run --env-file .env -p 6000:5000 tcp-server
     ```

---

## 💬 Ejecutar el cliente

Cargar las variables y ejecutar el cliente:

En Linux/macOS:
```bash
export $(cat .env | grep TCP_CLIENT)
python3 client.py
```

En PowerShell (Windows):
```powershell
$env:TCP_CLIENT_SERVER_HOST="127.0.0.1"
$env:TCP_CLIENT_SERVER_PORT="6000"
python client.py
```

---

## ✅ Casos de prueba manuales

1. **Enviar un mensaje normal**  
     - Escribe: `hola servidor`  
     - Respuesta esperada: `HOLA SERVIDOR`

2. **Desconectarse con "DESCONEXION"**  
     - Escribe: `DESCONEXION`  
     - Resultado esperado:  
        - El servidor desconecta al cliente  
        - El cliente muestra: `Conexión terminada.`

3. **Intentar desconexión en minúsculas**  
     - Escribe: `desconexion`  
     - Resultado esperado: `[INFO] To disconnect, type 'DESCONEXION' in uppercase exactly.`

---

## ✍️ Autor

Daniel López — Prueba Técnica para Kosmos
```
