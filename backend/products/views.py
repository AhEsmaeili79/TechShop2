# products/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_product(request):
    if request.user.role != 'seller':
        return Response({'error': 'Only sellers can add products'}, status=status.HTTP_403_FORBIDDEN)

    # Create the serializer with the request context
    serializer = ProductSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()  # The seller will be automatically set in the serializer
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
