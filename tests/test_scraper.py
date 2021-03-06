# -*- coding: iso-8859-1 -*-
# Copyright (C) 2013 Bastian Kleineidam
from unittest import TestCase
from dosagelib import scraper


class ScraperTester(TestCase):
    """Test scraper module functions."""

    def test_get_scraperclasses(self):
        for scraperclass in scraper.get_scraperclasses():
            scraperclass()
            scraperclass(indexes=["bla"])

    def test_find_scraperclasses_single(self):
        result = scraper.find_scraperclasses("CalvinAndHobbes")
        self.assertEqual(len(result), 1)

    def test_find_scraperclasses_multi(self):
        result = scraper.find_scraperclasses("a", multiple_allowed=True)
        self.assertTrue(len(result) > 1)

    def test_find_scraperclasses_error(self):
        self.assertRaises(ValueError, scraper.find_scraperclasses, "")
