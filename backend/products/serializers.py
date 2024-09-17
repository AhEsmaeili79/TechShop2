from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["seller"]

    def create(self, validated_data):
        # The seller will be set in the view, so remove it from validated_data
        request = self.context["request"]
        user = request.user
        validated_data["seller"] = user
        return super().create(validated_data)
