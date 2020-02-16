from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    def has_permission(self,request,view):
        return request.user and request.user.is_authenticated

    #her durumda çalışır
    #def has_permission(self,request,view): 
    #    print('çalıştı has_perm')
    #    return True
        
    message = "You must be the owner of this object."
    def has_object_permission(self,request,view,obj):
        #print('çalıştı has_obj_perm')
        return (obj.user == request.user) or request.user.is_superuser
