postgres = {
    'NAME': 'laptop',
    'USER': 'laptop',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '5432'
}

prod = {
    'SECURE_CONTENT_TYPE_NOSNIFF': True,
    'SECURE_BROWSER_XSS_FILTER': True,
    'SESSION_COOKIE_SECURE': True,
    'CSRF_COOKIE_SECURE': True,
    'X_FRAME_OPTIONS': 'DENY',
    'DEBUG': False
}

dev = {
    'SECURE_CONTENT_TYPE_NOSNIFF': False,
    'SECURE_BROWSER_XSS_FILTER': False,
    'SESSION_COOKIE_SECURE': False,
    'CSRF_COOKIE_SECURE': False,
    'X_FRAME_OPTIONS': 'ALLOW',
    'DEBUG': True,
}

env = dev

secret_key = ''

private_key_file = ''

mailgun_api_key = ''
