# blog/filters.py
import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    # Create filters for fields you want to filter by
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    # status = django_filters.ChoiceFilter(choices=Blog.STATUS_CHOICES, label='Status')
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at', label='Created At')

    class Meta:
        model = Blog
        fields = ['title', 'author', 'status', 'created_at']

