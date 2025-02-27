# Банк задач в lms.

Описывается регламент работы с задачами для контрольной. А так же задачи для домашней работы и задачи для зачета. Создание новых задач.
# Чистота метрики
## Проблемы
Контрольные по курсу информатики вместе с входным тестированием позволяют оценить успешность освоения материала и прогресс студента. Для этого задачи студент должен решать самостоятельно. Пути обхода:
* Списать у соседа
* Решить с помощью high-level студента
* "Слитые" задачи
* ИИ
## Пути решения
**Списать у соседа** - если студент может списать код и разобраться в нем это как минимум, удовлетворительно. Студенты с неудовлетворительным уровнем списать не могут. Так же защитой служит минимум 3 варианта задач.
**Решить с помощью high-level студента или ИИ** - решается изоляцией связи студента с внешним миром на время контрольной. 
* Контрольная пишется с компьютеров из учебных классов с фильтрацией по IP без доступа к внешнему интернету.
* Телефоны кладутся на стол преподавателя.
* Условие задачи защищается от копирования (при этом не должно быть штрафов за неудачные решения по причине ошибки компиляции и сборки, так как повысится число опечаток при копировании, при разработке новых задач нужно обращать внимание на краткость названия; если какой-то код должен быть скопирован, он выдается в отдельном файле, доступном для скачивания).
**"Слитые" задачи** - с ними можно бороться, как и со списыванием у соседей, повышая количество вариантов крайне похожих задач, так чтобы задачу проще было решить самому, а не найти свой вариант задачи из 20 "разных одинаковых задач". Так же нужно минимизировать количество людей, которые видят задачи до контрольной. Доступ к задачам ограничивается только авторами задач и прорешивателями (людьми, которые умеют вычитывать задачи, находить некорректные и расплывчатые формулировки и дыры в тестах).
То есть **при росте количества вариантов задачи увеличивается надежность задачи как метрики**.
Создать контрольную из 1 варианта - большой труд, из 2 вариантов - огромный труд. Команда Васюков/Беклемышева в семестр делает контрольные из 1 варианта, некоторые задачи могут быть в 2 вариантах. На ФРТК авторы задач отчасти исчезли (Овсянникова, Владимиров), осталась Дивари (умеет делать темы проектов и задачи, но нет опыта многих вариантов) и Дербышева (автор многовариантных задач к контрольной).
Молодых авторов задач у нас нет. При этом есть техническая возможность создавать задачи и отлаживать их любым человеком (не важно, преподавателем, аспирантом или студентом).
Брать задачу из олимпиады, школы и тп. через Подлесных - не выход. Так как нет вариантов задач, условия перегружены "литературностью" и нет простых задач. Т.е. можно брать 1-2 задачи без вариантов "гробов", которые нужны, чтобы топовые студенты не начинали решать задачи соседей после того, как их задачи закончились. Такие задачи могут выявить студентов для олимпиад (если кафедра в них заинтересована).
# Банк задач контрольной
Выход - **банк вариантов задач, который накапливается из года в год**. Если в задаче будет 100 вариантов, то любой поток может использовать их из года в год. Такой банк создан на базе контольных по языку Си и ранее использовался для проведения контрольных нескольких факультетов (ФРТК, ФУПМ, ФИВТ, ФАЛТ и тп). Осенью 2024 банк задач использовался для проведения 6 контрольных в семестре (2 контрольных, 3 потока). 
## Текущее состояние банка задач
### Первая контрольная
...
### Вторая контрольная

| Название задачи | Количество вариантов | Тема                                                             | Адаптивность к другим языкам                                  |
| --------------- | -------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- |
| `C_dist_noptr`  | 19                   | задача на структуры                                              | легко                                                         |
| `C_geom`        | 36                   | задача на структуры с указателями                                | легко С++                                                     |
| `C_mem_geom`    | 18                   | задача на структуры с выделением динамической памяти             | легко С++ (классы)                                            |
| `D`             | 11                   | задача на структуры (комбинации покера)                          | легко                                                         |
| `E`             | 21                   | строки                                                           | малоприменимо в C++ / python из-за функций работы со строками |
| `Emem`          | 17                   | строки с выделением динамической памяти                          | малоприменимо в C++ / python из-за функций работы со строками |
| `ES`            | 4                    | использование строк (период и палиндром)                         | любой язык                                                    |
| `F`             | 23                   | сортировка                                                       | любой язык                                                    |
| `G`             | 20                   | бинарные деревья                                                 | малоприменимо в C++ / python из-за библиотек                  |
| `ptr`           | 20                   | задача на структуры на длинную арифметику                        | легко С++ (классы)<br>бесполезна для python                   |
| `mem`           | 12                   | задача на структуры на длинную арифметику с динамической памятью | легко С++ (классы)<br>бесполезна для python                   |


