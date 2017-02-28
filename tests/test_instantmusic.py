"""test module."""
try:  # py3
    from unittest import mock
except ImportError:  # py2
    import mock

import pytest


def test_extract_videos():
    """test func."""
    html = mock.Mock()
    soup = mock.Mock()
    link_tag = mock.Mock()
    link_tag.text = 'link_text'
    link_tag.get.return_value = 'link_href'
    soup.find_all.return_value = [link_tag]
    with mock.patch(
            'instantmusic.instantmusic.BeautifulSoup', return_value=soup):
        from instantmusic import instantmusic
        res = instantmusic.extract_videos(html)
        assert res == [(b'link_text', 'link_href')]


def test_make_request():
    """test func."""
    req = mock.Mock()
    url = mock.Mock()
    hdr = mock.Mock()
    with mock.patch('instantmusic.instantmusic.requests') as m_req:
        m_req.get.return_value = req
        from instantmusic import instantmusic
        res = instantmusic.make_request(url=url, hdr=hdr)
        assert res == req


def test_grab_albumart():
    """test func."""
    req = mock.Mock()
    req.content = 'http://example.com/album_art.jpg'
    search = 'search_text'
    with mock.patch(
            'instantmusic.instantmusic.make_request', return_value=req), \
            mock.patch('instantmusic.instantmusic.qp', return_value=search):
        from instantmusic import instantmusic
        res = instantmusic.grab_albumart(search=search)
        assert res == req.content


def test_list_movies():
    """test func."""
    title = b'title'
    movies = [(title, None)]
    from instantmusic import instantmusic
    res = list(instantmusic.list_movies(movies))
    assert res == ['[0] {}'.format(title.decode('utf8'))]


@pytest.mark.parametrize(
    'response, exp_res',
    [
        ('random_text', ''),
        ('https://www.metrolyrics.com', 'htt'),
        ('http://www.metrolyrics.com', 'htt'), ]
)
def test_get_lyrics_url(response, exp_res):
    """test func."""
    from instantmusic import instantmusic
    res = instantmusic.get_lyrics_url(response)
    assert res == exp_res


def test_search_video():
    """test func."""
    query = 'query'
    response = mock.Mock()
    videos = mock.Mock()
    with mock.patch(
            'instantmusic.instantmusic.make_request', return_value=response),\
            mock.patch(
                'instantmusic.instantmusic.extract_videos',
                return_value=videos):
        from instantmusic import instantmusic
        res = instantmusic.search_videos(query)
        assert res == videos
