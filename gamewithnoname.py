attack = 50
power = 0
state = "无"
frank = 7
ling = 4
yourname = "none"
cp = "无"
frankstory = "你的队长，同时也是童年玩伴，实力中上，个性开朗健谈。"
lingstory = "人类方最强战斗力，第七基地大队长，身高160一直都是他不愿意提及的特点。"
darren = 5
darrenstory = "Frank小队队员，自缢副队长，厨艺很好，有的时候很溅。"
moses = 6
mosesstory = "军医，小队中年龄最大的队员，为人和善，经常被Darren欺负。"
def characteristic():
    global attack
    global cp
    global power
    global yourname
    global state
    print(yourname)
    print("战斗力=",attack)
    print("力量激活=",power)
    print("状态=",state)
    print("对象=",cp)
    
def social():
    global frank
    global frankstory
    global ling
    global lingstory
    global darren
    global darrenstory
    global cp
    global mosesstory
    global moses
    print("Frank好感度：",frank)
    print("ta的故事")
    print(frankstory)
    print("Ling好感度：",ling)
    print("ta的故事")
    print(lingstory)
    print("Darren好感度：",darren)
    print("ta的故事")
    print(darrenstory)
    print("对象=",cp)

def starter():
    print("欢迎来到无名游戏！")
    print("这是由高景睿自制的小游戏哦！")
    print("此游戏和现实世界没有任何瓜葛。")
    print("请不要过度解读这个游戏！")
    print("事先说明，这个游戏可能会涉及一些很恶心的东西！")
    print("至于是什么，就等着你去探索吧！")
    print("所以你要不要现在开始！")
    print("1.要")
    option = input("")
    if option == "1" :
        operational()
    else:
        starter()
        
def operational():
    print("游戏的规则非常的简单")
    print("你可以在剧情中作出选择，这将会改变剧情哦！")
    print("点击f可以查看角色属性！")
    print("点击g可以查看人物关系!")
    print("当好感度上升到10时，你可以向角色表白")
    print("当然，如果好感度下降到0时，他就会变成hater，然后处处针对你哦！")
    print("你听得懂吗！")
    print("管你听没听懂，玩就完了！")
    print()
    print()
    name()
    
def name():
    global yourname
    print("你的名字是？")
    yourname = input("")
    print("你确定使用",yourname,"这个名字了吗？中途不能更改哦！")
    print("1.确定")
    option = input("")
    if option == "1":
        wakeup()
    else:
        name()

def wakeup():
        global yourname
        print("刺眼的光芒，划过了你眼中的那一片黑暗。你睁开眼睛，发现自己躺在一个病房中，眼前的一切无一例外的染上了白色，除了你面前的两个人。")
        print("“你醒了！",yourname,"”，其中一个男子率先开口，他有着一头银色的头发，穿着军装，俊俏的脸上满是对你的关心，而另外一个男子和前方这位银发男子对比是肉眼可见的矮，他的发型看起来是只有女性会留的发型，然而，其却拥有说不出的威严，他就坐在那里，默不作声。")
        print("你突然发现，你对这两个人完全没有印象，你也完全不知道，你是谁，你在哪里，你将要往哪里去")
        wakeupoption()
def wakeupoption():
        print("你决定……")
        print("1.再次闭上眼睛。")
        print("2.询问他们的身份。")
        print("3.询问他们自己的身份。")
        print("4.询问他们现在在做的事情。")
        option = input("")
        if option == "f":
            characteristic()
            wakeupoption()
        elif option == "g":
            social()
            wakeupoption()
        elif option == "1":
            print("你闭上眼睛后，就再也没有醒来。")
            print("THE END")
        elif option == "2":
            whoareyou()
        elif option == "3":
            whoareme()
        elif option == "4":
            whatarewedoing()
