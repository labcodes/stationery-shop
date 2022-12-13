from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    code = models.CharField(max_length=255, verbose_name=_('Code'), primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_('Product name'))
    available_quantity = models.IntegerField(verbose_name=_('Available quantity'))
    description = models.TextField(verbose_name=_('Description'), blank=True, default='')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.code}: {self.name}'


class IOHistory(models.Model):
    """
    This model represents the history of inputs and outputs for a product inventory.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='history')
    quantity_in = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity In'))
    quantity_out = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity Out'))
    date = models.DateField(verbose_name=_('Date'))

    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('History')

    def __str__(self):
        return f'Product: {self.product.name} - In: {self.quantity_in} Out: {self.quantity_out} at: {self.date}'
