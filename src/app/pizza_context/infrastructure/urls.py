from app.pizza_context.infrastructure.ports import http
from django.urls import path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'pizzas', http.PizzaViewSet)
router.register(r'ingredients', http.IngredientVewSet)

urlpatterns = [

]
urlpatterns += router.urls
