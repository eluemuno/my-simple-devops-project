from app import app

def testHome():
    expResponse = app.test_client().get('/')
    assert expResponse.status_code == 200

def testEdit():
    expResponse = app.test_client().get('/edit')
    assert expResponse.status_code == 200

def testContenct():
    expResponse = app.test_client().get('/edit')
    assert b"Todo App" in expResponse.data
    assert b"Todo Title" in expResponse.data
    assert b"Add" in expResponse.data