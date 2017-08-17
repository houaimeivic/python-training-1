class BaseMusic(object):
    def __init__(self, people, song):
        self.people = people
        self.song = song


class Mp3(BaseMusic):
    pass


class Mp4(BaseMusic):
    def __init__(self, video, people, song):
        super(Mp4, self).__init__(people, song)
        self.video = video


song = Mp3('王力宏', 'Can You Feel My Word')
info = ('单曲Can You Feel My World被称为是王力宏的内心世界大独白，'
        '歌曲基调悲伤而无奈，表达了力宏在音乐旅程上闯荡8年的感想。'
        '收录在王力宏2003年发行的专辑《不可思议》里。')
video = Mp4(info, '王力宏', 'Can You Feel My Word')


class ControllerMixin(object):
    def start(self):
        if self.status == PlayerCore.PLAYING:
            return self.show_status()

        self.current_people = self.item.people
        self.current_song = self.item.song
        self.status = PlayerCore.PLAYING
        print '开始播放{}的{}'.format(self.current_people, self.current_song)

    def stop(self):
        if self.status == PlayerCore.STOP:
            return self.show_status()

        print '停止播放{}的{}'.format(self.current_people, self.current_song)
        self.current_song = None
        self.current_people = None
        self.status = PlayerCore.STOP


class PlayerCore(object):
    STOP = 'stop'
    PLAYING = 'playing'

    def __init__(self, item):
        self.item = item
        self.status = PlayerCore.STOP
        self.current_people = None
        self.current_song = None

    def show_status(self):
        if self.status == self.PLAYING:
            print '当前正在播放{}的{}'.format(self.current_people, self.current_song)
        else:
            print '当前没有播放'


class MusicPlayer(ControllerMixin, PlayerCore):
    def __init__(self, item, auto_play=True):
        if not isinstance(item, Mp3):
            raise Exception('只能播放mp3')

        super(MusicPlayer, self).__init__(item)

        if auto_play:
            self.start()


class VideoPlayer(ControllerMixin, PlayerCore):
    def __init__(self, item, auto_play=True):
        super(VideoPlayer, self).__init__(item)

        if auto_play:
            self.start()

    def start(self):
        super(VideoPlayer, self).start()

        if isinstance(self.item, Mp4):
            print self.item.video


mp3_player = MusicPlayer(song)
mp4_player = VideoPlayer(video, auto_play=False)