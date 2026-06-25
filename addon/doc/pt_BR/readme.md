# Complemento Relógio e calendário para o NVDA #

* Autores: Hrvoje Katić, Abdel e colaboradores do NVDA
* Compatibilidade com o NVDA: 2019.3 e versões posteriores

Este complemento habilita funcionalidades avançadas de relógio, temporizador de alarme e calendário para o NVDA.

Você pode configurar o NVDA para anunciar a hora e a data em formatos diferentes dos fornecidos por padrão pelo Windows. Além disso, você pode obter o dia atual, o número da semana, bem como os dias restantes até o final do ano atual, e também pode definir o anúncio automático da hora em intervalos especificados. O complemento também inclui funções de cronômetro e temporizador de alarme que permitem cronometrar tarefas, como copiar arquivos, instalar programas ou cozinhar refeições.

## Notas:

* se você instalar o complemento como uma atualização, durante o processo de instalação, o assistente detecta se a configuração antiga é compatível com a nova e oferece corrigi-la antes da instalação, então basta confirmar o botão OK.
* No Windows 10 e posteriores, você pode usar o aplicativo Alarmes e Relógio para gerenciar cronômetros e temporizadores.

## Comandos de teclas

* NVDA+F12: obter a hora atual
* NVDA+F12 pressionado duas vezes rapidamente: obter a data atual
* NVDA+F12 pressionado três vezes rapidamente: relata o dia atual, o número da semana, o ano atual e os dias restantes até o final do ano
* NVDA+Shift+F12: entrar na camada do relógio

## Comandos não atribuídos

Os seguintes comandos não estão atribuídos por padrão; se desejar atribuí-los, use o diálogo Gestos de entrada para adicionar comandos personalizados. Para isso, abra o menu NVDA, Preferências, depois Gestos de entrada. Expanda a categoria Relógio, localize os comandos não atribuídos na lista abaixo e selecione "Adicionar", depois insira o gesto que deseja usar.

* Tempo decorrido e restante até o próximo alarme. pressionar esse gesto duas vezes rapidamente cancela o próximo alarme.
* Parar o som do alarme em reprodução no momento.
* Exibir caixa de diálogo de agendamento de alarmes.
* Mostrar comandos em camada (teclas após NVDA+Shift+F12).

## Comandos em camada

Para usar comandos em camada, pressione NVDA+Shift+F12 seguido de uma das seguintes teclas:

* S: inicia, redefine ou para o cronômetro
* R: redefine o cronômetro para 0 sem reiniciar
* A: informa o tempo decorrido e restante até o próximo alarme
* T: abre o diálogo de agendamento de alarmes
* C: cancela o próximo alarme
* Espaço: anuncia o cronômetro atual ou contagem regressiva
* P: se um alarme for muito longo, permite pará-lo
* H: lista todos os comandos em camada (Ajuda)

## Configuração e uso

Para configurar a funcionalidade do relógio, abra o menu NVDA, Preferências, depois Configurações, e configure as seguintes opções no painel Relógio:

* Formato de exibição da hora e da data: use essas caixas de combinação para configurar como o NVDA anunciará a hora e a data ao pressionar NVDA+F12 uma ou duas vezes rapidamente.
* Intervalo: escolha o intervalo de anúncio da hora nesta caixa (desligado, a cada 10 minutos, 15 minutos, 30 minutos ou a cada hora).
* Anúncio da hora (ativado se o intervalo não estiver desligado): escolha entre fala e som, apenas som ou apenas fala.
* Som do toque do relógio (ativado se o intervalo não estiver desligado): selecione o som padrão do relógio.
* Sinos separados para horas e minutos intermediários (ativado se o intervalo não estiver desligado, desativado por padrão): ative esta caixa de seleção para personalizar os sons dos minutos intermediários separadamente do som da hora.
  * Som dos minutos intermediários (ativado se "sinos separados para horas e minutos intermediários" estiver marcado): selecione o som para os minutos intermediários.
* Horas silenciosas (ativado se o intervalo não estiver desligado): marque esta caixa para configurar o intervalo de horas silenciosas.
* Formato das horas silenciosas (ativado se as horas silenciosas estiverem ativadas): selecione como as opções são exibidas (formato de 12 ou 24 horas).
* Horário de início e término das horas silenciosas: selecione o intervalo de horas e minutos para as horas silenciosas nas caixas de combinação.

Para agendar alarmes, abra o menu NVDA, Ferramentas, depois selecione Agendar alarmes. O diálogo contém:

* Duração do alarme: selecione a duração do alarme/cronômetro em horas, minutos e segundos.
* Duração: insira a duração do alarme na unidade especificada acima.
* Som do alarme: selecione o som do alarme.
* Botões parar e pausar: parar ou pausar um alarme longo.

Clique em OK e uma mensagem informará a duração do alarme selecionado.
