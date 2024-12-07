// ...existing code...

INSTALLED_APPS = [
    // ...existing code...
    'django.contrib.staticfiles',
    'pwa',
    // ...existing code...
]

// ...existing code...

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

PWA_APP_NAME = 'Daryl\'s Portfolio'
PWA_APP_DESCRIPTION = "Daryl's Portfolio PWA"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/icons/icon-192x192.png',
        'sizes': '192x192',
        'type': 'image/png',
    },
    {
        'src': '/static/icons/icon-512x512.png',
        'sizes': '512x512',
        'type': 'image/png',
    }
]

// ...existing code...