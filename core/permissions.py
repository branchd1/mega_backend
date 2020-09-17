""" This module contains permission logic for objects """

from rest_framework import permissions

from core.models import Community


class IsOwner(permissions.BasePermission):

    """
    Custom permission to allow only owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        """
        Write permissions are only allowed to the owner of the object.

        Parameters
        ----------
        request
        view
        obj

        Returns
        -------
        bool
            True if object user is the current user, False otherwise

        """

        return obj.user == request.user


class IsCommunityAdmin(permissions.BasePermission):

    """
    Custom permission to allow only owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj: Community):

        """
        Write permissions are only allowed to the admins of the community

        Parameters
        ----------
        request
        view
        obj : Community
            The community being checked for permission

        Returns
        -------
        bool
            True if current user is an admin of obj Community,
            False if not

        """

        return request.user in obj.admins
