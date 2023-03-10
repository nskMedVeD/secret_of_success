from django.contrib import admin
from .models import *


class ContestMaterialAdmin(admin.ModelAdmin):
    pass


class ContestNominationAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContestMaterial, ContestMaterialAdmin)
admin.site.register(ContestNomination, ContestNominationAdmin)
admin.site.register(Institution)
admin.site.register(Author)


