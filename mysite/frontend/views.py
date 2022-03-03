from django.shortcuts import render
# from django.http import JsonResponse

def index(request):
    return render(request, 'home.html')

# def ajax_get_view(request):
    # data = {
           # 'my_data:data_to_display'
    #}
    #return JsonResponse(data)