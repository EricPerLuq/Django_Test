from django.contrib import admin
from core.models import *


class InlineSprint(admin.TabularInline):
	model = Sprint
	extra = 1

class InlineSpec(admin.TabularInline):
	model = Spec
	extra = 1

class ProjecteAdmin(admin.ModelAdmin):
	inlines = [ InlineSprint ,InlineSpec]

class SprintAdmin(admin.ModelAdmin):
	list_display= ['Projecte','data_inici','data_final','hores']


class SpecAdmin(admin.ModelAdmin):
	list_display=['Projecte','dificultat','hores','descripcio']

admin.site.register(Projecte,ProjecteAdmin)
admin.site.register(Sprint,SprintAdmin)
admin.site.register(Spec,SpecAdmin)
