from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSellerOrReadOnly(BasePermission):
    # anyone can read, only sellers can create
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_seller


class IsOwnerOrReadOnly(BasePermission):
    # anyone can read, only the product owner can edit or delete
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.seller == request.user
