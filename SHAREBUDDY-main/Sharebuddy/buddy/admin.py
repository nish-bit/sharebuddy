from django.contrib import admin

# Register your models here.
from buddy.models import Listings,Bids,Category,Comments

admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Category)
admin.site.register(Comments)

