from core.permissions import IsOwner

from rest_framework import viewsets, views

from rest_framework.response import Response

from accounts.serializers import ProfileSerializer, SpecialUserSerializer

from accounts.models import Profile

from rest_framework.parsers import MultiPartParser


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """ profile view set """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        """ return the current user profile only """
        return Profile.objects.filter(user=self.request.user)


class SpecialUserView(views.APIView):
    """ user view """

    def get(self, request):
        _user_serializer = SpecialUserSerializer(request.user)
        return Response(_user_serializer.data)

    def patch(self, request):
        _user_serializer = SpecialUserSerializer(request.user, data=request.data, partial=True)
        if _user_serializer.is_valid():
            _user_serializer.save()
            return Response(_user_serializer.data)
        else:
            return Response(_user_serializer.errors, status=400)