from django_filters import rest_framework as filter
from reviews.models import Title


class TitleFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name', lookup_expr='icontains')
    genre = filter.CharFilter(field_name='genre__slug')
    category = filter.CharFilter(field_name='category__slug')

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year')
