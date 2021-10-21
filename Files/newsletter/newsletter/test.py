from admin_panel.models import *

header = Header.objects.latest('id')
print(header)