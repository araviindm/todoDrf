from django import forms
from django.contrib import admin
from ast import literal_eval
from .models import Todo


class TodoAdminForm(forms.ModelForm):
    tags = forms.CharField(help_text='Enter a list of tags as a comma-separated string',
                           required=False,
                           widget=forms.TextInput
                           )

    class Meta:
        model = Todo
        fields = '__all__'

    def clean_tags(self):
        tags = self.cleaned_data['tags']

        if not tags:
            # No tags entered, return None to indicate null value
            return None

        try:
            # Parse the input as a Python literal
            tag_list = literal_eval(tags)
        except (ValueError, SyntaxError):
            raise forms.ValidationError('Please enter a valid list of strings.')

        # Ensure that the parsed value is a list
        if not isinstance(tag_list, list):
            raise forms.ValidationError('Please enter a valid list of strings.')

        # Ensure that all elements in the list are strings
        if not all(isinstance(tag, str) for tag in tag_list):
            raise forms.ValidationError('Please enter a valid list of strings.')

        unique_tags = list(set(tag_list))

        return unique_tags


class TagsFilter(admin.SimpleListFilter):
    title = 'Tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):
        # Retrieve all distinct tags from the model objects
        tags = Todo.objects.values_list('tags', flat=True).distinct()
        # Generate a list of (tag, tag) tuples for the filter choices
        return [(tag, tag) for tag in tags if tag]

    def queryset(self, request, queryset):
        # Filter queryset based on the selected tag
        tag = self.value()
        if tag:
            return queryset.filter(tags__contains=[tag])
        return queryset


class TodoAdmin(admin.ModelAdmin):
    form = TodoAdminForm
    fieldsets = (
        ('Section 1', {
            'fields': ('title', 'description'),
        }),
        ('Section 2', {
            'fields': ('due_date', 'tags', 'status'),
        }),
    )
    list_display = ['title', 'description', 'due_date', 'tags', 'status']
    list_filter = ['due_date', 'status']
    search_fields = ['title', 'description', 'tags']


admin.site.register(Todo, TodoAdmin)
