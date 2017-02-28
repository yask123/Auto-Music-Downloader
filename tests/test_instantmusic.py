"""test module."""
from itertools import product
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
        ('http://www.metrolyrics.com', 'htt'),
    ]
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


@pytest.mark.parametrize(
    "search_result, is_quiet, has_prompts",
    product(
        [[], mock.Mock()],
        [True, False],
        [True, False],
    )
)
def test_print_video_search_result(search_result, is_quiet, has_prompts):
    """test func."""
    movie_list = ['movie1']
    with mock.patch(
            'instantmusic.instantmusic.list_movies', return_value=movie_list):
        from instantmusic import instantmusic
        if not is_quiet and not search_result:
            with pytest.raises(SystemExit):
                instantmusic.print_video_search_result(
                    search_result, is_quiet, has_prompts)
            return
        instantmusic.print_video_search_result(
            search_result, is_quiet, has_prompts)


@pytest.mark.parametrize(
    'has_prompts, is_quiet', product([True, False], repeat=2))
def test_query_and_download(has_prompts, is_quiet):
    """test func."""
    search = mock.Mock()
    search_video_func_path = 'instantmusic.instantmusic.search_videos'
    print_vsr_path = 'instantmusic.instantmusic.print_video_search_result'
    fix_id3t_path = 'instantmusic.instantmusic.fix_id3_tags'
    pick_fsr = 'instantmusic.instantmusic.pick_from_search_result'
    title = mock.Mock()
    video_link = 'video_link'
    video_title = 'video_title'
    movie_list = [(video_title, video_link)]
    with mock.patch(search_video_func_path, return_value=movie_list),\
            mock.patch(print_vsr_path),\
            mock.patch(pick_fsr, return_value=movie_list[0]) as m_pfsr,\
            mock.patch(fix_id3t_path, return_value=title),\
            mock.patch('instantmusic.instantmusic.os') as m_os:
        from instantmusic import instantmusic
        # test
        res = instantmusic.query_and_download(search, has_prompts, is_quiet)
        # run
        assert res == title
        if has_prompts and not is_quiet:
            m_pfsr.assert_called_once_with(search_result=movie_list)
        command_tokens = [
            'youtube-dl',
            '--extract-audio',
            '--audio-format mp3',
            '--audio-quality 0',
            '--output \'%(title)s.%(ext)s\'',
            'https://www.youtube.com{}'.format(video_link),
        ]
        if is_quiet:
            command_tokens.insert(1, '-q')
        m_os.system.assert_called_once_with(' '.join(command_tokens))


@pytest.mark.parametrize(
    'argstring, flags, exp_res',
    [
        ('-s -p -i', ['-s'], False),
        ('-s -p -i', ['-t'], True),
    ]
)
def test_search_uses_flags(argstring, flags, exp_res):
    """test func."""
    from instantmusic import instantmusic
    assert exp_res == instantmusic.search_uses_flags(argstring, *flags)
