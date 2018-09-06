import QtQuick 2.5

Rectangle {
    id: mainLayout
    anchors.fill: parent
    width: 500; height: 500
    color: "lightGray"

    Rectangle {
        id: rect1
        width: 100
        height: 100
        color: "blue"
    }
    Rectangle {
        id: rect2
        anchors.top: rect1.bottom
        width: 100
        height: 50
        color: "red"
    }
    Rectangle {
        id: rect3
        anchors.left: rect2.right
        anchors.leftMargin: 5
        anchors.top: rect1.bottom
        anchors.bottom: rect2.bottom
        anchors.right: parent.right
        width:100
        height: 200
        border.width: 3
        color: "green"

        Text {
            id: buttonText
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            text: textValue.val()
            font.pointSize: 16
            font.italic: true
            font.bold: true
        }

        MouseArea {
            id:buttonMouseArea
            objectName: "buttonMouseArea"
            anchors.fill: parent
            onPressed: {
                buttonText.text = textValue.val()
            }
        }

    }
}