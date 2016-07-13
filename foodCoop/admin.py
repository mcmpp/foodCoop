from django.contrib import admin
from .models import Member
from .models import Share
from .models import Payment

admin.site.register(Member)
admin.site.register(Share)
admin.site.register(Payment)
