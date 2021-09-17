from rest_framework import throttling


class AllowMethod(throttling.AnonRateThrottle):
    scope = 'allow_method'
    def allow_request(self, request, view):
        if request.method == 'GET':
            return True
        return super().allow_request(request, view)
