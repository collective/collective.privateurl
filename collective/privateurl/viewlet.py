import inspect
import re
from zExceptions import Unauthorized
from zope.component import getMultiAdapter
from Products.Five.browser import BrowserView
from plone.app.layout.viewlets.common import ViewletBase

whitelist = re.compile(r'require_login\Z|login_form\Z|mail_password_form\Z|mail_password\Z|passwordreset\Z|pwreset_form\Z|pwreset_finish\Z')

class PrivateURL(ViewletBase):

    def update(self):
        self.portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')

    def index(self):
        # prevent re-raising Unauthorized when the standard error message is
        # rendered
        for frame_tuple in inspect.stack():
            if frame_tuple[0].f_code.co_name == 'raise_standardErrorMessage':
                return ''
        portal = self.portal_state.portal()
        if portal.hasProperty('privateurls'):           
            if self.portal_state.anonymous() \
                    and (whitelist.search(self.request.URL) is None):
                if portal.hasProperty('publicurls'):
                    for url in portal.publicurls:
                        if self.request.URL.startswith(url):
                            return ''
                for url in portal.privateurls:
                    if self.request.URL.startswith(url):
                        self.request['raised_unauthorized'] = True
                        raise Unauthorized                
        return ''
