from django.contrib import admin

# Register your models here.

"""Admin Registration for Account-section Models"""

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import IPLUser


class IPLUserCreationForm(forms.ModelForm):
    class Meta:
        model = IPLUser
        fields = ('email', 'is_secondaryUser')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(IPLUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


@admin.register(IPLUser)
class IPLUserAdmin(UserAdmin):
    """
    Customize 'IPL users' admin page.
    """
    add_form = IPLUserCreationForm
    list_display = ('email',)
    ordering = ('email',)
    search_fields = ('email',)
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_secondaryUser', 'created_dtm')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'is_secondaryUser')
        }),
        (('Dates & Timestamps'), {'fields': ('created_dtm',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password', 'is_staff', 'is_superuser', 'is_secondaryUser', 'created_dtm'),
        }),
    )

    def has_add_permission(self, request):
        """
        Allow only superusers to create users.
        """
        if not request.user.is_superuser:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        """
        Allow only superusers to change/modify users.
        Show user details to non-superusers.
        """
        if not request.user.is_superuser:
            self.readonly_fields = (
                'email', 'created_dtm',  'is_staff', 'is_superuser', 'is_secondaryUser')
        else:
            self.readonly_fields = tuple()
        return True

    def has_delete_permission(self, request, obj=None):
        """
        Allow only superusers to delete users.
        """
        if not request.user.is_superuser:
            return False
        return True

    def get_actions(self, request):
        """
        Allow delete action only for superusers.
        """
        actions = super(IPLUserAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            actions.pop('delete_selected', None)
        return actions