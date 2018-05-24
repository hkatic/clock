# Complemento reloj y calendario para NVDA #

* Autores: Hrvoje Katić y contribuidores de NVDA.
* Descargar [versión de desarrollo](https://ci.appveyor.com/project/HrvojeKati/clock/build/artifacts)

Este complemento habilita la funcionalidad avanzada de reloj y calendario para NVDA. En lugar de obtener siempre la hora y la fecha desde la barra de tareas de Windows, puedes personalizar cómo deberían verbalizarse y braillificarse las horas y las fechas por NVDA. Adicionalmente, puedes obtener el número de día y de semana actual del año actual, y también puedes ajustar el anunciado automático de la hora en un intervalo especificado. También hay una función de cronómetro integrada en el complemento que te permite programar tus tareas, como copiar archivos, instalar programas o la preparación de comida.

## Utilización

*	Abre el diálogo de configuración para este complemento desde el menú Preferencias de NVDA.
	*	Los primeros dos controles de Cuadro combinado te permiten elegir tus formatos preferidos de mostrado de hora y fecha.
	*	El control de Casilla de verificación etiquetado "Entrada al formato de 24 horas" Te permite configurar si deseas  entrar  el tiempo para las horas silenciosas en 12 horas (A.M. o P.M.), o en formato europeo de 24 horas.
	*	El control de Cuadro combinado etiquetado "Intervalo del anunciado automático" te permite ajustar el intervalo para el anunciado automático de la hora (Cada 15 minutos, Cada 30 minutos, Cada hora, o Desactivado).
	*	El control de Cuadro combinado etiquetado "Anunciado de la hora" te permite configurar cómo se debería informar el anunciado automático de la hora (Voz y sonido, Sólo Voz, o Sólo Sonido) cuando el anunciado automático de la hora esté funcionando.
	*	El control de Cuadro combinado etiquetado "Sonido de campana de reloj" te permite elegir entre varios sonidos de reloj que se reproducirán cuando el anunciado automático de la hora esté funcionando y se informe con sonido.
	*	El control de Casilla de verificación etiquetado "Horas silenciosas" te permite configurar el intervalo de tiempo cuando el anunciado automático de la hora no debería ocurrir, sin importar si el anunciado automático de la hora está habilitado o no.
	*	Los controles del cuadro Editar para el inicio y fin de la duración (solo visible si las horas silenciosas están habilitadas) te permiten configurar el intervalo de tiempo para las horas silenciosas. La hora debe ingresarse en formato HH:MM.
	*	Cuando esté hecho, tabula al botón Aceptar y actívalo para guardar tus opciones.
*	Pulsa NVDA+F12 una vez para obtener la hora actual, dos veces para obtener la fecha actual, o tres veces para obtener el número de día y de semana actual del año actual.

## Teclas de órdenes

- NVDA+F12, obtiene la hora actual.
- NVDA+F12 pulsada dos veces sucesivamente,  obtiene la fecha actual.
- NVDA+F12 pulsada tres veces sucesivamente, obtiene el número de día y de semana actual del año actual.

## Órdenes en capa

Para usar las órdenes en capa, pulsa NVDA+Shift+F12 seguido de una de las siguientes teclas:

- S: Inicia, detiene o restablece el cronómetro.
- R: Restablece el cronómetro a 0 sin iniciarlo.
- Barra espaciadora: Anuncia el cronómetro actual o  cuenta atrás del temporizador.
- H: Listar todas las órdenes en capa (Ayuda).


