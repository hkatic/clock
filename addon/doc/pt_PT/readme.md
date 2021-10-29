# Extra de Relógio e calendário para o NVDA #

* Autores: Hrvoje Katić, Abdel e colaboradores do NVDA
* Baixar a [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* Compatibilidade com o NVDA: 2019.3 e seguintes

Este complemento permite a funcionalidade avançada de relógio, temporizador
de alarme e calendário para NVDA.

Pode configurar o NVDA para anunciar a hora e a data em formatos diferentes
dos que o Windows fornece por defeito. Além disso, pode obter o dia actual,
o número da semana, bem como os dias restantes antes do fim do ano actual, e
também pode definir o anúncio automático da hora num intervalo
especificado. Há também um cronómetro e um temporizador de alarme integrados
no extra que lhe permite cronometrar as suas tarefas, tais como copiar
ficheiros, instalar programas, ou cozinhar refeições.

Nota:

* Se instalar uma atualização do extra, durante o processo de instalação, o
  assistente detecta se a configuração antiga é compatível com a nova e
  pergunta se quer fazer as alterações, que deverá confirmar no botão "ok".
* No Windows 10 e posteriores, pode utilizar a aplicação Alarmes e Relógio
  para gerir cronómetros e temporizadores.

## Comandos rápidos:

* NVDA+F12, diz a hora actual;
* nvda+f12, pressionado duas vezes, diz a data actual;
* NVDA+F12, pressionado três vezes rapidamente, informa o dia actual, o
  número da semana, o ano atual e os dias que faltam para o final do ano.
* NVDA+Shift+F12: entrar nos comandos em camada do relógio

## Comandos não atribuídos

Os seguintes comandos não estão atribuídos por defeito; se desejar
atribuí-los, utilize o menu Definir Comandos para adicionar comandos
personalizados. Para o fazer, abra o menu do NVDA, Preferências e depois
Definir Comandos. Expanda a categoria Relógio, depois localize os comandos
não atribuídos na lista abaixo e seleccione "Adicionar", depois introduza o
atalho que deseja utilizar.

* Tempo ecorrido e tempo restante antes do próximo alarme. Pressionar duas
  vezes rapidamente este comando irá cancelar o próximo alarme.
* Parar de tocar o som do alarme corrente.
* Mostra O diálogo de alarmes agendados

## Comandos em camada:

Para usar os comandos em camada, pressione NVDA+Shift+F12 seguido de uma das
seguintes teclas:

* S: Inicia, redefine ou pára o cronómetro;
* R: Redefine o cronómetro para 0, sem o reiniciar;
* A: dá o tempo decorrido e restante antes do próximo alarme
* P: Abre o diálogo de alarmes agendados
* C: Cancelar o próximo alarme
* Espaço: Lê o cronómetro actual ou o cronómetro de contagem regressiva;
* P: Se um alarme for muito longo, permite pará-lo;
* H: Lista todos os comandos em camada (Ajuda).

## Configuração e utilização

Para configurar as funcionalidades do relógio, abra o menudo  NVDA,
Preferências, depois Definições, e configure as seguintes opções a partir do
painel Relógio:

* Formato de hora e data: utilize estas caixas combinadas para configurar
  como o NVDA anunciará a hora e a data quando premir NVDA+F12 uma ou duas
  vezes, respectivamente, rapidamente.
* Intervalo: escolher o intervalo de tempo de anúncio a partir desta caixa
  combinada (desligado, a cada 10 minutos, 15 minutos, 30 minutos, ou a cada
  hora).
* Anúncio de tempo (activado se o intervalo de tempo não estiver desligado):
  escolha entre voz e som, apenas som, ou apenas voz.
* Sinal sonoro do relógio (activado se o intervalo não estiver desligado):
  seleccionar o sinal sonoro do relógio.
* Horas silenciosas (activado se o intervalo não estiver desligado):
  seleccione esta caixa de verificação para configurar o intervalo de horas
  silenciosas quando o anúncio automático da hora não deve ocorrer.
* Formato de horas silenciosas (activado se as horas silenciosas estiverem
  activadas): seleccionar como as opções de horas silenciosas são
  apresentadas (formato de 12 horas ou 24 horas).
* Início e fim de horas silenciosas: seleccione o intervalo de horas e
  minutos para as horas silenciosas a partir das caixas combinadas de horas
  e minutos.

Para agendar alarmes, abra o menu NVDA, Ferramentas, depois seleccione
Agendar Alarmes. O conteúdo do diálogo inclui:

* Duração do alarme em: seleccionar a duração do alarme/temporizador entre
  horas, minutos e segundos.
* Duração: introduzir a duração do alarme na unidade especificada acima.
* Som do alarme: seleccionar o som de alarme a ser tocado.
* Botões de paragem e pausa: parar ou pausar um longo som de alarme.

Clique OK, e uma mensagem irá informá-lo da duração do alarme seleccionado.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
