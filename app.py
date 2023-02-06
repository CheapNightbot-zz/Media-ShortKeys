import sys, os
import json

from PySide2.QtCore import Qt, QEvent
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QKeySequenceEdit, QShortcut
from PySide2.QtGui import QIcon, QKeySequence
from PySide2 import QtWidgets, QtGui

import MediaShortKeys
from MediaShortKeys import shortkey

# Some copy-paste from Documantation, lol
basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'com.SOFTtechnology.Media-ShortKeys.2.0.1.0'
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

        # Vertical layout - containing HOTKEY NAMES.
        hotkeyNames = QVBoxLayout()
        hotkeyNames.setAlignment(Qt.AlignLeft)
        hotkeyNames.setContentsMargins(15, 60, 0, 0)
        hotkeyNames.setSpacing(0)

        # Vertical layout - containing HOTKEY INPUT FIELDS.
        hotkeyField = QVBoxLayout()
        hotkeyField.setAlignment(Qt.AlignRight)
        hotkeyField.setContentsMargins(169, 60, 0, 0)
        hotkeyField.setSpacing(0)

        # Vertical layout - containing `UPDATE` BUTTON.
        hotkeyUpdate = QVBoxLayout()
        hotkeyUpdate.setAlignment(Qt.AlignRight)
        hotkeyUpdate.setContentsMargins(310, 54, 0, 0)
        hotkeyUpdate.setSpacing(7)

        # Vertical layout - containing `DEFAULT` BUTTON.
        hotkeyDefault = QVBoxLayout()
        hotkeyDefault.setAlignment(Qt.AlignRight)
        hotkeyDefault.setContentsMargins(400, 54, 0, 0)
        hotkeyDefault.setSpacing(7)

        # Backgroud image.
        background = QLabel("background-image")
        background.setAlignment(Qt.AlignCenter)
        background.setPixmap('assets/background.png')

        # Header image.
        header = QLabel("header-image")
        header.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        header.setPixmap('assets/header.png')

        # <--------------------->
        # Defining a variable for `QKeySequenceEdit().setDisabled(False)`
        # so that we can change it  later dynamically
        # with the `Update/Save` button.
        self.can_update = True
        # <--------------------->

        # Hotkey names.
        Volumeup = QLabel("Volume Up")
        Volumeup.setFixedSize(169, 50)
        font = Volumeup.font()
        font.setPointSize(10)
        Volumeup.setFont(font)
        Volumeup.setAlignment(Qt.AlignCenter)

        Volumedown = QLabel("Volume Down")
        Volumedown.setFixedSize(169, 50)
        font = Volumedown.font()
        font.setPointSize(10)
        Volumedown.setFont(font)
        Volumedown.setAlignment(Qt.AlignCenter)

        Medianext = QLabel("Media Next")
        Medianext.setFixedSize(169, 50)
        font = Medianext.font()
        font.setPointSize(10)
        Medianext.setFont(font)
        Medianext.setAlignment(Qt.AlignCenter)

        Mediaprevious = QLabel("Media Previous")
        Mediaprevious.setFixedSize(169, 50)
        font = Mediaprevious.font()
        font.setPointSize(10)
        Mediaprevious.setFont(font)
        Mediaprevious.setAlignment(Qt.AlignCenter)

        Playpause = QLabel("Play / Pause")
        Playpause.setFixedSize(169, 50)
        font = Playpause.font()
        font.setPointSize(10)
        Playpause.setFont(font)
        Playpause.setAlignment(Qt.AlignCenter)

        Muteunmute = QLabel("Mute / Unmute")
        Muteunmute.setFixedSize(169, 50)
        font = Muteunmute.font()
        font.setPointSize(10)
        Muteunmute.setFont(font)
        Muteunmute.setAlignment(Qt.AlignCenter)

        Mediastop = QLabel("Media Stop")
        Mediastop.setFixedSize(169, 50)
        font = Mediastop.font()
        font.setPointSize(10)
        Mediastop.setFont(font)
        Mediastop.setAlignment(Qt.AlignCenter)

        # Hotkey input fields.
        self.volume_Up = QKeySequenceEdit()
        self.volume_Up.setFixedSize(120, 50)
        self.volume_Up.setKeySequence("Ctrl+Shift+Up")
        self.volume_Up.setDisabled(self.can_update)
        self.volume_Up.editingFinished.connect(self.volumeUpChanged)

        self.volume_Down = QKeySequenceEdit()
        self.volume_Down.setFixedSize(120, 50)
        self.volume_Down.setKeySequence("Ctrl+Shift+Down")
        self.volume_Down.setDisabled(self.can_update)
        self.volume_Down.editingFinished.connect(self.volumeDownChanged)

        self.media_Next = QKeySequenceEdit()
        self.media_Next.setFixedSize(120, 50)
        self.media_Next.setKeySequence("Ctrl+Shift+Right")
        self.media_Next.setDisabled(self.can_update)
        self.media_Next.editingFinished.connect(self.mediaNextChanged)

        self.media_Previous = QKeySequenceEdit()
        self.media_Previous.setFixedSize(120, 50)
        self.media_Previous.setKeySequence("Ctrl+Shift+Left")
        self.media_Previous.setDisabled(self.can_update)
        self.media_Previous.editingFinished.connect(self.mediaPreviousChanged)

        self.play_Pause = QKeySequenceEdit()
        self.play_Pause.setFixedSize(120, 50)
        self.play_Pause.setKeySequence("Ctrl+Shift+Space")
        self.play_Pause.setDisabled(self.can_update)
        self.play_Pause.editingFinished.connect(self.playPauseChanged)

        self.mute_Unmute = QKeySequenceEdit()
        self.mute_Unmute.setFixedSize(120, 50)
        self.mute_Unmute.setKeySequence("Ctrl+Shift+M")
        self.mute_Unmute.setDisabled(self.can_update)
        self.mute_Unmute.editingFinished.connect(self.muteUnmuteChanged)

        self.media_Stop = QKeySequenceEdit()
        self.media_Stop.setFixedSize(120, 50)
        self.media_Stop.setKeySequence("Ctrl+Alt+Space")
        self.media_Stop.setDisabled(self.can_update)
        self.media_Stop.editingFinished.connect(self.mediaStopChanged)

        # Hotkey `update` buttons.
        self.update_volumeUp = QtWidgets.QPushButton("Update")
        self.update_volumeUp.setFixedSize(69, 25)
        self.update_volumeUp.clicked.connect(self.updateUpClicked)

        self.update_volumeDown = QtWidgets.QPushButton("Update")
        self.update_volumeDown.setFixedSize(69, 25)
        self.update_volumeDown.clicked.connect(self.updateDownClicked)

        self.update_mediaNext = QtWidgets.QPushButton("Update")
        self.update_mediaNext.setFixedSize(69, 25)
        self.update_mediaNext.clicked.connect(self.updateNextClicked)

        self.update_mediaPrevious = QtWidgets.QPushButton("Update")
        self.update_mediaPrevious.setFixedSize(69, 25)
        self.update_mediaPrevious.clicked.connect(self.updatePreviousClicked)

        self.update_playPause = QtWidgets.QPushButton("Update")
        self.update_playPause.setFixedSize(69, 25)
        self.update_playPause.clicked.connect(self.updatePlayPauseClicked)

        self.update_muteUnmute = QtWidgets.QPushButton("Update")
        self.update_muteUnmute.setFixedSize(69, 25)
        self.update_muteUnmute.clicked.connect(self.updateMuteUnmuteClicked)

        self.update_mediaStop = QtWidgets.QPushButton("Update")
        self.update_mediaStop.setFixedSize(69, 25)
        self.update_mediaStop.clicked.connect(self.updateStopClicked)

        # Hotkey`default` buttons.
        self.default_volumeUp = QtWidgets.QPushButton("Default")
        self.default_volumeUp.setFixedSize(69, 25)
        self.default_volumeUp.clicked.connect(self.defaultUpClicked)

        self.default_volumeDown = QtWidgets.QPushButton("Default")
        self.default_volumeDown.setFixedSize(69, 25)
        self.default_volumeDown.clicked.connect(self.defaultDownClicked)

        self.default_mediaNext = QtWidgets.QPushButton("Default")
        self.default_mediaNext.setFixedSize(69, 25)
        self.default_mediaNext.clicked.connect(self.defaultNextClicked)

        self.default_mediaPrevious = QtWidgets.QPushButton("Default")
        self.default_mediaPrevious.setFixedSize(69, 25)
        self.default_mediaPrevious.clicked.connect(self.defaultPreviousClicked)

        self.default_playPause = QtWidgets.QPushButton("Default")
        self.default_playPause.setFixedSize(69, 25)
        self.default_playPause.clicked.connect(self.defaultPlayPauseClicked)

        self.default_muteUnmute = QtWidgets.QPushButton("Default")
        self.default_muteUnmute.setFixedSize(69, 25)
        self.default_muteUnmute.clicked.connect(self.defaultMuteUnmuteClicked)

        self.default_mediaStop = QtWidgets.QPushButton("Default")
        self.default_mediaStop.setFixedSize(69, 25)
        self.default_mediaStop.clicked.connect(self.defaultStopClicked)

        # Adding all hotkey names into
        # hotkeyNames vertical layout.
        hotkeyNames.addWidget(Volumeup, 0)
        hotkeyNames.addWidget(Volumedown, 1)
        hotkeyNames.addWidget(Medianext, 2)
        hotkeyNames.addWidget(Mediaprevious, 3)
        hotkeyNames.addWidget(Playpause, 4)
        hotkeyNames.addWidget(Muteunmute, 5)
        hotkeyNames.addWidget(Mediastop, 6)

        # Adding all hotkey input fields into
        # hotkeyField vertical layout.
        hotkeyField.addWidget(self.volume_Up, 0)
        hotkeyField.addWidget(self.volume_Down, 1)
        hotkeyField.addWidget(self.media_Next, 2)
        hotkeyField.addWidget(self.media_Previous, 3)
        hotkeyField.addWidget(self.play_Pause, 4)
        hotkeyField.addWidget(self.mute_Unmute, 5)
        hotkeyField.addWidget(self.media_Stop, 6)

        # Adding `Update` button into
        # hotkeyUpdate vertical layout.
        hotkeyUpdate.addWidget(self.update_volumeUp, 0)
        hotkeyUpdate.addWidget(self.update_volumeDown, 1)
        hotkeyUpdate.addWidget(self.update_mediaNext, 2)
        hotkeyUpdate.addWidget(self.update_mediaPrevious, 3)
        hotkeyUpdate.addWidget(self.update_playPause, 4)
        hotkeyUpdate.addWidget(self.update_muteUnmute, 5)
        hotkeyUpdate.addWidget(self.update_mediaStop, 6)

        # Adding `Default` button into
        # hotkeyDefault vertical layout.
        hotkeyDefault.addWidget(self.default_volumeUp, 0)
        hotkeyDefault.addWidget(self.default_volumeDown, 1)
        hotkeyDefault.addWidget(self.default_mediaNext, 2)
        hotkeyDefault.addWidget(self.default_mediaPrevious, 3)
        hotkeyDefault.addWidget(self.default_playPause, 4)
        hotkeyDefault.addWidget(self.default_muteUnmute, 5)
        hotkeyDefault.addWidget(self.default_mediaStop, 6)

        # Adding everything into top level layout.
        layout.addWidget(background, 0, 0)
        layout.addWidget(header, 0, 0)
        layout.addLayout(hotkeyField, 0, 0)
        layout.addLayout(hotkeyNames, 0, 0)
        layout.addLayout(hotkeyUpdate, 0, 0)
        layout.addLayout(hotkeyDefault, 0, 0)

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
        '''
        - Event handler for Application minimize. \n\n
        It first checks if the event type (in our GUI) is `WindowStateChange`
        and if it is, then it checks whether it's `WindowMinimized`
        and hides GUI and activates system tray icon + a notification message.
        '''
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                tray_icon.show()
                window.hide()
                tray_icon.showMessage('Media-ShortKeys', 'Minimized to system tray!', QtGui.QIcon("assets\keyboard.ico"))

    # Functions for getting hotkey changes.
    def volumeUpChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Volume Up".\n\n
        Defining a variable `volumeUpChange` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.volumeUpChange = self.volume_Up.keySequence().toString()
        shortkey(self.volumeUpChange, 'B')
        # print(self.volumeUpChange)
    
    def volumeDownChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Volume Down".\n\n
        Defining a variable `volumeUpChanged` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.volumeDownChange = self.volume_Down.keySequence().toString()
        shortkey(self.volumeDownChange, 'C')
        # print(self.volumeDownChange)
    
    def mediaNextChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Media Next".\n\n
        Defining a variable `volumeUpChanged` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.mediaNextChange = self.volume_Up.keySequence().toString()
        shortkey(self.mediaNextChange, 'P')
        # print(self.mediaNextChange)

    def mediaPreviousChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Media Previous".\n\n
        Defining a variable `volumeUpChanged` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.mediaPreviousChange = self.volume_Up.keySequence().toString()
        shortkey(self.mediaPreviousChange, 'Q')
        # print(self.mediaPreviousChange)

    def playPauseChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Play / Pause".\n\n
        Defining a variable `volumeUpChanged` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.playPauseChange = self.volume_Up.keySequence().toString()
        shortkey(self.playPauseChange, 'G')
        # print(self.playPauseChange)

    def muteUnmuteChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Mute / Unmute".\n\n
        Defining a variable `volumeUpChanged` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.muteUnmuteChange = self.volume_Up.keySequence().toString()
        shortkey(self.muteUnmuteChange, 'D')
        # print(self.muteUnmuteChange)

    def mediaStopChanged(self):
        '''
        - Function for getting hotkey changes.
        - It gets triggered if user changes the hotkey value for "Media Stop".\n\n
        Defining a variable `volumeUpChanged` and giving it 
        value by getting the `volume_up`'s value converted into
        string using `.toString()` method. Then changing the hotkey
        combinations in the "MediaShortKeys.py" file
        (we have imported the function `shortkey()` from the file)
        by putting the new combinations from `volumeUpChange` 
        into `shortkey()` function.
        '''
        self.mediaStopChange = self.volume_Up.keySequence().toString()
        shortkey(self.mediaStopChange, 'J')
        # print(self.mediaStopChange)


    # `Update` & `Save` functions to change 
    # the value for `self.can_update`.
    # Also calling the `save_shortcuts()` function
    # here when user clicks "Save" button to immediately
    # save updated hotkey value to "shortcuts.json" file.
    def updateUpClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Volume Up".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_volumeUp.setText("Save")
            self.can_update = False
            self.volume_Up.setDisabled(self.can_update)
        else:
            self.update_volumeUp.setText("Update")
            self.can_update = True
            self.volume_Up.setDisabled(self.can_update)
            self.save_shortcuts()

    def updateDownClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Volume Down".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_volumeDown.setText("Save")
            self.can_update = False
            self.volume_Down.setDisabled(self.can_update)
        else:
            self.update_volumeDown.setText("Update")
            self.can_update = True
            self.volume_Down.setDisabled(self.can_update)
            self.save_shortcuts()

    def updateNextClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Media Next".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_mediaNext.setText("Save")
            self.can_update = False
            self.media_Next.setDisabled(self.can_update)
        else:
            self.update_mediaNext.setText("Update")
            self.can_update = True
            self.media_Next.setDisabled(self.can_update)
            self.save_shortcuts()

    def updatePreviousClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Media Previous".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_mediaPrevious.setText("Save")
            self.can_update = False
            self.media_Previous.setDisabled(self.can_update)
        else:
            self.update_mediaPrevious.setText("Update")
            self.can_update = True
            self.media_Previous.setDisabled(self.can_update)
            self.save_shortcuts()

    def updatePlayPauseClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Play / Pause".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_playPause.setText("Save")
            self.can_update = False
            self.play_Pause.setDisabled(self.can_update)
        else:
            self.update_playPause.setText("Update")
            self.can_update = True
            self.play_Pause.setDisabled(self.can_update)
            self.save_shortcuts()

    def updateMuteUnmuteClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Mute / Unmute".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_muteUnmute.setText("Save")
            self.can_update = False
            self.mute_Unmute.setDisabled(self.can_update)
        else:
            self.update_muteUnmute.setText("Update")
            self.can_update = True
            self.mute_Unmute.setDisabled(self.can_update)
            self.save_shortcuts()

    def updateStopClicked(self):
        '''
        - function to change the value of `self.can_update`.
        - It gets triggered if user clicks on "Update/Save"
        button next to "Media Stop".\n\n
        Function for checking if the value of `can_update`
        is "True" or "False"; then changing the button text
        according it, setting the value of `can_upate` to
        opposite and updating `.setDisabled(can_update)` with
        updated `can_update`'s value.
        '''
        if self.can_update:
            self.update_mediaStop.setText("Save")
            self.can_update = False
            self.media_Stop.setDisabled(self.can_update)
        else:
            self.update_mediaStop.setText("Update")
            self.can_update = True
            self.media_Stop.setDisabled(self.can_update)
            self.save_shortcuts()


    # `Default` functions to change hotkey to default
    # also calling `save_shortcuts()` function here for
    # changing the value of hotkeys in "shortcuts.json"
    # file when user resets hotkeys to default.
    def defaultUpClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Volume Up".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.volume_Up.setKeySequence("Ctrl+Shift+Up")
        self.save_shortcuts()

    def defaultDownClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Volume Down".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.volume_Down.setKeySequence("Ctrl+Shift+Down")
        self.save_shortcuts()

    def defaultNextClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Media Next".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.media_Next.setKeySequence("Ctrl+Shift+Right")
        self.save_shortcuts()

    def defaultPreviousClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Media Previous".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.media_Previous.setKeySequence("Ctrl+Shift+Left")
        self.save_shortcuts()

    def defaultPlayPauseClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Play / Pause".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.play_Pause.setKeySequence("Ctrl+Shift+Space")
        self.save_shortcuts()

    def defaultMuteUnmuteClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Mute / Unmute".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.mute_Unmute.setKeySequence("Ctrl+Shift+M")
        self.save_shortcuts()

    def defaultStopClicked(self):
        '''
        - `Default` function to change hotkey to default.
        - It gets triggered if user clicks the "Default" button next to "Media Stop".\n\n
        Just calling the `setKeySequence()` method on `QKeySequenceEdit()`
        and setting it's value to given KeySequence/Hotkey combination
        '''
        self.media_Stop.setKeySequence("Ctrl+Alt+Space")
        self.save_shortcuts()

    # Function for saving hotkey values so that
    # it doesn't change after application restarts.
    def save_shortcuts(self):
        shortcuts = {
            "volume_Up": self.volume_Up.keySequence().toString(),
            "volume_Down": self.volume_Down.keySequence().toString(),
            "media_Next": self.media_Next.keySequence().toString(),
            "media_Previous": self.media_Previous.keySequence().toString(),
            "play_Pause": self.play_Pause.keySequence().toString(),
            "mute_Unmute": self.mute_Unmute.keySequence().toString(),
            "media_Stop": self.media_Stop.keySequence().toString()
        }

        with open("shortcuts.json", "w") as f:
            json.dump(shortcuts, f)

    # Function to load hotkey values from "shortcuts.json" file.
    def load_shortcuts(self):
        try:
            with open("shortcuts.json", "r") as f:
                shortcuts = json.load(f)

            self.volume_Up.setKeySequence(QKeySequence(shortcuts["volume_Up"]))
            self.volume_Down.setKeySequence(QKeySequence(shortcuts["volume_Down"]))
            self.media_Next.setKeySequence(QKeySequence(shortcuts["media_Next"]))
            self.media_Previous.setKeySequence(QKeySequence(shortcuts["media_Previous"]))
            self.play_Pause.setKeySequence(QKeySequence(shortcuts["play_Pause"]))
            self.mute_Unmute.setKeySequence(QKeySequence(shortcuts["mute_Unmute"]))
            self.media_Stop.setKeySequence(QKeySequence(shortcuts["media_Stop"]))

        except FileNotFoundError:
            pass

    # Overriding the the close event function to make sure
    # it saves any changes to the hotkey values to "shorcuts.json"
    # file by calling `save_shortcuts()` function here.
    def closeEvent(self, event):
        self.save_shortcuts()
        super().closeEvent(event)

# SystemTrayIcon subclass.
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    '''- SystemTrayIcon subclass.'''
    def __init__(self, icon, parent=MainWindow):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        
        self.setToolTip(f'Media-ShortKeys v2.0.1')
        menu = QtWidgets.QMenu(parent)

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("assets\exit.ico"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconClick)


    def onTrayIconClick(self, reason):
        '''
        - Function for when user left-click on system tray icon. \n\n
        It activates/shows GUI window and then `showNormal()` method
        `window` shows/activates(?) GUI normal (otherwise it shows as minimized to taskbar).
        '''
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
    window.load_shortcuts()
    window.show()

    tray_icon = SystemTrayIcon(QtGui.QIcon("assets\keyboard.ico"), window)

    # Keyboard shortcut for quitting the application
    # makes no sense, but yeah, why not... xD
    quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), window)
    quit_shortcut.activated.connect(app.quit)

    # Application main loop.
    sys.exit(app.exec_())
