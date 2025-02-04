import pytest
from bs4 import BeautifulSoup

# Load the HTML file
@pytest.fixture
def load_html():
    with open("index.html", "r", encoding="utf-8") as file:
        return BeautifulSoup(file, "html.parser")

def test_charset(load_html):
    """Check if UTF-8 encoding is specified"""
    meta_tag = load_html.find("meta", {"charset": "UTF-8"})
    assert meta_tag, "UTF-8 charset is not set"

def test_language(load_html):
    """Check if the language is set to Hungarian (hu)"""
    html_tag = load_html.find("html")
    assert html_tag and html_tag.get("lang") == "hu", "Language is not set to Hungarian"

def test_title(load_html):
    """Check if the title is 'Háttér'"""
    title_tag = load_html.find("title")
    assert title_tag and title_tag.text.strip() == "Háttér", "Title is incorrect"

def test_h2_exists(load_html):
    """Check if there is an <h2> with 'Lorem ipsum'"""
    h2_tag = load_html.find("h2")
    assert h2_tag and h2_tag.text.strip() == "Lorem ipsum", "Missing or incorrect <h2> tag"

def test_background_image(load_html):
    """Check if the background image is set with correct size and position"""
    style_tag = load_html.find("style")
    assert style_tag, "No <style> tag found"
    
    css = style_tag.text
    assert "background-image" in css, "No background image set"
    assert "background-size: 220px" in css, "Background width is incorrect"
    assert "background-position: top right" in css, "Background position is incorrect"

