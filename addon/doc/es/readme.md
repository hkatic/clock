# Complemento de reloj y calendario para NVDA #

* Autores: Hrvoje Katić, Abdel y colaboradores de NVDA
* Compatibilidad con NVDA: 2019.3 y posterior

Este complemento habilita las funciones avanzadas de reloj, temporizador de alarma y calendario para NVDA.

Puedes configurar NVDA para anunciar la hora y la fecha en formatos distintos a los proporcionados por Windows de forma predeterminada. Además, puedes obtener el día actual, el número de semana, así como los días restantes hasta el final del año en curso, y también puedes configurar el anuncio automático de la hora en un intervalo determinado. También incluye funciones de cronómetro y temporizador de alarma integradas en el complemento, que permiten medir tareas como copiar archivos, instalar programas o cocinar.

Notas:

* si instalas el complemento como una actualización, durante el proceso de instalación el asistente detecta si la configuración anterior es compatible con la nueva y ofrece corregirla antes de instalarlo; después solo tendrás que confirmar con el botón Aceptar.
* En Windows 10 y posteriores, puedes usar la aplicación Alarmas y reloj para gestionar cronómetros y temporizadores.

## Teclas de órdenes

* NVDA+F12: obtener la hora actual
* NVDA+F12 pulsado dos veces rápidamente: obtener la fecha actual
* NVDA+F12 pulsado tres veces rápidamente: anuncia el día actual, el número de semana, el año actual y los días restantes hasta el final del año
* NVDA+Shift+F12: entrar en la capa del reloj

## Órdenes sin asignar

Las siguientes órdenes no están asignadas por defecto; si deseas asignarlas, utiliza el diálogo Gestos de entrada para añadir órdenes personalizadas. Para ello, abre el menú NVDA, Preferencias y luego Gestos de entrada. Expande la categoría Reloj, localiza las órdenes sin asignar en la lista inferior y selecciona "Añadir", después introduce el gesto que desees utilizar.

* Tiempo transcurrido y restante hasta la próxima alarma. Al pulsar este gesto dos veces rápidamente se cancelará la siguiente alarma.
* Detener el sonido de la alarma en reproducción.
* Mostrar el diálogo de programación de alarmas.
* Mostrar órdenes en capa (teclas que se pulsan después de NVDA+Shift+F12).

## Órdenes en capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las siguientes teclas:

* S: inicia, reinicia o detiene el cronómetro
* R: reinicia el cronómetro a 0 sin iniciarlo de nuevo
* A: anuncia el tiempo transcurrido y el tiempo restante hasta la próxima alarma
* T: abre el diálogo de programación de alarmas
* C: cancela la siguiente alarma
* Espacio: verbaliza el cronómetro o el temporizador de cuenta atrás actual
* p: si una alarma es demasiado larga, permite detenerla
* H: lista todas las órdenes en capa (Ayuda)

## Configuración y uso

Para configurar las funciones del reloj, abre el menú NVDA, Preferencias, Configuración, y ajusta las siguientes opciones desde el panel Reloj:

* Formato de hora y fecha: usa estos cuadros combinados para configurar cómo NVDA anunciará la hora y la fecha al pulsar NVDA+F12 una o dos veces respectivamente.
* Intervalo: selecciona el intervalo de anuncio de la hora desde este cuadro combinado (desactivado, cada 10 minutos, 15 minutos, 30 minutos o cada hora).
* Anuncio de hora (habilitado si el intervalo no está desactivado): elige entre voz y sonido, solo sonido o solo voz.
* Sonido de campanadas del reloj (habilitado si el intervalo no está desactivado): selecciona el sonido de campanadas predeterminado para los minutos intermedios y la hora en punto.
* Campanadas separadas para horas y minutos intermedios (habilitado si el intervalo no está desactivado, deshabilitado por defecto): activa esta casilla para personalizar las campanadas de los minutos intermedios por separado de la campana de la hora.
  * Sonido de campanadas de minutos intermedios (habilitado si está marcada la opción de campanas separadas): selecciona el sonido para los minutos intermedios.
* Horas silenciosas (habilitado si el intervalo no está desactivado): activa esta casilla para configurar un rango de horas en el que no se anunciará automáticamente la hora.
* Formato de horas silenciosas (habilitado si las horas silenciosas están activadas): selecciona cómo se presentan las opciones de horas silenciosas (formato de 12 o 24 horas).
* Hora de inicio y fin de horas silenciosas: selecciona el rango de horas y minutos para las horas silenciosas desde los cuadros combinados.

Para programar alarmas, abre el menú NVDA, Herramientas y selecciona Programar alarmas. El diálogo contiene:

* Duración de la alarma en: selecciona la duración entre horas, minutos y segundos.
* Duración: introduce la duración de la alarma en la unidad indicada anteriormente.
* Sonido de alarma: selecciona el sonido que se reproducirá.
* Botones de detener y pausar: detener o pausar un sonido de alarma largo.

Haz clic en Aceptar y un mensaje te informará de la duración de la alarma seleccionada.
