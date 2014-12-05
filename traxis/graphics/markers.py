from PyQt5 import QtWidgets, QtGui, QtCore
from traxis import constants


class MarkerList(QtWidgets.QListWidget):

    """Track Marker list class."""

    def __init__(self, parent=None):

        super().__init__(parent)

    def addMarker(self, x, y, size, width, scene):

        lastItem = self.item(self.count()-1)
        if lastItem:
            newMarkerId = lastItem.id + 1
        else:
            newMarkerId = 1

        newMarker = TrackMarker(newMarkerId, x, y, size, width, self)

        self.setCurrentItem(newMarker)

        scene.addItem(newMarker.ellipse)

        return newMarker

    def deleteMarker(self, marker):

        marker.ellipse.scene().removeItem(marker.ellipse)

        markerRow = self.row(marker)
        self.takeItem(markerRow)

    def empty(self):

        for row in range(self.count()):
            self.item(row).ellipse.scene().removeItem(self.item(row).ellipse)

        self.clear()

    def rescale(self, size, width):

        for row in range(self.count()):
            point = self.item(row)
            point.rescale(size, width)

    def setStartPoint(self, marker):
        
        oldStartPoint = self.getStartPoint()
        if oldStartPoint:
            oldStartPoint.setDesignation()
            oldStartPoint.recolor()

        marker.setDesignation('start')

    def setEndPoint(self, marker):
        
        oldEndPoint = self.getEndPoint()
        if oldEndPoint:
            oldEndPoint.setDesignation()
            oldEndPoint.recolor()

        marker.setDesignation('end')

    def getStartPoint(self):
        
        for row in range(self.count()):
            if self.item(row).designation == 'start':
                return self.item(row)

        return None

    def getEndPoint(self):
        
        for row in range(self.count()):
            if self.item(row).designation == 'end':
                return self.item(row)

        return None

    def highlightCurrent(self):
        
        for row in range(self.count()):
            self.item(row).recolor()

    def selectNext(self):

        if self.currentRow() == -1 or self.currentRow() == self.count() - 1:
            return
        else:
            self.setCurrentRow(self.currentRow() + 1)

    def selectPrevious(self):

        if self.currentRow() == -1 or self.currentRow() == 0:
            return
        else:
            self.setCurrentRow(self.currentRow() - 1)

class TrackMarker(QtWidgets.QListWidgetItem):

    """Track marker class."""

    def __init__(self, markerId, x, y, size, width, parent=None):

        self.id = markerId

        self.designation = None

        super().__init__("Point {}".format(self.id), parent)

        if size < 2: # set minimum size
            size = 2

        if width < 1: # set minimum width
            width = 1

        ellipseRect = QtCore.QRectF(x, y, size, size)
        ellipseRect.moveCenter(QtCore.QPointF(x, y))
        self.ellipse = QtWidgets.QGraphicsEllipseItem(ellipseRect)

        ellipsePen = QtGui.QPen(constants.DEFAULTMARKERCOLOR)
        ellipsePen.setWidth(width)
        self.ellipse.setPen(ellipsePen)

    def setDesignation(self, designation=None):

        if designation not in [None, 'start', 'end']:
            return
        self.designation = designation

        if designation == 'start':
            self.setText("s - Point {}".format(self.id))
        elif designation == 'end':
            self.setText("e - Point {}".format(self.id))
        else:
            self.setText("Point {}".format(self.id))

    def recolor(self):

        newPen = self.ellipse.pen()

        if self.isSelected():
            newPen.setColor(constants.HIGHLIGHTMARKERCOLOR)
        elif self.designation == 'start':
            newPen.setColor(constants.STARTMARKERCOLOR)
        elif self.designation == 'end':
            newPen.setColor(constants.ENDMARKERCOLOR)
        else:
            newPen.setColor(constants.DEFAULTMARKERCOLOR)

        self.ellipse.setPen(newPen)

    def move(self, dx, dy):

        newRect = self.ellipse.rect()
        newRect.translate(dx, dy)
        self.ellipse.setRect(newRect)

    def getAngle(self, origin, referenceMarker=None):

        # define marker vector
        markerX = self.ellipse.rect().center().x()
        markerY = self.ellipse.rect().center().y()
        markerVector = QtCore.QLineF(origin[0], origin[1], markerX, markerY)

        # define reference vector
        if referenceMarker:
            referenceX = referenceMarker.ellipse.rect().center().x()
            referenceY = referenceMarker.ellipse.rect().center().y()
        else:
            referenceX = origin[0] + 1
            referenceY = origin[1]
        referenceVector = QtCore.QLineF(origin[0], origin[1], referenceX, referenceY)

        # compute angle between marker and reference vectors
        angle = QtCore.QLineF.angleTo(referenceVector, markerVector)

        return angle

    def rescale(self, size, width):

        if size < 2: # set minimum size
            size = 2

        if width < 1: # set minimum width
            width = 1

        newRect = self.ellipse.rect()
        newRect.setWidth(size)
        newRect.setHeight(size)
        newRect.moveCenter(self.ellipse.rect().center())
        self.ellipse.setRect(newRect)

        newPen = self.ellipse.pen()
        newPen.setWidth(width)
        self.ellipse.setPen(newPen)
