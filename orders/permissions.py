from rest_framework import permissions


# TODO: implement permissions based on user roles


class IsAccountantUser(permissions.BasePermission):
    """
    Permissions for `accountant` user.
    """
    pass


class IsCashierUser(permissions.BasePermission):
    """
    Permissions for `cashier` user.
    """
    pass


class IsSellerUser(permissions.BasePermission):
    """
    Permissions for `seller` user.
    """
    pass
