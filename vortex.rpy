label vortex:
    nvl clear
    hide screen nvl
    scene bg vortex_sub_image
    $ renpy.pause(None)
    if vortex_firsttime == 0:
        "Вы ожидали чего-то более... внушительного от места, называемого Омутом. Грандиозный водоворот, изменяющая свой цвет вода, кровопролитные схватки с лезущими из глубин чертями — хоть что-нибудь из того, о чем без устали трепались подвыпившие мореходы. Но всё, что вы видите сами — буйки с флажками угрожающего фиолетового цвета, обозначающие границы омута, диковинное судно без палуб и парусов, качающееся на волнах, и скала странной округлой формы, поросшая чем-то неопрятным."
        "Вы готовитесь разочарованно вздохнуть (а кое-кто из вашей команды уже начал), когда скала открывает глаза и изучающе смотрит на ваш корабль. Вы судорожно сглатываете, пытаясь сообразить, что следует делать отважному капитану в такой ситуации, а скала уже закрывает глаза. Кажется, она разочарована не меньше вашего."
        "Тем временем в верхней части диковинного корабля распахивается люк. Из него высовывается голова, равномерно покрытая длинными спутанными волосами, и широко улыбается. Дико выглядящий моряк машет вам рукой и показывает, куда именно подплывать. Не ответить на приглашение было бы невежливо."
        menu:
            "Подойти к судну":
                nvl clear
                "Вы ведете корабль к цели, уворачиваясь от буйков. Поравнявшись с Бочкой — именно так вы её окрестили про себя — вы перекидываете трап, и по нему на борт тут же поднимается Обросший. Вы хихикаете: сегодня определенно хороший день для прозвищ. Первым делом Обросший осведомляется:"
                " — Это ничего, что я к вам? В cубмарине очень мало места. Сидели бы, как сельди в бочке."
                "Пока вы справляетесь с приступом идиотского хихиканья, старпом, бросив на вас внимательный взгляд, приглашает моряка устраиваться, как ему будет удобно. Обросший энергично кивает. Кажется, его бочка ему порядком надоела."
                " — Но где мои манеры! — Обросший хлопает себя по лбу, но натыкается на ниспадающие на лицо космы. Озадаченно нахмурившись, он прерывается, извлекает из кармана кусок бечевы и ухватывает волосы в хвост. Теперь хотя бы можно понять, где у него борода, а где прическа."
                " — Приятно познакомиться, господа. Меня зовут Монро, я несу вахту около этой орясины. Очень рад вас видеть."
                "Вы расшаркиваетесь. Обросший (то есть Монро, поспешно поправляетесь вы) с удовольствием разминается и приглашает вас задавать свои вопросы."
                menu:
                    "Судорожно ткнуть пальцем в глазастую скалу":
                        nvl clear
                        "Монро разражается довольным хохотом — гораздо более довольным, чем можно было ожидать. Вы оглядываетесь по сторонам и видите, что по меньшей мере половина команды повторила ваше движение. Это действительно выглядит комично. Отдышавшись, Монро извиняется ('никогда не могу удержаться, простите') и начинает рассказывать."
                        "Оказывается, скала с глазами — и не скала вовсе, а исполинский осьминог по имени Ворчальник, десятикратно превышающий в размерах любого обитающего в омуте. Его используют для транспортировки людей и груза вниз и вверх, а как именно — Монро рассказывать отказывается: не хочет портить впечатление. Судя по хитрому выражению на его свободной от растительности части лица, это воистину интересный опыт."
                        menu: 
                            "Попросить доставить вас к старателям":
                                nvl clear
                                "Вы не уверены, что хотите узнавать, как именно нужно пользоваться осьминогом для транспортировки людей, но работа есть работа. Вы благодарите Монро за рассказ и выясняете, может ли он доставить вас на станцию. Монро почти извиняющимся тоном отвечает:"
                                " — Только если у вас есть груз из Адмиралтейства или заказанные станцией товары. Иначе никак: гонять Ворчальника впустую строго запрещено."
                                "Впрочем, вы отчетливо замечаете хитринку в глазах моряка. Возможно, моряки в этой части моря не очень стремятся выполнять все приказы начальства."
                                $ vortex_firsttime = 2
                                jump vortex_dive
                            "Попрощаться с Монро и поплыть своей дорогой":
                                nvl clear
                                "Ну уж нет. Каким бы образом они не использовали осьминога, это явно что-то небезопасное. Они что, решили, что могут как-то управлять самым большим существом, кажется, всего моря? В этом попросту нет смысла. Может быть, когда вы приплывете в следующий раз, на вахте будет стоять кто-то более в своём уме. Разворачиваемся!"
                                $ vortex_firsttime = 1
                                show screen map_screen
                    "Держа себя в руках, осведомиться о глазастой скале":
                        nvl clear
                        "Вы усилием воли заставляете себя не кричать и размахивать руками, намекая таким образом моряку, что прямо за ним находится СКАЛА С ГЛАЗАМИ. Вместо этого вы вежливо спрашиваете, следует ли от каждого местного утеса ожидать таких грустных взглядов. Монро довольно хохочет, а отдышавшись, поясняет:"
                        " — Нет, капитан, не от каждого. Наш — единственный в своём роде. Его, кстати, зовут Ворчальником. Он наша гордость: самый большой осьминог Омута. Ворчальник по доброте своей помогает нам с транспортировкой людей и груза. Думаю, вы еще успеете с ним познакомиться."
                        "Вы не уверены, что хотите знакомиться с осьминогом по имени Ворчальник, но виду не подаёте."
                        menu: 
                            "Попросить доставить вас к старателям":
                                nvl clear
                                "Работа есть работа, пусть она и связана с огромными осьминогами. Вы благодарите Монро за рассказ и выясняете, может ли он доставить вас на станцию. Монро почти извиняющимся тоном отвечает:"
                                " — Только если у вас есть груз из Адмиралтейства или заказанные станцией товары. Иначе никак: гонять Ворчальника впустую строго запрещено."
                                "Впрочем, вы отчетливо замечаете хитринку в глазах моряка. Возможно, моряки в этой части моря не очень стремятся выполнять все приказы начальства."
                                $ vortex_firsttime = 2
                                jump vortex_dive
                            "Попрощаться с Монро и поплыть своей дорогой":
                                nvl clear
                                "Ну уж нет. Они дали гигантскому осьминогу имя, используют слово \"помогает\" по отношению к нему и думают, что он у них под контролем. В этом просто нет смысла. Гигантские осьминоги НЕБЕЗОПАСНЫ, черт побери. Может быть, когда вы приплывете в следующий раз, на вахте будет стоять кто-то более в своём уме. Разворачиваемся!"
                                $ vortex_firsttime = 1
                                show screen map_screen
                    "Сделать вид, что глазастая скала вас не интересует и попросить доставить вас к старателям":
                        nvl clear
                        "Юнга раскрывает рот, чтобы задать волнующий всех вопрос, но на него шикают: мол, капитан не спросил, и тебе не след. Неожиданное, но приятное проявление субординации. Вы, откашлявшись, официальным тоном выясняете, может ли уважаемый Монро доставить вас на станцию старателей. Монро, кажется, удивлен отсутствием привычной реакции, но виду не подаёт и отвечает:"
                        " — Если у вас есть груз из Адмиралтейства или заказанные станцией товары. Иначе никак: гонять Ворчальника впустую строго запрещено."
                        "Впрочем, вы отчетливо замечаете хитринку в глазах Монро. Возможно, моряки в этой части моря не очень стремятся выполнять все приказы начальства."
                        $ vortex_firsttime = 2
                        jump vortex_dive
                        
    if vortex_firsttime == 1:
        "И всё-таки вам пришлось вернуться в Омут еще раз. Команда, заинтригованная тайной осьминожьего транспорта, молчаливо надеется, что в этот раз вы всё-таки доведете дело до конца."
        "Вы подплываете поближе и видите, что Монро на этот раз сидит на башенке и курит, задумчиво разглядывая Ворчальника. Ворчальник равнодушно моргает, переводя взгляд с него на вас, и Монро оборачивается и машет вам рукой."
        " — Доброго дня! Плывите сюда, раскурим по трубочке."
        "Вы приближаетесь, опускаете трап и здороваетесь. Так как трубкой вы до сих пор не обзавелись, необходимо что-нибудь сказать."
        menu:
            "Попросить доставить вас к старателям":
                nvl clear
                "Вы сильны. Вы храбры. Отец хотел бы гордиться вами (и до сих пор хочет). Вы должны победить страх. Пройдя дорогой смертной тени, не убоитесь зла. Вы собираетесь с силами и деревянным голосом сообщаете, что вам необходимо попасть на станцию. Монро почти извиняющимся тоном отвечает:"
                " — Только если у вас есть груз из Адмиралтейства или заказанные станцией товары. Иначе никак: гонять Ворчальника впустую строго запрещено."
                "Впрочем, вы отчетливо замечаете хитринку в глазах моряка. Возможно, моряки в этой части моря не очень стремятся выполнять все приказы начальства."
                $ vortex_firsttime = 2
                jump vortex_dive
            "Вспомнить о некоторых неотложных делах и попрощаться":
                "Посмотрев на огромного осьминога, вы отчетливо вспоминаете, что давно хотели посетить бухту под Горой или уйти служить посудомойщиком в Крепость. Вы многословно объясняетесь, жмете моряку руку на прощание и возвращаетесь на борт. Лица вашей команды выражают самые разнообразные эмоции по поводу вашего малодушия, но вслух ничего не говорят."
                show screen map_screen
    else:
        nvl clear
        "Здесь ничего не меняется: колыхаются фиолетовые флажки, Ворчальник покоится там же, где и всегда, а субмарина медленно дрейфует от буйка к буйку. Вы подплываете ближе и привычно лавируете между флажками. Осьминог открывает глаза и смотрит на вас с равнодушной тоской. Иногда в такие моменты задумываетесь, понимает ли он, что происходит, или просто хочет, чтобы его оставили в покое."
        "Корабль сближается с субмариной и юнга тут же перепрыгивает на башенку. Взгромоздившись сверху, он начинает молотить кулаками по люку и кричать:"
        " — Вылезай, большая лохматая голова, к тебе гости!"
        " Наконец, люк со скрипом открывается, сбрасывая с себя худосочного юнгу, и тот с визгом летит в воду. Большая лохматая голова зевает, протирает глаза и приветствует вас."
        " — А, юный капитан! С чем пожаловали?"
        menu:
            "Попроситься вниз, на станцию":
                nvl clear
                "Вы кратко сообщаете цель своего визита, и Монро согласно кивает."
                " — Адмиралтейство шлёт презенты? Или вы привезли нам что-то поинтереснее? Правила вы помните, я надеюсь. Просто так мы осьминога не пошлем."
                "Произнося последние слова, моряк откровенно улыбается. Возможно, он уже считает вас своим."
                jump vortex_dive
            "Поболтать с Монро":
                "здесь будет какой-то рандомный контент"
            "Развернуться и уплыть":
                " — Прости, друг, не хотели тебя тревожить. Юнга собрался покончить с собой и попытался утопиться, нечаянно задев в прыжке субмарину. Сейчас мы его выудим и отправимся себе дальше, — поясняет ситуацию в кои-то веки выбравшийся на палубу кок, помогая промокшему насквозь юнге подняться на борт. Монро озадаченно трясет бородой, но соглашается и, пожелав вам удачи, спускается обратно в субмарину."
                show screen map_screen
