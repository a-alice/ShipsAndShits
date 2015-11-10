﻿# Main game script. All card-related python is in cardistry.rpy

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define narrator = Character(None, kind = nvl, what_color="#000000", size = 10)

init -2 python:
    menu = nvl_menu
    gl_no_rollback = True
    # Initialising global conflict variables so they exist when we call init_conflict()
    stack = []
    opponent_deck = []
    ret = ''
    price = '0'
    # Initialising new conflict variables
    test_table = None #  If no init_* functions were called before new screens, this will break
    # Globals for new trade system
    paid = 0
    withheld = 0
    # Initialising starting position
    current_port = monet

#  This is the beginning, from the very start to the first trip from Monet
label start:
    $ start_sweet_little_crimes = []
    $ start_firstofficer_helps = 0
    $ monet_names_on_the_wall = 0
    $ vortex_firsttime = 0
    $ gl_cargo = []
    # List of stuff you can append to gl_cargo: monetload, jerry, hurricane_blueprints
    $ gl_knowhow = []
    # List of stuff you can append to gl_knowhow: howtodive
    $ node_lost_in_sea_interview = []
    $ node_lost_in_sea_interview.append("firstofficer")
    $ node_lost_in_sea_interview.append("walkthrough")
    $ gl_cargo_jerry = 0
    $ gl_you_are_terrible = 0
    $ useless_variable = 0
    $ useless_variable_2 = 0
    $ player_deck = []
    $ player_deck.append(Card(u'З', 3, spendable = False, tooltip = u'Сказки и истории, которые вы слышали с детства'))
    $ player_deck.append(Card(u'С', 2, spendable = False, tooltip = u'Ваш фирменный обманный маневр, сопровождаемый ударом'))
    $ player_deck.append(Card(u'С', 3, spendable = True, tooltip = u'Кусок стекла, который вы зачем-то носите в кармане'))
    $ player_deck.append(Card(u'С', 10, spendable = False, tooltip = u'Спецоружие для Птицы, которая очень хочет избить невинного вахтовика'))
    #$ init_new_table() #  Initialising stack objects and other such crap
    image bg solid_bg = Solid('#EEE')
    show bg solid_bg
    menu:
        "Пропустить вступление":
            $ player_deck.append(Card(u'Д', 4, spendable = True, tooltip = u'Мелочь, оставшаяся после найма экипажа и пирушки по этому поводу'))
            $ player_deck.append(Card(u'Д', 4, spendable = True, tooltip = u'Мелочь, оставшаяся после оснастки и ремонта корабля'))
            $ player_deck.append(Card(u'И', 4, spendable = True, tooltip = u'Рекомендательное письмо, подписанное Иштваном Гандрабуром - уважаемым в городе человеком'))
            jump start_last_part
        "Начать вступление":
            label the_very_start:
            " — Я всегда говорил: твои песенки — дерьмо, Люсьен, и я не понимаю, где ты только находишь музыкантов, согласных это исполнять!"
            "Дом в одном из кругов Моне, гостиная внутри этого дома, три человека в этой гостиной. Тот, что грохочет сейчас, разнося Люсьена в пух и прах — ваш батюшка, замечательный, но иногда чрезмерно прямой человек. Люсьен, ритуально содрогающийся в соседнем кресле — ваш братишка, непутёвый в той же мере, что и вы сами: возможно, именно поэтому вы додумались испрашивать батюшкиного благословения на собственное дело вместе и в один и тот же день."
            " — Но чего я не понимаю ещё больше, так это того, как ты с этим умудряешься получать какие-то деньги вместо положенной брани и рыбьих голов в лицо! — Рокот продолжается, но уже идёт на убыль. Сейчас отец устанет негодовать и заговорит конструктивно — во всяком случае, утром Люсьен очень надеялся на такое развитие событий."
            " — Да, с людьми, да и с деньгами тоже ты управляться умеешь, этого не отнять. Скажи, о сын мой, зачем, зачем тебе при таком таланте делать что-то самому? Найми кого-нибудь и пусть работают за тебя! Хочешь прикасаться к высокому? Открой издательство! Городу остро не хватает порядочного еженедельного чтива."
            "Вообще-то это довольная здравая мысль. Одного взгляда на Люсьена достаточно, чтобы понять, что он тоже так считает: он едва заметно шевелит пальцами, как делает всегда, когда перед его взором встаёт очередной тщательно продуманный и финансово благонадёжный воздушный замок. Отец меж тем разворачивается к вам."
            nvl clear
            " — А тебе что нужно, другой мой сын? Или ты пришел поддержать своего хитроумного братца?"
            "Да уж, кажется, пора говорить."
            menu:
                    "Вкратце описать, как тесно вам стало в родном море":
                        "Вы, тщательно отмеряя слова, описываете, как вам обрыдло это застоявшееся болото, которое остальные называют морем. Здесь ведь просто нечего делать, от одного края до другого можно доплыть за два дня, и с помощью чего, скажите на милость, молодому бравому капитану вроде вас покрывать себя славой и успехом? Как по-вашему, единственное, чего вы на самом деле стоите — с батюшкиной помощью оплатить выездную пошлину и отправляться наружу, в мир, полный достойных вас приключений."
                        "Отец оглушительно хохочет."
                        " — Нечего делать, а? Что ж, такое вольнодумство необходимо пресекать в корне!"
                        "Это не звучит обнадёживающе."
                        " — Мы сделаем вот что: я дам тебе денег на покупку нового корабля. На той скорлупке, которой ты управляешь сейчас, ты немедленно и весьма бесславно потонешь, как только выйдешь из Гавани. Плюс набор команды, плюс некоторые карманные расходы, плюс подъёмные. Но на пошлину изволь заработать сам. Вот тут-то мы и выясним, готов ты отправиться в Великий Континентальный или нет."
                        jump start_fathers_gift
                    "Вкратце описать, как вам хочется изучить весь мир":
                        "Вы, тщательно отмеряя слова, описываете, как вы с детства воображали себе все эти чудеса и находки, то и дело проплываюшие мимо всякого корабля, вышедшего в Океан, как мечтали посмотреть на мореходов Вышнего моря и попробовать на вкус пену катарских гейзеров. В конце концов, это вина отца, что вы так жадно смотрите за горизонт: ведь это он рассказывал все эти удивительные байки о мире вокруг. Так что его долг, как порядочного родителя — оплатить вам выездную пошлину и благословить на новую, полную открытий жизнь."
                        "Отец оглушительно хохочет."
                        " — Ты ведь знаешь, что катарские гейзеры осушили еще в прошлом столетии? Как по мне, тебе стоит поработать над развеиванием иллюзий, о сын мой!"
                        "Это не звучит обнадеживающе."
                        " — И вот как ты их развеешь, одну за другой: я дам тебе денег — но только на новый корабль вместо той ужасной посудины, на палубе которой даже показываться стыдно. А на пошлину заработаешь сам. Заодно узнаем, насколько ты на самом деле хочешь повидать мир."
                        jump start_fathers_gift
                    "Вкратце описать, как вы жаждете настоящих рисковых дел":
                        "Вы, тщательно отмеряя слова, описываете, как вы хотите заняться настоящим делом, работать, рисковать, влезать в долги, чтобы потом триумфально расплачиваться парой-другой найденных сокровищ, сражаться на мечах, геройствовать — словом, заниматься всем тем, чем занимается всякий настоящий морской волк. Но определённо не возить батюшкину корреспонденцию от района к району. И разве за этот неблагодарный труд не полагается награды? Вы, например, готовы удовольствоваться оплатой выездной пошлины, дающей право отправиться за пределы вашего маленького моря."
                        "Отец оглушительно хохочет."
                        " — Господь милосердный, дитя захотело поработать! Неужели я дожил до этого момента?"
                        "Это не звучит обнадеживающе."
                        " — Я даже не буду указывать на главную ошибку в твоих рассуждениях. Вместо этого я, как порядочный родитель, дам тебе возможность заработать на пошлину самостоятельно. Деньги на новый корабль, на команду, на снаряжение — и вперёд, совершать свой первый трудовой подвиг. Устраивает?"
                        jump start_fathers_gift
            label start_fathers_gift:
                nvl clear
                "В глазах отца пляшут маленькие хитринки, а на всём остальном лице установилось весьма ехидное выражение."
                "А, впрочем, какого чёрта. Неужели он считает, что вы откажетесь? Не дождётся. Вы решительно соглашаетесь, вот что вы делаете. Следом за вами соглашается и Люсьен, который во время ваших с батюшкой пламенных речей был занят подсчётом вероятностей и прибылей. Возможно, он всё-таки немного умнее вас. А возможно, это вы решительнее и храбрее его. Будущее рассудит."
                "Не тратя больше времени на разговоры, вы вместе поднимаетесь в кабинет, где отец выписывает несколько чеков вам и вашему братцу."
                $ player_deck.append(Card(u'Д', 9, spendable = True, tooltip = u'Чек на сравнительно крупную сумму, выписанный отцом'))
                $ player_deck.append(Card(u'Д', 9, spendable = True, tooltip = u'Чек на сравнительно крупную сумму, выписанный отцом'))
                $ player_deck.append(Card(u'Д', 9, spendable = True, tooltip = u'Чек на сравнительно крупную сумму, выписанный отцом'))
                "{color=#0000ffff}Колода пополнена!{/color}"
                "Затем, получив-таки скупое отцовское благословление, вы расходитесь: вы — в порт, а Люсьен — в торговые кварталы."
                nvl clear
                "Вы потратили немало времени, выбирая корабль, изучая правила аукциона и согласовывая список подходящих вам кораблей со списком выставленных на продажу. Это долгое и не в меру огорчительное занятие, и наконец остаётся только одно судно, подходящее вам и по требованиям, и по бюджету: трёхмачтовый барк \"Мармозетка\"."
                "Аукцион тянется невыносимо долго, и наконец ведущий объявляет облюбованный вами корабль. Пора действовать."
                menu:
                    "Действовать":
                        $ init_conflict(u'9Д9Д')
                        show screen conf
                        "Аукцион! Таблички с номерами, взмывающие в воздух, свистки, стук молотка - аукцион!"
                        if ret[0] == 'F':
                            "Блядь, это невозможно, как ты вообще здесь оказался?"
                        elif ret == u'SДеньги':
                            "\"Мармозетка\" ваша! Вы торжественно расписываетесь во всех необходимых документах и вступаете в полноправное владение кораблем. Большая часть матросов изъявила желание остаться на судне, а вам нужна команда, так что отказывать им нет повода. А теперь — не обращать внимания на злобные взгляды вашего конкурента и вперёд! Вам еще нужно найти недостающих членов экипажа."
                            "Как только вы выходите из аукционного дома и проходите несколько шагов, на вас набрасываются со спины. Вывернувшись из первого захвата, вы разворачиваетесь и узнаете парня, с которым вы боролись за право купить \"Мармозетку\". Он не выглядит расположенным к разговору."
                            menu:
                                "Утихомирить наглеца":
                                    $ player_deck.append(Card(u'С', 4, spendable = True, tooltip = u'Помощь случайного прохожего'))
                                    $ init_conflict(u'3С3С3С')
                                    show screen conf
                                    "После драки кулаками не размахивают! Хотя вы не уверены, что эта поговорка сюда подходит."
                                    if ret[0] == 'F':
                                        "Это всё еще недостижимая ветка. Если ты здесь - свяжись с нами, сладкий."
                                    elif ret == u'SСила':
                                        nvl clear
                                        "Недоброжелатель повержен и падает в портовую пыль. Вы жмёте руку прохожему, вовремя напрыгнувшему сзади, и благодарите его. Прохожий — паренек даже моложе вас в тельняшке и неумело расклёшенных штанах — в свою очередь представляется и спрашивает, что это вы такого сделали, что на вас бросаются посреди улицы. Вы вкратце объясняете ситуацию. Паренек необычайно оживляется, только что не подпрыгивая на месте, и с огромным рвением просит вас принять его в команду — матросом, поломойщиком, кем угодно."
                                        "Кажется, за вами должок, да и лишние руки не помешают. Вы назначаете мальца юнгой и отдаёте свой первый приказ: явиться на борт ровно через неделю в полдень. Новоиспеченный юнга истово кивает, а затем вытягивается во фрунт и гаркает:"
                                        " — Капитан! Прошу выдать немного денег в счёт дальнейшего жалования с целью покупки матросской формы!"
                                        menu:
                                            "Обшарить карманы атаковавшего вас и выполнить просьбу":
                                                "Если он пришел на аукцион — значит, он так или иначе собирался потратить эти деньги. Кроме того, вы возьмёте не всё: только компенсацию за нанесенный ущерб. Быстро обыскав валяющееся в отключке тело, вы вытаскиваете бренчащий мелочью мешочек, половину его содержимого отдаёте юнге, а половину забираете себе. Интересно, можно ли считать это вашими первыми заработанными деньгами?"
                                                $ player_deck.append(Card(u'Д', 3, spendable = True, tooltip = u'Деньги прямиком из карманов вашего обидчика с аукциона'))
                                                "{color=#0000ffff}Колода пополнена!{/color}"
                                                $ start_sweet_little_crimes.append("angry_merchant")
                                                "Юнга, сияя от радости, пересчитывает монетки и, попрощавшись, уносится покупать настоящие клёши, напоследок клятвенно заверив, что прибудет точно к назначенному времени."
                                                jump start_after_shipboy
                                            "Отказать, посчитав мародёрство недостойным капитана занятием":
                                                "Нет уж, вы не будете начинать ваш путь к славе и успеху с подлого грабежа. А юнга вполне способен начать свой путь к славе и успеху в его нынешней матросской форме, о чём вы ему и сообщаете. Юнга с готовностью кивает и, попрощавшись, убегает собирать вещи, напоследок клятвенно заверив вас, что прибудет точно к указанному времени."
                                                jump start_after_shipboy
            label start_after_shipboy:
                nvl clear
                "Вся следующая неделя уходит на разнообразные корабельные заботы: вы еще дважды бегали к отцу за деньгами, оплатили переоснастку и косметический ремонт кораблика, наняли кока и рулевого, обнаружили в трюме спящего боцмана, отнесшегося к новости о смене капитана безразлично, и по отцовой наводке приняли на борт немолодого мужчину в истертой ливрее Адмиралтейства, согласившегося быть старпомом. Юнга, который действительно прибыл ровно через неделю, притащил с собой найденного в подворотне драного кошака и заявил, что его необходимо пустить на судно первым: на удачу. Юнгу неожиданно поддержал кок, рассказавший убедительную историю о том, как такая традиция распространена за океаном, и было решено так и сделать. Затем юнга еще два часа искал кошака по всем палубам и трюмам, пока вы не смирились с мыслью, что теперь в экипаж входит корабельный кот, и не приказали юнге заняться чем-нибудь более полезным."
                $ player_deck.append(Card(u'Д', 4, spendable = True, tooltip = u'Мелочь, оставшаяся после найма экипажа и пирушки по этому поводу'))
                $ player_deck.append(Card(u'Д', 4, spendable = True, tooltip = u'Мелочь, оставшаяся после оснастки и ремонта корабля'))
                "{color=#0000ffff}Колода пополнена!{/color}"
                "Наконец вы чувствуете, что лучше уже не сделать: плыть придётся на этом. Напоследок вы заходите домой — попрощаться с родителями и похвастаться кораблем. Выслушав ваши восторги, батюшка иронически интересуется, куда же вы поплывёте на вашем новом корабле."
                nvl clear
                "Что ж, это хороший вопрос."
                "Вздохнув, отец быстро набрасывает на листке бумаги рекомендательное письмо и советует пойти с этим в службы Адмиралтейства — узнать, есть ли у них работа для начинающего мореплавателя. Вы берёте письмо, благодарите отца еще раз, целуете маму, просите передать брату привет и наконец покидаете отчий дом. Видит бог, вы долго ждали этого момента. Пора отправляться в путь."
                $ player_deck.append(Card(u'И', 4, spendable = True, tooltip = u'Рекомендательное письмо, подписанное Иштваном Гандрабуром — уважаемым в городе человеком'))
                "{color=#0000ffff}Колода пополнена!{/color}"
                nvl clear
                label start_last_part:
                "Осталось только решить, куда именно."
                menu:
                    "В службы Адмиралтейства":
                        "Было бы странно дать волю гордости после того, как вы безропотно приняли от отца деньги на чёртов новый корабль. Будем же последовательны! Вы сверяете адрес и направляетесь в портовые отделы Адмиралтейства — именно там распределяется работа для мореходов, не имеющих специальной подготовки." 
                        "Невзрачное приземистое здание Адмиралтейства — настоящая белая ворона посреди кипящего жизнью порта. Некоторые портовые из числа особенно лихих постарались это исправить, и в нескольких местах здание разукрашено неприличными надписями и рисунками. Интересное отношение к месту, дающему работу большей части из них. Вы толкаете дверь и заходите внутрь."
                        "Внутри обнаруживается секретарь в ливрее, внимательно изучающий документы, лежащие перед ним на столе. За секретарем располагается дверь с табличкой \"РАБОТА\", из-за которой доносится гул голосов и неразборчивые крики. Вы подходите ближе и осведомляетесь насчет работы: вам разъясняют, что необходимо вписать своё имя в таблицу на стене, дождаться своей очереди и уже тогда пройти внутрь для обсуждения вакансии."
                        nvl clear
                        "Судя по длинному списку имен в объёмистой таблице, ждать придётся долго."
                        menu:
                            "Вписать своё имя в таблицу":
                                "Вы собираетесь быть законопослушным капитаном. Следовать правилам, не бежать впереди очереди и уважать закон — вот что вы собираетесь делать. А еще вы собираетесь вписать своё имя в свободную строчку в таблице, а затем дождаться, когда наступит ваша очередь. Согласно вычислениям секретаря, наступит она не сегодня и не завтра, но вы были к этому готовы. Попрощавшись, вы выходите из здания с намерением заняться пока чем-нибудь другим."
                                $ monet_names_on_the_wall = 1
                                # Здесь будет какая-нибудь переменная, имитирующая ход времени, когда я придумаю, какая.
                                jump monet
                            "Объяснить секретарю своё преимущественное право (конфликт)":
                                $ init_conflict(u'3С3С2И3И4Д')
                                show screen conf
                                "Ваша первая проблема в качестве вольного капитана! Волнительно, что и говорить."
                                if ret == u'FСила':
                                    "Секретарь оказывается неожиданно хорошо подготовлен — ну, или вам стоит поработать над своей формой. Как следует получив по носу, вы оказываетесь на полу, хватая ртом воздух. Секретарь, присев рядом, смотрит на вас и говорит:"
                                    " — Редко встречаешь такую страсть к тяжелой и плохо оплачиваемой работе. Никогда не думал уйти в контрабанду? Они сейчас при всей фортуне, с нынешними-то порядками."
                                    "Он легко вскакивает на ноги и добавляет:"
                                    " — Если вдруг соберешься, запомни вот что: у Сирот в фаворе этот чудной гигантский осьминог, а Контрабандисты действительно любят Янку. Про остальных не знаю, но тебе и это придется к месту."
                                    "Оставив вас размышлять над его словами, секретарь снова устраивается за столом и всем своим видом показывает, что очень занят."
                                elif ret == u'FДеньги':
                                    "В этой игре еще не было ни одной незапланированной возможности потратиться, а ты уже сидишь без гроша в кармане. Серьёзно, что с тобой не так?"
                                elif ret == u'FИнтриги':
                                    "Раз уж сюда можно добраться только дебагом, ваши старания должны быть вознаграждены. Слушайте же: у нашего программиста ужасно смешная борода!"
                                elif ret == u'SДеньги':
                                    "Секретарь, не особенно скрываясь, извлекает из протянутого вами конвертика деньги и тщательно их пересчитывает, а затем, улыбнувшись одними губами, зажмуривается. Откровенно говоря, вы всегда думали, что это только метафора, но, может быть, все взяточники буквально закрывают глаза на происходящее у них под носом? Что-то вроде цеховой традиции, быть может."
                                    "Как бы то ни было, путь к заветной двери свободен, и вы шагаете вперед, чтобы положить ладонь на ручку и мягко повернуть её вниз."
                                    jump start_your_first_contract
                                elif ret == u'SИнтриги':
                                    "Вы демонстрируете секретарю рекомендательное письмо. Он необыкновенно внимательно его читает — все имеющиеся там три строчки — и кивает."
                                    " — К сожалению, письмо придется подшить к вашему делу. Ну, знаете, чтобы у меня было, чем оправдать ваш проход вне очереди."
                                    "Что ж, небольшая цена за вашу первую самостоятельную работу. Вы, в свою очередь кивнув, проходите мимо секретаря к двери и кладете ладонь на ручку."
                                    jump start_your_first_contract
                                elif ret == u'SСила':
                                    "Секретарь, предварительно продемонстрировав неожиданные для человека его должности навыки боя, всё-таки падает на пол без сознания. Судя по всему, теперь ничего не мешает вам пройти в кабинет — кроме, может быть, угрызений совести."
                                    "Или нет."
                                    "Как бы то ни было, вам всё еще нужна работа. Вы подходите к двери, аккуратно переступив через секретаря, поворачиваете ручку и входите внутрь."
                                    $ start_sweet_little_crimes.append("beat_the_boys")
                                    jump start_your_first_contract
                            "Спросить помощи старпома":
                                "А ведь ваш старпом, наверное, не просто так носит пусть поношенную, но всё-таки ливрею Адмиралтейства. Вы, вернувшись на корабль, обсуждаете с ним странные порядки его бывшей службы и, посмотрев на вас с отчетливым сарказмом, старпом соглашается помочь."
                                "Секретарь рад увидеть старпома значительно больше, чем вы могли предполагать. Немедленно начинаются расспросы и довольный хохот, на которые старпом отвечает с большой неохотой. Наконец, ему удается свернуть на нужную вам тему, и вопрос решается за пару секунд: секретарь, на мгновение взглянув в вашу сторону, нетерпеливо машет рукой, что вы истолковываете как приглашение войти, и разворачивается обратно к старпому."
                                "Что ж, пренебрегать приглашениями невежливо. Вы подходите к двери, поворачиваете ручку и входите внутрь, к своему первому настоящему работодателю."
                                $ start_firstofficer_helps = 1
                                jump start_your_first_contract
                        label start_your_first_contract:
                            nvl clear
                            " — ...СОПРОВОДИТЕЛЬНОЕ В КРЕПОСТЬ, СКОЛЬКО УЖЕ МОЖНО, В САМОМ ДЕЛЕ!"
                            " — ПРИБЫЛИ ГРУЗОВЫЕ С КОНТИНЕНТА, ОФОРМИТЕ!"
                            " — ГОНИ ИХ В ШЕЮ, КОНТИНЕНТОМ ЗАНИМАЕМСЯ НЕ МЫ..."
                            "Зайдя в кабинет, вы на секунду глохнете. У этих стен должна быть невероятная звуконепроницаемость, раз снаружи вы слышали только неразборчивый гул. Немаленькое помещение полнится криками, бюрократической тарабарщиной и носящимися туда-сюда курьерами; впрочем, некоторые особенно умелые чиновники не пользуются даже ими, запуская крепко увязанные папки с документами в полёт. Увернувшись от одной такой, вы, лавируя в потоке документации и взмыленных курьеров, прибиваетесь к одному из столов и очень громко интересуетесь, где здесь можно получить работу."
                            "Подняв голову от заполнения длинного документа, безымянный служащий несколько секунд бессмысленно смотрит на вас, но затем трясет головой и отвечает:"
                            " — Работу? Да везде. У меня, например, её целая гора."
                            "Пока вы соображаете что ответить, служащий, выхватив из опасно качающейся стопки листок с заранее проставленной печатью, записывает несколько слов, вручает вам и указывает пальцем на один из столов в глубине помещения. Вы, кивнув, отправляетесь в указанном направлении и невольно вздрагиваете, когда за вашей спиной звучит очередной крик."
                            nvl clear
                            " — ДОН, МИЛЕНЬКИЙ, ПОДПИШИ МАЛЬЦУ ОМУТ!"
                            "Кажется, это про вас. И как прикажете к этому относиться?"
                            "Судя по всему, предыдущий крик дал некоему Дону пару секунд форы, и когда вы добираетесь наконец до нужного стола, он уже успел очнуться от бюрократического ража и приветливо вам улыбнуться. Нужные подписи оказываются на листке в мгновение ока, скоровогоркой вам объясняют дорогу до грузовых доков и тут же теряют к вам интерес, схватив пробегающего мимо паренька в ливрее и начав желчно допытываться, кто дал ему заверенные бланки особой важности."
                            "Вы разворачиваетесь и прокладываете дорогу обратно. Еще несколько минут ураганного заплыва в бушующем море документооборота — и вы на свободе. Пора в доки."
                            nvl clear
                            if start_firstofficer_helps == 1:
                                "Через пару десятков шагов вас нагоняет старпом. Некоторое время вы идёте бок о бок, а затем он, не глядя на вас, проговаривает:"
                                " — Я, конечно, был рад помочь, но уходил из Адмиралтейства под ваше начало не для того, чтобы вновь с ним связываться. Я носил ливрею четырнадцать лет, в конце концов."
                                "Старпом улыбается краем рта."
                                " — Вы не представляете, как эти весельчаки способны надоесть."
                                "Вы продолжаете путь в молчании."
                                jump start_docks
                            elif start_firstofficer_helps == 0:
                                jump start_docks
                        label start_docks:
                            nvl clear
                            "Государственные доки если и отличаются от остального порта, то ненамного: меньше матерящихся корсаров и алчных взглядов, больше суеты и вечной спешки."
                            " — Знаете, шеф, будь я на месте нашего великого правительства — тут же увеличил бы доки раза в четыре, зуб моряка. Стыд и срам, главный торговый порт и вечно не пройти-не проплыть, — делится мыслями рулевой, оглядываясь вокруг со смесью насмешки и приязни."
                            " — Давно же я тут не был, вот что скажу! Предыдущий наш корабль был вычеркнут из всех списков сразу после того, как мы контрабандой переправили четыре дюжины бассетов мимо псарен какой-то шишки. Шеф, вы не представляете, каково это — плыть на одном корабле с почти полусотней кровожадных тварей в трюмах, все матросы ходили искусанные... — байка даже не тянет на правдоподобную, но на то, чтобы убить время до прихода докера, сгодится."
                            $ player_deck.append(Card(u'З', 2, spendable = True, tooltip = u'Не очень хорошо выдуманная контрабандистская байка'))
                            "{color=#0000ffff}Колода пополнена!{/color}"
                            nvl clear
                            "Наконец очередь доходит до вас. Вы предъявляете заполненную и подписанную бумагу, и молчаливый докер с вашей помощью заносит на борт ящики с продовольствием и пресной водой для старателей из Омута."
                            $ gl_cargo.append("monetload")
                            "Еще час, заполненный деловитым сопением боцмана, с почти неприличной любовью то так, то этак расставляющего ящики по трюму, и веселой руганью рулевого, уверенно выводящего \"Мармозетку\" из забитого кораблями порта — и вы, наконец, выплываете в пролив, соединяющий полноводную Столицу с морем. Вот оно. Начинается."
                            menu:
                                "Вперёд!":
                                   show screen map_screen
                    "В вольное море":
                        "Ну уж нет. С этого момента вы — сами по себе, и это ваша собственная история успеха начинается здесь. Никаких больше поблажек и подачек! Пора уже узнать, чего вы стоите сами по себе, без помощи вашего дражайшего батюшки и прочих сочувствующих. Вперед, покорять родные гавани!"
                        show screen map_screen
        "Зайти в меню разнообразного дебага":
            menu:
                "Вступить в беспричинный конфликт":
                    #nvl clear
                    jump gamble
                "Перечитать предыдущие уже не три строчки":
                    nvl clear
                    jump start
                "Куда-нибудь поплыть":
                    nvl clear
                    jump map_label
                "Включить торговый экран":
                    nvl clear
                    jump trade_test
                "Включить новый экран торговли":
                    nvl clear
                    jump new_conflict
        
