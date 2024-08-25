from django.contrib import admin
from accounts.models import Accounts
from business.models import Salons, SalonImages, Services

# Register your models here.

# auth
admin.site.register(Accounts)
# business
admin.site.register(Salons)
admin.site.register(SalonImages)
admin.site.register(Services)
