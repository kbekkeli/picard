# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options_folksonomy.ui'
#
# Created: Sat Feb 16 20:39:33 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FolksonomyOptionsPage(object):
    def setupUi(self, FolksonomyOptionsPage):
        FolksonomyOptionsPage.setObjectName("FolksonomyOptionsPage")
        FolksonomyOptionsPage.resize(QtCore.QSize(QtCore.QRect(0,0,367,267).size()).expandedTo(FolksonomyOptionsPage.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(FolksonomyOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")

        self.rename_files_3 = QtGui.QGroupBox(FolksonomyOptionsPage)
        self.rename_files_3.setObjectName("rename_files_3")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.rename_files_3)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.ignore_tags_2 = QtGui.QLabel(self.rename_files_3)
        self.ignore_tags_2.setObjectName("ignore_tags_2")
        self.vboxlayout1.addWidget(self.ignore_tags_2)

        self.ignore_tags = QtGui.QLineEdit(self.rename_files_3)
        self.ignore_tags.setObjectName("ignore_tags")
        self.vboxlayout1.addWidget(self.ignore_tags)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_5 = QtGui.QLabel(self.rename_files_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.hboxlayout.addWidget(self.label_5)

        self.min_tag_usage = QtGui.QSpinBox(self.rename_files_3)
        self.min_tag_usage.setMaximum(100)
        self.min_tag_usage.setObjectName("min_tag_usage")
        self.hboxlayout.addWidget(self.min_tag_usage)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_6 = QtGui.QLabel(self.rename_files_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.hboxlayout1.addWidget(self.label_6)

        self.max_tags = QtGui.QSpinBox(self.rename_files_3)
        self.max_tags.setMaximum(100)
        self.max_tags.setObjectName("max_tags")
        self.hboxlayout1.addWidget(self.max_tags)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.ignore_tags_4 = QtGui.QLabel(self.rename_files_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_tags_4.sizePolicy().hasHeightForWidth())
        self.ignore_tags_4.setSizePolicy(sizePolicy)
        self.ignore_tags_4.setObjectName("ignore_tags_4")
        self.hboxlayout2.addWidget(self.ignore_tags_4)

        self.join_tags = QtGui.QComboBox(self.rename_files_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.join_tags.sizePolicy().hasHeightForWidth())
        self.join_tags.setSizePolicy(sizePolicy)
        self.join_tags.setEditable(True)
        self.join_tags.setObjectName("join_tags")
        self.join_tags.addItem("")
        self.hboxlayout2.addWidget(self.join_tags)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.vboxlayout.addWidget(self.rename_files_3)

        spacerItem = QtGui.QSpacerItem(181,31,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.label_5.setBuddy(self.min_tag_usage)
        self.label_6.setBuddy(self.min_tag_usage)

        self.retranslateUi(FolksonomyOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(FolksonomyOptionsPage)

    def retranslateUi(self, FolksonomyOptionsPage):
        self.rename_files_3.setTitle(_("Folksonomy Tags"))
        self.ignore_tags_2.setText(_("Ignore tags:"))
        self.label_5.setText(_("Minimal tag usage:"))
        self.min_tag_usage.setSuffix(_(" %"))
        self.label_6.setText(_("Maximal number of tags:"))
        self.ignore_tags_4.setText(_("Join multiple tags with:"))
        self.join_tags.addItem(_(" / "))
        self.join_tags.addItem(_(", "))

