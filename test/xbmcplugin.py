# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
''' This file implements the Kodi xbmcplugin module, either using stubs or alternative functionality '''

from __future__ import absolute_import, division, print_function, unicode_literals
from xbmcextra import kodi_to_ansi, uri_to_path

SORT_METHOD_NONE = 0
SORT_METHOD_LABEL = 1
SORT_METHOD_LABEL_IGNORE_THE = 2
SORT_METHOD_DATE = 3
SORT_METHOD_SIZE = 4
SORT_METHOD_FILE = 5
SORT_METHOD_DURATION = 8
SORT_METHOD_TITLE = 9
SORT_METHOD_TITLE_IGNORE_THE = 10
SORT_METHOD_GENRE = 16
SORT_METHOD_COUNTRY = 17
SORT_METHOD_DATEADDED = 21
SORT_METHOD_PROGRAM_COUNT = 22
SORT_METHOD_EPISODE = 24
SORT_METHOD_VIDEO_TITLE = 25
SORT_METHOD_VIDEO_SORT_TITLE = 26
SORT_METHOD_VIDEO_SORT_TITLE_IGNORE_THE = 27
SORT_METHOD_STUDIO = 33
SORT_METHOD_STUDIO_IGNORE_THE = 34
SORT_METHOD_FULLPATH = 35
SORT_METHOD_LASTPLAYED = 37
SORT_METHOD_PLAYCOUNT = 38
SORT_METHOD_UNSORTED = 40
SORT_METHOD_CHANNEL = 41
SORT_METHOD_BITRATE = 43
SORT_METHOD_DATE_TAKEN = 44


def addDirectoryItems(handle, listing, length):
    ''' A reimplementation of the xbmcplugin addDirectoryItems() function '''
    for item in listing:
        label = kodi_to_ansi(item[1].label)
        path = uri_to_path(item[0])
        # perma = kodi_to_ansi(item[1].label)  # FIXME: Add permalink
        if item[2]:
            print('» %s%s' % (label, path if path else ''))
        else:
            print('· %s%s' % (label, path if path else ''))
    return True


def addSortMethod(handle, sortMethod):
    ''' A stub implementation of the xbmcplugin addSortMethod() function '''
    return


def endOfDirectory(handle, succeeded=True, updateListing=True, cacheToDisc=True):
    ''' A stub implementation of the xbmcplugin endOfDirectory() function '''
    return


def setContent(handle, content):
    ''' A stub implementation of the xbmcplugin setContent() function '''
    return


def setPluginFanart(handle, image, color1=None, color2=None, color3=None):
    ''' A stub implementation of the xbmcplugin setCategoryt() function '''
    return


def setPluginCategory(handle, category):
    ''' A reimplementation of the xbmcplugin setPluginCategory() function '''
    print(kodi_to_ansi('[B]** %s **[/B]' % category))


def setResolvedUrl(handle, succeeded, listitem):
    ''' A stub implementation of the xbmcplugin setResolvedUrl() function '''
    return
