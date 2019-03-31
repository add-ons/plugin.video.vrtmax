# -*- coding: utf-8 -*-

# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, unicode_literals
from datetime import datetime
import dateutil.tz

from resources.lib.vrtplayer import CHANNELS


class MetadataCreator:

    def __init__(self):
        self._brands = None
        self._datetime = None
        self._duration = None
        self._episode = None
        self._genre = None
        self._geolocked = None
        self._icon = None
        self._mediatype = None
        self._offtime = None
        self._ontime = None
        self._pageid = None
        self._permalink = None
        self._plot = None
        self._plotoutline = None
        self._score = None
        self._season = None
        self._subtitle = None
        self._title = None
        self._tvshowtitle = None
        self._videoid = None
        self._year = None

    @property
    def brands(self):
        return self._brands

    @brands.setter
    def brands(self, value):
        self._brands = value

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value):
        self._datetime = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def episode(self):
        return self._episode

    @episode.setter
    def episode(self, value):
        self._episode = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def geolocked(self):
        return self._geolocked

    @geolocked.setter
    def geolocked(self, value):
        self._geolocked = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value

    @property
    def mediatype(self):
        return self._mediatype

    @mediatype.setter
    def mediatype(self, value):
        self._mediatype = value

    @property
    def offtime(self):
        return self._offtime

    @offtime.setter
    def offtime(self, value):
        self._offtime = value

    @property
    def ontime(self):
        return self._ontime

    @ontime.setter
    def ontime(self, value):
        self._ontime = value

    @property
    def pageid(self):
        return self._pageid

    @pageid.setter
    def pageid(self, value):
        self._pageid = value

    @property
    def permalink(self):
        return self._permalink

    @permalink.setter
    def permalink(self, value):
        self._permalink = value

    @property
    def plot(self):
        return self._plot

    @plot.setter
    def plot(self, value):
        self._plot = value.strip()

    @property
    def plotoutline(self):
        return self._plotoutline

    @plotoutline.setter
    def plotoutline(self, value):
        self._plotoutline = value.strip()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def season(self):
        return self._season

    @season.setter
    def season(self, value):
        self._season = value

    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def tvshowtitle(self):
        return self._tvshowtitle

    @tvshowtitle.setter
    def tvshowtitle(self, value):
        self._tvshowtitle = value

    @property
    def videoid(self):
        return self._videoid

    @videoid.setter
    def videoid(self, value):
        self._videoid = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    def get_video_dict(self):
        epoch = datetime.fromtimestamp(0, dateutil.tz.UTC)
        video_dict = dict()

        if self.brands:
            video_dict['studio'] = CHANNELS.get(self.brands[0], {'studio': 'VRT'}).get('studio')
        else:
            video_dict['studio'] = 'VRT'

        if self.datetime:
            video_dict['aired'] = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
            video_dict['date'] = self.datetime.strftime('%Y-%m-%d')
        elif self.ontime and self.ontime != epoch:
            video_dict['aired'] = self.ontime.strftime('%Y-%m-%d %H:%M:%S')
            video_dict['date'] = self.ontime.strftime('%Y-%m-%d')

        if self.ontime and self.ontime != epoch:
            video_dict['dateadded'] = self.ontime.strftime('%Y-%m-%d %H:%M:%S')
#            video_dict['startdate'] = self.ontime.strftime('%Y-%m-%d %H:%M:%S')
        elif self.datetime:
            video_dict['dateadded'] = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
#            video_dict['startdate'] = self.datetime.strftime('%Y-%m-%d %H:%M:%S')

#        if self.offtime and self.offtime != epoch:
#            video_dict['enddate'] = self.offtime.strftime('%Y-%m-%d %H:%M:%S')
#        elif self.ontime and self.ontime != epoch:
#            video_dict['enddate'] = self.ontime.strftime('%Y-%m-%d %H:%M:%S')
#        elif self.datetime:
#            video_dict['enddate'] = self.datetime.strftime('%Y-%m-%d %H:%M:%S')

        if self.duration:
            video_dict['duration'] = self.duration

        if self.episode:
            video_dict['episode'] = self.episode

        if self.genre:
            video_dict['genre'] = self.genre
            video_dict['tag'] = self.genre

        # NOTE: Does not seem to have any effect
        if self.geolocked:
            video_dict['overlay'] = 3
            # video_dict['overlay'] = 'OverlayLocked.png'
        else:
            video_dict['overlay'] = 3

        # NOTE: Does not seem to have any effect
        if self.icon:
            video_dict['icon'] = self.icon
            video_dict['actualicon'] = self.icon

        if self.mediatype:
            video_dict['mediatype'] = self.mediatype

        if self.permalink:
            video_dict['path'] = self.permalink
            video_dict['showlink'] = [self.permalink]

        if self.plot:
            video_dict['plot'] = self.plot

        if self.plotoutline:
            video_dict['plotoutline'] = self.plotoutline
            video_dict['tagline'] = self.plotoutline

        if self.score:
            video_dict['rating'] = self.score

        if self.season:
            video_dict['season'] = self.season

        # NOTE: Does not seem to have any effect
        if self.subtitle:
            video_dict['tagline'] = self.subtitle

        if self.title:
            video_dict['title'] = self.title

        if self.tvshowtitle:
            video_dict['tvshowtitle'] = self.tvshowtitle
            video_dict['set'] = self.tvshowtitle

        if self.videoid:
            video_dict['videoid'] = self.videoid

        if self.year:
            video_dict['year'] = self.year

        return video_dict
