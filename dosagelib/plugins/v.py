# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre


class VampireCheerleaders(_BasicScraper):
    url = 'http://www.vampirecheerleaders.net/'
    stripUrl = url + 'strips-vc/%s'
    firstStripUrl = stripUrl % 'fang_service'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.vampirecheerleaders\.net/strips-vc/[^"]+)', before="cndprev"))
    help = 'Index format: name'


class Vendetta(_BasicScraper):
    url = 'http://www.vendettacomic.com/'
    stripUrl = url + 'archive.php?date=%s.jpg'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(archive\.php\?date=\d+\.jpg)') +
      tagre("img", "src", r"/images/prev\.jpg"))
    help = 'Index format: yyyymmdd'


class VGCats(_BasicScraper):
    url = 'http://www.vgcats.com/comics/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(images/\d{6}\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') +
      tagre("img", "src", r"back\.gif"))
    help = 'Index format: n (unpadded)'


class VGCatsSuper(VGCats):
    name = 'VGCats/Super'
    url = 'http://www.vgcats.com/super/'
    stripUrl = url + '?strip_id=%s'


class VGCatsAdventure(VGCats):
    name = 'VGCats/Adventure'
    url = 'http://www.vgcats.com/ffxi/'
    stripUrl = url + '?strip_id=%s'


class VictimsOfTheSystem(_BasicScraper):
    url = 'http://www.votscomic.com/'
    stripUrl = url + '?id=%s.jpg'
    firstStripUrl = stripUrl % '070103-002452'
    imageSearch = compile(tagre("img", "src", r'(comicpro/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?id=\d+-\d+\.jpg)') + "Previous")
    help = 'Index format: nnn-nnn'


class ViiviJaWagner(_BasicScraper):
    url = 'http://www.hs.fi/viivijawagner/'
    stripUrl = None
    imageSearch = compile(tagre("link", "href", r'(http://hs\d+\.snstatic\.fi/webkuva/oletus/[^"]+)', before="image_src"))
    prevSearch = compile(tagre("a", "href", r'(/viivijawagner/[^"]+)', before="prev-cm"))
    help = 'Index format: none'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('=')[1]
