from django.shortcuts import render
from django.shortcuts import HttpResponse
from tyc.tianyancha import TianYanCha


# Create your views here.
def index(request):
    target = request.GET.get('target')
    tyc = TianYanCha(target)
    shuihao = tyc.run()
    dic = {
        'target': target,
        'shui_hao': shuihao,
        'success': '1' if shuihao is not None else '0'
    }
    return HttpResponse(str(dic))


def home(request):
    name = "hello world!"
    dic = {
        "name": name
    }
    return HttpResponse(str(dic))
