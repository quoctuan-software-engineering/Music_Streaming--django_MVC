from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Song, Album, Genre, Artist


# Register your models here.
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Artist)


class CustomUserAdmin(BaseUserAdmin):
    # Thêm 'favorite_songs' vào fieldsets (hiển thị trong admin)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Favorites', {
            'fields': ('favorite_songs',),
        }),
    )

    # Nếu bạn dùng `add_fieldsets` (cho form tạo mới user):
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Favorites', {
            'fields': ('favorite_songs',),
        }),
    )

    filter_horizontal = ('favorite_songs',)  # Cho phép chọn nhiều bài

# Gỡ bỏ đăng ký User mặc định
admin.site.unregister(User)

# Đăng ký lại với custom admin
admin.site.register(User, CustomUserAdmin)
