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

También hay las funciones de cronómetro, de temporizador de alarma
integrados en el complemento que te permite programar tus tareas, como
copiar archivos, instalar programas o la preparación de comida

## Nota:

Si instalas el complemento como una actualización, durante el proceso de
instalación, el asistente detecta si la configuración anterior es compatible
con la nueva y ofrece corregirla antes de instalarla.

## Uso

*	Abre el diálogo de configuración para este complemento desde el menú de Herramientas  de NVDA o desde el panel de configuración de acuerdo con tu versión de NVDA;
	*	En el  diálogo de configuración de reloj, los primeros dos controles de Cuadro combinado te permiten elegir tus formatos de hora y fecha preferidas;
	*	El control de Casilla de verificación etiquetado "Entrada en formato de 24 horas" Te permite configurar si deseas  entrar  el tiempo para las horas silenciosas en 12 horas (A.M. o P.M.), o en formato europeo de 24 horas;
	*	El control de Cuadro combinado etiquetado "Intervalo" te permite ajustar el intervalo para el anuncio automático de la hora (Cada 15 minutos, Cada 30 minutos, Cada hora, o Desactivado);
	*	El control de Cuadro combinado etiquetado "Anuncio de las horas" te permite configurar cómo se debería informar el anuncio automático de la hora (Voz y sonido, Sólo Voz, o Sólo Sonido) cuando el anuncio automático de la hora esté funcionando;
	*	El control de Cuadro combinado etiquetado "Sonido de la campana del reloj" te permite elegir entre varios sonidos de reloj que se reproducirán cuando el anuncio automático de la hora esté funcionando y se informe con sonido;
	*	El control de Casilla de verificación etiquetado "Horas silenciosas" te permite configurar el intervalo de tiempo cuando el anuncio automático de la hora no debería ocurrir, sin importar si el anuncio automático de la hora está habilitado o no;
	*	Los controles del cuadro Editar para el inicio y el fin de la duración (solo visible si las horas silenciosas están habilitadas) te permiten configurar el intervalo de tiempo para las horas silenciosas. La hora debe ingresarse en formato HH:MM;
	*	Cuando hayas terminado, tabula al botón Aceptar y actívalo pulsando Intro para guardar tus opciones;
	*	En el  diálogo de configuración de la alarma, el primer control del Cuadro combinado te permite elegir el contador de cuenta atrás  preferido antes de que suene la alarma;
	*	El control del cuadro Editar te permite escribir tu tiempo de espera antes de que suene la alarma. Esta duración debe especificarse en  1 o más dígitos, no en un número decimal;
	*	El control de Cuadro combinado etiquetado "Sonido de la alarma" te permite elegir entre varios sonidos de alarma que se reproducirán cuando llegue la hora de la alarma;
	*	Cuando hayas terminado, tabula al botón Aceptar y actívalo pulsando Intro. Un mensaje debe mostrarse para recordarte  el tiempo de espera antes de la alarma;
*	Pulsa NVDA+F12 una vez para saber la hora actual, dos veces para saber la fecha actual, o tres veces para saber el día actual, el número de semana, el año actual y los días restantes para que acabe el año.

## Teclas de órdenes

- NVDA+F12, saber la hora actual;
- NVDA+F12 pulsado dos veces rápidamente, saber la fecha actual;
- NVDA+F12 pulsado tres veces rápidamente, anuncia el número de día, número
de semana, el año actual y los días restantes para que se acabe.

- Control+F12, da el tiempo transcurrido y restante antes de la próxima
alarma;
- Control+F12 pulsado dos veces rápidamente, cancelar la próxima alarma.

## Órdenes de capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las
siguientes teclas:

- S: inicia, detiene o restablece el cronómetro; - R: restablece el
cronómetro a 0 sin reiniciarlo; - A: da el tiempo transcurrido y el tiempo
restante antes de la próxima alarma; - C: cancela la próxima alarma; - Barra
espaciadora: verbaliza el cronómetro o contador de cuenta atrás actual; - H:
lista todas las órdenes de capa (Ayuda).

## Compatibilidad

- Este complemento es compatible con las versiones de NVDA desde 2014.3
hasta 2019.1.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

