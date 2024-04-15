from .models import Category


def get_categories_select(request):
    categories = Category.objects.all()
    return {'categories': categories}