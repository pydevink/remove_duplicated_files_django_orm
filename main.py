from django.db.models import Count, Max

unique_fields = ['field_1', 'field_2']

duplicates = (
    MyModel.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
)

for duplicate in duplicates:
    (
        MyModel.objects
            .filter(**{x: duplicate[x] for x in unique_fields})
            .exclude(id=duplicate['max_id'])
            .delete()
    )
