# -*- coding: utf-8 -*-

# GNU General Public License v2.0 (see COPYING or https://www.gnu.org/licenses/gpl-2.0.txt)

import unittest
from resources.lib.vrtplayer import vrtapihelper
from mock import MagicMock


class ApiHelperTests(unittest.TestCase):

    def test_get_api_data_single_season(self):
        mock = MagicMock()
        mock.get_localized_string.return_value = 'vrttest'
        api_helper = vrtapihelper.VRTApiHelper(mock)
        title_items, sort = api_helper.get_episode_items('/vrtnu/a-z/piet-piraat.relevant/')
        self.assertEqual(7, len(title_items))

    def test_get_api_data_multiple_seasons(self):
        mock = MagicMock()
        mock.get_localized_string.return_value = 'vrttest'
        api_helper = vrtapihelper.VRTApiHelper(mock)
        title_items, sort = api_helper.get_episode_items('/vrtnu/a-z/thuis.relevant/')
        self.assertTrue(len(title_items) < 5)

    def test_get_api_data_specific_season(self):
        mock = MagicMock()
        mock.get_localized_string.return_value = 'vrttest'
        api_helper = vrtapihelper.VRTApiHelper(mock)
        title_items, sort = api_helper.get_episode_items('/vrtnu/a-z/thuis.relevant/')
        self.assertTrue(len(title_items) == 2)

    def test_get_api_data_specific_season_without_broadcastdate(self):
        mock = MagicMock()
        mock.get_localized_string.return_value = 'vrttest'
        api_helper = vrtapihelper.VRTApiHelper(mock)
        title_items, sort = api_helper.get_episode_items('/vrtnu/a-z/postbus-x.relevant/')       
        self.assertTrue(len(title_items) == 3)


if __name__ == '__main__':
    unittest.main()
