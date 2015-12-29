import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pathfinder.settings.development')

import django
django.setup()

from django.contrib.auth.models import UserManager, User

from pathfinder.apps.trail.models import Spark, UserProfile, Category


def populate():
    web_dev_cat = add_cat('Web Development')
    test_user = User.objects.get(username='test')

    add_spark(category=web_dev_cat, author=test_user,
                name="JY Pathfinder", slug="jy-pathfinder", 
                url='https://www.youtube.com/watch?v=_48mYcZxi38',
                start_date='2010-12-14',
                description='JY Pathways is a 501(c)(3) non-profit organization committed to developing the potential and growing talent in our global community.')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="Facebook Ads API", slug='facebook-ads-api',
                url='https://www.youtube.com/watch?v=KGnWBuHeCpE',
                start_date='2013-10-14',
                description='Programmatically access Facebooks advertising platform.')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="LinkedIn Premium", slug='linkedin-premium',
                url='https://premium.linkedin.com/',
                start_date='2013-11-11',
                description='Leverage the worlds largest professional network to enhance your brand')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="AngularJS Demo", slug='angularjs-demo',
                url='https://twitter.com/angularjs',
                start_date='2009-1-2',
                description='Bringing “simple” back to the development of complex webapps...')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="3D Printing", slug='3d-printing',
                url='https://www.instagram.com/explore/tags/3dprinting/',
                start_date='2012-1-1',
                description='WOW...')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="GFW VPN", slug='gfw-vpn',
            url='https://www.google.com/maps/place/China/@34.4889982,86.0280106,4z/data=!3m1!4b1!4m2!3m1!1s0x31508e64e5c642c1:0x951daa7c349f366f',
                start_date='1949-10-1',
                description='Referring to legislation and projects initiated by the Chinese government that attempt to regulate the internet in Mainland China.')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="Calculate Prime Number", slug='calculate-prime-number',
                url='https://en.wikipedia.org/wiki/Generating_primes',
                start_date='1999-5-1',
                description='a variety of algorithms make it possible to generate prime numbers efficiently.')
    
    add_spark(category=web_dev_cat, author=test_user,
                name="Tic Tac Toe Game", slug='tic-tac-toe',
                url='https://www.flickr.com/photos/eilonwy77/6270262038',
                start_date='2015-5-5',
                description='A game')

    

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for s in Spark.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(s)))

def add_spark(category, author, name, slug, url, start_date, description):
    s = Spark.objects.get_or_create(category=category, author=author,
                                    name=name, slug=slug, url=url,
                                    start_date=start_date, description=description)[0]
    s.save()
    return s

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()