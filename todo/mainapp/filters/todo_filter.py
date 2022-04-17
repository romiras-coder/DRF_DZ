import django_filters
from django_filters.widgets import RangeWidget
from django_filters import rest_framework as filters
from ..models.todo import Todo


class TodoFilter(filters.FilterSet):
    project__name = filters.CharFilter(lookup_expr='contains')
    date_create = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Todo
        fields = ['project__name', 'date_create']
