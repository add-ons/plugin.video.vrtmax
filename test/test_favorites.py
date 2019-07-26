# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# pylint: disable=missing-docstring

from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
from addon import kodi
from apihelper import ApiHelper
from favorites import Favorites

xbmc = __import__('xbmc')
xbmcaddon = __import__('xbmcaddon')
xbmcgui = __import__('xbmcgui')
xbmcplugin = __import__('xbmcplugin')
xbmcvfs = __import__('xbmcvfs')

xbmcaddon.ADDON_SETTINGS['usefavorites'] = 'true'


class TestFavorites(unittest.TestCase):

    _favorites = Favorites(kodi)
    _apihelper = ApiHelper(kodi, _favorites)

    def test_get_recent_episodes(self):
        ''' Test items, sort and order '''
        episode_items, sort, ascending, content = self._apihelper.list_episodes(page=1, variety='recent')
        self.assertEqual(len(episode_items), 50)
        self.assertEqual(sort, 'dateadded')
        self.assertFalse(ascending)
        self.assertEqual(content, 'episodes')

    def test_get_offline_episodes(self):
        ''' Test items, sort and order '''
        episode_items, sort, ascending, content = self._apihelper.list_episodes(page=1, variety='offline')
        self.assertTrue(episode_items)
        self.assertEqual(sort, 'dateadded')
        self.assertFalse(ascending)
        self.assertEqual(content, 'episodes')

    def test_follow_unfollow(self):
        programs = [
            {'program_title': 'Winteruur', 'program': 'winteruur'},
            {'program_title': 'De Campus Cup', 'program': 'de-campus-cup'},
            {'program_title': 'Terug naar Siberië', 'program': 'terug-naar-siberie'},
            {'program_title': '22/3 - 1 jaar later - het onderzoek', 'program': '22-3-1-jaar-later---het-onderzoek'},
            {'program_title': 'Belle & Sebastian', 'program': 'belle---sebastian'},
        ]
        for program_item in programs:
            program_title = program_item.get('program_title')
            program = program_item.get('program')
            self._favorites.follow(program=program, title=program_title)
            self.assertTrue(self._favorites.is_favorite(program))

            self._favorites.unfollow(program=program, title=program_title)
            self.assertFalse(self._favorites.is_favorite(program))

            self._favorites.follow(program=program, title=program_title)
            self.assertTrue(self._favorites.is_favorite(program))

    def test_programs(self):
        programs = self._favorites.programs()
        self.assertTrue(programs)
        print(programs)

    def test_titles(self):
        titles = self._favorites.titles()
        self.assertTrue(titles)
        print(sorted(titles))


if __name__ == '__main__':
    unittest.main()
