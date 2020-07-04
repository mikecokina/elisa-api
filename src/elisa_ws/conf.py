# Default base_url - starts '/'
_DEFAULT_BASE_URL = ''

# Default CORS allowed origins
_DEFAULT_CORS_ORIGINS = ['localhost', '127.0.0.1']


class Settings(object):
    def __init__(self):
        self.base_url = _DEFAULT_BASE_URL
        self.cors_allowed_origins = _DEFAULT_CORS_ORIGINS

    def to_dict(self):
        return {
            'base_url': self.base_url,
            'cors_allowed_origins': self.cors_allowed_origins
        }


settings = Settings()
