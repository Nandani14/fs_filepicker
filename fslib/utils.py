# -*- coding: utf-8 -*-
"""

    fslib.utils
    ~~~~~~~~~~~~~~~~

    This module provides utils for the fslib.

    This file is part of fs_filepicker.

    :copyright: Copyright 2017 Reimar Bauer
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import fnmatch
import sys

from PyQt5.QtCore import pyqtProperty, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


def match_extension(name, extensions=None):
    """
    Determines if a file name matches an extension

    :param name: filename to be examined
    :param extensions: fnmatch file pattern
    :return: boolean True, if match is successful
    """
    if extensions is None:
        extensions = [u"*.*"]
    state = []
    for pattern in extensions:
        state.append(fnmatch.fnmatch(name, pattern))
    return True in state


def root_url():
    if sys.platform.startswith('win'):
        return u"file:///"
    else:
        return u"/"


class WidgetText(QWidget):
    def __init__(self, text, parent=None):
        QWidget.__init__(self, parent)
        self._text = text
        self.setLayout(QHBoxLayout())
        self.lbText = QLabel(self)
        self.lbText.setAlignment(Qt.AlignRight)
        self.layout().addWidget(self.lbText)
        self.lbText.setText(self._text)


class WidgetImageText(QWidget):
    # inspired by
    # https://stackoverflow.com/questions/45896291/how-to-show-image-and-text-at-same-cell-in-qtablewidget-in-pyqt
    # slightly modified
    def __init__(self, text, img, value, parent=None):
        QWidget.__init__(self, parent)
        self._text = text
        self._img = img
        self._value = value
        self.setLayout(QHBoxLayout())
        self.lbPixmap = QLabel(self)
        self.lbText = QLabel(self)
        self.lbModtime = QLabel(self)
        self.lbSize = QLabel(self)
        self.lbModtime = QLabel(self)
        self.lbText.setMinimumWidth(600)
        self.lbText.setAlignment(Qt.AlignLeft)
        self.lbSize.setMinimumWidth(200)
        self.lbSize.setAlignment(Qt.AlignLeft)
        self.lbModtime.setMinimumWidth(300)
        self.lbModtime.setAlignment(Qt.AlignLeft)
        self.layout().addWidget(self.lbPixmap)
        self.layout().addWidget(self.lbText)
        self.initUi()

    def initUi(self):
        self.lbPixmap.setPixmap(QPixmap(self._img).scaled(self.lbPixmap.size(), Qt.KeepAspectRatio))
        self.lbText.setText(self._text)

    @pyqtProperty(str)
    def img(self):
        return self._img

    @pyqtProperty(str)
    def text(self):
        return self._text

    @pyqtProperty(str)
    def value(self):
        return self._value
