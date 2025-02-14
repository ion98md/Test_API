from rest_framework import serializers


class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, max_digits=5, decimal_places=2)

