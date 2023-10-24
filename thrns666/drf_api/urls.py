from django.urls import path, include
from drf_api.views import *
from rest_framework import routers

# order_router = routers.SimpleRouter()
# order_router.register('orders', OrderViewSet)
#
# product_router = routers.SimpleRouter()
# product_router.register('products', ProductViewSet)

urlpatterns = [
    # path('v1/', include(product_router.urls)),
    # path('v1/', include(order_router.urls)),
    path('v1/orders', OrderAPIList.as_view()),
    path('v1/ordersdestroy/<int:pk>/', OrderAPIDestroy.as_view())
]