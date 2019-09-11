from django.http import HttpResponse
def index(request):
    return HttpResponse('index数据')
def urltest(request,city,year):
    return HttpResponse("%s年在%s" %(year,city))
def html(request):
    html1="""
    <html>
        <head>
        </head>
        <body>
          <a href='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=高清美女大图&hs=2&pn=4&spn=0&di=138160&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=3100930816%2C3644936363&os=2096763997%2C2703225228&simid=4233764710%2C599444136&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=girl&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.sccnn.com%2Fbimg%2F337%2F24851.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bfvvgg_z%26e3Bv54AzdH3F2w53tg2p7h7AzdH3F6jgo7p7h7AzdH3Fgextg2u7geAzdH3Fda89a9d8-88888l_z%26e3Bip4s&gsm=0&islist=&querylist='>
             <img src='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568004527944&di=509b6d4bdf714f45c7adcd948311b377&imgtype=0&src=http%3A%2F%2Fimg.sccnn.com%2Fbimg%2F337%2F24851.jpg' title='beautiful' alt='图片打包中' >
          </a>
        </body>


    </html>

    """
    return HttpResponse(html1)
from django.shortcuts import render
def indextmp(request):
    name='哈士奇'
    return render(request,'index.html',{'name':name})

def tpltest(request,age):
    name='xiaoxiaowang'
    # age=23
    age=int(age)
    hobby=['eat','sleep','shopping']
    score={'math':100,'chinese':99,'english':98}
    myjs="""
           <script>
              alert('啊哈哈哈哈!!!')
           </script>
    """
    # return render(request,'tlptest.html',{'name':name,'age':age,'hobby':hobby,'score':score})
    return render(request,'tlptest.html',locals())



def beautifuldemo(request):
    params= [
        {"name":"bea1","img":"1.jpg","url":"https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7%E9%BA%A6%E6%A0%BC%E9%9B%B7%E8%BF%AA/6118977?fromtitle=%E9%BA%A6%E8%BF%AA&fromid=136057&fr=aladdin"},
        {"name":"bea2","img":"2.jpg","url":"https:www.baidu.com"},
        {"name":"bea3","img":"3.png","url":"https:www.sina.com"},
        {"name":"bea4","img":"4.jpg","url":"https:www.taobao.com"},
    ]
    return render(request,'beademo.html',locals())