from django.contrib import admin

from tracker.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'description', 'created_at', 'changed_at')
    list_filter = ('id', 'text', 'description', 'created_at', 'changed_at')
    search_fields = ('text', 'description', 'created_at', 'updated_at')
    fields = ('text', 'description')
    readonly_fields = ('id',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
    list_filter = ('id', 'status_name')
    search_fields = ('status_name',)
    fields = ('status_name',)
    readonly_fields = ('id',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    list_filter = ('id', 'type_name')
    search_fields = ('type_name',)
    fields = ('type_name',)
    readonly_fields = ('id',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
