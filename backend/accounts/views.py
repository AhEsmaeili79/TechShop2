from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserSerilizer,UpdateProfileSerializer,Profiledetail
from rest_framework import generics


@api_view(['POST'])
def signup(request):
    data=request.data
    serializer = UserSerilizer(data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def update_profile(request,id):
    try:
        user = CustomUser.objects.get(id=id)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        data = request.data
        serializer = UpdateProfileSerializer(user,data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

@api_view(["GET"])

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.auth.delete()  # Delete the token upon logout
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)



class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = Profiledetail
