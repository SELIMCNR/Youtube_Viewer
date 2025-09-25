from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class VideoWindow(QMainWindow):
    def __init__(self, video_url, title, x, y):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(x, y, 320, 180)
        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl(video_url))
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    video_ids = [
        "SVftQYGv3lk",
        "6byM1j52USQ",
        "sdwhtOzknPo",
        "EekRzaHQP_0",
        "SVftQYGv3lk",
        "vD5h_XjAcms",
         "6byM1j52USQ",
        "sdwhtOzknPo",
        "EekRzaHQP_0"
    ]

    windows = []
    for i, vid in enumerate(video_ids):
        url = f"https://www.youtube.com/embed/{vid}?autoplay=1&mute=1&loop=1&playlist={vid}"
        x = 100 + (i % 5) * 340  # yatay konum
        y = 100 + (i // 5) * 200  # dikey konum
        win = VideoWindow(url, f"NomadWatcher #{i+1}", x, y)
        win.show()
        windows.append(win)

    sys.exit(app.exec_())