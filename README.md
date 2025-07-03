# 🍅 Pomodoro Timer
Un cronómetro Pomodoro elegante y funcional desarrollado en Python con interfaz gráfica moderna, estadísticas detalladas y notificaciones sonoras.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Características
- 🎯 **Temporizador Pomodoro Completo**: Ciclos de trabajo y descanso personalizables
- 📊 **Estadísticas Detalladas**: Seguimiento diario, total y racha de días consecutivos
- 🔊 **Notificaciones Sonoras**: Alertas diferenciadas para trabajo y descanso
- 🎨 **Interfaz Moderna**: Diseño limpio y profesional con ttkbootstrap
- ⚙️ **Configuración Flexible**: Ajusta los tiempos según tus necesidades
- 💾 **Persistencia de Datos**: Las estadísticas se guardan automáticamente
- 🚀 **Ejecutable**: Funciona sin necesidad de instalar Python


## Estructura del proyecto:
```
pomodoro-timer/
├── pomodoro.py           # Código principal
├── requirements.txt      # Dependencias
├── README.md            # Este archivo
├── LICENSE              # Licencia
└── dist/                # Ejecutable generado
    └── Pomodoro Timer.exe
```

## 🚀 Instalación
### Opción 1: Ejecutar desde código fuente
1. **Clona el repositorio:**
   ```
   git clone https://github.com/crosaless/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. **Instala las dependencias:**
   ```
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```
   python pomodoro.py
   ```

### Opción 2: Ejecutable (Windows)
1. Descarga el archivo `Pomodoro Timer.exe` desde la carpeta "dist"
2. Ejecuta el archivo descargado
3. ¡Listo! No necesitas instalar Python


## 🎯 Uso
### Configuración Básica

**Configura los tiempos:**
- **Trabajo**: Tiempo de concentración (default: 25 min)
- **Descanso corto**: Pausa breve (default: 5 min)
- **Descanso largo**: Pausa larga cada 4 pomodoros (default: 15 min)

**Inicia el temporizador:**
- Haz clic en "Iniciar" para comenzar
- El temporizador alternará automáticamente entre trabajo y descanso

**Controla la sesión:**
- **Parar**: Pausa el temporizador actual
- **Reiniciar**: Vuelve al estado inicial

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NewFeature`)
3. Commit tus cambios (`git commit -m 'Add some NewFeature'`)
4. Push a la rama (`git push origin feature/NewFeature`)
5. Abre un Pull Request

## 💡 Ideas para contribuir

- [ ] Soporte para sonidos personalizados
- [ ] Exportar estadísticas a CSV
- [ ] Modo oscuro/claro
- [ ] Integración con calendario
- [ ] Notificaciones del sistema
- [ ] Múltiples perfiles de usuario
