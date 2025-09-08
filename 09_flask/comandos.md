**<h1 align="center">Ejemplo 09 - Comandos</h1>**  

## **Entorno virtual**
Es un espacio aislado en el cual intérprete, bibliotecas y scripts de Python están aislados de la instalación del sistema y de otros entornos virtuales. Por lo que cada proyecto contiene solamente las dependencias que necesita, lo que facilita la posibilidad de compartir el proyecto y que otros desarrolladores puedan replicarlo e instalar solo las dependencias necesarias.  

### **Crear entorno**  
```
python -m venv nombre_entorno
```  

### **Activar entorno virtual**  
```
nombre_entorno/Scripts/activate
```  

### **Instalar bibliotecas**  
```
pip install nombre_biblioteca
```  

### **Generar listado de bibliotecas**  
```
pip freeze > requirements.txt
```  

### **Desactivar entorno virtual**  
```
deactivate
```  

### **Instalar bibliotecas desde requirements**
```
pip install -r requirements.txt
```

> [!NOTE]  
> Documentación entornos virtuales: https://docs.python.org/es/3/tutorial/venv.html

## **Flask**
Flask es un “micro” framework web minimalista y ligero para el lenguaje de programación Python, diseñado para facilitar la creación de aplicaciones web de forma rápida y con pocas líneas de código.

### **Instalar Flask**
```
pip install flask
```

### **Instalar CORS**  
CORS: Cross Origin Resource Sharing, permite a servidores en diferentes dominios pueda intercambiar  o compartir recursos.
```
pip install flask-cors
```  
  
> [!NOTE]  
> Documentación entornos virtuales: https://flask.palletsprojects.com/en/stable/