label vortex_dive:
    menu:
        "Показать значение переменной vortex_firsttime":
            "переменная равна %(vortex_firsttime)d"
            jump vortex_dive
        "Сказать, что груз у вас есть":
            if "monetload" in gl_cargo:
                nvl clear
                " — Есть? Вот и славно, мы как раз ждем поставки! — радуется Монро и добавляет:"
                " — Но придется его досмотреть. Не обессудьте, правила есть правила."
                "Вы отправляетесь в трюм; Монро следует за вами. Спустившись в коридор перед трюмом, вы распахиваете перед Монро дверь, давая ему возможность самому всё осмотреть. Монро заглядывает внутрь, проверяет маркировки и объявляет, что, если его старые глаза не врут, поводов не пускать вас на станцию он не видит совершенно, и вы с парой матросов отправляетесь вместе с ним обратно к судну. Кое-как загрузившись на борт крохотной субмарины, вы пытаетесь устроиться поудобнее (безрезультатно) и заодно подсмотреть управление: мало ли, когда пригодится. Монро дожидается, пока все найдут себе место, и затем командует погружение."
                menu:
                    "Погружаемся!":
                        jump vortex_deep_dive
                
            else:
                nvl clear
                " — Есть? Вот и славно, мы как раз ждем поставки! — радуется Монро и добавляет:"
                " — Но придется его досмотреть. Не обессудьте, правила есть правила."
                "Вы отправляетесь в трюм; Монро следует за вами. Спустившись в коридор перед трюмом, вы распахиваете перед Монро дверь, давая ему возможность самому всё осмотреть."
                " — Капитан, не хочется вас огорчать, но здесь нет ничего из наших грузов. Вы уверены, что вас не ограбили по пути?"
                menu:
                    "Извиниться, сославшись на дырявую память":
                        nvl clear
                        "Вы извиняетесь, сетуя на свою забывчивость. Монро добродушно хлопает вас по плечу и советует есть побольше морепродуктов: они полезны для мозга. Довольно ироничный совет, но в лице моряка нет ни намёка на шутку."
                        " — Ну, если это всё, то я откланяюсь. Вахта есть вахта, верно?"
                        " Вы дружески прощаетесь и некоторое время наблюдаете, как моряк переходит на своё странное судно и захлопывает за собой люк. Затем поворачиваете корабль и уплываете сами."
                        show screen map_screen
                    "Дать ему гаечным ключом по голове (конфликт)":
                        label vortex_cargo_fight:
                        nvl clear
                        " — Вы уверены, что... ЫК! — говорит Монро, получив по затылку гаечным ключом, но, к сожалению, не падает оземь, а разворачивается и смотрит на вас уже не так дружелюбно, как раньше. Кажется, придётся драться."
                        $ init_conflict_table(u'3С3С4С5С')
                        if ret[0] == u'F':
                            "Это определенно больно."
                        elif ret == u'SСила':
                            "Даже ошарашенный и слегка потерявший ориентацию моряк — всё еще серьёзный противник. После непродолжительной, но яростной схватки Монро наконец мягко сползает по стенке. Самое время подумать, для чего вы совершили нападение на вахтовика при исполнении."
                            " — Капитан, для чего мы совершили бесчестное нападение на вахтовика при исполнении? — интересуется старпом. Вы не помните, чтобы назначали его своим внутренним голосом, но сейчас определенно есть вопросы поважнее. Например, что делать с телом или как же всё-таки попасть в Омут."
                            label vortex_gtfo:
                            menu:
                                "Уплыть отсюда, оставив Монро":
                                    "Черт. Черт. Черт. Черт. Нужно замести следы и надеяться, что Монро ничего не вспомнит. Нужно замести следы быстро и еще быстрее дать деру. Мама всегда говорила, что у вас проблемы с агрессией, и видит бог, она была права. Дождавшись, когда моряка перетащат в его бочку, вы на всех парусах уходите обратно в море."
                                    $ vortex_firsttime = -1
                                    show screen map_screen
                                "Уплыть отсюда, забрав Монро с собой":
                                    "Люди — это ресурсы. Пленные избитые люди — это без сомнений ресурсы. Жертва не сможет указать на своего обидчика, если сидит связанная в трюме. Вы не уверены, откуда в вашей голове столько кровожадной мудрости, но это лучше, чем ничего. Вы тщательно связываете моряка и на всех парусах уходите обратно в море."
                                    $ vortex_firsttime = -2
                                    $ gl_cargo.append("monroe")
                                    show screen map_screen
                                "Захватить судно Монро и попробовать попасть в Омут самостоятельно" if useless_variable == 0:
                                    $ useless_variable = 1
                                    if "howtodive" in gl_knowhow:
                                        "Перекочевав на субмарину, вы задумчиво оглядываете рычаги управления. Вы помните, как приводить этот механизм в действие — такое не забывается — но не уверены, что хотите повторять. Возможно, потому что план включает в себя в числе прочего стрельбу по огромному осьминогу."
                                        label vortex_deep_dive_lawless:
                                        " — Вы ведь знаете, как управляться с этим жестяным гробом? Скажите, что знаете. Пожалуйста, капитан! — нервничает юнга. Вы бы и сами хотели услышать точный ответ на этот вопрос."
                                        "Оставив юнгу следить за рычагами и найдя ему таким образом занятие, вы взбираетесь по лесенке наверх, находите взглядом баллисту и"  
                                    else:
                                        nvl clear
                                        "Перекочевав на cубмарину (кажется, так её называл моряк), вы кое-как устраиваетесь и начинаете рассматривать рычаги управления. К сожалению, вы ни разу не видели, как вообще работает этот механизм. Это определенно просчет с вашей стороны."
                                        label vortex_massacre:
                                        menu: 
                                            "Бросить бессмысленные попытки и всё-таки дать деру отсюда":
                                                jump vortex_gtfo
                                            "Постараться вспомнить, что вы знаете об Омуте и том, как он работает":
                                                $ init_conflict_table(u'4З')
                                                "Прямо сейчас вы молитесь, что читали и слушали достаточно."
                                                if ret[0] == u'F':
                                                    "Бесполезно. Сколько бы вы не копались в своей бедной дырявой голове, знаний об Омуте там не найти. Пора сматываться, вот как вам кажется."
                                                    jump vortex_gtfo
                                                elif ret == u'SЗнания':
                                                    "Да, вы действительно слышали кое-что о способе погружения в Омут, и вам не нравится эта идея. Более того, вы находите эту идею запредельно идиотской. Довольно сложно было бы выдумать идею хуже. Тем не менее, у вас на руках бессознательное тело, и поворачивать назад уже нет смысла. Вы вздыхаете и беретёсь за рычаги."
                                                    $ gl_cargo.append("monroe")
                                                    jump vortex_deep_dive_lawless
                                            "Привести Монро в чувство и пытать его, пока он не расскажет всё сам" if useless_variable_2 == 0:
                                                "Это ужасная идея. Вы — ужасный человек. Теперь в этой игре есть Счетчик Ужасного Человека, и его стрелка только что передвинулась на единицу вперед. Поверьте мне, вы не хотите, чтобы она двигалась вперед."
                                                $ gl_you_are_terrible += 1
                                                $ useless_variable_2 = 1
                                                "А теперь подумайте, блядь, снова."
                                                jump vortex_massacre
        "Мановением руки сотворить в трюме груз: вы ведь могучий волшебник и фокусник":
            "Вы нагло пользуетесь тем, что линия с получением груза еще не прописана, и создаёте весь необходимый груз из ничего. В конце концов, не ваша вина, что автор — ленивая жопа. Вы даже в чем-то ему сочувствуете."
            $ gl_cargo.append("monetload")
            jump vortex_dive
        "Решить проблему другим способом (конфликт)":
            $ init_conflict_table(u'4С4С5С6С3Д3Д4Д')
            "Есть множество способов убеждения несговорчивых."
            #$ _return = renpy.show_screen('conf')
            if ret[0] == u'F':
                "Я пока не очень понимаю, как работает система возврата проигравшей масти, поэтому попытались вы подкупить бравого моряка или дать ему в морду — останется неузнанным. В любом случае, у вас не получилось."
            elif ret == u'SДеньги':
                "Монро с довольным видом прячет в карман звонко бренчащий мешочек и неизвестно зачем дважды бьёт себя пальцем по кончику носа. Изучать местные обычаи у вас сейчас нет желания, и вы с парой матросов отправляетесь следом за ним. Кое-как загрузившись на борт крохотной субмарины, вы пытаетесь устроиться поудобнее (безрезультатно) и заодно подсмотреть управление: мало ли, когда пригодится. Монро дожидается, пока все найдут себе место, и затем командует погружение."
                menu:
                    "Погружаемся!":
                        jump vortex_deep_dive
            elif ret == u'SСила':
                "Даже не ожидающий нападения моряк — всё еще серьёзный противник. После непродолжительной, но яростной схватки Монро наконец мягко сползает по стенке. Самое время подумать, для чего вы совершили нападение на вахтовика при исполнении."
                " — Капитан, для чего мы совершили бесчестное нападение на вахтовика при исполнении? — интересуется старпом. Вы не помните, чтобы назначали его своим внутренним голосом, но сейчас определенно есть вопросы поважнее. Например, что делать с телом или как же всё-таки попасть в Омут."
                jump vortex_gtfo
