from src.Button import Button


def testInitButton():
    try:
        button = Button(text="Test")
    except:
        assert False
    else:
        assert True


def testButtonPos():
    btn = Button(text="Test")
    assert btn.rect.x == btn.rect.y == 0
