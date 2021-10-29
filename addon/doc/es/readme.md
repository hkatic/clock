# Complemento reloj y calendario para NVDA #

* Autores: Hrvoje Katić, Abdel y colaboradores de NVDA
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2019.3 en adelante

Este complemento habilita funciones avanzadas de reloj, temporizador de
alarma   y  calendario para NVDA.

Puedes configurar NVDA para que anuncie la fecha y la hora en formatos
distintos a los que tiene Windows por defecto. Además, puedes obtener el día
actual, número de semana, así como los días restantes para que acabe el año
en curso, y también puedes establecer el anuncio automático de la hora tras
un intervalo dado. También hay funciones de temporizador de alarma y
cronómetro incorporadas en el complemento que te permiten medir tus tareas,
tales como copiar archivos, instalar programas o cocinar comida.

Notas:

* si instalas el complemento como una actualización, durante el proceso de
  instalación, el asistente detecta si la configuración anterior es
  compatible con la nueva y ofrece corregirla antes de instalar. Simplemente
  debes validar con el botón Aceptar para confirmar.
* En Windows 10 o posterior, puedes usar la aplicación Reloj y alarmas para
  gestionar cronómetros y temporizadores.

## Teclas de órdenes

* NVDA+f12: obtiene la hora actual
* NVDA+f12 pulsado dos veces rápidamente: obtiene la fecha actual
* NVDA+F12 pulsado tres veces rápidamente: anuncia el número de día, número
  de semana, el año actual y los días que faltan hasta fin de año
* NVDA+shift+f12: entra en la capa del reloj

## Órdenes sin asignar

Las siguientes órdenes vienen sin asignar por defecto; si quieres
asignarlas, utiliza el diálogo Gestos de entrada para añadir órdenes
personalizadas. Para ello, abre el menú NVDA, Preferencias, y luego Gestos
de entrada. Expande la categoría Reloj, encuentra las órdenes sin asignar de
la lista de debajo y selecciona "Añadir". Finalmente, teclea el gesto que te
gustaría utilizar.

* Tiempo transcurrido y restante antes de la próxima alarma. Al pulsar dos
  veces rápidamente este gesto, se cancelará la alarma.
* Detener sonido de la alarma actual en reproducción.
* Mostrar cuadro de diálogo para programar alarmas.

## Órdenes de capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las
siguientes teclas:

* S: inicia, detiene o reinicia el cronómetro
* R: pone el cronómetro a 0 sin reiniciarlo
* A: da el tiempo transcurrido y el tiempo restante antes de la próxima
  alarma
* T: abre el diálogo de programación de alarmas.
* C: cancela la próxima alarma
* Espacio: verbaliza el cronómetro o la cuenta atrás actual
* p: si una alarma es demasiado larga, permite pararla
* H: lista todas las órdenes de capa (Ayuda)

## Configuración y uso

Para configurar la funcionalidad del reloj, abre el menú de NVDA,
Preferencias, Opciones, y configura las siguientes opciones desde el panel
Reloj:

* Formato de visualización de fecha y hora: usa estos cuadros combinados
  para configurar cómo anunciará NVDA la hora y la fecha al pulsar NVDA+f12
  una o dos veces rápidamente, respectivamente.
* Intervalo: elige el intervalo de anuncio de hora desde este cuadro
  combinado (apagado, cada 10 minutos, 15 minutos, 30 minutos, o cada hora).
* Anuncio de hora (habilitado si el intervalo no está apagado): elige entre
  voz y sonido, sólo sonido o sólo voz.
* Sonido de campana del reloj (habilitado si el intervalo no está apagado):
  selecciona el sonido de la campana.
* Horas silenciosas (habilitada si el intervalo no está apagado): selecciona
  esta casilla para configurar el intervalo de horas silenciosas en el que
  no debería producirse el anuncio automático de hora.
* Formato de hora para las horas silenciosas (activado si las horas
  silenciosas están activadas): selecciona cómo se presentan las opciones de
  las horas silenciosas (formatos de 12 o 24 horas).
* Horas de inicio y fin de las horas silenciosas: selecciona el intervalo de
  horas y minutos de las horas silenciosas desde los cuadros combinados de
  horas y minutos.

Para programar alarmas, abre el menú de NVDA, Herramientas, Programar
alarmas. Los contenidos del diálogo incluyen:

* Duración de la alarma en: selecciona la duración de la alarma o el
  temporizador entre horas, minutos y segundos.
* Duración: introduce la duración de la alarma en la unidad indicada
  anteriormente.
* Sonido de alarma: elige el sonido de alarma que se reproducirá.
* Botones detener y pausar: detener o pausar un sonido de alarma largo.

Pulsa Aceptar, y un mensaje te informará la duración de la alarma
seleccionada actualmente.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
