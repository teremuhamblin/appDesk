def paginate(queryset, limit=50):
    return queryset[:limit]
