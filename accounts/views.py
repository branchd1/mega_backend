from core.permissions import IsOwner

from rest_framework import viewsets

from accounts.serializers import ProfileSerializer


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """ profile view set """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        """ return the current user profile only """
        return [self.request.user.profile, ]
