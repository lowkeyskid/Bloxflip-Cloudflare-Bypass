import random

class ua:
    def __init__(self):
        self.browsers = [
            ('Mozilla/5.0', 'Windows NT 10.0; Win64; x64', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Chrome/{}', 'Safari/537.36'),
            ('Mozilla/5.0', 'Windows NT 10.0; Win64; x64', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Edge/{}', 'Safari/537.36'),
            ('Mozilla/5.0', 'Macintosh; Intel Mac OS X 10_15_7', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Firefox/{}', 'Gecko/20100101 Firefox/{}'),
            ('Mozilla/5.0', 'Macintosh; Intel Mac OS X 10_15_7', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Safari/{}', 'Version/{} Safari/537.36'),
            ('Mozilla/5.0', 'Android 10; Mobile; rv:{}'.format(random.randint(80, 90)), 'Gecko/{}'.format(random.randint(20100101, 20230101)), 'Firefox/{}', 'Mobile'),
            ('Mozilla/5.0', 'iPhone; CPU iPhone OS 14_6 like Mac OS X', 'AppleWebKit/605.1.15 (KHTML, like Gecko)', 'Version/{}', 'Mobile/15E148 Safari/604.1'),
        ]

        self.chrome_versions = [random.randint(50, 120) for i in range(10)]
        self.edge_versions = [random.randint(80, 120) for i in range(10)]
        self.firefox_versions = [random.randint(80, 120) for i in range(10)]
        self.safari_versions = [random.randint(12, 16) for i in range(10)]

        self.versions = {
            'Chrome': self.chrome_versions,
            'Edge': self.edge_versions,
            'Firefox': self.firefox_versions,
            'Safari': self.safari_versions
        }
    
    def generate(self):
        browser = random.choice(self.browsers)
        type = browser[3].split('/')[0]
        version = random.choice(self.versions.get(type, [random.randint(1, 99)]))
        
        user_agent = browser[0] + ' ' + browser[1] + ' ' + browser[2]
        user_agent += ' ' + browser[3].format(version) + ' ' + browser[4].format(version)

        return user_agent