## Создание многовариантной контрольной
Самое сложное - первичное накопление задач. Простую задачу давать лучше 1 вариант на 1-2 успешных решения, 5 и более успешных решений на вариант создают проблемы для систем антиплагиата. То есть для факультета из 70 человек нужно 14+ вариантов, менее 5 вариантов можно давать только на непростых задачах. Или преподаватели стахановски делают по набору вариантов в темпе 1 задача в год и наполнение происходит 5 лет. Или задачи прошлого года добавляются в варианты следующего года и идет прогрессия 2-4-6-10-12-14 вариантов в те же 5 лет, но задачи первого года с большой вероятностью известны студентам (это можно посмотреть по % успешных решений старых вариантов относительно новых вариантов).
Этот процесс можно ускорить, если авторов задач будет больше. Или если воспользоваться банком задач других факультетов.
Для первого года изучения информатики темы задач примерно одинаковые и только слегка зависят от изучаемого языка. В банке задачи делятся на:
* не зависящие от языка (даны координаты прямоугольника, повернуть его на 90 градусов относительно центра координат, напечатать координаты полученного прямоугольника; задачи на сортировку)
* легко модифицируемые (написать функцию поворота прямоугольника относительно центра координат, прямоугольник передается в виде указателя на структуру; модифицируем в объект класса С++/python или словарь python)
* языкозависимые (например, используется специфическая библиотека для работы с матрицами или рисования графиков).
То есть если факультет готов вкладываться, он может взять языконезависимые задачи и модифицировать легко модифицируемые в первый год. Для этого можно взять или неопытных авторов, а опытные делают 1-2 уникальные задачи или один год авторы занимаются только модификацией под свой язык.
### Поддержание многовариантной контрольной
Далее каждый год факультет "платит дань" новыми вариантами за каждую контрольную, исходя из формулы **(количество студентов / 5) с округлением вверх**. Эти варианты могут или добавляться с существующим задачам (еще Х вариантов задач на сортировку), или быть началом новой задачи (задача на стек/словарь, Х вариантов).
# Регламент добавления задач и проведения контрольных
## Доступ к материалам контрольных
* Доступ к задачам во время контрольной имеют:
	* студенты (только к своим задачам и вариантам)
	* преподаватели (не авторы) - такой же доступ, что у студентов для проверки работоспособности системы.
* Доступ к задачам контрольных вне времени контрольных имеют:
	* авторы задач - те, кто придумывают и создают задачи для банка.
	* прорешиватели - кто проверяет новые задачи (условия, тесты и тп)
	* эти люди называются создателями контрольных
	* прочие люди не имеют доступа к условиям задач и тестов вне времени контрольной.
## Регламент проведения контрольной
* В начале семестра (или ранее, но не позже второй недели семестра) отвественный за контрольную (например, лектор) выдает  
	* список тем контрольной
	* количество желаемых задач с указанием сложности
	* количество групп и студентов, которые будут писать контрольную
	* даты контрольных (с учетом графика учебных пожарных тревог, ответственный - зам.зав.кафедрой)
	* будет ли переписывание контрольных (дата, время)
* На основании этой информации создатели контрольных коллегиально решают какие варианты/задачи каким потокам они будут давать с учетом создания новых задач.
	* Новые задачи даются преимущественно потоку, на котором преподает автор задачи.
	* По договоренности возможен взаимозачет задач.
	* За новыми задачами закрепляются прорешиватели.
	* По потокам назначается кто будет создавать контест контрольной для потоков (создатели контестов).
	* О времени и датах контрольных сообщается в техподдержку lms.
* Ответственные за факультет организуют создание кафедральных групп, в которых будет проходить контрольная с учетом распределения и переводов.
* Не позднее, чем за неделю все задачи контрольной должны быть созданы и не позже, чем за 2 дня - прорешены и поправлены.
* За 2 дня до контрольной создатель контеста создает контест контрольной.
* (Кто?) обеспечивает, чтобы ссылка на контест во время конторольной была доступна студентам потока контрольной.
* (Кто?) напоминает в поддержку lms.
* Ответственный за факультет организует уведомление преподавателей и студентов факультета о дате и времени контрольной не позднее, чем за неделю до ее проведения.
* Отвественный за факультет организует рассадку студентов по компьютерам в учебных классов с учетом недостатка компьютеров. Возможно выделение дополнительной аудитории и ассистента в нее, если в компьютерах учебных классов по расписанию недостаточно работающих компьютеров с доступом к контесту контрольной.
* **Дорешивание контрольной запрещено**. Для выяснения текущего уровня студента преподаватель может использовать задачи для зачета.
## Техническое сопровождение контрольной
* Ответственный за факультет назначает 1-2 человек ответственных за техническое сопровождение контрольной (1+ человек на корпус).
* Отвественный за факультет заранее узнает в каких аудиториях недостаток / избыток компьютеров и передает эту информацию тех.ответственным.
* Отвественный за факультет дает контакты ответственных за тех. сопровождение остальным преподавателям потока контрольной.
* Отвественный за факультет и руководство кафедры обеспечивают 1+ ассистента на время проведения контрольной. Ассистенту даются контакты ответственных за тех.сопровождение, отвественным за тех.сопровождение даются контакты ассистентов). 
* Если не хватает компьютеров в аудиториях с учетом пересаживания за пустые места, ассистент идет в дополнительную аудиторию.
* Если в аудитории отсутствует преподаватель, ответственный за факультет решает проблему. Студенты не должны писать контрольную безнадзорно.
* В начале контрольной тех.ответственный убеждается, что в его аудитории могут войти в контест и начать решать задачи.
* После старта контрольной в своей аудитории (не позже 10 минут от старта контрольной) тех.отвественный проходит по другим аудиториям его корпуса и проверяет, что 
	* в аудитории есть преподаватель / ассистент,
	* телефоны положены на стол преподавателя,
	* все студенты смогли войти в контест и начать решать задачи.
