from src.Button import Button


def testInitButton():
    try:
        button = Button(text="Test")
        assert True
    except:
        assert False


def testButtonPos():
    btn = Button(text="Test")
    assert btn.rect.x == btn.rect.y == 0
