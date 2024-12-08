from django.http import HttpResponse

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # self.blacklisted_IPs = ["127.0.0.2"]
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print("Inside simple middleware")
        import pprint
        # pprint.pprint(request)
        # print("here",request.body)
        # print("Path", request.path)
        # if request.path == '/admin/' and request.user.email !=  "admin@gmail.com":
        #     return HttpResponse("You are not allowed here")
        # pprint.pprint(request.META.get('REMOTE_ADDR'))
        # client_ip_address = request.META.get('REMOTE_ADDR')

        # if client_ip_address in self.blacklisted_IPs:
            # return HttpResponse("You have been blacklisted")
        request.new_data = "new data set by simple middleware"

        response = self.get_response(request)

        # print("Hello from middleware end", response.cookies)
        # Code to be executed for each request/response after
        # the view is called.

        return response