* В случае обнаружения проблем помогает их решать или экскалирует ответственному за факультет / руководству кафедры.
* *Вопросы судьям - как в lms их задавать?* Если преподаватель не может ответить на вопрос студента по задаче, то он передает вопрос тех. ответственному.
* После отработки системы антиплагиата таблица с результатами всех студентов потока доводится до сведения всех преподавателей. В таблице должна быть возможность быстрого нахождения всех студентов группы.
* Апелляция. 
  Назначается время апелляции за задачу (можно первый заход сразу после контрольной, второй - на следующей неделе)
  Если студент не согласен с баллами за задачу, он может апеллировать к тех.отвественному. По результатам может быть рекомендовано преподавателю изменить оценку за контрольную *(можно ли кому-то менять баллы за решение студента?)*
  Надо бы прописать штрафы за апелляцию не по делу, чтобы нам все студенты не пошли на апелляцию. Например, сдача зачета комиссии.
### Переписывание контрольной
* В начале семестра должно быть решено - будет ли переписывание контрольной. 
	* Это считается еще +1 контрольной и "оплачивается" задачами из рассчета 15 человек (условная студенческая группа).
	* На переписывание выделяются отдельные варианты задач для тех задач, где варианты разделяются между потоками.
* Назначается преподаватель, который проводит переписывание.
* Пропустившие контрольную по уважительной причине, могут написать контрольную.
* Переписывание "неуда" за контрольную запрещено. Для этого есть "задачи на зачет".
## Утечка задач
Если преподаватель берет задачу из контрольной и использует её вне времени контрольной, то задача считается утекшей по вине преподавателя и он обязан возместить или 5 вариантов задачи (можно по договоренности с автором задачи на варианты другой задачи) или оплачивается создание 5 вариантов задачи этого уровня (откуда перераспределить деньги решает руководство кафедры, как заинтересованная сторона).
## Создание задачи
* Авторы в начале семестра согласовывает темы новых задач и количество вариантов исходя из количества потоков и студентов в них.
* Руководство кафедры вправе переложить создание необходимого количества вариантов задач на методистов и оплатить их работу.
* При создании абсолютно новой по типу задачи автору рекомендовано добавить 1 задачу этого типа в домашние задачи, если таковых задач там еще нет.
* Для новых задач для контрольной заводится отдельная категория "Новые задачи на проверку" (чтобы нечаянно не послать недоделанную задачу в контрольную)
* Автор в задаче обязательно указывает, что он автор (или, если он берет где-то задачу, то указывает откуда берет и эта задача не может идти в контрольную).
* Далее вся группа по подготовке контрольной исследует эту задачу, включая беседу с автором, прорешивание, проверку в том числе на засвеченность где-то еще, определение проверябильности автоматом, изменение тестов или вообще отколонение по разным причинам. Может быть классная задача, не не на контрольную. 
* Если задача прошла проверку, помещается в раздел "Задачи для контрольной" и попадает в к
# Категории задач
Задачи делятся на 3 категории. Одна задача может быть только в одной категории.
* **Задачи для контрольных** - ограниченный доступ только авторов и прорешивателей, доступ остальных только во время контрольных.
* **Задачи домашние** - доступна всем студентам все время вне зависимости от курса, группы, года и тп. Потому что преподаватель второго курса может решить, что у студента недостаточно знаний из первого курса по, например, структурам, и назначить ему дополнительные домашние задачи.
  Как костыль можно использовать онлайн курсы степика, где каждый может зарегистрироваться на курсе, там есть теория, преподаватель может создать класс по курсу, записать туда студента и отслеживать его успеваемость.
* **Задачи на зачет** - сюда переносятся слишком сложные, простые, излишне литературные, слитые и тп задачи из контрольных, которые не будут никогда в контрольных.
  доступны:
	* студентам - только в определенное время, которое назначил преподаватель, например, во время текущей пары, дальше задача закрывается.
	* преподавателям - условия задач, возможность назначать одну задачу одному студенту на определенное время.
	* доступность возможна вне курсов, ибо одна задача на сортировку подойдет и для Си, и для С++, и для python.
* **Новые задачи на проверку** - сюда попадают задачи потенциально на контрольную. Новые задачи для домашней работы и зачета могут идти сразу в категорию домашних или зачетных задач.
