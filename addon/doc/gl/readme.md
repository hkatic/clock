# Complemento de Reloxo e calendario para NVDA #

* Autores: Hrvoje Katić, Abdel e contribuíntes co NVDA;
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]


Este complemento habilita a funcionalidade avanzada de reloxo, contador con
alarma e calendario para NVDA.

No canto de obter hora e data dende Windows, podes personalizar cómo
deberían falarse e braillificarse as datas en NVDA:

Ademais, podes obter o número do día actual, da semana, así como os días que
restan antes do final do ano, e tamén podes establecer anunciado automático
da hora nun intervalo específico.

Tamén están dispoñibles integradas no complemento as características de
cronómetro e temporizador con alarma, que che permitirán temporizar as túas
tarefas, como o copiado de arquivos, a instalación de programas ou o
cociñado de carne.

## Nota:

Se instalas o complemento como unha actualización, durante o proceso de
instalación, o asistente detecta se a configuración vella é compatible coa
nova e ofrece correxila antes da instalación, de forma que só tes que
validar o botón Aceptar para confirmalo.

## Uso

*	Abre o diálogo de configuración para este complemento dende o menú Ferramentas do NVDA ou dende o panel de opcións De acordo coa túa versión de NVDA;
	*	No diálogo de configuración de Clock, os primeiros controis de Caixa Combinada permítenche escoller os teus formatos de amosado de hora e data preferidos;
	*	O control  de Caixa de Verificación etiquetado como "Input in 24-hour format" (Entrada en formato de 24 horas) permíteche configurar se queres introducir a hora para as horas silenciosas en formato de 12- horas (A.M. ou P.M.), ou no formato europeo de 24 horas;
	*	O control de Caixa Combinada etiquetado como "Auto-announce interval" (Intervalo do autoanunciado) permíteche establecer o intervalo para o anunciado automático da hora (Cada 15 minutos, Cada 30 minutos, Cada hora, ou Desactivado);
	*	O control de Caixa Combinada etiquetado como "time announcement" (anunciado da hora) permíteche configurar como debería reportarse o anuncio automático de hora (Fala e son, Só fala, ou Só son) cando o anunciado automático de hora estea a funcionar;
	*	O control Caixa combinada  etiquetado como "Clock chime sound" (son da campá do Clock) permíteche escoller entre varios sons de reloxo que se reproducirán cando o anunciado automático da hora estea activo e sexa reportado mediante sons;
	*	O control de Caixa de Verificación etiquetado como "Quiet hours" (horas silenciosas) permíteche configurar un rango horario onde non debería facerse o anunciado automático da hora, sen importar se o anunciado automático está activo ou non;
	*	Os controles de Caixa de edición de hora de inicio e fin (só visible se as horas silenciosas están activas) permíteche configurar o rango horario para as horas silenciosas. A hora debe introducirse no formato HH:MM;
	*	Unha vez feito, tabula ata o botón Aceptar e actívao premendo Intro para gardar os teus axustes;
	*	No diálogo de Configuración da alarma, o primeiro control de Caixa Combinada permíteche escoller o teu marcador de conta atrás preferido antes de que a alarma soe;
	*	O control de Caixa de edición permíteche escribir o teu tempo de agarda antes de que a alarma soe. Esta duración débese especificar cun ou máis díxitos, non un número decimal;
	*	O control de Caixa combinada etiquetado como "Alarm sound" (son de alarma) permíteche escoller entre varios sons de alarma que se reproducirán cando o tempo da alarma expire;
	*	Unha vez feito, tabula ao botón Aceptar e actívao premendo Intro. Deberíase amosar unha mensaxe para recordarche o tempo de agarda antes da alarma;
*	Preme NVDA+F12 unha vez para obter a hora actual, dúas veces para obter a data actual, ou tres veces para obter o número de día e semana actual do ano en curso.

## Teclas de ordes

- NVDA+F12, obtén a hora actual.  - NVDA+F12 premeda dúas veces
sucesivamente,  obtén a data actual.  - NVDA+F12 premeda tres veces
sucesivamente, obtén o número de día, o número de semana, o ano actual e o
número de días restante ata o final do ano.

- Control+F12, proporciona algunhas informacións sobre a vindeira alarma; -
Control+F12 premido dúas veces rapidamente, cancelar a vindeira alarma.

## Ordes en capa

Para utilizar as ordes en capa, preme NVDA+Shift+F12 seguido dunha das
seguintes teclas:

- S: Inicia, reinicia ou detén o cronómetro; - R: Restablece o cronómetro a
cero sen reinicialo; - A: proporciona o tempo restante e transcorrido antes
da vindeira alarma; - C: Cancelar a vindeira alarma; - Spacebar: Anuncia o
contador actual do cronómetro ou da conta atrás; - H: Listar todas as ordes
en capa (axuda)..

## compatibilidade

- Este complemento é compatible coas versións do NVDA no rango da 2014.3 ata
a 2019.1.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

