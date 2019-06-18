# -*- coding: utf-8 -*-

# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

''' A list of static data '''

from __future__ import absolute_import, division, unicode_literals

# Fallback list of categories so we don't depend on web scraping only
CATEGORIES = [
    dict(name='Audiodescriptie', id='met-audiodescriptie', msgctxt=''),
    dict(name='Cultuur', id='cultuur', msgctxt=''),
    dict(name='Docu', id='docu', msgctxt=''),
    dict(name='Entertainment', id='entertainment', msgctxt=''),
    dict(name='Films', id='films', msgctxt=''),
    dict(name='Human interest', id='human-interest', msgctxt=''),
    dict(name='Humor', id='humor', msgctxt=''),
    dict(name='Kinderen', id='voor-kinderen', msgctxt=''),
    dict(name='Koken', id='koken', msgctxt=''),
    dict(name='Lifestyle', id='lifestyle', msgctxt=''),
    dict(name='Muziek', id='muziek', msgctxt=''),
    dict(name='Nieuws en actua', id='nieuws-en-actua', msgctxt=''),
    dict(name='Series', id='series', msgctxt=''),
    dict(name='Sport', id='sport', msgctxt=''),
    dict(name='Talkshows', id='talkshows', msgctxt=''),
    dict(name='Vlaamse Gebarentaal', id='met-gebarentaal', msgctxt=''),
    dict(name='Wetenschap en natuur', id='wetenschap-en-natuur', msgctxt=''),
]

CHANNELS = [
    dict(
        id='O8',
        name='een',
        label='Eén',
        studio='Een',
        live_stream='https://www.vrt.be/vrtnu/kanalen/een/',
        live_stream_id='vualto_een_geo',
    ),
    dict(
        id='1H',
        name='canvas',
        label='Canvas',
        studio='Canvas',
        live_stream='https://www.vrt.be/vrtnu/kanalen/canvas/',
        live_stream_id='vualto_canvas_geo',
    ),
    dict(
        id='O9',
        name='ketnet',
        label='Ketnet',
        studio='Ketnet',
        live_stream='https://www.vrt.be/vrtnu/kanalen/ketnet/',
        live_stream_id='vualto_ketnet_geo',
    ),
    dict(
        id='1H',
        name='ketnet-jr',
        label='Ketnet Junior',
        studio='Ketnet Junior',
        live_stream_id='ketnet_jr',
    ),
    dict(
        id='12',
        name='sporza',
        label='Sporza',
        studio='Sporza',
        live_stream_id='vualto_sporza_geo',
    ),
    dict(
        id='13',
        name='vrtnws',
        label='VRT NWS',
        studio='VRT NWS',
        live_stream_id='vualto_nieuws',
        # live_stream_id='vualto_journaal',
    ),
    dict(
        id='11',
        name='radio1',
        label='Radio 1',
        studio='Radio 1',
    ),
    dict(
        id='24',
        name='radio2',
        label='Radio 2',
        studio='Radio 2',
    ),
    dict(
        id='31',
        name='klara',
        label='Klara',
        studio='Klara',
    ),
    dict(
        id='41',
        name='stubru',
        label='Studio Brussel',
        studio='Studio Brussel',
        # live_stream='https://stubru.be/live',
        live_stream_id='vualto_stubru',
    ),
    dict(
        id='55',
        name='mnm',
        label='MNM',
        studio='MNM',
        # live_stream='https://mnm.be/kijk/live',
        live_stream_id='vualto_mnm',
    ),
    dict(
        id='',
        name='vrtnxt',
        label='VRT NXT',
        studio='VRT NXT',
    ),
]

FEATURED = [
    # Tijdsgerelateerd
    dict(name='Exclusief online', id='exclusief-online', msgctxt=''),
    dict(name='Laatste aflevering', id='laatste-aflevering', msgctxt=''),
    dict(name='Laatste kans', id='laatste-kans', msgctxt=''),
    dict(name='Nieuw', id='Nieuw', msgctxt=''),
    dict(name='Volledige reeks', id='volledige-reeks', msgctxt=''),
    dict(name='Volledige seizoen', id='volledig-seizoen', msgctxt=''),
    # Inhoudsgerelateerd
    dict(name='Kortfilm', id='kortfilm', msgctxt=''),
]
