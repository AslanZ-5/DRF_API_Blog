from rest_framework.permissions import BasePermission, SAFE_METHODS
# SAFE_METHODS ('GET','OPTIONS','HEAD')

class IsOwner(BasePermission):
    message = 'You must be the owner of the object'
    my_safe_method = ['GET']
    # The methods should return True if the request
    # should be granted access, and False otherwise
    def has_permission(self,request,view):
        if request.method in self.my_safe_method:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
