from .main import Xmpp

def start():
    return Xmpp()

config = [{
    'name': 'xmpp',
    'groups': [
        {
            'tab': 'notifications',
            'list': 'notification_providers',
            'name': 'xmpp',
            'options': [
                {
                    'name': 'enabled',
                    'default': 0,
                    'type': 'enabler',
                },
                {
                    'name': 'to',
                    'label': 'Send to',
                },
                {
                    'name': 'from',
                    'label': 'Send from',
                },
                {
                    'name': 'xmpp_pass',
                    'label': 'XMPP password',
                    'type': 'password',
                },
                {
                    'name': 'on_snatch',
                    'default': 0,
                    'type': 'bool',
                    'advanced': True,
                    'description': 'Also send message when movie is snatched.',
                },
            ],
        }
    ],
}]
