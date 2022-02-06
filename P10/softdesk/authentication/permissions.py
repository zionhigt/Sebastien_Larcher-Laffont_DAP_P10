from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorOnly(BasePermission):
    """ Allow only owner of object """
     
    #   Only available for obj had author_user_id
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.id == obj.author_user_id.id)