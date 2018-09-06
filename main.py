import os
import sys
from PySide2 import QtCore
from PySide2.QtCore import QUrl, QObject, Slot, Qt
from PySide2.QtGui import QGuiApplication
import PySide2.QtQml
from PySide2.QtQuick import QQuickView

# Properties

class TextValue(QObject):
    def __init__(self):
        super(TextValue, self).__init__()
        self.texList = ["","Once", "Twice", "Again"]
        self.textid = 0
        self.baseText = "Hurt Me"
        self.text = ""

    @Slot(result=str)
    def val(self):
        self.text = "{} {} !".format(self.baseText, self.texList[self.textid])
        self.textid = 0 if self.textid == 3 else self.textid + 1
        return self.text
# main
def main():
    app = QGuiApplication( sys.argv )
    app.setAttribute(Qt.AA_UseDesktopOpenGL)
    view = QQuickView()
    context = view.rootContext()
    prop_dict= {"textValue": TextValue}
    for propName, prop in prop_dict.items():
        prop = prop()
        print(propName, prop)
        context.setContextProperty(propName, prop)
    qmlFile = os.path.join( os.path.dirname(__file__), "ui.qml" )
    view.setSource(QUrl.fromLocalFile( os.path.abspath( qmlFile ) ))

    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setMinimumSize(QtCore.QSize(200, 200))
    view.show()
    res = app.exec_()
    del view
    sys.exit(res)

if __name__ == '__main__':
    main()