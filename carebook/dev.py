from base import *
 
DEBUG = True
 
INSTALLED_APPS.append('debug_toolbar')
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')
 
# # Paypal environment variables
# SITE_URL = 'http://127.0.0.1:8000'
# PAYPAL_NOTIFY_URL = '<your ngrok URL>'
# PAYPAL_RECEIVER_EMAIL = '<your Paypal merchant email>'