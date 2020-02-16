from rest_framework.throttling import SimpleRateThrottle,AnonRateThrottle,UserRateThrottle

class RegisterSimpleThrottle(SimpleRateThrottle):
    scope = 'registersimplethrottle'

    def get_cache_key(self,request,view):
        if request.user.is_authenticated or request.method=='GET':
            return None
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }


class RegisterAnonThrottle(AnonRateThrottle):
    scope = 'registeranonthrottle'
    #giriş yapmadan GET veya POST farketmez engel atıyo


class RegisterUserRateThrottle(UserRateThrottle):
    scope = 'registeruserratethrottle'
    #giriş yapsakta kullanıcıya göre yine engel atıcak

    
