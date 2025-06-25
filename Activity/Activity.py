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
eleccion_estudios = ""
eleccion_proyecto = ""
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
        texto_juego.config(text=f"Bienvenido, {nombre}. ¿Dónde querés estudiar para convertirte en un Desarrollador de software especializado en IA?")
        boton_opcion1.config(text="Universidad Tecnológica Nacional (UTN)", command=lambda: elegir("UTN"))
        boton_opcion2.config(text="FaMAF", command=lambda: elegir("FaMAF"))
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
    global eleccion_estudios, eleccion_proyecto, eleccion_final

    respuestas = {
        "UTN": "📚 Estudiás en la UTN y te unís a un grupo de investigación en IA.",
        "FaMAF": "🚀 Estudiás en FaMAF y participás en proyectos con modelos matemáticos avanzados.",
        "Online": "💻 Completás cursos online mientras trabajás como freelancer.",
        "Chatbot": "🤖 Tu chatbot filosófico te lleva a una charla TED.",
        "Salud": "🧬 Tu IA médica salva vidas y ganás una beca.",
        "Memes": "😂 Tu app de memes se vuelve viral y educativa.",
        "Empresa": "🌍 Te contratan en OpenAI para desarrollar nuevas tecnologías.",
        "Startup": "🚀 Fundás una startup y ayudás a mejorar el mundo.",
        "Docencia": "📘 Enseñás IA y creás una comunidad de aprendizaje."
    }

    if etapa == 1:
        eleccion_estudios = opcion
    elif etapa == 2:
        eleccion_proyecto = opcion
    elif etapa == 3:
        eleccion_final = opcion

    messagebox.showinfo("Decisión", respuestas[opcion])
    avanzar_etapa()


