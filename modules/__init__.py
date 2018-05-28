import os
import unittest

import foursquare

if 'X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY' in os.environ and 'CLIENT_SECRET' in os.environ and 'ACCESS_TOKEN' in os.environ:
    CLIENT_ID = os.environ['X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY']
    CLIENT_SECRET = os.environ['55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD']
    # ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
else:
    try:
        from foursquare.tests._creds import *
    except ImportError:
        print("Please create a creds.py file in this package, based upon creds.example.py")


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'testdata')


class BaseEndpointTestCase(unittest.TestCase):
    default_geo = u'40.7,-74.0'
    default_geo_radius = 100
    default_userid = u'1070527'
    default_venueid = u'40a55d80f964a52020f31ee3'
    default_tipid = u'53deb1f6498e0d374af17ca7'
    default_listid = u'32/tips'
    default_photoid = u'4d0fb8162d39a340637dc42b'
    default_settingid = u'receivePings'
    default_specialid = u'4e0debea922e6f94b1410bb7'
    default_special_venueid = u'4e0deab3922e6f94b1410af3'
    default_eventid = u'4e173d2cbd412187aabb3c04'
    default_pageid = u'1070527'

class BaseAuthenticationTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.api = foursquare.Foursquare(
            client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
            client_secret=CLIENT_SECRET,
            redirect_uri='http://localhost'
        )

class BaseAuthenticatedEndpointTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.api = foursquare.Foursquare(
            client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
            client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
#             access_token=ACCESS_TOKEN
        )

class BaseUserlessEndpointTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.api = foursquare.Foursquare(
            client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
            client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD'
        )

class MultilangEndpointTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.apis = []
        for lang in ('es', 'fr', 'de', 'it', 'ja', 'th', 'ko', 'ru', 'pt', 'id'):
            self.apis.append(
                foursquare.Foursquare(
                    client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
                    client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
                    lang=lang
                )
            )