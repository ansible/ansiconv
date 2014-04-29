import ansiconv 


def test_basic_to_plain():
    expected = 'Foo'
    actual = ansiconv.to_plain('\033[0;32mFoo')
    assert actual == expected


def test_basic_to_html():
    expected = '<span class="ansi32">Foo</span>'
    actual = ansiconv.to_html('\033[0;32mFoo')
    assert actual == expected


def test_basic_to_html_replace_newline():
    expected = '<span class="ansi32">Foo<br />\nBar</span>'
    actual = ansiconv.to_html('\033[0;32mFoo\nBar', replace_newline=True)
    assert actual == expected


def test_to_html_with_multiple_color_changes():
    expected = '<span class="ansi32">Foo</span><span class="ansi31">Bar</span>'
    actual = ansiconv.to_html('\033[0;32mFoo\033[0;31mBar')
    assert actual == expected


def test_to_html_with_cursor_up_command():
    expected = '<span class="ansi34">Foo</span>'
    actual = ansiconv.to_html('\033[0;30mFoo\n\033[A\033[0;34mFoo')
    assert actual == expected


def test_block_with_single_color_code_to_html():
    expected = ('m', '<span class="ansi31">Foo</span>')
    actual = ansiconv._block_to_html('[0;31mFoo')
    assert actual == expected


def test_block_with_multiple_codes_to_html():
    expected = ('m', '<span class="ansi1 ansi33">Foo</span>')
    actual = ansiconv._block_to_html('[1;33mFoo')
    assert actual == expected


def test_block_with_cursor_up_code_to_html():
    expected = ('A', '')
    actual = ansiconv._block_to_html('[A')
    assert actual == expected


def test_css_rule():
    expected = '.foo { color: #000000; }'
    actual = ansiconv.css_rule('.foo', color="#000000")
    assert expected == actual


def test_base_css_dark():
    expected = """
.ansi_fore { color: #FFFFFF; }
.ansi_back { background-color: #000000; }
.ansi1 { font-weight: bold; }
.ansi3 { font-weight: italic; }
.ansi4 { text-decoration: underline; }
.ansi9 { text-decoration: line-through; }
.ansi30 { color: #000000; }
.ansi31 { color: #FF0000; }
.ansi32 { color: #00FF00; }
.ansi33 { color: #FFFF00; }
.ansi34 { color: #0000FF; }
.ansi35 { color: #FF00FF; }
.ansi36 { color: #00FFFF; }
.ansi37 { color: #FFFFFF; }
.ansi40 { background-color: #000000; }
.ansi41 { background-color: #FF0000; }
.ansi42 { background-color: #00FF00; }
.ansi43 { background-color: #FFFF00; }
.ansi44 { background-color: #0000FF; }
.ansi45 { background-color: #FF00FF; }
.ansi46 { background-color: #00FFFF; }
.ansi47 { background-color: #FFFFFF; }
.ansi90 { color: #000000; }
.ansi91 { color: #FF0000; }
.ansi92 { color: #00FF00; }
.ansi93 { color: #FFFF00; }
.ansi94 { color: #0000FF; }
.ansi95 { color: #FF00FF; }
.ansi96 { color: #00FFFF; }
.ansi97 { color: #FFFFFF; }
""".strip()
    actual = ansiconv.base_css()
    assert expected == actual


def test_base_css_light():
    expected = """
.ansi_fore { color: #000000; }
.ansi_back { background-color: #FFFFFF; }
.ansi1 { font-weight: bold; }
.ansi3 { font-weight: italic; }
.ansi4 { text-decoration: underline; }
.ansi9 { text-decoration: line-through; }
.ansi30 { color: #000000; }
.ansi31 { color: #FF0000; }
.ansi32 { color: #00FF00; }
.ansi33 { color: #FFFF00; }
.ansi34 { color: #0000FF; }
.ansi35 { color: #FF00FF; }
.ansi36 { color: #00FFFF; }
.ansi37 { color: #FFFFFF; }
.ansi40 { background-color: #000000; }
.ansi41 { background-color: #FF0000; }
.ansi42 { background-color: #00FF00; }
.ansi43 { background-color: #FFFF00; }
.ansi44 { background-color: #0000FF; }
.ansi45 { background-color: #FF00FF; }
.ansi46 { background-color: #00FFFF; }
.ansi47 { background-color: #FFFFFF; }
.ansi90 { color: #000000; }
.ansi91 { color: #FF0000; }
.ansi92 { color: #00FF00; }
.ansi93 { color: #FFFF00; }
.ansi94 { color: #0000FF; }
.ansi95 { color: #FF00FF; }
.ansi96 { color: #00FFFF; }
.ansi97 { color: #FFFFFF; }
""".strip()
    actual = ansiconv.base_css(dark=False)
    assert expected == actual