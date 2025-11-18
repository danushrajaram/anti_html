from anti_html import strip_html_tags

def test_strip_html():
    html = "<h1>Hello</h1><p>World</p>"
    assert strip_html_tags(html) == "Hello World"
