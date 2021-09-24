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

## Órdenes de capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las
siguientes teclas:

* S: inicia, detiene o reinicia el cronómetro
* R: pone el cronómetro a 0 sin reiniciarlo
* A: da el tiempo transcurrido y el tiempo restante antes de la próxima
  alarma
* C: cancela la próxima alarma
* Espacio: verbaliza el cronómetro o la cuenta atrás actual
* p: si una alarma es demasiado larga, permite pararla
* H: lista todas las órdenes de capa (Ayuda)

## Uso

* Abre el diálogo de configuración de este complemento desde el diálogo de
  opciones de NVDA.

    * En el panel de configuración del reloj, los dos primeros cuadros
      combinados permiten controlar tus formatos preferidos a la hora de
      mostrar fecha y hora.
    * El cuadro combinado llamado "Intervalo" te permite configurar el
      intervalo de anuncio automático de la hora (cada 10 minutos, cada 15
      minutos, cada 30 minutos, cada hora o desactivado).
    * El cuadro combinado "Anuncio de la hora" (visible sólo si la opción
      "Desactivado" no está seleccionada en el cuadro combinado de
      intervalo) te permite configurar cómo debería anunciarse
      automáticamente la hora (voz y sonido, sólo voz o sólo sonido) cuando
      el anuncio automático de la hora está en funcionamiento.
    * El cuadro combinado llamado "Sonido de la campana del reloj" (visible
      sólo si la opción "Desactivado" no está seleccionada en el cuadro
      combinado de intervalo) te permite elegir entre varios sonidos de
      relojes, que se escucharán cuando el anuncio automático de la hora
      esté en funcionamiento y con sonido.
    * La casilla de verificación "Horas silenciosas" (visible sólo si la
      opción "Desactivado" no está seleccionada en el cuadro combinado de
      intervalo) te permite configurar un rango de tiempo en el que la hora
      no se anunciará automáticamente.
    * La casilla de verificación "Entrada en formato 24 horas" (visible sólo
      si las horas silenciosas están activadas) te permite indicar si
      quieres especificar las horas en formato de 12 horas (A.M. y P.M.) o
      en formato europeo de 24 horas.
    * Los cuadros de edición para las horas de inicio y finalización
      (visibles sólo si las horas silenciosas están activadas) te permiten
      configurar el rango de tiempo de las horas silenciosas. La hora
      debería introducirse siguiendo el formato "HH:MM" si está activada la
      entrada en formato de 24 horas, en cualquier otro caso se debe emplear
      el formato de 12 horas que se describe a continuación.
    * Cuando acabes, tabula hasta el botón Aceptar y actívalo pulsando intro
      para guardar las opciones.
    * En el diálogo de configuración de la alarma, el primer cuadro
      combinado te permite elegir tu temporizador de cuenta atrás preferido
      antes de que la alarma suene.
    * El cuadro de edición te permite escribir un tiempo de espera antes de
      que suene la alarma. Esta duración debe especificarse con uno o más
      dígitos sin decimales.
    * El cuadro combinado "Sonido de alarma" te permite elegir entre
      diversos sonidos de alarma que se reproducirán cuando llegue la hora
      de la alarma.
    * El botón Pausar te permite pausar o reanudar las alarmas demasiado
      largas.
    * El botón Detener te permite parar las alarmas demasiado largas.
    * Cuando acabes, tabula hasta el botón Aceptar y actívalo pulsando
      intro. Se debería mostrar un mensaje para recordarte cuánto tiempo de
      espera hay hasta la alarma.

* Pulsa NVDA+f12 una vez para obtener la hora actual, dos para obtener la
  fecha, o tres para saber el día actual, número de semana y días restantes
  para que se acabe el año en curso.

## Sintaxis de las horas silenciosas

1. Para evitar fallos, las horas silenciosas deben seguir una sintaxis
   rigurosa y precisa.
2. Si marcas la casilla "Entrada en formato 24 horas", el formato debe ser
   "HH:MM".
3. Si desmarcas la casilla "Entrada en formato de 24 horas", el formato debe
   ser "HH:MM AM" o "HH:MM PM", HH debe contener un número entre 0 y 12 y
   los sufijos "AM|PM" pueden estar en minúscula o mayúscula.
4. Si marcas la casilla "horas silenciosas" y dejas los campos "Hora de
   inicio de las horas silenciosas" o "Hora de finalización de las horas
   silenciosas" vacíos o escribes un valor erróneo, se desmarcará la casilla
   "Horas silenciosas" automáticamente para evitar errores y se mostrará un
   mensaje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
