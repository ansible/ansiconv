import ansiconv 

def test_basic_to_plain():
    assert ansiconv.to_plain('\033[0;32mFoo') == 'Foo'

def test_basic_to_html():
    assert ansiconv.to_html('\033[0;32mFoo') == '<span class="ansi32">Foo</span>'