def whoareyou():
    global frank
    frank = frank - 1
    print("“你们是谁？”你疑惑的问道。")
    print("“你忘记我们了吗！我是Frank, ",yourname,"”那个银发少年着急的说，”我是你的童年玩伴啊，连我都忘记了吗？”")
    print("“看来伤得有点重啊！”那个矮小的男子说到，可爱的棕色呆毛甩了甩，”那就再次表明身份吧！我是Ling，七号基地的大队长，也是这次出墙行动的指挥官。”")
    print("虽然是一个非常严肃的男孩子，但是好可爱！我看了看四周，那个叫Frank的家伙随后和我说明了情况。")
    print("“这里是2号基地的废墟，我们招到了怪物的袭击，来到了这里避难。在收集完资源后，我们将会回到七号基地。”")
    print("你顺着他的眼神，看到了窗外，一片黑暗，破旧的城市有着人活过的痕迹，其中还有几具尸体。你转身看向Frank，才发现眼泪在他的眼眶中打转，突然像是忍不住一般，冲了过来，狠狠的拥抱了你。")
    print("“感谢上帝，你还活着！你还活着真是太好了！对不起，丢人了。”最后一句话像是对Ling说的，他一言不发，只是看着你们两个。许久，他才突出一句，“真好啊！”")
    print("“这次行动损失了129个队友，还好，你没有死！你没有丢下我！”他的眼泪好像是感激，一把鼻涕一把眼泪感谢他的上帝。")
    print("“他的康复训练就交给你了，但是，",yourname,"你先和我出来，我有事情要和你说。”Ling 冷静的说，一个人静静的离开了病房，没有关门，只留下了和你相拥的Frank。")
    whoareyouoption()
    
def whoareyouoption():
    print("你的决定。")
    print("1.听从Ling")
    print("2.继续和Frank对话")
    option = input("")
    if option == "f":
        characteristic()
        whoareyouoption()
    elif option == "g":
        social()
        whoareyouoption()
    elif option == "1":
        superpowertold()
    elif option == "2":
        talkwithfrank("nothing")

def whoareme():
    global ling
    global yourname
    ling = ling - 1
    print("“我是谁？”你疑惑的问道。")
    print("“你是",yourname,",第34队的队员！”那个银发少年着急的说，”你还记得我吗？我是你的童年玩伴Frank啊，连我都忘记了吗？”")
    print("“看来伤得有点重啊！连自己是谁都忘记了，情况不容乐观。”那个矮小的男子说到，可爱的棕色呆毛甩了甩，”那就再次表明身份吧！我是Ling，七号基地的大队长，也是这次出墙行动的指挥官。”")
    print("虽然是一个非常严肃的男孩子，但是好可爱！我看了看四周，那个叫Frank的家伙随后和我说明了情况。")
    print("“这里是2号基地的废墟，我们招到了怪物的袭击，来到了这里避难。在收集完资源后，我们将会回到七号基地。”")
    print("你顺着他的眼神，看到了窗外，一片黑暗，破旧的城市有着人活过的痕迹，其中还有几具尸体。你转身看向Frank，才发现眼泪在他的眼眶中打转，突然像是忍不住一般，冲了过来，狠狠的拥抱了你。")
    print("“感谢上帝，你还活着！你还活着真是太好了！对不起，丢人了。”最后一句话像是对Ling说的，他一言不发，只是看着你们两个。许久，他才突出一句，“真好啊！”")
    print("“这次行动损失了129个队友，还好，你没有死！你没有丢下我！”他的眼泪好像是感激，一把鼻涕一把眼泪感谢他的上帝。")
    print("“他的康复训练就交给你了，但是，",yourname,"你先和我出来，我有事情要和你说。”Ling 冷静的说，一个人静静的离开了病房，没有关门，只留下了和你相拥的Frank。")
    whoareyouoption()


def whatarewedoing():
    global yourname
    global ling
    ling = ling + 1
    print("“现在是什么情况？到底发生了什么！”你疑惑的问道。")
    print("“你好，你还记得你自己的名字吗！”那个银发少年着急的说。")
    print("“我是",yourname,"，对吗？”你非常不自信的回答，但是你不想让他们知道你失去记忆了。")
    print("“看来差不多恢复了”那个矮小的男子说到，可爱的棕色呆毛甩了甩，看着银发家伙。“Frank,我和你说过了，一切会往好的发现发展的！相信我！")
    print("虽然是一个非常严肃的男孩子，但是好可爱！我看了看四周，那个叫Frank的家伙随后和我说明了情况。")
    print("“这里是2号基地的废墟，我们招到了怪物的袭击，来到了这里避难。在收集完资源后，我们将会回到七号基地。”")
    print("你顺着他的眼神，看到了窗外，一片黑暗，破旧的城市有着人活过的痕迹，其中还有几具尸体。你转身看向Frank，才发现眼泪在他的眼眶中打转，突然像是忍不住一般，冲了过来，狠狠的拥抱了你。")
    print("“感谢上帝，你还活着！你还活着真是太好了！对不起，丢人了。”最后一句话像是对Ling说的，他一言不发，只是看着你们两个。许久，他才突出一句，“真好啊！”")
    print("“这次行动损失了129个队友，还好，你没有死！你没有丢下我！”他的眼泪好像是感激，一把鼻涕一把眼泪感谢他的上帝。")
    print("“他的康复训练就交给你了，但是，",yourname,"你先和我出来，我有事情要和你说。还有，我叫Ling。”Ling 冷静的说，一个人静静的离开了病房，没有关门，只留下了和你相拥的Frank。")
    whoareyouoption()

