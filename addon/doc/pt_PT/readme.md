# Extra de Relógio e calendário para NVDA #

* Autores: Hrvoje Katić, Abdel e colaboradores do NVDA
* Compatibilidade com o NVDA: 2019.3 e posterior

Este extra ativa funcionalidades avançadas de relógio, temporizador de alarme e calendário para o NVDA.

Pode configurar o NVDA para anunciar a hora e a data em formatos diferentes dos fornecidos por defeito pelo Windows. Além disso, pode obter o dia atual, o número da semana, bem como os dias restantes até ao fim do ano atual, e também pode definir o anúncio automático da hora em intervalos especificados. O extra também inclui funcionalidades de cronómetro e temporizador de alarme que permitem cronometrar tarefas, como copiar ficheiros, instalar programas ou cozinhar refeições.

## Notas:

* se instalar o extra como atualização, durante o processo de instalação, o assistente deteta se a configuração antiga é compatível com a nova e oferece a sua correção antes da instalação, depois basta confirmar o botão OK.
* No Windows 10 e posterior, pode utilizar a aplicação Alarmes e Relógio para gerir cronómetros e temporizadores.

## Comandos de teclas

* NVDA+F12: obter a hora atual
* NVDA+F12 premido duas vezes rapidamente: obter a data atual
* NVDA+F12 premido três vezes rapidamente: anuncia o dia atual, o número da semana, o ano atual e os dias restantes até ao fim do ano
* NVDA+Shift+F12: entrar na camada do relógio

## Comandos não atribuídos

Os seguintes comandos não estão atribuídos por defeito; se quiser atribuí-los, utilize a caixa de diálogo Gestos de entrada para adicionar comandos personalizados. Para isso, abra o menu NVDA, Preferências, depois Gestos de entrada. Expanda a categoria Relógio, encontre os comandos não atribuídos na lista abaixo e selecione "Adicionar", depois introduza o gesto que pretende utilizar.

* Tempo decorrido e restante até ao próximo alarme. premir este gesto duas vezes rapidamente cancela o próximo alarme.
* Parar o som do alarme atualmente em reprodução.
* Mostrar caixa de diálogo de agendamento de alarmes.
* Mostrar comandos em camada (teclas após NVDA+Shift+F12).

## Comandos em camada

Para usar comandos em camada, prima NVDA+Shift+F12 seguido de uma das seguintes teclas:

* S: inicia, repõe ou para o cronómetro
* R: repõe o cronómetro para 0 sem reiniciar
* A: indica o tempo decorrido e restante até ao próximo alarme
* T: abre a caixa de diálogo de agendamento de alarmes
* C: cancela o próximo alarme
* Espaço: anuncia o cronómetro atual ou temporizador de contagem decrescente
* P: se um alarme for demasiado longo, permite pará-lo
* H: lista todos os comandos em camada (Ajuda)

## Configuração e utilização

Para configurar a funcionalidade do relógio, abra o menu NVDA, Preferências, depois Definições, e configure as seguintes opções no painel Relógio:

* Formato de apresentação da hora e da data: utilize estas caixas de combinação para configurar como o NVDA irá anunciar a hora e a data quando premir NVDA+F12 uma ou duas vezes rapidamente.
* Intervalo: escolha o intervalo de anúncio da hora nesta caixa (desligado, a cada 10 minutos, 15 minutos, 30 minutos ou a cada hora).
* Anúncio da hora (ativado se o intervalo não estiver desligado): escolha entre voz e som, apenas som ou apenas voz.
* Som do toque do relógio (ativado se o intervalo não estiver desligado): selecione o som padrão do relógio.
* Sinos separados para horas e minutos intermédios (ativado se o intervalo não estiver desligado, desativado por defeito): ative esta caixa para personalizar os sons dos minutos intermédios separadamente do som da hora.
  * Som dos minutos intermédios (ativado se "sinos separados para horas e minutos intermédios" estiver marcado): selecione o som para os minutos intermédios.
* Horas silenciosas (ativado se o intervalo não estiver desligado): selecione esta caixa para configurar o intervalo de horas silenciosas.
* Formato das horas silenciosas (ativado se as horas silenciosas estiverem ativadas): selecione como as opções são apresentadas (formato de 12 ou 24 horas).
* Hora de início e fim das horas silenciosas: selecione o intervalo de horas e minutos para as horas silenciosas nas caixas de combinação.

Para agendar alarmes, abra o menu NVDA, Ferramentas, depois selecione Agendar alarmes. O diálogo inclui:

* Duração do alarme: selecione a duração do alarme/temporizador em horas, minutos e segundos.
* Duração: introduza a duração do alarme na unidade especificada acima.
* Som do alarme: selecione o som do alarme.
* Botões parar e pausar: parar ou pausar um alarme longo.

Prima OK e será apresentada uma mensagem a indicar a duração do alarme selecionada.
