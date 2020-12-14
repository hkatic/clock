# Extra de Relógio e calendário para o NVDA #

* Autores: Hrvoje Katić, Abdel and NVDA contributors;
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]


Este extra permite funcionalidades avançadas de relógio, despertador e
calendário para o NVDA.

Em vez de obter sempre a hora e a data do Windows, pode personalizar a forma
como as horas e as datas devem ser faladas e mostradas em Braille pelo NVDA.

Além disso, pode obter o dia actual, o número da semana, bem como os dias
que faltam para o final do ano actual, e também pode definir o anúncio
automático das horas, no intervalo especificado.

Existem também um cronômetro e recursos de temporizador de alarme
incorporados ao extra, os quais permitem que indique um tempo para a
realização das suas tarefas, como copiar arquivos, instalar programas ou
cozinhar refeições.

## Nota:

Se instalar uma atualização do extra, durante o processo de instalação, o
assistente detecta se a configuração antiga é compatível com a nova e
pergunta se quer fazer as alterações, que deverá confirmar no botão "ok".

## Utilização:

* Abra a janela de configuração deste extra no menu de ferramentas do NVDA
  ou no painel de configurações, de acordo com a sua versão do NVDA;

    * Na caixa de diálogo de Configuração do Relógio, as duas primeiras
      Caixas combinadas permitem que escolha os seus formatos preferidos
      para mostrar hora e data;
    * A caixa combinada chamada "Intervalo" Permite-lhe definir o intervalo
      para o anúncio automático das horas (A cada 10 minutos, a cada 15
      minutos, a cada 30 minutos, a cada hora ou desligado);
    * A caixa de combinação rotulada "Anúncio de tempo" (visível apenas se a
      opção "Desligado" não estiver seleccionada na caixa de combinação de
      intervalo) permite configurar como o anúncio de hora automático deve
      ser feito (voz e som, somente voz ou somente som) quando o anúncio
      automático de horas está a funcionar;
    * A caixa de combinação chamada "Som da campainha do relógio" (visível
      apenas se a opção "odesligado" não estiver seleccionada na caixa de
      combinação do intervalo) permite escolher entre vários sons de relógio
      que serão reproduzidos quando o anúncio automático da hora estiver a
      funcionar e definido com som;
    * A caixa de marcação chamada "horas silenciosas" (somente visível se a
      opção "desligado" não estiver seleccionada na caixa de combinação do
      intervalo) permite configurar o intervalo de tempo durante o qual o
      anúncio de hora automático não deve ocorrer;
    * A caixa de selecção rotulada "entrada no formato de 24 horas" (visível
      apenas se as horas silenciosas estiverem activadas) permite configurar
      o horário de entrada para as horas silenciosas em 12 horas (AM ou PM)
      ou para o europeu de 24 horas ;
    * as caixas de edição para os horários de início e fim (visíveis apenas
      se as horas de silêncio estiverem activadas) permitem configurar o
      intervalo de tempo para as horas de silêncio. A hora deve ser inserida
      no formato HH:MM se a caixa de selecção "entrada no formato de 24
      horas" estiver marcada, caso contrário deve usar um formato de 12
      horas conforme descrito abaixo;
    * Depois de configurado, tab até "ok", para salvar as configurações
    * Na caixa de diálogo Configuração de alarme, a primeira Caixa de
      combinação permite que escolha o tempo de contagem regressiva antes do
      toque do alarme;
    * A caixa de edição permite-lhe escrever o tempo de espera antes do
      toque do alarme. Essa duração deve ser expressa em 1 ou mais dígitos,
      não num número decimal;
    * A caixa de combinação rotulada "Som de alarme" permite escolher entre
      os vários sons de alarme que serão reproduzidos;
    * O botão de pausa permite pausar / retomar alarmes muito longos;
    * O botão parar permite parar alarmes demasiado longos;
    * Quando terminar, clique no botão OK e active-o, pressionando
      Enter. Deve ser mostrada Uma mensagem, indicando o tempo que falta até
      ao alarme; 

* - NVDA+F12, diz a hora actual. - NVDA+F12, pressionado duas vezes
  rapidamente, diz a data actual. - NVDA+F12, pressionado três vezes
  rapidamente, informa o número actual do dia e da semana do ano em curso,
  bem como os dias que faltam para terminar o ano actual.

## Comandos rápidos:

* NVDA+F12, diz a hora actual;
* nvda+f12, pressionado duas vezes, diz a data actual;
* NVDA+F12, pressionado três vezes rapidamente, informa o dia actual, o
  número da semana, o ano atual e os dias que faltam para o final do ano.
* Há um script que fornece o tempo restante e o decorrido antes do próximo
  alarme;
* Não há nenhum comando atribuído a este script, Terá que que o definir na
  caixa de diálogo "definir comandos", na categoria "Relógio";
* Este comando, pressionado duas vezes, cancela o próximo alarme
* Há também um script para parar o som que está a ser tocado. também não tem
  comando atribuído.
* Este script também pode ser chamado usando os comandos em camada, do
  relógio, descritos abaixo.

## Comandos em camada:

Para usar os comandos em camada, pressione NVDA+Shift+F12 seguido de uma das
seguintes teclas:

* S: Inicia, redefine ou pára o cronómetro;
* R: Redefine o cronómetro para 0, sem o reiniciar;
* A: fornece o tempo restante e o decorrido antes do próximo alarme;
* C: Cancela o próximo alarme;
* Espaço: Lê o cronómetro actual ou o cronómetro de contagem regressiva;
* P: Se um alarme for muito longo, permite pará-lo;
* H: Lista todos os comandos em camada (Ajuda).

## Sintaxe a ser usada para as horas silenciosas

* Para evitar bugs, as horas silenciosas devem seguir uma sintaxe rigorosa e
  precisa;
* Se marcar a caixa de selecção "Entrada no formato de 24 horas", o formato
  deve ser "HH:MM";
* Se desmarcar a caixa de selecção "Entrada no formato de 24 horas", o
  formato deve ser "HH:MM AM" ou "HH:MM PM", o HH deve conter um formato de
  12 horas, de 0 a 12 e o sufixo "AM "|" PM "pode estar em minúsculas ou
  maiúsculas
* Se marcar a caixa de selecção horas silenciosas e mantiver o campo "Início
  das horas silenciosas" ou "tempo para terminarem as horas de silêncio"
  vazio ou escrever um valor incorrecto, a caixa de selecção "horas
  silenciosas" será desmarcada automaticamente para evitar erros;
* Deve ser mostrada uma mensagem, para indicar o seu erro

## Compatibilidade:

* Este extra é compatível com as versões do NVDA que se encontram entre a
  2014.3 e a 2019.3, inclusive.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

