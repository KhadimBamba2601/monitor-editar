import psutil
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox

# Función para mostrar el uso de CPU, memoria y disco
def mostrar_estadisticas_en_ventana():
    print("\n--- Estadísticas del Sistema ---")
    # Uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU: {uso_cpu}%")

    # Uso de memoria
    memoria = psutil.virtual_memory()
    print(f"Uso de Memoria: {memoria.percent}% (Usado: {memoria.used / (1024**3):.2f} GB / Total: {memoria.total / (1024**3):.2f} GB)")

    # Uso de disco
    disco = psutil.disk_usage('/')
    print(f"Uso de Disco: {disco.percent}% (Usado: {disco.used / (1024**3):.2f} GB / Total: {disco.total / (1024**3):.2f} GB)")

 # Crea un mensaje con las estadísticas formateado
    mensaje = f"""
    --- Estadísticas del Sistema ---
    Uso de CPU: {uso_cpu}%
    Uso de Memoria: {memoria.percent}% (Usado: {memoria.used / (1024**3):.2f} GB / Total: {memoria.total / (1024**3):.2f} GB
    Uso de Disco: {disco.percent}% (Usado: {disco.used / (1024**3):.2f} GB / Total: {disco.total / (1024**3):.2f} GB
    """
    # Crea una ventana emergente y muestra el mensaje
    ventana = tk.Tk()
    ventana.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Estadísticas del Sistema", mensaje)
    #Ejecutar la ventana
    ventana.destroy()

def monitorizar_sistema(duracion=15, intervalo=5):
    print("Iniciando monitorización del sistema...")
    inicio = datetime.now()
    try:
        while (datetime.now() - inicio).seconds < duracion:
            mostrar_estadisticas_en_ventana()
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nMonitorización detenida por el usuario.")
    finally:
        print("\nFinalizó la monitorización del sistema.")
# Ejecutar la monitorización    
if __name__ == "__main__":
    monitorizar_sistema(duracion=15, intervalo=5)
    
