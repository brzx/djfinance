from django.contrib import admin

# Register your models here.
from .models import AssetType, Asset, AccountTurnOver

class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ['assetname', 'detailtype', 'create_dt', 'update_dt']
admin.site.register(AssetType, AssetTypeAdmin)

class AssetAdmin(admin.ModelAdmin):
    list_display = ['user', 'as_type', 'as_iden', 'as_organ', 'amount', 'create_dt', 'update_dt']
admin.site.register(Asset, AssetAdmin)

class AccountTurnOverAdmin(admin.ModelAdmin):
    list_display = ['user', 'asset', 'ac_type','amount', 'create_dt', 'update_dt']
admin.site.register(AccountTurnOver, AccountTurnOverAdmin)