label new_conflict:

    $ test_card = Card(u'Д', 10, spendable=True, tooltip='Эта карта была куплена при тестировании магазина')
    $ test_card2 = Card(u'Д', 10, spendable=True, cost = 8, tooltip='Эта карта тоже была куплена при тестировании магазина')
    $ player_deck.append(Card(u'Д', 7, spendable = True))
    $ player_deck.append(Card(u'Д', 8, spendable = True))
    $ player_deck.append(Card(u'Д', 8, spendable = True))
    $ player_deck.append(Card(u'Д', 8, spendable = True))
    $ init_trade_table([test_card, test_card2])
    "Включаем"
    #$ init_new_conflict()
    show screen test_screen
    jump start

label trade_test:
    $ test_card = Card(u'Д', 10, spendable=True, tooltip='Эта карта была куплена при тестировании магазина')
    $ init_trade(10, test_card)
    "Здесь вы можете купить десятку денег за десятку денег. Я подозреваю, что в реальности бизнес работает как-то иначе, но для дебага сойдёт"
    show screen trade
    "Включаем магазин"
    if ret == 'Sold':
        "Сделка завершена. Убедитесь в этом на экране колоды."
        jump start
    if ret == 'NotSold':
        "Сделка отменена."
        jump start

label gamble:
    $ init_conflict(u'0З1С')
    show screen conf
    "Вы вступили в конфликт. Ни его цель, ни награда за победу вам не ясны."
    #$ _return = renpy.show_screen('conf')
    if ret[0] == 'F':
        jump failure
    elif ret == u'SЗнания':
        jump success_knowledge
    elif ret == u'SСила':
        jump success_force

label success_knowledge:
    "Вы победили, применив свой безмерный интеллект"
    jump success

label success_force:
    "Вы победили, применив свою безмерную силу"
    jump success

label failure:
    nvl clear
    $ player_deck.append(Card(u'З', 11, spendable = True, tooltip = u'Эта карта была выдана после поражения'))
    "Раз уж вы потерпели поражение, ваша колода была усилена"
    "Теперь поражение невозможно в принципе"
    jump gamble

label success:
    "Вы победили в нашей игре"
    return

label map_label:
    show screen map_screen
    "Showing map"

#  The rest is in port files, even Monet's events