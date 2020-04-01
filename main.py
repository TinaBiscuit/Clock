import vlc
import time


player = vlc.MediaPlayer("http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p")
player.play()
time.sleep(5000)