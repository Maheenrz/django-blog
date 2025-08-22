from django.shortcuts import render
from .models import Post
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})


from django.http import JsonResponse

# --- API Views ---


@csrf_exempt
def get_data(request):
    return JsonResponse({"message": "This is GET request"})

@csrf_exempt
def post_data(request):
    name = request.GET.get("name", "No Name Sent")
    return JsonResponse({"message": f"This is POST request, name={name}"})

@csrf_exempt
def put_data(request):
    name = request.GET.get("name", "No Name Sent")
    return JsonResponse({"message": f"This is PUT request, name={name}"})

@csrf_exempt
def delete_data(request):
    name = request.GET.get("name", "No Name Sent")
    return JsonResponse({"message": f"This is DELETE request, name={name}"})