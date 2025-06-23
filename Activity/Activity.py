import tkinter as tk
from tkinter import messagebox

# Configuración principal
ventana = tk.Tk()
ventana.title("Camino hacia el Futuro: Desarrollador de IA")
ventana.geometry("1024x600")
ventana.config(bg="#282c34")
frame_central = tk.Frame(ventana, bg="#282c34")
frame_central.pack(expand=True)

# Variables globales
nombre = ""
etapa = 0
eleccion_final = ""
mensaje = "Bienvenido a tu aventura en IA"
indice = 0
mensaje_inicio = "🌟 Camino hacia el Futuro 🌟\nIngresá tu nombre para comenzar"
indice_texto = 0




# ----------- FUNCIONES -----------

def mostrar_pantalla_inicio():
    texto_inicio.pack(pady=20)
    entry_nombre.pack(pady=10)
    boton_comenzar.pack(pady=10)
    ocultar_elementos_juego()


def ocultar_pantalla_inicio():
    texto_inicio.pack_forget()
    entry_nombre.pack_forget()
    boton_comenzar.pack_forget()

def mostrar_elementos_juego():
    texto_juego.pack(pady=30)
    boton_opcion1.pack(pady=5)
    boton_opcion2.pack(pady=5)
    boton_opcion3.pack(pady=5)

def ocultar_elementos_juego():
    texto_juego.pack_forget()
    boton_opcion1.pack_forget()
    boton_opcion2.pack_forget()
    boton_opcion3.pack_forget()

def comenzar_juego():
    global nombre
    nombre = entry_nombre.get()
    if not nombre.strip():
        messagebox.showwarning("Falta el nombre", "Por favor ingresá tu nombre para empezar.")
        return
    ocultar_pantalla_inicio()
    avanzar_etapa()

def animar_inicio():
    global indice_texto
    if indice_texto < len(mensaje_inicio):
        texto_actual = texto_inicio.cget("text")
        texto_inicio.config(text=texto_actual + mensaje_inicio[indice_texto])
        indice_texto += 1
        ventana.after(40, animar_inicio)
    else:
        entry_nombre.pack(pady=10)
        boton_comenzar.pack(pady=10)

def mostrar_pantalla_inicio():
    texto_inicio.config(text="")
    texto_inicio.pack(pady=20)
    ocultar_elementos_juego()
    animar_inicio()


def avanzar_etapa():
    global etapa
    etapa += 1
    mostrar_elementos_juego()

    if etapa == 1:
        texto_juego.config(text=f"Bienvenido, {nombre}. ¿Dónde querés estudiar para convertirte en un Desarrollador de IA?")
        boton_opcion1.config(text="Universidad de Buenos Aires (UBA)", command=lambda: elegir("UBA"))
        boton_opcion2.config(text="MIT", command=lambda: elegir("MIT"))
        boton_opcion3.config(text="Cursos online (Coursera)", command=lambda: elegir("Online"))
    elif etapa == 2:
        texto_juego.config(text="Elegí tu primer proyecto de inteligencia artificial:")
        boton_opcion1.config(text="Chatbot filosófico", command=lambda: elegir("Chatbot"))
        boton_opcion2.config(text="Sistema que predice enfermedades", command=lambda: elegir("Salud"))
        boton_opcion3.config(text="App de memes con IA", command=lambda: elegir("Memes"))
    elif etapa == 3:
        texto_juego.config(text="¿Qué camino profesional querés seguir?")
        boton_opcion1.config(text="Trabajar en una empresa internacional", command=lambda: elegir("Empresa"))
        boton_opcion2.config(text="Crear tu propia startup", command=lambda: elegir("Startup"))
        boton_opcion3.config(text="Hacer un doctorado y enseñar", command=lambda: elegir("Docencia"))
    elif etapa == 4:
        mostrar_final()

def elegir(opcion):
    global eleccion_final
    respuestas = {
        "UBA": "📚 Estudiás en la UBA y te unís a un grupo de investigación en IA.",
        "MIT": "🚀 Estudiás en MIT y participás en proyectos con robots inteligentes.",
        "Online": "💻 Completás cursos online mientras trabajás como freelancer.",
        "Chatbot": "🤖 Tu chatbot filosófico te lleva a una charla TED.",
        "Salud": "🧬 Tu IA médica salva vidas y ganás una beca.",
        "Memes": "😂 Tu app de memes se vuelve viral y educativa.",
        "Empresa": "🌍 Te contratan en OpenAI para desarrollar nuevas tecnologías.",
        "Startup": "🚀 Fundás una startup y ayudás a mejorar el mundo.",
        "Docencia": "📘 Enseñás IA y creás una comunidad de aprendizaje."
    }

    if opcion in ["Empresa", "Startup", "Docencia"]:
        eleccion_final = opcion

    messagebox.showinfo("Decisión", respuestas[opcion])
    avanzar_etapa()

def mostrar_final():
    ocultar_elementos_juego()

    finales = {
        "Empresa": f"🎯 {nombre}, ahora formás parte de una empresa de clase mundial, desarrollando tecnología que cambia vidas. ¡Estás construyendo el futuro con IA!",
        "Startup": f"🚀 {nombre}, fundaste tu propia startup y ahora liderás un equipo que crea soluciones inteligentes para el mundo real. ¡Sos un innovador nato!",
        "Docencia": f"📘 {nombre}, como investigador y docente, formás nuevas generaciones de mentes brillantes. ¡Sos una inspiración en el mundo de la IA!"
    }

    texto_juego.config(text=finales.get(eleccion_final, "🎉 ¡Felicitaciones! Completaste tu viaje hacia tu trabajo ideal como Desarrollador de IA."))
    texto_juego.pack(pady=40)

# ----------- INTERFAZ -----------

# Pantalla de inicio (centrada dentro del frame)
texto_inicio = tk.Label(frame_central, text="", font=("Arial", 16), fg="white", bg="#282c34", wraplength=500)
entry_nombre = tk.Entry(frame_central, font=("Arial", 14))
boton_comenzar = tk.Button(frame_central, text="Iniciar Aventura", font=("Arial", 14), command=comenzar_juego)

# Elementos del juego (también centrados)
texto_juego = tk.Label(frame_central, text="", font=("Arial", 14), wraplength=550, fg="white", bg="#282c34")
boton_opcion1 = tk.Button(frame_central, text="", font=("Arial", 12), width=40)
boton_opcion2 = tk.Button(frame_central, text="", font=("Arial", 12), width=40)
boton_opcion3 = tk.Button(frame_central, text="", font=("Arial", 12), width=40)

# Mostrar inicio al arrancar
mostrar_pantalla_inicio()

# Ejecutar ventana
ventana.mainloop()





