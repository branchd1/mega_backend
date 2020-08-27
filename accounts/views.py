from core.permissions import IsOwner

from rest_framework import viewsets

from accounts.serializers import ProfileSerializer

from rest_framework.parsers import MultiPartParser


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """ profile view set """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        """ return the current user profile only """
        return [self.request.user.profile, ]
