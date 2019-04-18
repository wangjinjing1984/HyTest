#from django.db import models
# models.py
from django.db import models


class Test(models.Model):
    #客户会员
    name = models.CharField(max_length=20)

class Customer(models.Model):
    market_cost_price = models.FloatField()
    cust_clear_free = models.FloatField(null=True)
    one_tenthous_cost = models.FloatField(null=True)
    retail_cost = models.FloatField(null=True)
    hot_sell_degree = models.CharField(max_length=10,null=True)
    buy_difficulty = models.CharField(max_length=10,null=True)
    activite_product_list = models.TextField(null=True)
    customer_message = models.TextField(null=True)
    product_hk_info = models.TextField(null=True)
    dutyfree_storeprice = models.FloatField(null=True)
    hot_sell_product = models.TextField(null=True)
    findpro_help = models.TextField(null=True)


class inner_Customer(models.Model):
    pass


# Create your models here.