def superpowertold():
    global yourname
    global ling
    ling = ling +1
    print("你和Ling走了出去。到来一个没有人的角落，他在确定完没有人监听后,他压低了声音，说到“你知道为什么你能够在经历这么严重的意外还能活下来吗？”")
    print("“为什么？”你问。")
    print("“因为你体内有怪物的血统，他们有着自动修复身体的能力。”")
    superpowertoldask()
    print("我看着他，他一脸严肃的仰视我，拍了拍我的肩膀，对我说：“反正，现在你的任务就是掌握这一场力量，为了全人类，请掌握怪物的力量！还有，不要让其他人知道！否者，人类将会面对灭顶之灾！”")
    superpowertoldoption()
def superpowertoldask():
    global ling
    global lingstory
    print("你的疑问？")
    print("1.怪物？")
    print("2.血统？")
    option = input("")
    if option == "f":
            characteristic()
            superpowertoldask()
    elif option == "g":
            social()
            superpowertoldask()
    elif option == "1":
        ling = ling - 1
        print("“什么是怪物？”")
        print("“忘记你失忆了。”他失望的摇了摇头。")
    elif option == "2":
        ling = ling + 1
        print("“什么是怪物血统？为什么我会有这一种东西。”")
        print("“一时半会也说不清除，你就当做一场实验吧！一场拯救全人类的实验！”")
def superpowertoldoption():
    global ling
    global lingstory
    print("你的回应。")
    print("1.好的，放心交给我吧！")
    option = input("")
    if option == "f":
            characteristic()
            superpowertoldoption()
    elif option == "g":
            social()
            superpowertoldoption()
    elif option == "1":
        ling = ling + 1
        lingstory = lingstory + "这个第七基地大队长，好像相当有责任心，他和我说的话，究竟是什么意识？我拥有怪物的力量？真的假的?"
        know = "true"
        talkwithfrank(know)
def talkwithfrank(know):
    global frank
    global frankstory
    if know == "true":
        print("“你回来了，他和你说了什么？” Frank问道，你最后还是相信Ling。")
        print("“只是嘘寒问暖而已。”")
        print("“没事就好”")
    else:
        print("“你这样，不太好吧？” Frank 说到，")
        print("“你……算了，你还是留在这里多休息一下吧！让我和你说一下发生了什么。”")
        frank = frank + 1
    print("“你也知道，我失去记忆了，可以，再次和我说明发生了什么吗？”")
    print("“乐意效劳！” 你们两个走出了病房，周围破败的都市映入你们的眼帘，和病房不同，周围皆是灰暗。断壁残骸中，透露出一种阴森。")
    print("“百年前，人类占据了这一整块大陆，整个地球，然而，一天，一种神秘的怪物突然出现，开始疯狂的攻击一切。")
    print("他们拥有超级发达的肌肉，速度肉眼难以追踪，更别说和他们对抗。")
    print("由于他们的迫害，人类因此躲到了地下城。这一片大陆，有10个地下城，然而，9个已近被摧毁，只剩下一个地下城，那就是七号地下城。”")
    print("他的表情不像是开玩笑，他轻轻的叹了一口气。")
    print("“为了寻找资源，我们来到了这里，收集还没被破坏的任何能源，来维持七号地下城的供应。”")
    print("“每次出去寻找支援，死亡的人口都会占据总人口超过一半。每次都要看到队友死在我面前……”")
    print("你感受到来，那个绝望的气氛")
    print("“算了，不谈伤心事情了！快去备用食堂吃一份点心吧！明天要开始康复训练了哦！”")
    talkwithfrankoption()
def talkwithfrankoption():
    global frank
    print("“你的回答”")
    print("1.是！")
    option = input("")
    if option == "f":
            characteristic()
            talkwithfrankoption(frank)
    elif option == "g":
            social()
            talkwithfrankoption(frank)
    elif option == "1":
            frank = frank + 1
            eatcockroach()
