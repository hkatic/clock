# Complemento Reloxo e calendario para NVDA #

* Autores: Hrvoje Katić, Abdel e colaboradores de NVDA
* Compatibilidade con NVDA: 2019.3 e posteriores

Este complemento activa funcionalidades avanzadas de reloxo, temporizador de alarma e calendario para NVDA.

Podes configurar NVDA para anunciar a hora e a data en formatos diferentes dos que Windows proporciona por defecto. Ademais, podes obter o día actual, o número de semana, así como os días restantes ata o final do ano actual, e tamén podes establecer o anuncio automático da hora en intervalos especificados. O complemento tamén inclúe funcións de cronómetro e temporizador de alarma que permiten medir o tempo das túas tarefas, como copiar ficheiros, instalar programas ou cociñar comidas.

## Notas:

* se instalas o complemento como actualización, durante o proceso de instalación o asistente detecta se a configuración antiga é compatible coa nova e ofrece corrixila antes da instalación, despois só tes que confirmar o botón OK.
* En Windows 10 e posteriores, podes usar a aplicación Alarmas e Reloxo para xestionar cronómetros e temporizadores.

## Comandos de teclado

* NVDA+F12: obter a hora actual
* NVDA+F12 premido dúas veces rapidamente: obter a data actual
* NVDA+F12 premido tres veces rapidamente: anuncia o día actual, o número de semana, o ano actual e os días restantes ata o final do ano
* NVDA+Shift+F12: entrar na capa do reloxo

## Comandos non asignados

Os seguintes comandos non están asignados por defecto; se queres asignalos, usa o diálogo Xestos de entrada para engadir comandos personalizados. Para iso, abre o menú NVDA, Preferencias, logo Xestos de entrada. Expande a categoría Reloxo, localiza os comandos non asignados na lista de abaixo e selecciona "Engadir", despois introduce o xesto que desexes usar.

* Tempo transcorrido e restante ata a seguinte alarma. premer dúas veces rapidamente este xesto cancela a seguinte alarma.
* Deter o son da alarma que se está a reproducir.
* Mostrar diálogo de programación de alarmas.
* Mostrar comandos en capa (teclas despois de NVDA+Shift+F12).

## Comandos en capa

Para usar comandos en capa, preme NVDA+Shift+F12 seguido dunha das seguintes teclas:

* S: inicia, reinicia ou detén o cronómetro
* R: reinicia o cronómetro a 0 sen reinicialo
* A: indica o tempo transcorrido e restante ata a seguinte alarma
* T: abre o diálogo de programación de alarmas
* C: cancela a seguinte alarma
* Espazo: anuncia o cronómetro actual ou a conta atrás
* P: se unha alarma é demasiado longa, permite detela
* H: lista todos os comandos en capa (Axuda)

## Configuración e uso

Para configurar a funcionalidade do reloxo, abre o menú NVDA, Preferencias, logo Configuración, e configura as seguintes opcións no panel Reloxo:

* Formato de visualización da hora e da data: usa estas caixas combinadas para configurar como NVDA anunciará a hora e a data ao premer NVDA+F12 unha ou dúas veces rapidamente.
* Intervalo: escolle o intervalo de anuncio da hora nesta caixa (desactivado, cada 10 minutos, 15 minutos, 30 minutos ou cada hora).
* Anuncio da hora (activado se o intervalo non está desactivado): escolle entre voz e son, só son ou só voz.
* Son do reloxo (activado se o intervalo non está desactivado): selecciona o son predeterminado do reloxo.
* Sinais separados para horas e minutos intermedios (activado se o intervalo non está desactivado, desactivado por defecto): activa esta caixa para personalizar os sinais dos minutos intermedios por separado do son da hora.
  * Son dos minutos intermedios (activado se “sinais separados para horas e minutos intermedios” está marcado): selecciona o son para os minutos intermedios.
* Horas silenciosas (activado se o intervalo non está desactivado): marca esta caixa para configurar o intervalo de horas silenciosas.
* Formato das horas silenciosas (activado se as horas silenciosas están activadas): escolle como se presentan as opcións (formato de 12 ou 24 horas).
* Horario de inicio e fin das horas silenciosas: escolle o intervalo de horas e minutos para as horas silenciosas nas caixas combinadas.

Para programar alarmas, abre o menú NVDA, Ferramentas, logo selecciona Programar alarmas. O diálogo inclúe:

* Duración da alarma: escolle a duración da alarma/temporizador en horas, minutos e segundos.
* Duración: introduce a duración da alarma na unidade indicada arriba.
* Son da alarma: selecciona o son da alarma.
* Botóns de deter e pausar: deter ou pausar unha alarma longa.

Preme OK e mostrarase unha mensaxe coa duración da alarma seleccionada.
