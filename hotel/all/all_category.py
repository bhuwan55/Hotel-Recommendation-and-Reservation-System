from all_hotels.models import Category

def getAllCategory():
    return Category.objects.all()
