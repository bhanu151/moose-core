# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'electrodeParasDialog.ui'
#
# Created: Tue Jun 28 11:16:43 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Electrode_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(469, 521)
        self.mooseTreeLabel = QtGui.QLabel(dialog)
        self.mooseTreeLabel.setGeometry(QtCore.QRect(30, 20, 101, 17))
        self.mooseTreeLabel.setObjectName(_fromUtf8("mooseTreeLabel"))
        self.mtree = MooseTreeWidget(dialog)
        self.mtree.setGeometry(QtCore.QRect(30, 40, 191, 131))
        self.mtree.setObjectName(_fromUtf8("mtree"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(250, 40, 171, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectedCompartmentLabel = QtGui.QLabel(dialog)
        self.selectedCompartmentLabel.setGeometry(QtCore.QRect(280, 70, 151, 17))
        self.selectedCompartmentLabel.setObjectName(_fromUtf8("selectedCompartmentLabel"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 130, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.electrodeSelectionCombo = QtGui.QComboBox(dialog)
        self.electrodeSelectionCombo.setGeometry(QtCore.QRect(310, 120, 131, 31))
        self.electrodeSelectionCombo.setObjectName(_fromUtf8("electrodeSelectionCombo"))
        self.electrodeSelectionCombo.addItem(_fromUtf8(""))
        self.electrodeSelectionCombo.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 67, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 216, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 250, 81, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 284, 91, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.baseLevelEdit = QtGui.QLineEdit(dialog)
        self.baseLevelEdit.setGeometry(QtCore.QRect(260, 210, 71, 27))
        self.baseLevelEdit.setObjectName(_fromUtf8("baseLevelEdit"))
        self.firstLevelEdit = QtGui.QLineEdit(dialog)
        self.firstLevelEdit.setGeometry(QtCore.QRect(260, 245, 71, 27))
        self.firstLevelEdit.setObjectName(_fromUtf8("firstLevelEdit"))
        self.secondLevelEdit = QtGui.QLineEdit(dialog)
        self.secondLevelEdit.setGeometry(QtCore.QRect(260, 280, 71, 27))
        self.secondLevelEdit.setObjectName(_fromUtf8("secondLevelEdit"))
        self.label_7 = QtGui.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 356, 91, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(dialog)
        self.label_8.setGeometry(QtCore.QRect(253, 357, 81, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 399, 91, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(dialog)
        self.label_10.setGeometry(QtCore.QRect(250, 397, 101, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.firstDelayEdit = QtGui.QLineEdit(dialog)
        self.firstDelayEdit.setGeometry(QtCore.QRect(130, 350, 71, 27))
        self.firstDelayEdit.setObjectName(_fromUtf8("firstDelayEdit"))
        self.secondDelayEdit = QtGui.QLineEdit(dialog)
        self.secondDelayEdit.setGeometry(QtCore.QRect(130, 390, 71, 27))
        self.secondDelayEdit.setObjectName(_fromUtf8("secondDelayEdit"))
        self.firstWidthEdit = QtGui.QLineEdit(dialog)
        self.firstWidthEdit.setGeometry(QtCore.QRect(370, 350, 71, 27))
        self.firstWidthEdit.setObjectName(_fromUtf8("firstWidthEdit"))
        self.secondWidthEdit = QtGui.QLineEdit(dialog)
        self.secondWidthEdit.setGeometry(QtCore.QRect(370, 390, 71, 27))
        self.secondWidthEdit.setObjectName(_fromUtf8("secondWidthEdit"))
        self.closePushButton = QtGui.QPushButton(dialog)
        self.closePushButton.setGeometry(QtCore.QRect(110, 460, 95, 27))
        self.closePushButton.setObjectName(_fromUtf8("closePushButton"))
        self.okayPushButton = QtGui.QPushButton(dialog)
        self.okayPushButton.setGeometry(QtCore.QRect(290, 460, 95, 27))
        self.okayPushButton.setObjectName(_fromUtf8("okayPushButton"))

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.closePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.electrodeSelectionCombo, self.baseLevelEdit)
        dialog.setTabOrder(self.baseLevelEdit, self.firstLevelEdit)
        dialog.setTabOrder(self.firstLevelEdit, self.secondLevelEdit)
        dialog.setTabOrder(self.secondLevelEdit, self.firstDelayEdit)
        dialog.setTabOrder(self.firstDelayEdit, self.firstWidthEdit)
        dialog.setTabOrder(self.firstWidthEdit, self.secondDelayEdit)
        dialog.setTabOrder(self.secondDelayEdit, self.secondWidthEdit)
        dialog.setTabOrder(self.secondWidthEdit, self.closePushButton)
        dialog.setTabOrder(self.closePushButton, self.okayPushButton)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Electrode Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.mooseTreeLabel.setText(QtGui.QApplication.translate("dialog", "Moose Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.mtree.setToolTip(QtGui.QApplication.translate("dialog", "Select cells to visualize, double click to add cell OR select and click \'+\' button, click \'A\' button to draw all cells", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialog", "Compartment Selected:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectedCompartmentLabel.setText(QtGui.QApplication.translate("dialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialog", "Electrode:", None, QtGui.QApplication.UnicodeUTF8))
        self.electrodeSelectionCombo.setItemText(0, QtGui.QApplication.translate("dialog", "Current Clamp", None, QtGui.QApplication.UnicodeUTF8))
        self.electrodeSelectionCombo.setItemText(1, QtGui.QApplication.translate("dialog", "Voltage Clamp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dialog", "Pulse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dialog", "Base Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dialog", "First Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dialog", "Second Level", None, QtGui.QApplication.UnicodeUTF8))
        self.baseLevelEdit.setText(QtGui.QApplication.translate("dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.firstLevelEdit.setText(QtGui.QApplication.translate("dialog", "25e-6", None, QtGui.QApplication.UnicodeUTF8))
        self.secondLevelEdit.setText(QtGui.QApplication.translate("dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dialog", "First Delay", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("dialog", "First Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("dialog", "Second Delay", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("dialog", "Second Width", None, QtGui.QApplication.UnicodeUTF8))
        self.firstDelayEdit.setText(QtGui.QApplication.translate("dialog", "2e-3", None, QtGui.QApplication.UnicodeUTF8))
        self.secondDelayEdit.setText(QtGui.QApplication.translate("dialog", "1e8", None, QtGui.QApplication.UnicodeUTF8))
        self.firstWidthEdit.setText(QtGui.QApplication.translate("dialog", "50e-3", None, QtGui.QApplication.UnicodeUTF8))
        self.secondWidthEdit.setText(QtGui.QApplication.translate("dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.closePushButton.setText(QtGui.QApplication.translate("dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.okayPushButton.setText(QtGui.QApplication.translate("dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

from moosetree import MooseTreeWidget