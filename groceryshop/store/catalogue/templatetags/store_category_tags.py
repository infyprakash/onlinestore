from django import template
from oscar.core.loading import get_class, get_model
from django.template.loader import get_template


register = template.Library()




@register.simple_tag
def get_categories():
    Category = get_model('catalogue', 'Category')
    cat = Category.objects.all()
    data = []
    for c in cat:
        pd = c.product_set.all()
        if pd:
            data.append({'category':c,'product':pd})
    return data





# t = get_template('oscar/catalogue/browse.html')
# register.inclusion_tag(t)(get_categories)

# c.get_first_root_node()
# c.get_first_root_node().get_absolute_url()

# In [11]: for item in data:
#     ...:     for k,v in item.items():
#     ...:         products = item['product']
#     ...:         for p in products:
#     ...:             print(p.get_absolute_url())


