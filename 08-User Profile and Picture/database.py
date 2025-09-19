# python manage.py shell

#  from django.contrib.auth.models import User
#  user = User.objects.filter(username = 'UjjwalCSE').first()
#  user
# <User: UjjwalCSE>
#  user.profile
# <Profile: UjjwalCSE Profile>
#  user.profile.image
# ImageFieldFile: profile_pics/pic.png>
# user.profile.image.width
# 791
# user.profile.image.height
# 913


# >>> user.profile.image.url
# '/profile_pics/pic.png'
# >>> #  for 2nd user
# >>> user = User.objects.filter(username = 'MyTestUser1').first()
# >>> user
# <User: MyTestUser1>
# >>> user.profile.image
# <ImageFieldFile: default.jpg>
# >>> exit()
# (.venv) PS D:\Laptop\Coding\Django\08-User Profile and Picture>