from django.contrib import admin
from .models import Client, Property,Review
from import_export.admin import ImportExportModelAdmin

class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['firstname',  'dob']
	# search_fields = ['author', 'title']
	# list_filter = ['dop']

class PropertyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['property_name',  'price']

class ReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['property_name',  'price', 'user']

admin.site.register(Client, ClientAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Review, ReviewAdmin)