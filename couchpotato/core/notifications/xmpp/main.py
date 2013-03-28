from couchpotato.core.helpers.encoding import toUnicode
from couchpotato.core.helpers.variable import splitString
from couchpotato.core.logger import CPLog
from couchpotato.core.notifications.base import Notification
from email.mime.text import MIMEText
import smtplib
import traceback

log = CPLog(__name__)


class Xmpp(Notification):

    def notify(self, message = '', data = {}, listener = None):

        # Extract all the settings from settings
        from_address = self.conf('from')
        to_address = self.conf('to')
        xmpp_pass = self.conf('xmpp_pass')

        # Make the basic message
        message = toUnicode(message)

        try:
            from pyxmpp2.simple import send_message
            send_message(from_address, xmpp_pass, to_address, message)

            log.info('XMPP notification sent')
            return True

        except:
            log.error('XMPP communication failed: %s', traceback.format_exc())
            return False
