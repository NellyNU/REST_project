from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contacts
from .serializer import ContactsSerializer

@api_view(['POST'])
def create_user(request):
    serializer = ContactsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        contact = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def list_users(request):
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, pk):
    try:
        contact = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactsSerializer(contact)
    return Response(serializer.data)
