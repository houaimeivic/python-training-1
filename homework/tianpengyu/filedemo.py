# coding=utf-8
def run():
    with open('jiang_jin_jiu.txt', 'r') as file:
        for line in file:
            print line

run()


def normal_run():
    file = open('jiang_jin_jiu.txt')

    print 'current:{}'.format(file.tell())
    for line in file:
        print line
        print 'current:{}'.format(file.tell())

    print 'current:{}'.format(file.tell())
    file.close()


def write_model_exception():
    file = open('jiang_jin_jiu.txt', 'w')
    for line in file:
        print line

    file.close()


def write_model():
    file = open('jiang_jin_jiu.txt', 'w')
    contents = [
        '唐 - 李白',
        '君不见，黄河之水天上来，奔流到海不复回。',
        '君不见，高堂明镜悲白发，朝如青丝暮成雪。',
        '人生得意须尽欢，莫使金樽空对月。',
        '天生我材必有用，千金散尽还复来。',
        '烹羊宰牛且为乐，会须一饮三百杯。',
        '岑夫子，丹丘生，将进酒，杯莫停。',
        '与君歌一曲，请君为我倾耳听。',
        '钟鼓馔玉不足贵，但愿长醉不复醒。',
        '古来圣贤皆寂寞，惟有饮者留其名。',
        '陈王昔时宴平乐，斗酒十千恣欢谑。',
        '主人何为言少钱，径须沽取对君酌。',
        '五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。',
    ]
    file.writelines(['{}\n'.format(line) for line in contents])
    print 'current:{}'.format(file.tell())

    contents.insert(0, '将进酒')
    file.seek(0)
    file.writelines(['{}\n'.format(line) for line in contents])
    file.close()


def other_write_model_append():
    append_write = open('jiang_jin_jiu.txt', 'a')
    print 'current:{}'.format(append_write.tell())
    append_write.write('hello in the end')
    print 'current:{}'.format(append_write.tell())
    append_write.seek(0)
    print 'current:{}'.format(append_write.tell())
    append_write.write('hello in the start')
    append_write.close()


def other_write_model_rw():
    read_write = open('jiang_jin_jiu.txt', 'r+')
    for line in read_write:
        print line

    read_write.seek(0)
    read_write.write('快喝酒')
    read_write.seek(0, 2)
    read_write.write('(完)')
    read_write.close()

    run()