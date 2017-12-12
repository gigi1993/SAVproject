from django.contrib import admin
from .models import Click
# Register your models here.
class ClickAdmin(admin.ModelAdmin):  
	list_display = ['click_id', 'date', 'ip_address', 'clicked']
	class Meta:
		model = Click

admin.site.register(Click, ClickAdmin)