label vortex_deep_dive:
    if "howtodive" in gl_knowhow:
        ""
    else:
        nvl clear
        "Вы с интересом, смешанным с небольшой долей страха, наблюдаете за действиями Монро, поглядывая время от времени в иллюминатор. Доля страха понемногу увеличивается, когда вы подходите ближе к исполину Ворчальнику и, наконец, вы оказываетесь полностью в его тени. Осьминог медленно открывает глаза — вблизи это еще более страшно — и вы готовы поклясться, что слышите тяжелый вздох."
        "Монро, старательно изображая на лице вселенскую скуку, откидывает люк и поднимается наружу, садясь за небольшую баллисту. У вас возникает очень нехорошее предчувствие, которое сменяется ЧЕРТОВСКИ НЕХОРОШИМ ПРЕДЧУВСТВИЕМ, когда вы, присмотревшись, замечаете на шкуре Ворчальника небольшие, но многочисленные шрамы. Вы переглядываетесь со командой и чувствуете некоторое облегчение: они напуганы не меньше вашего."
        "Пока вы были заняты анализом эмоций ваших матросов, просвистел первый выстрел. Почти сразу сразу за ним звучит второй, и вы выясняете, что были чудовищно правы в своих предчувствиях: в осьминоге торчит два свежих гарпуна. Вы, замерев от ужаса, наблюдаете, как осьминог приходит в движение, как начинают двигаться его скрытые под водой щупальца, как у него открывается рот..."
        " — ВОТ ЗА ЭТО МЫ ПРОЗВАЛИ ЕГО ВОРЧАЛЬНИКОМ! — ликующе кричит Монро, стремительно скатываясь вниз и очень, очень, очень быстро захлопывая за собой люк. Вы едва его слышите за неистовым рёвом оскорбленного гиганта, а затем ощущаете, как вся ваша посудина поднимается в воздух. Вы решаете, что все вокруг сошли с ума, и на том успокаиваетесь — но только до тех пор, пока осьминог не ныряет."
        $ gl_knowhow.append("howtodive")
        jump vortex_cave

label vortex_cave:
    nvl clear
    hide screen nvl
    scene bg vortex_cave_image
    $ renpy.pause(None)
    "Переведя дыхание, вы вылазите из субмарины. Из-под Марины. К сожалению, помимо картинки и плохих шуток, в пещере ничего нет."
    "Может быть, стоит попытать счастья где-нибудь ещё."
    show screen map_screen
    "Whatever, man"