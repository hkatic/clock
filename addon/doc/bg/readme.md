# Добавка за NVDA за часовника и календара

- Автори: Hrvoje Katić, Abdel и други сътрудници на NVDA
- Изтегляне на [стабилна версия][1]
- Съвместимост с NVDA: от 2019.3 и по-нови версии
- NVDA compatibility: 2019.3 and later

Тази добавка за NVDA разширява възможностите за работа с часовника, алармата
за обратно отброяване и календара.

You can configure NVDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

Забележки:

- if you install the add-on as an update, during the installation process, the wizard detects if the old configuration is compatible with the new one and offers to correct it before installing, then you'll just have to validate the OK button to confirm that.
- В Windows 10 и по -нови версии можете да използвате приложението "Аларми и
  часовник" за управление на хронометъра и таймерите.

## Клавишни комбинации

- NVDA+F12: Съобщаване на текущия час.
- Двукратно бързо натискане на NVDA+F12: Съобщаване на текущата дата.
- Трикратно бързо натискане на NVDA+F12: Съобщаване на текущия ден, номера
  на седмицата, текущата година и оставащите дни преди края на годината
- NVDA+Shift+F12: Влизане в слоя за часовника

## Неприсвоени команди

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.

- Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
- Спира просвирването на звука от текущата аларма.
- Показване на диалоговия прозорец за планиране на аларми.
- Show layered commands (keys to be pressed after NVDA+Shift+F12).

## Слоеви команди

За да използвате слоевите команди, натиснете NVDA+Shift+F12, последвано от
един от следните клавиши:

- S: Стартира, нулира или спира хронометъра
- R: Нулира хронометъра, без да го рестартира
- A: Съобщава оставащото и изминалото време преди следващата аларма
- T: Отваряне на диалоговия прозорец за планиране на аларми.
- C: Отмяна на следващата аларма
- Интервал: Изговаря текущия хронометър или таймера за обратно отброяване
- P: Ако дадена аларма е прекалено дълга, ви позволява да я спрете
- H: Списък на всички слоеви команди (Помощ)

## Настройка и начин на употреба

За да конфигурирате функциите на часовника, отворете менюто на NVDA ->
Настройки -> Опции и от категорията "Часовник" конфигурирайте следните
опции:

- Формат за показване на час и дата: Използвайте тези падащи списъци, за да
  конфигурирате как NVDA ще съобщава часа и датата, когато натиснете
  NVDA+F12 еднократно или двукратно.
- Интервал: Изберете интервала за съобщаване на часа от този падащ списък
  (изключено, на всеки 10 минути, 15 минути, 30 минути или на всеки час).
- Съобщаване на часа (активно, ако интервалът не е зададен на "Изключено"):
  Изберете между реч и звук, само звук или само реч.
- Звук на часовника (активно, ако интервалът не е зададен на "Изключено"):
  Изберете звука на часовника.
- Тихи часове (активно, ако интервалът не е зададен на "Изключено"):
  Поставете отметка в това поле, за да конфигурирате диапазона на тихите
  часове, в който не трябва да се извършва автоматично оповестяване на часа.
  - Intermediate minutes chime sound (enabled if "Separate hour and intermediate minute chimes" is checked): Select the clock chime sound specifically for intermediate minutes.
- Формат на часа за тихи часове (активно, ако е включен режима "Тихи
  часове"): Изберете как да се представят опциите за тихи часове (12-часов
  или 24-часов формат).
- Начален и краен час за тихите часове: Изберете диапазона в часове и минути
  за тихи часове от падащите списъци за часове и минути.
- Quiet hours start and end times: select hour and minute range for quiet hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The dialog contents include:

- Продължителност на алармата в: Изберете продължителност на
  алармата/таймера между часове, минути и секунди.
- Продължителност: Въведете продължителността на алармата в посочената
  по-горе единица.
- Звук на алармата: Изберете звука на алармата, който да се възпроизвежда.
- Бутони "Спри" и "Пауза": Спиране или поставяне на пауза на дълъг алармен
  звук.

Задействайте бутона "OK" и съобщение ще ви информира за продължителността на
текущо избраната аларма.

[1]: https://addons.nvda-project.org/files/get.php?file=cac
[2]: https://www.nvaccess.org/addonStore/legacy?file=clock
