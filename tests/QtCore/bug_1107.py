from PySide import QtCore, QtGui

if __name__ == "__main__":
    app = QtGui.QApplication([])
    print("QApplication created")
    tid = QtCore.QThread.currentThreadId()
    print("currentThreadId called")
