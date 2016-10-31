import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0

ApplicationWindow {
    visible: true

    minimumHeight: 420
    minimumWidth: 640
    maximumHeight: 420
    maximumWidth: 640

    Label {
        id: symbolLabel
        objectName: "symbolLabel"
        x: 50
        y: 50
        text: qsTr("Symbol")
    }

    TextField {
        id: symbolField
        objectName: "symbolField"
        x: 120
        y: 37
        text: qsTr("")
    }

    Button {
        id: lookupButton
        objectName: "lookupButton"
        x: 170
        y: 83
        text: qsTr("Look up")
    }

    Label {
        id: recentValue
        objectName: "recentValue"
        x: 120
        y: 129
        width: 30
        height: 13
        text: qsTr("")
    }
}