def eatcockroach():
    print("你们来到了临时餐厅，那是由一架卡车专修而成，那个厨师愉快的向你们招手。")
    print("“喂，你们要吃什么？Frank”")
    print("“来一碗爆炒蟑螂！你呢？”他征求你的意见，突然像是意识到了什么似的，开口道“两份！Darren多谢了！”")
    print("“好耶！”")
    print("你们两个找到废墟中其中一个位置坐下。你看着桌子上的爆炒蟑螂，好奇道：“我们应该要吃这些东西吗？”")   
    print("碗里的蟑螂让你觉得恶心。")
    print("“谢谢！这还要感谢Darren啊！如果不是他每天想办法做出不同的菜肴，我们就只能吃冷冻的蟑螂了！”")
    print("“小意思，兴趣而已！”Darren做菜完，走到你们面前。“请慢用。”")
    eatcockroachoption()
def eatcockroachoption():
    global attack
    global darren
    global darrenstory
    print("一边是早已饥肠辘辘的肚子，一边是让人难以下咽的蟑螂，你决定......")
    print("1.大快朵颐")
    print("2.强忍恶心吃下去")
    print("3.拒绝食用")
    option = input("")
    if option == "f":
            characteristic()
            eatcockroachoption(darren,attack,darrenstory)
    elif option == "g":
            social()
            eatcockroachoption(darren,attack,darrenstory)
    elif option == "1":
        darren = darren + 1
        print("你一口一个蟑螂，吃得津津有味。darren看着你满嘴流油，开心的笑了。")
        print("“好吃吗？”")
        print("“好吃！”")
        darrenstory = darrenstory + "虽然是兴趣爱好，但是煮的东西还蛮好吃的！连这一种食材都能做成佳肴！太强了！而且还不收钱！"
        attack = attack + 10
        noticeling()
    elif option == "2":
        print("你看着手中的蟑螂，最后为了生存，还是觉得吃下它。对不起了，自己的味觉。")
        print("也......没那么糟糕吗！”")
        attack = attack + 20
        noticeling()
    elif option == "3":
        print("你拒绝食用，然后饿死了。")
        print("THE END")
def noticeling():
    global a
    global b
    global c
    global d
    print("就在你们吃着口中的蟑螂时，耳边突然传来声音。你感到疑惑，这才发现耳中有一个微型耳机。")
    print("“这是？”")
    print("“通知。”Frank回答了你的疑问。")
    print("“大家好，我是临时大队长Ling，有一件事情通知大家，我们将要在五天内回城！如果想要活着回去见自己的亲人和爱人的话，请做好万全的准备！我们继续用飞翼阵容出发。谢谢大家！”")
    print("“终于可以回了......”darren长叹一口气，笑了笑“都不懂我妹妹怎么了。”")
    print("“忘了和你介绍，这个人是darren，也是我的手下。”")
    print("“我会超越你的！”")
    print("那一天就在几人的闲聊中结束。")
    global day
    day = 5
    a=0
    b=0
    c=0
    d=0
    while day >=1:
        prepareforback(day)
        day = day - 1

def prepareforback(day):
    global a
    global c
    global frank
    print(day,"天后返航，在此之前，你可以做任何事情。增加自己的生存率才是最重要的哦！")
    print("你要在这一天做什么呢？")
    if frank == 10:
        print("1.和Frank告白")
    else:
        print("1.和frank一起玩。")
    print("2.康复训练。")
    print("3.和ling对话")
    print("4.去吃东西。")
    option = input("")
    if option == "f":
        characteristic()
        prepareforback(day)
    elif option == "g":
        social(frank, ling, cp, frankstory, lingstory, darren, darrenstory)
        prepareforback(day)
    elif option == "1":
        playwithfrankbeforeback()
    elif option == "2":
        healtraining()
    elif option == "3":
        talkwithlingbeforeback()
    elif option == "4":
        eatbeforeback()
