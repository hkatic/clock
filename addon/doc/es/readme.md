# Complemento reloj y calendario para NVDA #

* Autores: Hrvoje Katić, Abdel y contribuidores de NVDA;
* Descargar [versión estable][1];
* Descargar [versión de desarrollo][2].


Este complemento habilita la funcionalidad avanzada del reloj, del
temporizador de  alarma   y del calendario para NVDA. En lugar de obtener
siempre la hora y la fecha desde la barra de tareas de Windows, puedes
personalizar cómo deberían verbalizarse y braillificarse las horas y las
fechas por NVDA. Adicionalmente, puedes obtener el número de día y de semana
actual del año actual, y también puedes ajustar el anunciado automático de
la hora en un intervalo especificado. También hay las funciones del
cronómetro, del temporizador de alarma integradas en el complemento que te
permite programar tus tareas, como copiar archivos, instalar programas o la
preparación de comida.

## Utilización

*	Abre el diálogo de configuración para este complemento desde el menú de Herramientas  de NVDA o desde el panel de configuración de acuerdo con tu versión de NVDA;
	*	En el  diálogo de configuración del reloj, los primeros dos controles de Cuadro combinado te permiten elegir tus formatos preferidos de mostrado de hora y fecha;
	*	El control de Casilla de verificación etiquetado "Entrada al formato de 24 horas" Te permite configurar si deseas  entrar  el tiempo para las horas silenciosas en 12 horas (A.M. o P.M.), o en formato europeo de 24 horas;
	*	El control de Cuadro combinado etiquetado "Intervalo del anunciado automático" te permite ajustar el intervalo para el anunciado automático de la hora (Cada 15 minutos, Cada 30 minutos, Cada hora, o Desactivado);
	*	El control de Cuadro combinado etiquetado "Anunciado de la hora" te permite configurar cómo se debería informar el anunciado automático de la hora (Voz y sonido, Sólo Voz, o Sólo Sonido) cuando el anunciado automático de la hora esté funcionando;
	*	El control de Cuadro combinado etiquetado "Sonido de campana de reloj" te permite elegir entre varios sonidos de reloj que se reproducirán cuando el anunciado automático de la hora esté funcionando y se informe con sonido;
	*	El control de Casilla de verificación etiquetado "Horas silenciosas" te permite configurar el intervalo de tiempo cuando el anunciado automático de la hora no debería ocurrir, sin importar si el anunciado automático de la hora está habilitado o no;
	*	Los controles del cuadro Editar para el inicio y fin de la duración (solo visible si las horas silenciosas están habilitadas) te permiten configurar el intervalo de tiempo para las horas silenciosas. La hora debe ingresarse en formato HH:MM;
	*	Cuando hayas terminado, tabula al botón Aceptar y actívalo pulsando Intro para guardar tus opciones;
	*	En el  diálogo de configuración de la alarma, el primer control del Cuadro combinado te permite elegir la cuenta atrás del temporizador preferido antes de que suene la alarma;
	*	El control del cuadro Editar te permite escribir tu tiempo de espera antes de que suene la alarma. Esta duración debe especificarse en  1 o más dígitos, no en un número decimal;
	*	El control de Cuadro combinado etiquetado "Sonido de la alarma" te permite elegir entre varios sonidos de alarma que se reproducirán cuando llegue la hora de la alarma;
	*	Cuando hayas terminado, tabula al botón Aceptar y actívalo pulsando Intro. Un mensaje debe mostrarse para recordarte  el tiempo de espera antes de la alarma;
*	Pulsa NVDA+F12 una vez para obtener la hora actual, dos veces para obtener la fecha actual, o tres veces para obtener el número de día y de semana actual del año actual.

## Teclas de órdenes

- NVDA+F12, obtiene la hora actual; - NVDA+F12 pulsada dos veces
sucesivamente,  obtiene la fecha actual; - NVDA+F12 pulsada tres veces
sucesivamente, obtiene el número de día y de semana actual del año actual.

- Control+F12, da algunas informaciones sobre la próxima alarma; -
Control+F12 pulsada dos veces sucesivamente, cancela la siguiente alarma.

## Órdenes en capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las
siguientes teclas:

- S: Inicia, detiene o restablece el cronómetro; - R: Restablece el
cronómetro a 0 sin iniciarlo; - A: Da el tiempo transcurrido y el tiempo
restante antes de la próxima alarma; - C: Cancela la siguiente alarma; -
Barra espaciadora: Anuncia el cronómetro actual o  cuenta atrás del
temporizador; - H: Listar todas las órdenes en capa (Ayuda).

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

