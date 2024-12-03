from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/images', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/images', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина пользователя {self.user.username}" if self.user else "Корзина гостя"


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        return self.quantity * self.product.price


class Promotion(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='promotions/', verbose_name="Изображение")
    active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Промоакция"
        verbose_name_plural = "Промоакции"


def cart_view(request):
    cart_items = request.session.get('cart_items', [])  # Например, вы храните корзину в сессии
    cart_total = sum(item['quantity'] * item['product'].price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)