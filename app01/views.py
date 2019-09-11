from django.shortcuts import render
from django.http import  HttpResponse
from . models import  *


# Create your views here.


def index(request):
    return HttpResponse('index')

# def addperson(request):
#     #1 save
#     person=Person(name='lisi',age=20,height=170)
#     person.save()
#     return HttpResponse('增加数据')


# def addperson(request):
#     #create
#     data=dict(name='xiaowang',age=23,height=170)
#     Person.objects.create(**data)
#     return HttpResponse('增加数据')

#
# def chaxun(request):
    #all
#     data=Person.objects.all()
#     for i in data:
#         print(i.name)
#         print(i.height)
#         print(i.age)
#         return HttpResponse('查询数据')
# #
#
# def chaxun(request):
#     #get
#     data=Person.objects.get(id=2)
#     print(data.name)
#     print(data.age)
#     return HttpResponse('查询数据')
def chaxun(request):
#     #filter
#     # data=Person.objects.filter(name='xiaowang').first()
#     # print(data.age)
#     # data=Person.objects.filter(name='xiaowang').last()
#     # print(data.age)
#     #升序
#     # data=Person.objects.all().order_by('age')
#     #降序
#     data=Person.objects.all().order_by('-age')
#     for i in data:
#         print(i.age)
    data=Person.objects.filter(name='xiaowang')
    for i in data:
        # print(i.age)
        print(i.name)
    data=Person.objects.exclude(name='xiaowang')
    for i in data:
        # print(i.age)
        print(i.name)
    return HttpResponse('查询数据')




def update(request):
    #save
    # data=Person.objects.get(id=1)
    # data.name='zhangsan'
    # data.save()
    #update
    Person.objects.filter(id=1).update(name='ping')
    return HttpResponse('修改数据')



def delete(request):
    Person.objects.filter(id=3).delete()
    return HttpResponse('删除数据')



#一对多关系增加
def addmore(request):
    # Publish.objects.create(name='清华出版社',address='北京')
    # Publish.objects.create(name='中国出版社',address='北京朝阳')
    # Publish.objects.create(name='重庆出版社',address='重庆')
    #增加书
    Book.objects.create(name='python入门到精通',p_id=1)
    #第二种方法
    Book.objects.create(name='网络安全',p=Publish.objects.get(name='中国出版社'))

    return HttpResponse('一对多关系增加')

def chaxunmore(request):
    publish=Publish.objects.get(name='中国出版社')
    book=Book.objects.filter(p_id=publish.id).all()
    for i in book:
        print(i.name)
    return HttpResponse('一对多查询')


def updatemore(request):
    publish=Publish.objects.get(name='中国出版社')
    book=Book.objects.filter(p_id=publish.id).all()
    print(book.update(name='黑客'))
    return HttpResponse('一对多修改数据')