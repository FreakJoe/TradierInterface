import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

from tradier import Tradier

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
ctx = engine.rootContext()
ctx.setContextProperty('main', engine)
engine.load('ui\main.qml')
win = engine.rootObjects()[0]
win.show()

t_handle = Tradier()

def set_recent_value():
	symbol = symbol_field.property('text')
	recent_value = t_handle.get_moving_average(symbol, 60)
	recent_value_field.setProperty('text', '60-day moving average: {}'.format(recent_value))


lookup_button = win.findChild(QObject, "lookupButton")
symbol_field = win.findChild(QObject, "symbolField")
recent_value_field = win.findChild(QObject, "recentValue")
lookup_button.clicked.connect(set_recent_value)

sys.exit(app.exec_())