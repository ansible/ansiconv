import ansiconv 


def test_basic_to_plain():
    expected = 'Foo'
    actual = ansiconv.to_plain('\033[0;32mFoo')
    assert actual == expected


def test_basic_to_html():
    expected = '<span class="ansi32">Foo</span>'
    actual = ansiconv.to_html('\033[0;32mFoo')
    assert actual == expected


def test_css_rule():
    expected = '.foo { color: #000000; }'
    actual = ansiconv.css_rule('.foo', color="#000000")
    assert expected == actual