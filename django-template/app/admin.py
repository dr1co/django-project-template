"""
Django Admin configuration.

This file is used to register your local (ORM) models in Django's built-in
admin interface, enabling CRUD operations (Create, Read, Update and Delete)
without having to build screens manually.

For more information on customizing the Admin, see:
    https://docs.djangoproject.com/en/6.0/ref/contrib/admin/

Examples:

1. Simple Model Registration
    from django.contrib import admin
    from .models import Employee

    admin.site.register(Employee)


2. Custom Registration (showing columns, filters and search fields)
    @admin.register(Employee)
    class EmployeeAdmin(admin.ModelAdmin):
        # Columns shown in the admin list view
        list_display = ("id", "name", "department", "created_at")

        # Quick filters in the sidebar
        list_filter = ("department", "created_at")

        # Fields that enable the search bar at the top
        search_fields = ("name", "department")

        # Default ordering when the page loads
        ordering = ("-created_at",)
"""

from django.contrib import admin  # noqa: F401

# Register your models here.
