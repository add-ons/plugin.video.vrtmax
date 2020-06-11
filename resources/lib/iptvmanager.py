# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Implementation of IPTVManager class"""

from __future__ import absolute_import, division, unicode_literals

from data import CHANNELS
from kodiutils import log


class IPTVManager:
    """Interface to IPTV Manager"""

    def __init__(self, port):
        """Initialize IPTV Manager object"""
        self.port = port

    def via_socket(func):  # pylint: disable=no-self-argument
        """Send the output of the wrapped function to socket"""

        def send(self):
            """Decorator to send over a socket"""
            import json
            import socket
            log(2, "Sending data output to IPTV Manager using port {port}", port=self.port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.1', self.port))
            try:
                sock.send(json.dumps(func()).encode())  # pylint: disable=not-callable
            finally:
                sock.close()

        return send

    @via_socket
    def send_channels():  # pylint: disable=no-method-argument
        """Return JSON-M3U formatted information to IPTV Manager"""
        streams = []
        for channel in CHANNELS:
            if not channel.get('live_stream_id'):
                continue
            item = dict(
                id=channel.get('epg_id'),
                name=channel.get('label'),
                logo=channel.get('logo'),
                preset=channel.get('preset'),
                stream='plugin://plugin.video.vrt.nu/play/id/{live_stream_id}'.format(**channel),
            )
            if channel.get('has_tvguide'):
                item.update(dict(vod='plugin://plugin.video.vrt.nu/play/airdate/{name}/{{start}}/{{stop}}'.format(**channel)))

            streams.append(item)
        return dict(version=1, streams=streams)

    @via_socket
    def send_epg():  # pylint: disable=no-method-argument
        """Return JSONTV formatted information to IPTV Manager"""
        from tvguide import TVGuide
        epg_data = TVGuide().get_epg_data()
        return dict(version=1, epg=epg_data)
