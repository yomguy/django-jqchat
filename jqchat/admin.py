# -*- coding: utf-8 -*-

from models import Message, Room
from django.contrib import admin

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'last_activity_formatted', 'description', 'description_modified')

    # When changing a description, we need to know the request.user as an attribute
    # of the room instance. This snippet below adds it.
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Room, RoomAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'created', 'unix_timestamp', 'user', 'text', 'event')
    list_filter = ['room', 'user']

admin.site.register(Message, MessageAdmin)

