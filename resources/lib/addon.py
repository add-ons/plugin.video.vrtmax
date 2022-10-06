# -*- coding: utf-8 -*-
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""This is the actual VRT MAX video plugin entry point"""

from __future__ import absolute_import, division, unicode_literals
from routing import Plugin

try:  # Python 3
    from urllib.parse import unquote_plus
except ImportError:  # Python 2
    from urllib import unquote_plus

from kodiutils import end_of_directory, execute_builtin, get_global_setting, localize, log_access, notification, ok_dialog, refresh_caches
from utils import from_unicode, to_unicode

plugin = Plugin()  # pylint: disable=invalid-name


@plugin.route('/')
def main_menu():
    """The VRT MAX plugin main menu"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_main_menu()


@plugin.route('/noop')
def noop():
    """The API interface to do nothing"""
    end_of_directory()


@plugin.route('/cache/delete')
@plugin.route('/cache/delete/<cache_file>')
def delete_cache(cache_file='*.json'):
    """The API interface to delete caches"""
    refresh_caches(cache_file=cache_file)


@plugin.route('/tokens/delete')
def delete_tokens():
    """The API interface to delete all VRT tokens"""
    from tokenresolver import TokenResolver
    TokenResolver().delete_tokens()


@plugin.route('/follow/<program_name>/<title>')
@plugin.route('/follow/<program_name>/<program_id>/<title>')
def follow(program_name, title, program_id=None):
    """The API interface to follow a program used by the context menu"""
    from favorites import Favorites
    Favorites().follow(program_name=program_name, title=to_unicode(unquote_plus(from_unicode(title))), program_id=program_id)


@plugin.route('/unfollow/<program_name>/<title>')
@plugin.route('/unfollow/<program_name>/<program_id>/<title>')
def unfollow(program_name, title, program_id=None):
    """The API interface to unfollow a program used by the context menu"""
    move_down = bool(plugin.args.get('move_down'))
    from favorites import Favorites
    Favorites().unfollow(program_name=program_name, title=to_unicode(unquote_plus(from_unicode(title))), program_id=program_id, move_down=move_down)


@plugin.route('/favorites')
def favorites_menu():
    """The My favorites menu"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_favorites_menu()


@plugin.route('/favorites/programs')
@plugin.route('/favorites/programs/<end_cursor>')
def favorites_programs(end_cursor=''):
    """The favorites 'My programs' listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_tvshow_menu(end_cursor=end_cursor, use_favorites=True)


@plugin.route('/favorites/docu')
def favorites_docu():
    """The favorites docu listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_favorites_docu_menu()


@plugin.route('/favorites/music')
def favorites_music():
    """The favorites music listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_favorites_music_menu()


@plugin.route('/favorites/recent')
@plugin.route('/favorites/recent')
@plugin.route('/favorites/recent/<end_cursor>')
def favorites_recent(end_cursor=''):
    """The favorites recent listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_recent_menu(end_cursor=end_cursor, use_favorites=True)


@plugin.route('/favorites/offline')
@plugin.route('/favorites/offline/<page>')
def favorites_offline(page=1):
    """The favorites offline listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_offline_menu(page=page, use_favorites=True)


@plugin.route('/favorites/refresh')
def favorites_refresh():
    """The API interface to refresh the favorites cache"""
    from favorites import Favorites
    Favorites().refresh(ttl=0)
    notification(message=localize(30982))


@plugin.route('/favorites/manage')
def favorites_manage():
    """The API interface to manage your favorites"""
    from favorites import Favorites
    Favorites().manage()


@plugin.route('/resumepoints/continue')
@plugin.route('/resumepoints/continue/<end_cursor>')
def resumepoints_continue(end_cursor=''):
    """The resumepoints continue listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_continue_menu(end_cursor=end_cursor)


@plugin.route('/resumepoints/refresh')
def resumepoints_refresh():
    """The API interface to refresh the resumepoints cache"""
    from resumepoints import ResumePoints
    ResumePoints().refresh(ttl=0)
    notification(message=localize(30983))


@plugin.route('/programs')
@plugin.route('/programs/<program_name>')
@plugin.route('/programs/<program_name>/<season_name>')
def programs(program_name=None, season_name=None):
    """The Programs / Seasons / Episodes listing"""
    from vrtplayer import VRTPlayer
    if program_name:
        VRTPlayer().show_episodes_menu(program_name=program_name, season_name=season_name)
    else:
        VRTPlayer().show_tvshow_menu()


@plugin.route('/categories')
@plugin.route('/categories/<category>')
def categories(category=None):
    """The categories menu and listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_category_menu(category=category)


@plugin.route('/channels')
@plugin.route('/channels/<channel>')
@plugin.route('/channels/<channel>/<end_cursor>')
def channels(channel=None, end_cursor=''):
    """The channels menu and listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_channels_menu(channel=channel, end_cursor=end_cursor)


@plugin.route('/livetv')
def livetv():
    """The livetv menu"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_livetv_menu()


