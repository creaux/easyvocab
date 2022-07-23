# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dialogUNXxYU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys
import codecs

# import the main window object (mw) from aqt
from aqt import mw
from aqt.qt import *

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "site-packages"))
import googletrans

from . import file_select_dialog, progress_dialog
from .. import util, generate


class MainDialog(object):
    def setupUi(self, Dialog):
       if not Dialog.objectName():
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(514, 473)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 511, 471))
        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(165, 440, 166, 25))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(61, 11, 386, 397))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 5)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(328, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 0, 2, 5)

        self.horizontalSpacer_5 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 2, 2, 2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 4)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 5, 0, 1, 2)

        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 5, 2, 1, 4)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 4, 1, 1)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 7, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 7, 3, 1, 2)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(2)

        self.gridLayout.addWidget(self.spinBox, 8, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 8, 1, 1, 4)


        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

        # perform final setup actions
        # note that these are actions outside of the ones auto generated by QtDesigner
        self.customSetup(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generate Foreign Language Cards", None))
        self.groupBox.setTitle("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter words...", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Import words file</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Select file...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Source Language", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Target Language", None))
#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Choose or create a deck to import words into</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBox.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Deck", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Deck", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Create reverse vocab cards in addition to normal ones.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Create reverse cards", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>The default number of translations to use on the reverse side of each card</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Default number of translations", None))
    # retranslateUi


    # Custom functions

    # Call the select file dialog, and handle opening and wiring in the file contents to the text box
    def populateFileText(self):
        filename = file_select_dialog.selectFile()

        if filename and filename != '':
                with codecs.open(filename, mode='r', encoding='utf-8') as file:
                    self.setBoxText(str(file.read()))

        return

    def create_progress_dialog(self) -> None:
        dialog = QDialog()
        dialog.ui = progress_dialog.ProgressDialog()
        dialog.ui.setupUi(dialog)

        return dialog

    def accept_dialog(self, Dialog):
        progress = self.create_progress_dialog()

        text       = self.textEdit.toPlainText()
        collection = mw.col

        options = {}

        # Get the target deck from the main dialog
        deck = self.comboBox.currentData()

        # Get the language settings from the self
        src  = self.comboBox_2.currentData()
        dest = self.comboBox_3.currentData()
        options['language'] = {'src': src, 'dest': dest}

        # Get the reverse setting from the main dialog
        reverse = self.radioButton.isChecked()
        options['reverse'] = reverse

        # Get the number of translations to include
        num_translations = self.spinBox.value()
        options['num_translations'] = num_translations

        generate.generate_cards(collection, deck, text, options, { 'main': Dialog, 'progress': progress })
        progress.exec_()

    # Custom dialog setup
    # Encapsulated in this function to limit the impact of UI changes / redesign
    def customSetup(self, Dialog):
        # connect select file button to the select file dialog
        self.pushButton.clicked.connect(self.populateFileText)

        # populate the deck list from anki into the combo box
        self.populateDecks(self.comboBox)

        # populate the set of source and target languages into their respective combo box
        self.populateLanguages(self.comboBox_2)
        self.populateLanguages(self.comboBox_3)

        # set the default target language to english
        index = self.comboBox_3.findData("en")
        self.comboBox_3.setCurrentIndex(index)

        # wire the accept button
        self.buttonBox.accepted.connect(util.wrap_nonary(self.accept_dialog)(Dialog))


    # Set the text within the main words entry text box
    def setBoxText(self, text):
        self.textEdit.setText(text)

    # Retrieve decks from anki and use them to populate the combo box
    def populateDecks(self, comboBox):
        decks = mw.col.decks.all_names_and_ids()

        index = 0

        for deck in decks:
            comboBox.addItem(deck.name, deck)

            if deck.name == 'Default':
                comboBox.setCurrentIndex(index)
            
            index += 1

    # Pull languages from googletrans and populate the combo boxes
    def populateLanguages(self, comboBox):
        # Add default empty entry for language dialog
        comboBox.addItem("", None)

        languages = googletrans.LANGUAGES

        for language_code, language_name in languages.items():
            comboBox.addItem(util.capitalize(language_name), language_code)