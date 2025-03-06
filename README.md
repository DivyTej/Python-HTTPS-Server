# Python-HTTPS-Server

## Features

### Main Features

1. **Starts Encrypted Python Server**: Starts encrypted https python server.

---

## Installation

1. Clone the repository (if applicable):
   ```bash
   git clone https://github.com/DivyTej/Python-HTTPS-Server.git
   cd Python-HTTPS-Server
   ```

---

## Example Workflow

### Input File
- Certificate & Key file

### Running the Script
1. Make the required files:
   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
   ```
   
2. Execute the script:
   ```bash
   python https_server.py
   ```

3. Example output:
   ```
  2025-03-06 08:35:15,310 - INFO - Serving HTTPS on 0.0.0.0:8080 with SSL encryption.
  ^C2025-03-06 08:35:17,631 - INFO - 
  Server is shutting down...
  2025-03-06 08:35:17,631 - INFO - Server stopped gracefully.
   ```

---


## Contact

For questions or support, please contact [Divy Tej](https://linkedin.com/in/divytej).

---
