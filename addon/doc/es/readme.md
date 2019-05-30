# Complemento reloj y calendario para NVDA #

* Autores: Hrvoje Katić, Abdel y contribuidores de NVDA;
* Descargar [versión estable][1];
* Descargar [versión de desarrollo][2].


Este complemento habilita la funcionalidad avanzada de reloj, de
temporizador de alarma   y  calendario para NVDA.

En lugar de obtener siempre la hora y la fecha desde la barra de tareas de
Windows, puedes personalizar cómo deberían verbalizarse y braillificarse las
horas y las fechas por NVDA.

Además, puedes obtener el día actual, el número de la semana, así como los
días restantes para que acabe el año y también puedes ajustar el anuncio
automático de la hora en un intervalo especificado.

También existen las funciones de cronómetro, de temporizador de alarma
integrados en el complemento que te permite programar tus tareas, como
copiar archivos, instalar programas o preparar comida.

## Nota:

Si instalas el complemento como una actualización, durante el proceso de
instalación, el asistente detecta si la configuración anterior es compatible
con la nueva y ofrece corregirla antes de instalarla.

## Uso

* Abre el diálogo de configuración de este complemento desde el menú
  herramientas de NVDA o desde el diálogo de opciones, según corresponda en
  función de la versión que tengas de NVDA;

    * En el diálogo de configuración del reloj, los dos primeros cuadros
      combinados permiten controlar tus formatos preferidos a la hora de
      mostrar fecha y hora;
    * El cuadro combinado llamado "Intervalo" te permite configurar el
      intervalo de anuncio automático de la hora (cada 10 minutos, cada 15
      minutos, cada 30 minutos, cada hora o desactivado);
    * El cuadro combinado "Anuncio de la hora" (visible sólo si la opción
      "Desactivado" no está seleccionada en el cuadro combinado de
      intervalo) te permite configurar cómo debería anunciarse
      automáticamente la hora (voz y sonido, sólo voz o sólo sonido);
    * El cuadro combinado llamado "Sonido de la campana del reloj" (visible
      sólo si la opción "Desactivado" no está seleccionada en el cuadro
      combinado de intervalo) te permite elegir entre varios sonidos de
      relojes, que se escucharán cuando se produzca el anuncio automático
      con sonido;
    * La casilla de verificación "Horas silenciosas" (visible sólo si la
      opción "Desactivado" no está seleccionada en el cuadro combinado de
      intervalo) te permite configurar un rango de tiempo en el que la hora
      no se anunciará automáticamente;
    * La casilla de verificación "Entrada en formato 24 horas" (visible sólo
      si las horas silenciosas están activadas) te permite indicar si
      quieres especificar las horas en formato de 12 horas (A.M. y P.M.) o
      en formato europeo de 24 horas;
    * Los cuadros de edición para las horas de inicio y finalización
      (visibles sólo si las horas silenciosas están activadas) te permiten
      configurar el rango de tiempo de las horas silenciosas. La hora
      debería introducirse siguiendo el formato "HH:MM" si está activada la
      entrada en formato de 24 horas, en cualquier otro caso se debe emplear
      el formato de 12 horas que se describe a continuación;
    * Cuando acabes, tabula hasta el botón Aceptar y actívalo pulsando intro
      para guardar las opciones;
    * En el diálogo de configuración de la alarma, el primer cuadro
      combinado te permite elegir tu temporizador de cuenta atrás preferido
      antes de que la alarma suene;
    * El cuadro de edición te permite escribir un tiempo de espera antes de
      que suene la alarma. Esta duración debe especificarse con uno o más
      dígitos sin decimales;
    * El cuadro combinado "Sonido de alarma" te permite elegir entre
      diversos sonidos de alarma que se reproducirán cuando llegue la hora
      de la alarma;
    * El botón Pausar te permite pausar o reanudar las alarmas demasiado
      largas;
    * El botón Detener te permite parar las alarmas demasiado largas;
    * Cuando acabes, tabula hasta el botón Aceptar y actívalo pulsando
      intro. Se debería mostrar un mensaje para recordarte cuánto tiempo de
      espera hay hasta la alarma;

* Pulsa NVDA+f12 una vez para obtener la hora actual, dos para obtener la
  fecha, o tres para saber el día actual, número de semana y días restantes
  para que se acabe el año en curso.

## Teclas de órdenes

* NVDA+f12: obtiene la hora actual;
* NVDA+f12 pulsado ddos veces rápidamente: obtiene la fecha actual;
* NVDA+F12 pulsado tres veces rápidamente, anuncia el número de día, número
  de semana, el año actual y los días restantes para que se acabe.
* Hay un script que verbaliza el tiempo transcurrido y el tiempo restante
  antes de la siguiente alarma;
* No hay un gesto de teclado asociado a este script. Deberás asignarlo por
  ti mismo en el diálogo "Gestos de entrada", en la categoría "Reloj";
* Si se pulsa este gesto dos veces rápidamente, se cancela la siguiente
  alarma;
* También hay un script para detener el sonido que se reproduce actualmente,
  su gesto no está definido;
* Dicho script puede llamarse usando las órdenes de capa del reloj que se
  describen a continuación.

## Órdenes de capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las
siguientes teclas:

* S: inicia, detiene o reinicia el cronómetro;
* R: pone el cronómetro a 0 sin reiniciarlo;
* A: da el tiempo transcurrido y el tiempo restante antes de la próxima
  alarma;
* C: cancela la próxima alarma;
* Espacio: verbaliza el cronómetro o la cuenta atrás actual;
* p: si una alarma es demasiado larga, permite pararla;
* H: lista todas las órdenes de capa (Ayuda).

## Sintaxis de las horas silenciosas

* Para evitar fallos, las horas silenciosas deben seguir una sintaxis
  rigurosa y precisa;
* Si marcas la casilla "Entrada en formato 24 horas", el formato debe ser
  "HH:MM";
* Si desmarcas la casilla "Entrada en formato de 24 horas", el formato debe
  ser "HH:MM AM" o "HH:MM PM", HH debe contener un número entre 0 y 12 y los
  sufijos "AM|PM" pueden estar en minúscula
* Si marcas la casilla "horas silenciosas" y dejas los campos "Hora de
  inicio de las horas silenciosas" o "Hora de finalización de las horas
  silenciosas" vacíos o escribes un valor erróneo, se desmarcará la casilla
  "Horas silenciosas" automáticamente para evitar errores;
* Debería mostrarse un mensaje para informar de tu error.

## Compatibilidad

* Este complemento es compatible con las versiones de NVDA desde 2014.3
  hasta 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

