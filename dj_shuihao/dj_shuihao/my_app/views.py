from django.shortcuts import HttpResponse
from tyc.tianyancha import TianYanCha
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def get_func(request):
    target = request.GET.get('target')
    tyc = TianYanCha(target)
    shuihao = tyc.run()
    dic = {
        'target': target,
        'shui_hao': shuihao,
        'success': '1' if shuihao is not None else '0'
    }
    return HttpResponse(str(dic))


def post_func(request):
    if request.method == 'POST':
        target = dict(request.POST)
        name = target['target'][0]
        tyc = TianYanCha(name)
        shuihao = tyc.run()
        dic = {
            'target': name,
            'shui_hao': shuihao,
            'success': '1' if shuihao is not None else '0'
        }

    return HttpResponse(str(dic))


def sub_function(request):
    pass


def home(request):
    return render_to_response("index.html")

    # name = "hello world!"
    # dic = {
    #     "name": name
    # }
    # return HttpResponse(str(dic))
