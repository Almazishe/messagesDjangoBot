from django.db.models import Case, When
from .serializers import UsersListSerializer
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    response_data = {}
    if request.method == 'POST':
        serializer = RegistrationSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            user = serializer.save()
            response_data['success'] = 'User registered successfully.'

            response_data['user'] = {
                'id': user.id,
                'username': user.username,
            }
            return Response(
                data=response_data,
                status=status.HTTP_201_CREATED
            )
        else:
            response_data = serializer.errors
            return Response(
                data=response_data,
                status=status.HTTP_400_BAD_REQUEST
            )

    else:
        response_data['error'] = 'Only POST request\'s accepted.'

    return Response(
        data=response_data,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list(request):
    response_data = {}
    if request.method == 'GET':
        users = User.objects.order_by(
            Case(When(id=request.user.id, then=0), default=1)
        )
        serializer = UsersListSerializer(users, many=True)

        response_data['users'] = serializer.data
        response_data['total_count'] = users.count()

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )
    else:
        response_data['error'] = 'Only GET request\'s accepted.'

    return Response(
        data=response_data,
        status=status.HTTP_400_BAD_REQUEST
    )