def healtraining():
    import random
    global attack
    global frankstory
    global mosesstory
    global d
    global yourname
    if d == 0:
        print("“听清楚了，对于失忆的你，我再此讲解和怪物作战的方法！”Frank说到，作为小队长，这个东西理应由他负责。")
        print("“怪物这种东西，有着极高的移动速度，肉眼难以捕捉，所以，我们需要这一个放在耳边的装置，它可以预判怪物的行进方向。而作为辅助，这个背在身后的气体可以作为辅助，帮助集中注意力和增强自身能力，根据吸入的计量，可以控制增强的幅度。但是吸收太多会对身体照成威胁，要注意咯！还有这个，就是光剑，可以切换剑模式和枪模式，但是作为防御的我们，还是用剑模式会比较安全。这是防御衣，虽然完全没有办法挡住怪物的攻击，但是拥有很强大的力量”他用很快的速度说完，然后管你有没有听懂，就丢下你去处理其他事情了。")
        print("“喂，可以再重复一次吗？喂！喂喂！”")
        print("你只能自顾自练习起来。")
        attack = attack + 50
        frankstory = frankstory + "总是很忙的家伙，非常注重效率。"
        d = d+1
    else: 
        f = "abc"
        g = random.choice(f)
        if g == "a":
            print("你的对手是Frank。")
            if attack >= 150:
                print("你非常意外的打败了Frank，他对于自己的大意感到懊悔，但是还是承认了你的实力。")
            else:
                print("不出意外，你输的很惨，不过他还是故意和你过了几招，给你一个台阶下。")
                print("但是另外一边的Darren没有为Moses保留任何面子。")
                print("你学到了很多战斗技巧。")
                attack = attack + 20
        elif g == "b":
            print("你的对手是Darren")
            if attack >= 135:
                print("Darren感到惊讶，自己居然会输掉和你的对局，然后……")
                print("“我让你的，不然你怎么可能打得赢我？怎么可能？怎么可能？”")
                print("“怎么不可能？”你怼回去。")
                print("你学会了揍嘴硬男的方法。")
                attack = attack + 10
            else:
                print("Darren一脸轻松的打败了你，还嘲讽你菜就多练，玩不起就别玩。")
                print("你下次一定能狠狠暴打这家伙一顿的。")
                attack = attack + 25
        else:
            print("你的对手是Moses")
            if attack >= 115:
                print("你击败了他。")
                print("“非常抱歉没有让",yourname,"大人打的尽心。”")
                print("“我大概，不会忘记你吧！”")
def talkwithlingbeforeback():
    global ling
    global lingstory
    global c
    if c == 0:
        print("“可以和我说这次行动的概要吗？”你找到了ling。")
        print("“好的。”ling说到，“这是报告。”")
        print("他递给了你一叠纸张，“你之前应该拿过了。")
        print("「第104次出城行动")
        print("行动目的：寻找资源供应七号地下城。")
        print("行动负责人：Yang大队长")
        print("行进路线：从第七地下城出发，中途在旧矿洞修整，然后绕过森林，沿着海岸线抵达第五地下城。")
        print("出击人数400人」")
        print("你的回应")
        print("1.谢谢你")
        print("2.可是为什么我们在七号地下城")
        print("“谢谢！”我对他道谢。")
        print("“不用客气。”他礼貌的回答。")
        print("“你说的对，这次，是一次失败的行动。”他叹口气，“在矿洞中遭到了怪物的袭击，我们被迫转向，来到了这个...比较近但是资源几乎已经拿光的第二地下城。”")
        print("“非常抱歉。”你说到：“但是，这个Yang大队长...”")
        print("“你跟我来。”")
        print("你们走到了废墟中，那里堆积着很多尸体。他走到其中一具面前，对你说到：“他...死了。不堪重负自杀了。应该是被上面的压力和死去的同伴...”")
        print("你的回复：")
        print("1.加油")
        print("你拍了拍他的肩，虽然已你的身高可以轻松拍到他的头。他笑了笑，没有说话。")
        ling = ling + 1
        c = c +1
        lingstory = lingstory + "在坚毅的外表下，有着超乎常人的压力，可能身高就是这样才变成那样的吧……"
    else:
        print("Ling在忙，没有时间和你对话。")
        prepareforback(day)

def eatbeforeback():
    global attack
    global darren
    import random
    global day
    b = "ab"
    e = random.choice(b)
    print("今天你来到了餐厅")
    print("“接下来是蟑螂翅膀！”")
    print("Darren上菜，他还是一样热情：“吃不玩不准走！”")
    print("你决定")
    print("1.夸他")
    print("2.指出他食物的不足")
    option = input("")
    if option == "f":
            characteristic()
            eatbeforeback()
    elif option == "g":
            social()
            eatbeforback()
    elif option == "1":
        print("“相当好吃！”你竖起大拇指。")
        if e == "a":
            print("“谢谢夸奖，”Darren贱贱的笑：“能吃到未来大队长亲手做的美食是你的荣幸！”")
            darren = darren + 1
        elif e == "b":
            print("他默不作声，只是看着自己的食物。")
            darren = darren - 1
    elif option == "2":
        print("“味道有一点不对劲啊……”你投诉。")
        if e == "a":
            print("“感觉味道有一点奇怪。”")
            print("“爱吃吃，不吃我要吃！”")
            darren = darren - 1
        elif e == "b":
            print("“谢谢，看来，是盐放太多了，对吗？”")
            darren = darren + 1
    attack = attack + 10
