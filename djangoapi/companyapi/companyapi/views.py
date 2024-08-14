from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home Page Requested")
    friends=[
            'ankit',
            'anuj',
            'uttam' ]
    return JsonResponse(friends,safe=False)