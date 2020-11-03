from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

from rest_framework.permissions import IsAuthenticated


from django.contrib.auth import get_user_model
User = get_user_model()


from .serializers import SendMessageSerializer

from .models import Message



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    response_data = {}
    if request.method == 'POST':
        serializer = SendMessageSerializer(
            data=request.data,
            context={
                'request': request,
            }
        )

        if serializer.is_valid():
            message = serializer.save()
            response_data['success'] = 'Message successfully sent.'

            return Response(
                data=response_data,
                status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        response_data['error'] = 'Only POST request\'s accepted.'
    
    
    return Response(
        data=response_data,
        status=status.HTTP_400_BAD_REQUEST
    )