import pytest
from gui import Window
from PySide2 import QtCore
from pytestqt import qtbot



@pytest.fixture()
def app(qtbot):
    main = Window()
    qtbot.addWidget(main)
    return main


def test_valid_input(app, qtbot):

    app.func_text_box.setText("y=x")
    app.x_max_text_box.setText("0")
    app.x_min_text_box.setText("10")
    qtbot.mouseClick(app.btn, QtCore.Qt.LeftButton)

    assert app.valid == True

def test_valid_input2(app, qtbot):

    app.func_text_box.setText("y=3*x")
    app.x_max_text_box.setText("0")
    app.x_min_text_box.setText("10")
    qtbot.mouseClick(app.btn, QtCore.Qt.LeftButton)

    assert app.valid == True

def test_valid_input3(app, qtbot):

    app.func_text_box.setText("y=x--5")
    app.x_max_text_box.setText("0")
    app.x_min_text_box.setText("10")
    qtbot.mouseClick(app.btn, QtCore.Qt.LeftButton)

    assert app.valid == True

def test_invalid_input(app, qtbot):

    app.func_text_box.setText("y=blabla")
    app.x_max_text_box.setText("0")
    app.x_min_text_box.setText("10")
    qtbot.mouseClick(app.btn, QtCore.Qt.LeftButton)

    assert app.valid == False

def test_invalid_input2(app, qtbot):

    app.func_text_box.setText("y=x+/3")
    app.x_max_text_box.setText("0")
    app.x_min_text_box.setText("10")
    qtbot.mouseClick(app.btn, QtCore.Qt.LeftButton)

    assert app.valid == False

def test_invalid_input3(app, qtbot):

    app.func_text_box.setText("y=x+3")
    app.x_max_text_box.setText("a")
    app.x_min_text_box.setText("c")
    qtbot.mouseClick(app.btn, QtCore.Qt.LeftButton)

    assert app.valid == False

   



    