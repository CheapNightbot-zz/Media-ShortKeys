import sys, os

from PySide2.QtCore import Qt, QEvent
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QKeySequenceEdit
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets, QtGui

import MediaShortKeys

# Some copy-paste from Documantation, lol
basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'com.SOFTtechnology.Media-ShortKeys.2.0.0.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

# End of some copy-paste from Documantation

# MainWindow subclass.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media-ShortKeys")
        self.setFixedSize(512, 512)
        self.setIcon()
        self.setFont("Trebuchet MS")

        # Top level layout - containing everything in ui.
        layout = QGridLayout()
        layout.setMargin(0)

        # Vertical layout - containing hotkey input fields.
        hotkeyField = QVBoxLayout()
        hotkeyField.setAlignment(Qt.AlignRight)
        hotkeyField.setContentsMargins(269, 60, 0, 0)
        hotkeyField.setSpacing(0)

        # Vertical layout - containing hotkey names.
        hotkeyNames = QVBoxLayout()
        hotkeyNames.setAlignment(Qt.AlignLeft)
        hotkeyNames.setContentsMargins(80, 60, 0, 0)
        hotkeyNames.setSpacing(0)

        # Backgroud image.
        background = QLabel("background-image")
        background.setAlignment(Qt.AlignCenter)
        background.setPixmap('assets/background.png')

        # Header image.
        header = QLabel("header-image")
        header.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        header.setPixmap('assets/header.png')

        # Hotkey input fields.
        volumeUp = QKeySequenceEdit()
        volumeUp.setFixedSize(169, 50)
        volumeUp.setKeySequence("Ctrl+Shift+Up")
        volumeUp.setDisabled(True)
        # self.volumeUpChange = self.volumeUp.keySequence().toString()
        # self.volumeUp.editingFinished.connect(self.volumeUpChanged)

        volumeDown = QKeySequenceEdit()
        volumeDown.setFixedSize(169, 50)
        volumeDown.setKeySequence("Ctrl+Shift+Down")
        volumeDown.setDisabled(True)
        # self.volumeDown = volumeDown.keySequence().toString()
        #volumeDown.editingFinished.connect(self.volumeDownChanged)

        mediaNext = QKeySequenceEdit()
        mediaNext.setFixedSize(169, 50)
        mediaNext.setKeySequence("Ctrl+Shift+Right")
        mediaNext.setDisabled(True)
        # self.mediaNext = mediaNext.keySequence().toString()
        #mediaNext.editingFinished.connect(self.mediaNextChanged)

        mediaPrevious = QKeySequenceEdit()
        mediaPrevious.setFixedSize(169, 50)
        mediaPrevious.setKeySequence("Ctrl+Shift+Left")
        mediaPrevious.setDisabled(True)
        # self.mediaPrevious = mediaPrevious.keySequence().toString()
        #mediaPrevious.editingFinished.connect(self.mediaPreviousChanged)

        playPause = QKeySequenceEdit()
        playPause.setFixedSize(169, 50)
        playPause.setKeySequence("Ctrl+Shift+Space")
        playPause.setDisabled(True)
        # self.playPause = playPause.keySequence().toString()
        #playPause.editingFinished.connect(self.playPauseChanged)

        muteUnmute = QKeySequenceEdit()
        muteUnmute.setFixedSize(169, 50)
        muteUnmute.setKeySequence("Ctrl+Shift+M")
        muteUnmute.setDisabled(True)
        # self.muteUnmute = muteUnmute.keySequence().toString()
        #muteUnmute.editingFinished.connect(self.muteUnmuteChanged)

        mediaStop = QKeySequenceEdit()
        mediaStop.setFixedSize(169, 50)
        mediaStop.setKeySequence("Ctrl+Alt+Space")
        mediaStop.setDisabled(True)
        # self.mediaStop = mediaStop.keySequence().toString()
        #mediaStop.editingFinished.connect(self.mediaStopChanged)

        # Hotkey names.
        Volumeup = QLabel("Volume Up")
        Volumeup.setFixedSize(169, 50)
        font = Volumeup.font()
        font.setPointSize(12)
        Volumeup.setFont(font)
        Volumeup.setAlignment(Qt.AlignCenter)

        Volumedown = QLabel("Volume Down")
        Volumedown.setFixedSize(169, 50)
        font = Volumedown.font()
        font.setPointSize(12)
        Volumedown.setFont(font)
        Volumedown.setAlignment(Qt.AlignCenter)

        Medianext = QLabel("Next")
        Medianext.setFixedSize(169, 50)
        font = Medianext.font()
        font.setPointSize(12)
        Medianext.setFont(font)
        Medianext.setAlignment(Qt.AlignCenter)

        Mediaprevious = QLabel("Previous")
        Mediaprevious.setFixedSize(169, 50)
        font = Mediaprevious.font()
        font.setPointSize(12)
        Mediaprevious.setFont(font)
        Mediaprevious.setAlignment(Qt.AlignCenter)

        Playpause = QLabel("Play / Pause")
        Playpause.setFixedSize(169, 50)
        font = Playpause.font()
        font.setPointSize(12)
        Playpause.setFont(font)
        Playpause.setAlignment(Qt.AlignCenter)

        Muteunmute = QLabel("Mute / Unmute")
        Muteunmute.setFixedSize(169, 50)
        font = Muteunmute.font()
        font.setPointSize(12)
        Muteunmute.setFont(font)
        Muteunmute.setAlignment(Qt.AlignCenter)

        Mediastop = QLabel("Stop")
        Mediastop.setFixedSize(169, 50)
        font = Mediastop.font()
        font.setPointSize(12)
        Mediastop.setFont(font)
        Mediastop.setAlignment(Qt.AlignCenter)

        # Adding all hotkey input fields into
        # hotkeyField vertical layout.
        hotkeyField.addWidget(volumeUp, 0)
        hotkeyField.addWidget(volumeDown, 1)
        hotkeyField.addWidget(mediaNext, 2)
        hotkeyField.addWidget(mediaPrevious, 3)
        hotkeyField.addWidget(playPause, 4)
        hotkeyField.addWidget(muteUnmute, 5)
        hotkeyField.addWidget(mediaStop, 6)

        # Adding all hotkey names into
        # hotkeyNames vertical layout.
        hotkeyNames.addWidget(Volumeup, 0)
        hotkeyNames.addWidget(Volumedown, 1)
        hotkeyNames.addWidget(Medianext, 2)
        hotkeyNames.addWidget(Mediaprevious, 3)
        hotkeyNames.addWidget(Playpause, 4)
        hotkeyNames.addWidget(Muteunmute, 5)
        hotkeyNames.addWidget(Mediastop, 6)

        # Adding everything into top level layout.
        layout.addWidget(background, 0, 0)
        layout.addWidget(header, 0, 0)
        layout.addLayout(hotkeyField, 0, 0)
        layout.addLayout(hotkeyNames, 0, 0)

        # Creating dummy of `QWidget` and adding top level
        # layout to this widget, then adding this widget
        # to the center of our application `MainWindow` class.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Function for setting application window's icon.
    def setIcon(self):
        appIcon = QIcon("assets\keyboard.ico")
        self.setWindowIcon(appIcon)

    # Event handler for Application minimize.
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                tray_icon.show()
                window.hide()
                tray_icon.showMessage('Media-ShortKeys', 'Minimized to system tray!', QtGui.QIcon("assets\keyboard.ico"))


# SystemTrayIcon subclass.
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=MainWindow):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        
        self.setToolTip(f'Media-ShortKeys v2.0.0')
        menu = QtWidgets.QMenu(parent)

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("assets\exit.ico"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconClick)


    def onTrayIconClick(self, reason):
        if reason == self.Trigger:
            window.show()
            window.showNormal()
            tray_icon.hide()
            

if __name__ == '__main__':
    # Creating instance of `QApplication`.
    app = QApplication(sys.argv)

    # Creating an object from `MainWindow` class,
    # then calling `show` method to this object so
    # that our application GUI actually show to user,
    # otherwise it will be hidden/invisible.
    window = MainWindow()
    window.show()

    tray_icon = SystemTrayIcon(QtGui.QIcon("assets\keyboard.ico"), window)

    # Application main loop.
    sys.exit(app.exec_())
