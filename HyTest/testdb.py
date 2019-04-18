# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test,Customer


# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')   #name='runoob'
    test2 = Customer(market_cost_price='99')
    test2.save()
    test1.save()

    return HttpResponse("<p>数据添加成功！</p>")