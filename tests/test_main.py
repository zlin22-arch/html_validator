import HTML_Validator


def test__extract_tags_1():
    assert HTML_Validator._extract_tags('') == []

def test__extract_tags_2():
    assert HTML_Validator._extract_tags('python in fun') == []

def test__extract_tags_3():
    assert HTML_Validator._extract_tags('<strong></strong>') == ['<strong>','</strong>']

def test__extract_tags_4():
    assert HTML_Validator._extract_tags('python in <strong>fun</strong>') == ['<strong>','</strong>']

def test__extract_tags_5():
    assert HTML_Validator._extract_tags('<a><b><c></a></b><f>') == ['<a>','<b>','<c>','</a>','</b>','<f>']


def test_validate_html_1():
    assert HTML_Validator.validate_html('')

def test_validate_html_2():
    assert HTML_Validator.validate_html('<a></a>')

def test_validate_html_3():
    assert not HTML_Validator.validate_html('<a>')

def test_validate_html_4():
    assert not HTML_Validator.validate_html('</a>')

def test_validate_html_5():
    assert HTML_Validator.validate_html('<strong></strong><b></b>')

def test_validate_html_6():
    assert HTML_Validator.validate_html('<strong><b></b></strong>')

def test_validate_html_6():
    assert HTML_Validator.validate_html('<strong><strong></strong></strong>')

def test_validate_html_7():
    assert not HTML_Validator.validate_html('<strong><b></strong></b>')

def test_validate_html_8():
    assert HTML_Validator.validate_html('this is a test <emph>hello!</emph>')

def test_validate_html_9():
    assert HTML_Validator.validate_html('''
    <html>
    <head>
    <title>This is an awesome webpage!</title>
    </head>
    <body>
    <p>Programming is the <strong>best</strong>!</p>
    </body>
    </html>
    ''')

def test_validate_html_10():
    assert not HTML_Validator.validate_html('''
    <html>
    <head>
    <title>This is an awesome webpage!</title>
    </head>
    <body>
    <p>Programming is the <strong>best</strong>!
    </body>
    </html>
    ''')

#def test_validate_html_1():
    #assert not HTML_Validator.validate_html('<')

