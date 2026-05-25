# Complemento de Reloxo e calendario para NVDA

- Authors: Hrvoje Katić, Abdel and NVDA contributors
- Descargar  [versión estable][1]
- Compatibilidade con NVDA: 2019.3 en diante
- NVDA compatibility: 2019.3 and later

Este complemento habilita a funcionalidade avanzada de reloxo, temporizador
con alarma e calendario para NVDA.

You can configure NVDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

Notas:

- se instalas o complemento como unha actualización, durante o proceso de
  instalación, o asistente detecta se a configuración vella é compatible coa
  nova e ofrece corrixila antes da instalación, de forma que só tes que
  validar o botón Aceptar para confirmalo.
- En Windows 10 e posterior, podes utilizar a aplicación Alarmas e Reloxo
  para administrar cronómetro e temporizadores.

## Teclas de ordes

- NVDA+F12: obter hora actual
- NVDA+F12 pulsado dúas veces rapidamente: obter data actual
- NVDA+F12 premida tres veces rapidamente: obtén o número de día, o número
  de semana, o ano actual e o número de días restante ata o final do ano
- NVDA+Shift+F12: entrar na capa do reloxo

## Ordes non asignadas

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.

- Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
- Deter son de alarma en reprodución.
- Amosar a caixa de diálogo de programación de alarmas.
- Show layered commands (keys to be pressed after NVDA+Shift+F12).

## Ordes en capa

Para utilizar as ordes en capa, preme NVDA+Shift+F12 seguido dunha das
seguintes teclas:

- S: Inicia, detén ou reinicia o cronómetro
- R: Restablece o cronómetro a 0 sen reinicialo
- A: Fornece o tempo transcorrido e restante ata a vindeira alarma
- T: abre o diálogo de programación de alarmas.
- C: Cancelar a vindeira alarma
- Espazo: Anuncia o temporizador actual do cronómetro ou da conta atrás
- p: Se unha alarma é demasiado longa, permite detela
- H: Listar tódolos comandos en capa (Help=Axuda)

## Configuración e uso

Para configurar a funcionalidade de reloxo, abre o menú de NVDA,
Preferencias, logo Opcions, e configura as seguintes opcións dende o panel
de Clock:

- Formato de amosado de hora e data: utiliza estes cadros combinados para
  configurar como anunciará NVDA a hora e a data cando premas NVDA+F12 unha
  vez ou dúas veces rapidamente, respectivamente.
- Intervalo: escolle o intervalo de anunciado da hora neste cadro combinado
  (desactivado, cada 10 minutos, 15 minutos, 30 minutos, ou cada hora).
- Anuncio da hora (dispoñible se o intervalo non está desactivado): escolle
  entre fala e son, só son ou só fala.
- Son de campá do reloxo (dispoñible se intervalo non está desactivado):
  selecciona o son da campá do reloxo.
- Horas caladas (dispoñible se o intervalo non está desactivado): selecciona
  esta caixa de verificación para configurar un rango de horas caladas onde
  non debería anunciarse a hora automaticamente.
  - Intermediate minutes chime sound (enabled if "Separate hour and intermediate minute chimes" is checked): Select the clock chime sound specifically for intermediate minutes.
- Formato de hora das horas caladas (dispoñible se as horas caladas están
  activadas): selecciona como se presentan as opcións das horas caladas
  (formato de 12 ou 24 horas).
- Horas de inicio e finalización das horas caladas: selecciona o rango de
  hora e minuto para as horas caladas nos cadros combinados de horas e
  minutos.
- Quiet hours start and end times: select hour and minute range for quiet hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The dialog contents include:

- Duración da alarma en: selecciona a duración da alarma/temporizador en
  horas, minutos, e segundos.
- Duración: introduce a duración da alarma na unidade especificada
  anteriormente.
- Son de alarma: selecciona o son de alarma a reproducir.
- Botóns deter e pausa: deter ou pausar un son de alarma longo.

Faga click en OK, e un diálogo informarate da duración de alarma actualmente
seleccionada.

[1]: https://addons.nvda-project.org/files/get.php?file=cac
[2]: https://www.nvaccess.org/addonStore/legacy?file=clock