def mostrar_final():
    ocultar_elementos_juego()

    combinacion = (eleccion_estudios, eleccion_proyecto, eleccion_final)

    
    finales_personalizados = {
    ("UTN", "Chatbot", "Empresa"): f"{nombre}, estudiaste en la UTN, donde desarrollaste un chatbot filosófico que llamó la atención de una empresa internacional. Hoy aplicás pensamiento crítico en sistemas de IA para el mundo corporativo.",
    ("UTN", "Chatbot", "Startup"): f"{nombre}, desde la UTN y con tu chatbot filosófico como carta de presentación, fundaste una startup que revoluciona la educación con inteligencia artificial conversacional.",
    ("UTN", "Chatbot", "Docencia"): f"{nombre}, tu formación en la UTN y tu chatbot te inspiraron a enseñar sobre ética en IA. Hoy sos un referente académico en universidades tecnológicas.",

    ("UTN", "Salud", "Empresa"): f"{nombre}, tu paso por la UTN te permitió desarrollar una IA médica de precisión. Una multinacional de salud te contrató para liderar investigaciones en tecnología biomédica.",
    ("UTN", "Salud", "Startup"): f"{nombre}, desde tus bases en la UTN creaste una IA que predice enfermedades. Ahora liderás tu propia startup que mejora la salud pública en zonas vulnerables.",
    ("UTN", "Salud", "Docencia"): f"{nombre}, gracias a tu experiencia en la UTN y tu sistema de predicción médica, hoy enseñás en institutos de salud y formás nuevas generaciones de tecnólogos sanitarios.",

    ("UTN", "Memes", "Empresa"): f"{nombre}, comenzaste en la UTN con una app de memes con IA y una empresa de marketing digital te contrató para liderar su área creativa de contenido automatizado.",
    ("UTN", "Memes", "Startup"): f"{nombre}, tu paso por la UTN y tu talento con los memes te llevó a crear una startup de entretenimiento con IA que es furor en redes sociales.",
    ("UTN", "Memes", "Docencia"): f"{nombre}, usaste la creatividad que desarrollaste en la UTN para enseñar programación a jóvenes con humor y recursos visuales. Hoy sos educador tech con impacto real.",

    ("FaMAF", "Chatbot", "Empresa"): f"{nombre}, tu sólida formación en FaMAF y un chatbot filosófico único te abrieron las puertas de una empresa de IA aplicada a derechos humanos.",
    ("FaMAF", "Chatbot", "Startup"): f"{nombre}, desde FaMAF creaste un chatbot con capacidad de razonamiento lógico. Fundaste una startup de asistentes virtuales que piensan antes de responder.",
    ("FaMAF", "Chatbot", "Docencia"): f"{nombre}, uniendo tu carrera en FaMAF y tu pasión por la filosofía, hoy enseñás sobre lenguajes formales y ética computacional en la universidad.",

    ("FaMAF", "Salud", "Empresa"): f"{nombre}, tu precisión matemática de FaMAF fue clave para diseñar una IA médica. Hoy trabajás para una empresa de biotecnología desarrollando algoritmos predictivos.",
    ("FaMAF", "Salud", "Startup"): f"{nombre}, tu proyecto de salud basado en IA y tu visión científica de FaMAF te llevaron a crear una startup que optimiza diagnósticos con inteligencia artificial.",
    ("FaMAF", "Salud", "Docencia"): f"{nombre}, con tu formación en FaMAF y tu interés en salud, te convertiste en docente de ciencia de datos aplicada a la medicina. Formás parte de un cambio vital.",

    ("FaMAF", "Memes", "Empresa"): f"{nombre}, los conocimientos técnicos de FaMAF y tu app de memes con IA te posicionaron en una empresa de contenido interactivo donde liderás proyectos virales.",
    ("FaMAF", "Memes", "Startup"): f"{nombre}, combinaste la lógica de FaMAF con la creatividad de tu app de memes y fundaste una startup que transforma el aprendizaje en experiencias divertidas.",
    ("FaMAF", "Memes", "Docencia"): f"{nombre}, tu enfoque matemático y tu app de memes educativa te hicieron pionero en enseñar ciencia de forma lúdica. Sos referente de innovación educativa.",

    ("Online", "Chatbot", "Empresa"): f"{nombre}, te formaste por tu cuenta y creaste un chatbot increíble. Una empresa tecnológica notó tu talento autodidacta y te contrató como desarrollador principal.",
    ("Online", "Chatbot", "Startup"): f"{nombre}, aprendiendo online, lograste diseñar un chatbot filosófico viral. Hoy liderás una startup de comunicación consciente entre humanos y máquinas.",
    ("Online", "Chatbot", "Docencia"): f"{nombre}, con tu experiencia como autodidacta, enseñás a otros a desarrollar sus propios chatbots. Democratizás el conocimiento de IA desde cero.",

    ("Online", "Salud", "Empresa"): f"{nombre}, aunque estudiaste de forma online, lograste crear una IA médica tan efectiva que una empresa internacional te sumó a su equipo de investigación aplicada.",
    ("Online", "Salud", "Startup"): f"{nombre}, tus conocimientos digitales y tu app de salud basada en IA impactaron en miles de personas. Fundaste una startup sin fronteras.",
    ("Online", "Salud", "Docencia"): f"{nombre}, combinaste tu formación online y tu IA médica para formar a nuevos profesionales de forma remota. Sos referente global en educación digital en salud.",

    ("Online", "Memes", "Empresa"): f"{nombre}, tu creatividad autodidacta y tu app de memes basada en IA hicieron que una empresa de entretenimiento te fichara como líder creativo de proyectos virales.",
    ("Online", "Memes", "Startup"): f"{nombre}, tu espíritu emprendedor te llevó a fundar una startup desde tu casa con IA para crear contenido humorístico personalizado. Sos viral y disruptivo.",
    ("Online", "Memes", "Docencia"): f"{nombre}, tu historia inspira: aprendiste online, creaste una app educativa de memes y ahora enseñás a chicos a programar jugando. Sos puro ejemplo."
    }


    final = finales_personalizados.get(
        combinacion,
        f"🎉 {nombre}, completaste tu viaje como Desarrollador de IA con un camino único e inspirador. ¡El futuro es tuyo!"
    )

    texto_juego.config(text=final)
    texto_juego.pack(pady=40)
    boton_reiniciar.pack(pady=10)


def reiniciar_juego():
    global etapa, nombre, eleccion_estudios, eleccion_proyecto, eleccion_final, indice_texto
    etapa = 0
    nombre = ""
    eleccion_estudios = ""
    eleccion_proyecto = ""
    eleccion_final = ""
    indice_texto = 0

    texto_inicio.config(text="")
    entry_nombre.delete(0, tk.END)
    boton_reiniciar.pack_forget()
    mostrar_pantalla_inicio()


# ----------- INTERFAZ -----------

# Pantalla de inicio
texto_inicio = tk.Label(frame_central, text="", font=("Arial", 16), fg="white", bg="#282c34", wraplength=500)
entry_nombre = tk.Entry(frame_central, font=("Arial", 14))
boton_comenzar = tk.Button(frame_central, text="Iniciar Aventura", font=("Arial", 14), command=comenzar_juego)
boton_reiniciar = tk.Button(frame_central, text="Volver a empezar", font=("Arial", 12), command=lambda: reiniciar_juego())

# Elementos del juego
texto_juego = tk.Label(frame_central, text="", font=("Arial", 14), wraplength=550, fg="white", bg="#282c34")
boton_opcion1 = tk.Button(frame_central, text="", font=("Arial", 12), width=40)
boton_opcion2 = tk.Button(frame_central, text="", font=("Arial", 12), width=40)
boton_opcion3 = tk.Button(frame_central, text="", font=("Arial", 12), width=40)

# Mostrar inicio al arrancar
mostrar_pantalla_inicio()

# Ejecutar ventana
ventana.mainloop()