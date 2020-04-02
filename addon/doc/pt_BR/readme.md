# Complemento de relógio e calendário para o NVDA (Clock and calendar Add-on for NVDA) #

* Autores: Hrvoje Katić, Abdel e colaboradores do NVDA;
* Baixe a [versão estável][1];
* Baixe a [versão em desenvolvimento][2].


Esse complemento permite a funcionalidade avançada de relógio, despertador e
calendário para o NVDA.

Em vez de obter sempre a hora e data do Windows, pode personalizar a forma
como as horas e datas devem ser faladas e mostradas em Braille pelo NVDA.

Além disso, pode obter o dia atual, o número da semana, bem como os dias que
faltam para o final do ano atual, e também pode definir o anúncio automático
das horas no intervalo especificado.

Existe também um cronômetro e recursos de temporizador embutidos no
complemento, que permitem agendar suas tarefas, como copiar arquivos,
instalar programas ou preparar refeições.

## Nota:

Se instalar uma atualização do complemento, durante o processo de
instalação, o assistente detecta se a configuração antiga é compatível com a
nova e se oferecerá para corrigi-la antes da instalação, basta ratificar com
botão OK para confirmar isso.

## Utilização

* Abra a janela de configuração deste complemento no menu de ferramentas do
  NVDA ou no painel de configurações, de acordo com a sua versão do NVDA;

    * No diálogo de Configuração do Relógio, as duas primeiras Caixas
      combinadas permitem que escolha os seus formatos preferidos para
      mostrar hora e data;
    * O controle Caixa de Combinação chamado "Intervalo" permite definir o
      intervalo para o anúncio automático de hora (a cada 10 minutos, a cada
      15 minutos, a cada 30 minutos, a cada hora ou desativado);
    * O controle Caixa de Combinação rotulado "Anúncio de tempo" (visível
      apenas se a opção "desligado" não estiver selecionada na caixa de
      combinação de intervalo) permite configurar como o anúncio de hora
      automático deve ser feito (Voz e Som, Somente Voz ou Somente Som)
      quando o anúncio automático de horas está funcionando;
    * O controle Caixa de combinação chamado "Som da badalada do relógio"
      (visível apenas se a opção "desligado" não estiver selecionada na
      caixa de combinação do intervalo) permite escolher entre vários sons
      de relógio que serão reproduzidos quando o anúncio automático da hora
      estiver funcionando e informado com som;
    * O controle Caixa de Seleção chamado "Horas silenciosas" (somente
      visível se a opção "desligado" não estiver selecionada na caixa de
      combinação do intervalo) permite configurar o intervalo de tempo
      durante o qual o anúncio de hora automático não deve ocorrer;
    * O controle Caixa de Seleção rotulado "entrada no formato de 24 horas"
      (visível apenas se as horas silenciosas estiverem habilitadas) permite
      configurar o horário de entrada para as horas silenciosas em 12 horas
      (AM ou PM) ou para o formato europeu de 24 horas;
    * Os controles Caixas de edição para os horários de início e fim
      (visíveis apenas se as horas silenciosas estiverem habilitadas)
      permitem configurar o intervalo de tempo para as horas de silêncio. A
      hora deve ser inserida no formato HH:MM se a caixa de seleção "entrada
      no formato de 24 horas" estiver marcada, caso contrário deve usar um
      formato de 12 horas conforme descrito abaixo;
    * Quando terminar, vá para o botão OK e ative-o pressionando Enter para
      salvar suas configurações;
    * No diálogo Configuração de alarme, o primeiro controle Caixa de
      Combinação permite que escolha o seu temporizador preferido antes do
      toque do alarme;
    * O controle Caixa de edição permite-lhe escrever seu tempo de espera
      antes do toque do alarme. Essa duração deve ser expressa em 1 ou mais
      dígitos, não num número decimal;
    * O controle Caixa de combinação rotulado "Som de alarme" permite
      escolher entre os vários sons de alarme que serão reproduzidos quando
      chegar a hora do alarme;
    * O botão pausa permite pausar/retomar alarmes muito longos;
    * O botão parar permite parar alarmes demasiado longos;
    * Quando terminar, vá para o botão OK e ative-o pressionando Enter. Uma
      mensagem deve ser exibida para lembrá-lo do tempo de espera até o
      alarme;

* Pressione NVDA+F12 uma vez para obter a hora atual, duas vezes para obter
  a data atual ou três vezes para obter o dia atual, o número da semana e os
  dias restantes para o final do ano atual.

## Comandos principais

* NVDA+F12, obtém a hora atual;
* NVDA+F12 pressionado duas vezes rapidamente, obtém a data atual;
* NVDA+F12, pressionado três vezes rapidamente, informa o dia atual, o
  número da semana, o ano atual e os dias que faltam para o final do ano.
* Há um script que fornece o tempo restante e o decorrido antes do próximo
  alarme;
* Não há nenhum comando de teclado atribuído a esse script, terá que fazer
  isso sozinho na caixa de diálogo "Definir comandos", na categoria
  "Relógio";
* Este comando pressionado duas vezes, cancela o próximo alarme;
* Há outro script para interromper o som que está sendo reproduzido no
  momento, também não tem comando definido;
* Este script também pode ser chamado usando os comandos em camada, do
  relógio, descritos abaixo.

## Comandos em camada

Para usar os comandos em camada, pressione NVDA+Shift+F12 seguido de uma das
seguintes teclas:

* S: Inicia, redefine ou pára o cronômetro;
* R: Redefine o cronômetro para 0, sem reiniciá-lo;
* A: fornece o tempo restante e o decorrido antes do próximo alarme;
* C: Cancela o próximo alarme;
* Espaço: Fala o cronômetro atual ou o temporizador de contagem regressiva;
* p: Se um alarme for muito longo, permite pará-lo;
* H: Lista todos os comandos em camada (Ajuda).

## Sintaxe a ser usada para as horas silenciosas

* Para evitar falhas, as horas silenciosas devem seguir uma sintaxe rigorosa
  e precisa;
* Se marcar a caixa de seleção "Entrada no formato de 24 horas", o formato
  deve ser "HH:MM";
* Se desmarcar a caixa de seleção "Entrada no formato de 24 horas", o
  formato deve ser "HH:MM AM" ou "HH:MM PM", o HH deve conter um formato de
  12 horas, de 0 a 12 e o sufixo "AM"|"PM" pode estar em minúsculas ou
  maiúsculas
* Se marcar a caixa de seleção "Horas silenciosas" e manter o campo "Início
  das horas silenciosas" ou "Fim das horas silenciosas" vazio, ou digitar um
  valor incorreto, a caixa de seleção "Horas silenciosas" será desmarcada
  automaticamente, para evitar erros;
* Uma mensagem deve ser exibida para relatar seu erro.

## Compatibilidade

* Esse complemento é compatível com as versões do NVDA que variam de 2014.3
  a 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

