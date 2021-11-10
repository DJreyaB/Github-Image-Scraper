from imagescraper.github_images import image_url_retrieval
import pytest

def test_image_url_retrieval_affirm():
    url = "https://github.com/DJreyaB"
    assert image_url_retrieval(url) == "https://avatars.githubusercontent.com/u/37115281?v=4"

def test_image_url_retrieval_negative():
    url = "https://github.com/DJreya"
    with pytest.raises(TypeError) as e:
        assert image_url_retrieval(url) == e.value