def playwithfrankbeforeback():
    global frank
    global frankstory
    global a
    if frank == 10:
        print("未完待续")
    elif a == 0:
        print("你选择去找Frank一起去查第二基地，看看那里有什么。")
        print("一步步走在废墟上，底下的靴子保护了脚底。")
        print("“第七基地也是这样吗？”你问。")
        print("“大概就是还没毁灭前的样子吧！”他说到。“黑暗的荧幕包裹了这一座城市。”")
        print("“原来这是荧幕啊！”你看了看黑暗的天空。")
        print("“这东西，防御力是最顶的，怪物突破不了，然而......”")
        print("他看向了那个被人缝起来的裂缝......")
        print("“怪物突然出现，那荧幕突然破碎.....”他颤抖的说到，“于是，数百万人.....”")
        print("你看向城市，大概50公里大。数百万人，看起来是有一点拥挤啊。")
        playwithfrankbeforeback1()
        frankstory= frankstory + "总是强迫自己乐观并且带给人正面向上精神的人，看起来是一个好队长。"
        a = a + 1
    elif a == 1:
        print("今天你们两个来到了一个破旧的公园。")
        print("“没有想到繁忙的城市还有这一种东西啊！”你说到。")
        print("“来，这是球拍！”他递给了你一把球拍“要不要来一场羽球比赛！”")
        print("5：11，不出意外，你输了。")
        print("“菜就多练，玩不起就别玩！”Frank出言嘲讽。")
        playwithfrankbeforeback2()
        frankstory = frankstory + "就算在如此恶劣的环境下，也可以寻找乐趣的人。"
        a = a + 1
    elif a == 2:
        print("你们今天到了darren的餐厅吃饭。")
        print("“话说，你在七号基地有亲人吗？”你问道。")
        print("“对了，你忘了，我们都是孤儿，为了讨一个生活，才来到敢死队啊！”")
        print("“对啊，那家伙没妈！” darren调侃")
        print("“你不也一样。”")
        print("“那在乎的人呢？”我又问到。")
        print("“在乎的人...大概也只剩下你们了...”他略带伤感的说了这一句话。")
        print("Darren露出了一个奇怪的表情，好像看到了很恶心的东西一般。")
        print("“不要这样肉麻好吗！”")
        print("今日在欢笑声度过。")
        frank = frank + 1
        frankstory = frankstory + "虽然是孤儿，但是完全没有介意自己的身份。"
    elif a == 3:
        print("Frank今天很忙，你只能自己一个人玩。")
        prepareforback(day)
    return a

def playwithfrankbeforeback2():
        global frank
        print("此时此刻，你决定..")
        print("1.顶回去")
        print("2.默不作声")
        option = input("")
        if option == "f":
            characteristic()
            playwithfrankbeforeback2()
        elif option == "g":
            social()
            playwithfrankbeforeback2()
        elif option == "1":
            print("“你就在得瑟一回吧！”我怼回去。")
            print("两个人就这样开始了嘴战，并没有伤感情！好兄弟就应该这样吧！")
            frank = frank + 1
        elif option == "2":
            print("他看了看天空，你默不作声。")
            print("“所以说，在这种环境地下，我们是不是...太放纵自己了。”他沉思。")
        frank = frank + 1
def playwithfrankbeforeback1():
        global frank
        print("你接话......")
        print("1.到底是怎么被破坏的......")
        print("2.7号基地也是灰蒙蒙一片吗？")
        option = input("")
        if option == "f":
            characteristic()
            playwithfrankbeforeback1()
        elif option == "g":
            social()
            playwithfrankbeforeback1()
        elif option == "1":
            print("“到底是什么东西有能力破坏这个城市？”")
            print("“根据调查，破坏裂缝的是一个超级大的子弹。怪物是什么，我们都没有彻底了解......就连他们长什么样，我们也一无所知。”")
            print("“你们，不是经历过战斗...”你看了看frank，欲言又止。")
            print("“没事。”他拍了拍你的肩膀，“人类会赢的。”")
            frank = frank - 1
        elif option == "2":
            print("“七号基地也是这样吗？你们就生活在黑暗之下？”")
            print("“当然不是。我们生活的地方，屏幕映照着外面的天空！”")
            frank = frank + 1

starter()
