from import_export import resources
from orderapp import models


class ProductResource(resources.ModelResource):
    class Meta:
        model = models.Product

