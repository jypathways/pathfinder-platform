import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pathfinder.settings.development')

import django
django.setup()

from django.contrib.auth.models import UserManager, User

from pathfinder.apps.trail.models import Project, UserProfile, Category


def populate():
    web_dev_cat = add_cat('Computer Science')
    test_user = User.objects.get(username='admin')

    add_project(category=web_dev_cat, author=test_user,
        title="JY Pathfinder", slug="jy-pathfinder")
    
    add_project(category=web_dev_cat, author=test_user,
        title="Facebook Ads API", slug='facebook-ads-api')
    
    add_project(category=web_dev_cat, author=test_user,
        title="LinkedIn Premium", slug='linkedin-premium')
    
    add_project(category=web_dev_cat, author=test_user,
        title="AngularJS Demo", slug='angularjs-demo')
    
    add_project(category=web_dev_cat, author=test_user,
        title="3D Printing", slug='3d-printing')
    
    add_project(category=web_dev_cat, author=test_user,
        title="GFW VPN", slug='gfw-vpn')
    
    add_project(category=web_dev_cat, author=test_user,
        title="Calculate Prime Number", slug='calculate-prime-number')
    
    add_project(category=web_dev_cat, author=test_user,
        title="Tic Tac Toe Game", slug='tic-tac-toe')

    

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Project.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_project(category, author, title, slug):
    p = Project.objects.get_or_create(category=category, author=author, 
                                      title=title, slug=slug)[0]
    p.url="http://test.com"
    p.likes=1234
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()