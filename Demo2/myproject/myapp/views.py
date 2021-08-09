from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
def index(request):
    return HttpResponse('<h1>hello world<h1>')

def test(request):
    # return HttpResponse('<h1>hello world<h1>')
    hi='你好，世界是美好的'
    test='这是一个测试页，动态页面正常显示，测试成功'
    return render(request, 'test.html', {'hi': hi, 'test': test})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == 'test' and password == '123'):
            return redirect('/test/')
        else:
            return render(request, "login.html", {'error': '用户名或密码错误！'})