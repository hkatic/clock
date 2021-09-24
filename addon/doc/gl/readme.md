# Complemento de Reloxo e calendario para NVDA #

* Autores: Hrvoje Katić, Abdel e contribuíntes co NVDA
* Descargar  [versión estable][1]
* Descarga [versión de desenvolvemento][2]
* Compatibilidade con NVDA: 2019.3 en diante

Este complemento habilita a funcionalidade avanzada de reloxo, temporizador
con alarma e calendario para NVDA.

Podes configurar NVDA para anunciar hora e data en formatos distintos dos
que fornece Windows por defecto. Adicionalmente, podes obter o día actual, o
número de semana, así como os días restantes ata o final do ano actual, e
tamén podes configurar o anuncio automático da hora no intervalo
especificado. Tamén hai características de cronómetro e temporizador con
alarma integradas no complemento que che permiten cronometrar as túas
tarefas, como a copia de arquivos, a instlaación de programas ou o cociñado
de alimentos.

Notas:

* Se instalas o complemento como unha actualización, durante o proceso de
  instalación, o asistente detecta se a configuración vella é compatible coa
  nova e ofrece corrixila antes da instalación, de forma que só tes que
  validar o botón Aceptar para confirmalo.
* En Windows 10 e posterior, podes utilizar a aplicación Alarmas e Reloxo
  para administrar cronómetro e temporizadores.

## Teclas de ordes

* NVDA+F12: obter hora actual
* NVDA+F12 pulsado dúas veces rapidamente: obter data actual
* NVDA+F12 premida tres veces rapidamente: obtén o número de día, o número
  de semana, o ano actual e o número de días restante ata o final do ano
* NVDA+Shift+F12: entrar na capa do reloxo

## Ordes non asignadas

As seguintes ordes están sen asignar por defecto; se desexas asignalas,
utiliza o diálogo de Xestos de Entrada para engadir ordes
persoalizadas. Para facelo, abre o menú NVDA, Preferencias, logo Xestos de
Entrada. Expande a categoría Clock, despois localiza ordes sen asignar da
lista inferior e selecciona "Engadir", logo escribe o xesto que queiras
utilizar.

* Tempo transcorrido e restante antes da seguinte alarma. Premer este xesto
  dúas veces rapidamente cancelará a seguinte alarma.
* Deter son de alarma en reprodución.

## Ordes en capa

Para utilizar as ordes en capa, preme NVDA+Shift+F12 seguido dunha das
seguintes teclas:

* S: Inicia, detén ou reinicia o cronómetro
* R: Restablece o cronómetro a 0 sen reinicialo
* A: Fornece o tempo transcorrido e restante ata a vindeira alarma
* C: Cancelar a vindeira alarma
* Espazo: Anuncia o temporizador actual do cronómetro ou da conta atrás
* p: Se unha alarma é demasiado longa, permite detela
* H: Listar tódolos comandos en capa (Help=Axuda)

## Uso

* Abre o ciálogo de configuración deste complemento dende o diálogo de
  Opcións de NVDA.

    * No panel de configuración do reloxo, os dous primeiros controis de
      caixa combinada permítenche escoller os formatos de amosado de hora e
      data que prefiras.
    * O control de caixa combinada etiquetado "Intervalo" permíteche
      establecer o intervalo do anuncio automático da hora (cada 10 minutos,
      cada 15 minutos, cada 30 minutos, cada hora ou desactivado).
    * O control de caixa combinada etiquetado "Anunciado da hora" (só
      visible se a opción "Desactivado" non está seleccionada na caixa
      combinada intervalo) permíteche configurar como se informará do
      anuncio automático da hora (fala e son, só fala ou só son) cando este
      anunciado estea habilitado.
    * O control de caixa combinada etiquetada "Son de campá do reloxo" (só
      visible se a opción "Desactivado" non está seleccionada na caixa
      combinada intervalo) permíteche elixir entre distintos sons de reloxo
      que se reproducirán cando o anunciado automático da hora estea
      habilitado e se informe mediante son.
    * O control de caixa de verificación etiquetado "Horas caladas" (só
      visible se a opción "Desactivado" non está seleccionada na caixa
      combinada intervalo) permíteche configurar un rango de horas onde non
      debería anunciarse a hora automaticamente.
    * O control de caixa de verificación etiquetado "entrada en formato de
      24 horas" (só visible se as horas caladas están activadas) permíteche
      configurar se queres introducir as horas das horas caladas en formato
      de 12 horas (A.M. ou P.M.) ou en formato europeo de 24 horas.
    * Os controis de caixa de edición da hora de comezo e finalización (só
      visible se as horas caladas están activadas) permítenche configurar o
      rango de tempo das horas caladas. A hora debe introducirse no formato
      HH:MM se a caixa de verificación "Entrada no formato de 24 horas" está
      marcada, noutro caso deberás utilizar un formato de 12 horas como se
      describe máis abaixo.
    * Cando estea listo, tabula ata o botón Aceptar e actívao premendo intro
      para gardar a túa configuración.
    * No diálogo Configuración da alarma, o primeiro control de caixa
      combinada permíteche escoller o teu temporizador de conta atrás
      preferido antes do son da alarma.
    * O control de caixa de edición permíteche escribir o teu tempo de
      espera antes do son da alarma. Esta duración débese especificar cun ou
      máis díxitos, non cun número decimal.
    * O control de caixa combinada etiquetado "Son da alarma" permíteche
      escoller entre varios sons de alarma que se reproducirán cando se
      chegue o tempo de alarma.
    * O botón pausa permíteche pausar/reanudar alarmas demasiado longas.
    * O botón deter permíteche parar alarmas demasiado longas.
    * Cando estea listo, tabula ó botón Aceptar e actívao premendo
      intro. Debería amosarse unha mensaxe para lembrarche o tempo de agarda
      antes da alarma.

* Preme NVDA+F12 unha vez para obter a hora actual, dúas veces para obter a
  data actual ou tres veces para obter o número de día, o número de semana,
  o ano actual e o número de días restante ata o final do ano.

## Sintaxe para utilizar nas horas caladas

1. Para evitar fallos, as horas caladas deben seguir unha sintaxe rigorosa e
   precisa.
2. Se marcas a caixa de verificación "Entrada en formato de 24 horas", o
   formato debe ser "HH:MM".
3. Se desmarcas a caixa de verificación "Entrada en formato de 24 horas", o
   formato debe ser "HH:MM AM" ou "HH:MM PM", HH debe conter un formato de
   12 horas, de 0 a 12 e o sufixo "AM"|"PM" pode estar en minúsculas ou
   maiúsculas.
4. Se marcas a caixa de verificación "Horas caladas" e deixas vacíos os
   campos de "Hora de comezo das horas caladas" ou "Hora de finalización das
   horas caladas", a caixa de verificación "Horas caladas" desmarcarase
   automaticamente, para evitar erros.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
