from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from app.pizza_context.infrastructure.models.pizza import Pizza
from app.pizza_context.infrastructure.ports.http.ingredient import IngredientSerializer


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Pizza
        fields = '__all__'


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all().prefetch_related('ingredients')
    serializer_class = PizzaSerializer
