from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from app.pizza_context.infrastructure.models.ingredient import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientVewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
