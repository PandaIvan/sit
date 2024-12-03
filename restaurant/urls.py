from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from restaurant import views  # Импортируем views из приложения menu


urlpatterns = [
    path("", views.slider, name="index"),  # Главная страница
    path("menu/", views.menu, name="menu"),  # Путь для страницы меню
    path("cart/", views.cart, name="cart"),  # Страница корзины
    path(
        "add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"
    ),  # Добавление в корзину
    path(
        "remove_from_cart/<int:product_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),
    # Удаление из корзины
    path("checkout/", views.checkout, name="checkout"),  # Страница оформления заказа
    path(
        "category/<int:pk>/", views.category_detail, name="category_detail"
    ),  # Категория
    path("test-session/", views.test_session, name="test_session"),
    path("get-session/", views.get_session, name="get_session"),
    path("clear-session/", views.clear_session, name="clear_session"),
    #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
