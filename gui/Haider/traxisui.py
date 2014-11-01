# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traxis.ui'
#
# Created: Sat Nov  1 16:03:12 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_traxis(object):
    def setupUi(self, traxis):
        
        ##### main Widget
        traxis.setObjectName("traxis")
        traxis.resize(1070, 665)
        traxis.setMaximumSize(QtCore.QSize(100000, 1000000))

        ##### creating the window 
        self.centralWidget = QtWidgets.QWidget(traxis)
        self.centralWidget.setObjectName("centralWidget")

        ##### Layout of the main window - allows for resizing
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        #### Layout inside the main one..
        #### main layout in the GUI
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")

        #### Layout for the top button
        self.TopBtnLayout = QtWidgets.QHBoxLayout()
        self.TopBtnLayout.setObjectName("TopBtnLayout")
        
        ### QList Widget for displaying points
        ## layout organizations
        self.verticalLayout_pointLabel = QtWidgets.QVBoxLayout()
        self.verticalLayout_pointLabel.setObjectName("verticalLayout_pointLabel")
        ## Label on the top
        self.label_points = QtWidgets.QLabel(self.centralWidget)
        self.label_points.setObjectName("label_points")
        self.verticalLayout_pointLabel.addWidget(self.label_points)
        ## List Widget
        self.listWidget_points = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_points.setObjectName("listWidget_points")
        self.verticalLayout_pointLabel.addWidget(self.listWidget_points)
        
        ### add the layout to the main button layour
        self.TopBtnLayout.addLayout(self.verticalLayout_pointLabel)
        
        ### Line to visually divide the area
        self.vLine_div2 = QtWidgets.QFrame(self.centralWidget)
        self.vLine_div2.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.vLine_div2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vLine_div2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vLine_div2.setObjectName("vLine_div2")
        ## add to the top Layout
        self.TopBtnLayout.addWidget(self.vLine_div2)

        ### Technical buttons
        ## Layout for that
        self.tech_calc_btnLayout = QtWidgets.QVBoxLayout()
        self.tech_calc_btnLayout.setObjectName("tech_calc_btnLayout")
        
        ## for reset button
        # Label for reset
        self.label_tech = QtWidgets.QLabel(self.centralWidget)
        self.label_tech.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.label_tech.setObjectName("label_tech")
        self.tech_calc_btnLayout.addWidget(self.label_tech)
        # Button for reset
        self.btn_reset = QtWidgets.QPushButton(self.centralWidget)
        self.btn_reset.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.btn_reset.setObjectName("btn_reset")
        # add to the tech_calc_btn Layout                
        self.tech_calc_btnLayout.addWidget(self.btn_reset)

        ## for Zoom Button
        # label
        self.label_Zoom = QtWidgets.QLabel(self.centralWidget)
        self.label_Zoom.setObjectName("label_Zoom")
        self.tech_calc_btnLayout.addWidget(self.label_Zoom)
        # Slider for Zoom
        self.sld_zoom = QtWidgets.QSlider(self.centralWidget)
        self.sld_zoom.setEnabled(True)
        self.sld_zoom.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.sld_zoom.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sld_zoom.setAccessibleName("")
        self.sld_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.sld_zoom.setObjectName("sld_zoom")
        self.tech_calc_btnLayout.addWidget(self.sld_zoom)
        ## Label for Calculation button
        self.label_calc = QtWidgets.QLabel(self.centralWidget)
        self.label_calc.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.label_calc.setObjectName("label_calc")
        self.tech_calc_btnLayout.addWidget(self.label_calc)
        ## Calculation track momentum button
        self.btn_trackMom = QtWidgets.QPushButton(self.centralWidget)
        self.btn_trackMom.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.btn_trackMom.setObjectName("btn_trackMom")
        self.tech_calc_btnLayout.addWidget(self.btn_trackMom)
        ## Calculation optical density button
        self.btn_optDen = QtWidgets.QPushButton(self.centralWidget)
        self.btn_optDen.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.btn_optDen.setObjectName("btn_optDen")
        self.tech_calc_btnLayout.addWidget(self.btn_optDen)
        ## Calculation Angle button       
        self.btn_angle = QtWidgets.QPushButton(self.centralWidget)
        self.btn_angle.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.btn_angle.setStyleSheet("")
        self.btn_angle.setObjectName("btn_angle")
        self.tech_calc_btnLayout.addWidget(self.btn_angle)
        ## space at the bottom to maintain the size 
        spacerItem = QtWidgets.QSpacerItem(16777215, 16777192, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tech_calc_btnLayout.addItem(spacerItem)

        ## add the layout to the main button layour
        self.TopBtnLayout.addLayout(self.tech_calc_btnLayout)
        
        ### Line to visually divide the area        
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        ## add the layout to the main button layour
        self.TopBtnLayout.addWidget(self.line_2)
        
        ### User Selection buttons
        ## Layout for that
        self.usrSel_layout = QtWidgets.QVBoxLayout()
        self.usrSel_layout.setObjectName("usrSel_layout")

        ## Label for the select button
        self.label_userSle = QtWidgets.QLabel(self.centralWidget)
        self.label_userSle.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.label_userSle.setObjectName("label_userSle")
        self.usrSel_layout.addWidget(self.label_userSle)
        
        ## button for placing marker on the track
        self.btn_placeMar = QtWidgets.QPushButton(self.centralWidget)
        self.btn_placeMar.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.btn_placeMar.setObjectName("btn_placeMar")
        # --------CHANGE-------- : added this option to make the button be in the clickable
        self.btn_placeMar.setCheckable(True)
        self.usrSel_layout.addWidget(self.btn_placeMar)

        ## DL box 
        # Layout
        self.dlForm = QtWidgets.QFormLayout()
        self.dlForm.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dlForm.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dlForm.setObjectName("dlForm")
        # Label for DL
        self.setDlLabel = QtWidgets.QLabel(self.centralWidget)
        self.setDlLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setDlLabel.setObjectName("setDlLabel")
        self.dlForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.setDlLabel)
        # LineEdit
        self.setDlLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.setDlLineEdit.setObjectName("setDlLineEdit")
        self.dlForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.setDlLineEdit)
        self.usrSel_layout.addLayout(self.dlForm)

        ## Angle Button
        self.btn_drwAngle = QtWidgets.QPushButton(self.centralWidget)
        self.btn_drwAngle.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.btn_drwAngle.setObjectName("btn_drwAngle")
        # --------CHANGE-------- : added this option to make the button be in the clickable
        self.btn_drwAngle.setCheckable(True)
        self.usrSel_layout.addWidget(self.btn_drwAngle)

        ## Spacer Item
        spacerItem1 = QtWidgets.QSpacerItem(16777215, 16777192, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.usrSel_layout.addItem(spacerItem1)
        
        ## add the layout to the main button layout
        self.TopBtnLayout.addLayout(self.usrSel_layout)
        
        ### Line to visually divide the area        
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        ## add the layout to the main button layout
        self.TopBtnLayout.addWidget(self.line_3)
        
        ### Console Ouput
        ## layout
        self.ConsoleLayout = QtWidgets.QVBoxLayout()
        self.ConsoleLayout.setObjectName("ConsoleLayout")

        ## label
        self.label_console = QtWidgets.QLabel(self.centralWidget)
        self.label_console.setObjectName("label_console")
        self.ConsoleLayout.addWidget(self.label_console)

        ## Acutal output
        self.textBrowser_consoleOutput = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_consoleOutput.setMinimumSize(QtCore.QSize(250, 0))
        self.textBrowser_consoleOutput.setObjectName("textBrowser_consoleOutput")
        self.ConsoleLayout.addWidget(self.textBrowser_consoleOutput)

        ## add the layout to the main button layout
        self.TopBtnLayout.addLayout(self.ConsoleLayout)

        ## add to the main window layour
        self.mainLayout.addLayout(self.TopBtnLayout)

        ### Spacer to maintain the size of the QLabel bottom
        spacerItem2 = QtWidgets.QSpacerItem(16777215, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        ## add to the main window layour
        self.mainLayout.addItem(spacerItem2)
        
        ### Line to visually divide the area                
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        ## add to the main window layour
        self.mainLayout.addWidget(self.line)


        ### Main label
        ## --------CHANGE-------- 
        ## Changing from a QLabel to QScroll Areas
        ## leaving the old code still, for refereces
        #self.picLabel = QtWidgets.QLabel(self.centralWidget)
        #self.picLabel.setMinimumSize(QtCore.QSize(0, 312))
        #self.picLabel.setMaximumSize(QtCore.QSize(16777215, 16777192))
        #self.picLabel.setText("")
        #self.picLabel.setScaledContents(True)
        #self.picLabel.setObjectName("picLabel")
        #self.mainLayout.addWidget(self.picLabel)
        ### ------- START OF ADDITION -------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, traxis.size().height()/1.5))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777192))
        self.scrollArea.setWidgetResizable(True)
        self.mainLayout.addWidget(self.scrollArea)
        ### ------- END OF ADDITION -------
        
        ## Add to the main layout
        self.verticalLayout.addLayout(self.mainLayout)
        traxis.setCentralWidget(self.centralWidget)
        
        ## menu bar and status bar below
        self.menuBar = QtWidgets.QMenuBar(traxis)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1070, 22))
        self.menuBar.setObjectName("menuBar")
        traxis.setMenuBar(self.menuBar)
        
        self.mainToolBar = QtWidgets.QToolBar(traxis)
        self.mainToolBar.setObjectName("mainToolBar")
        traxis.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        
        self.statusBar = QtWidgets.QStatusBar(traxis)
        self.statusBar.setObjectName("statusBar")
        traxis.setStatusBar(self.statusBar)


        ## To the correct mane and labels
        self.retranslateUi(traxis)
        QtCore.QMetaObject.connectSlotsByName(traxis)

    ## sets the label and what is displayed when the button is clicked
    def retranslateUi(self, traxis):
        _translate = QtCore.QCoreApplication.translate
        traxis.setWindowTitle(_translate("traxis", "traxis"))
        self.label_points.setText(_translate("traxis", "Points on picture"))
        self.label_tech.setText(_translate("traxis", "Technical buttons"))
        self.btn_reset.setToolTip(_translate("traxis", "<html><head/><body><p>Reset all the selected points and calculated variables</p></body></html>"))
        self.btn_reset.setText(_translate("traxis", "Reset"))
        self.label_Zoom.setText(_translate("traxis", "Zoom"))
        self.sld_zoom.setToolTip(_translate("traxis", "<html><head/><body><p>Zoom Control</p></body></html>"))
        self.label_calc.setText(_translate("traxis", "Calculate"))
        self.btn_trackMom.setToolTip(_translate("traxis", "<html><head/><body><p>Calculate Track momentum</p></body></html>"))
        self.btn_trackMom.setText(_translate("traxis", "Cal Track Momemetum"))
        self.btn_optDen.setToolTip(_translate("traxis", "<html><head/><body><p>Calculate Optical Density</p></body></html>"))
        self.btn_optDen.setText(_translate("traxis", "Calc Optical Density"))
        self.btn_angle.setToolTip(_translate("traxis", "<html><head/><body><p>Calculate Opening Angle</p></body></html>"))
        self.btn_angle.setText(_translate("traxis", "Caculate Angle"))
        self.label_userSle.setText(_translate("traxis", "User selection"))
        self.btn_placeMar.setToolTip(_translate("traxis", "<html><head/><body><p>Place a new marker on the track</p></body></html>"))
        self.btn_placeMar.setText(_translate("traxis", "Place track marker"))
        self.setDlLabel.setText(_translate("traxis", "set DL"))
        self.btn_drwAngle.setToolTip(_translate("traxis", "<html><head/><body><p>Draw reference for angle</p><p><br/></p></body></html>"))
        self.btn_drwAngle.setText(_translate("traxis", "Draw angle ref."))
        self.label_console.setText(_translate("traxis", "Console"))
        