@plugin.route('/recent')
@plugin.route('/recent/<end_cursor>')
def recent(end_cursor=''):
    """The most recent items listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_recent_menu(end_cursor=end_cursor)


@plugin.route('/offline')
@plugin.route('/offline/<page>')
def offline(page=1):
    """The soon offline listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_offline_menu(page=page)


@plugin.route('/featured')
@plugin.route('/featured/<feature>')
def featured(feature=None):
    """The featured menu and listing"""
    from vrtplayer import VRTPlayer
    VRTPlayer().show_featured_menu(feature=feature)


@plugin.route('/tvguide')
@plugin.route('/tvguide/date')
@plugin.route('/tvguide/date/<date>')
@plugin.route('/tvguide/date/<date>/<channel>')
def tvguide(date=None, channel=None):
    """The TV guide menu and listings by date"""
    from tvguide import TVGuide
    TVGuide().show_tvguide(date=date, channel=channel)


@plugin.route('/tvguide/channel')
@plugin.route('/tvguide/channel/<channel>')
@plugin.route('/tvguide/channel/<channel>/<date>')
def tvguide_channel(channel=None, date=None):
    """The TV guide menu and listings by channel"""
    from tvguide import TVGuide
    TVGuide().show_tvguide(channel=channel, date=date)


@plugin.route('/search')
def search():
    """The Search menu and history"""
    from search import Search
    Search().search_menu()


@plugin.route('/search/clear')
def clear_search():
    """Clear the search history"""
    from search import Search
    Search().clear()


@plugin.route('/search/add/<keywords>')
def add_search(keywords):
    """Add to search history"""
    from search import Search
    Search().add(keywords)


@plugin.route('/search/edit')
@plugin.route('/search/edit/<keywords>')
def edit_search(keywords=None):
    """Edit from search history"""
    from search import Search
    Search().search(keywords=keywords, edit=True)


@plugin.route('/search/query')
@plugin.route('/search/query/<keywords>')
@plugin.route('/search/query/<keywords>/<page>')
def search_query(keywords=None, page=1):
    """The Search interface and query listing"""
    from search import Search
    Search().search(keywords=keywords, page=page)


@plugin.route('/search/remove/<keywords>')
def remove_search(keywords):
    """Remove from search history"""
    from search import Search
    Search().remove(keywords)


@plugin.route('/play/id/<video_id>')
@plugin.route('/play/id/<video_id>/<publication_id>')
def play_id(video_id, publication_id=None):
    """The API interface to play a video by video_id and/or publication_id"""
    from vrtplayer import VRTPlayer
    VRTPlayer().play(dict(video_id=video_id, publication_id=publication_id))


@plugin.route('/play/latest/<program_name>')
def play_latest(program_name):
    """The API interface to play the latest episode of a program"""
    from vrtplayer import VRTPlayer
    VRTPlayer().play_latest_episode(program_name=program_name)


@plugin.route('/play/upnext/<episode_id>')
def play_upnext(episode_id):
    """The API interface to play the next episode of a program"""
    from vrtplayer import VRTPlayer
    VRTPlayer().play_upnext(episode_id=episode_id)


@plugin.route('/play/airdate/<channel>/<start_date>')
@plugin.route('/play/airdate/<channel>/<start_date>/<end_date>')
def play_air_date(channel, start_date, end_date=None):
    """The API interface to play an episode of a program given the channel, start (and end) timestamp(s) in ISO 8601 format (e.g. 2020-06-15T10:35:00)"""
    from vrtplayer import VRTPlayer
    VRTPlayer().play_episode_by_air_date(channel, start_date, end_date)


@plugin.route('/play/episode/<episode_id>')
def play_episode_id(episode_id):
    """The API interface to play a video by using a episodeId"""
    from vrtplayer import VRTPlayer
    VRTPlayer().play_episode_by_episode_id(episode_id=episode_id)


@plugin.route('/iptv/channels')
def iptv_channels():
    """Return JSON-M3U formatted data for all live channels"""
    from iptvmanager import IPTVManager
    port = int(plugin.args.get('port')[0])
    IPTVManager(port).send_channels()


@plugin.route('/iptv/epg')
def iptv_epg():
    """Return JSONTV formatted data for all live channel EPG data"""
    from iptvmanager import IPTVManager
    port = int(plugin.args.get('port')[0])
    IPTVManager(port).send_epg()


@plugin.route('/update/repos')
def update_repos():
    """Force an update of the repositories"""
    if get_global_setting('general.addonupdates') == 0:  # Automatic updates is enabled
        execute_builtin('UpdateAddonRepos')
        ok_dialog(heading=localize(30450), message=localize(30451))  # Repositories are being updated
    else:
        ok_dialog(heading=localize(30452), message=localize(30453))  # Automatic updates is disabled
        show_settings_addons()


@plugin.route('/show/settings/addons')
def show_settings_addons():
    """Open the Kodi System Settings in the Add-ons category"""
    execute_builtin('ActivateWindow(SystemSettings,addons)')


def run(argv):
    """Addon entry point from wrapper"""
    log_access(argv)
    plugin.run(argv)
