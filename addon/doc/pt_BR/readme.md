# Complemento de relógio e calendário para o NVDA (Clock and calendar Add-on for NVDA) #

* Autores: Hrvoje Katić, Abdel e colaboradores do NVDA
* Baixe a [versão estável][1]

* Compatibilidade com NVDA: 2019.3 e posteriores

Este complemento habilita a funcionalidade avançada de relógio, temporizador
com alarme e calendário para o NVDA.

Você pode configurar o NvDA para anunciar a hora e a data em formatos
diferentes dos fornecidos pelo Windows por padrão. Além disso, pode obter o
dia atual, o número da semana, bem como os dias restantes para o fim do ano
atual, e também pode definir o anúncio automático de hora em um intervalo
especificado. Há também um cronômetro e recursos de temporizador com alarme
integrados ao complemento que permitem cronometrar suas tarefas, como copiar
arquivos, instalar programas ou cozinhar refeições.

Notas:

* se instalar uma atualização do complemento, durante o processo de
  instalação, o assistente detecta se a configuração antiga é compatível com
  a nova e se oferecerá para corrigi-la antes da instalação, basta ratificar
  com botão OK para confirmar isso.
* No Windows 10 e posteriores, você pode usar o aplicativo Alarmes e Relógio
  para gerenciar o cronômetro e os temporizadores.

## Comandos principais

* NVDA+F12: obtém a hora atual
* NVDA+F12 pressionado duas vezes rapidamente: obtém a data atual
* NVDA+F12 pressionado três vezes rapidamente: informa o dia atual, o número
  da semana, o ano atual e os dias que faltam para o fim do ano
* NVDA+Shift+F12: entra camada de relógio

## Comandos não atribuídos

Os comandos a seguir não são atribuídos por padrão; se desejar atribuí-los,
use o diálogo Definir Comandos — Gestos de Entrada — para adicionar comandos
personalizados. Para fazer isso, abra o menu NVDA, Preferências e Definir
Comandos. Expanda a categoria Relógio, localize os comandos não atribuídos
na lista abaixo e selecione "Adicionar" e insira o comando — gesto — que
deseja usar.

* Tempo decorrido e restante antes do próximo alarme. pressionar este
  comando — gesto — duas vezes rapidamente cancelará o próximo alarme.
* Parar de tocar o som do alarme no momento.
* Exibe a caixa de diálogo agendar alarmes.

## Comandos em camada

Para usar os comandos em camada, pressione NVDA+Shift+F12 seguido de uma das
seguintes teclas:

* S: Inicia, redefine ou pára o cronômetro
* R: Redefine o cronômetro para 0, sem reiniciá-lo
* A: fornece o tempo restante e o decorrido antes do próximo alarme
* T: abre o diálogo de agendamento de alarmes.
* C: Cancela o próximo alarme
* Espaço: Fala o cronômetro atual ou o temporizador de contagem regressiva
* p: Se um alarme for muito longo, permite pará-lo
* H: Lista todos os comandos em camada (Ajuda)

## Configuração e uso

Para configurar a funcionalidade do relógio, abra o menu NvDA, Preferências,
Configurações, e configure as seguintes opções no painel Relógio:

* Formato de exibição de data e hora: use essas caixas de combinação para
  configurar como o NVDA anunciará a hora e a data quando você pressionar
  NVDA+F12 uma ou duas vezes rapidamente, respectivamente.
* Intervalo: escolha o intervalo do anúncio de horário nesta caixa de
  combinação (desligado, a cada 10 minutos, 15 minutos, 30 minutos ou a cada
  hora).
* Anúncio de hora (habilitado se o intervalo não estiver desativado):
  escolha entre fala e som, somente som ou somente fala.
* Som da badalada do relógio (habilitado se o intervalo não estiver
  desativado): selecione o som da badalada do relógio.
* Horas silenciosas (habilitado se o intervalo não estiver desativado):
  marque esta caixa de seleção para configurar o intervalo de horas
  silenciosas quando o anúncio automático de horário não deve ocorrer.
* Formato de horas silenciosas (habilitado se horas silenciosas estiver
  habilitada): selecione como as opções de horário silencioso são
  apresentadas (formato de 12 ou 24 horas).
* Horários de início e término de horas silenciosas: selecione o intervalo
  de horas e minutos para horários silenciosos a partir das caixas de
  combinação de horas e minutos.

Para agendar alarmes, abra o menu NVDA, Ferramentas e selecione Agendar
Alarmes. O conteúdo da caixa de diálogo inclui:

* Duração do alarme em: selecione a duração do alarme/cronômetro entre
  horas, minutos e segundos.
* Duração: insira a duração do alarme na unidade especificada acima.
* Som do alarme: selecione o som do alarme a ser reproduzido.
* Botões de parar e pausar: parar ou pausar um som de alarme longo.

Clique em OK e uma mensagem informará a duração do alarme atualmente
selecionado.

[[!tag stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=clock
