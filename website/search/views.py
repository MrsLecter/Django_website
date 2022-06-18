from django.shortcuts import render
import re

from numpy import integer
import website.data_access



def search(request):
    keyword = request.GET.get('keyword', '')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    category = request.GET.get('category')

    all_items = website.data_access.getAllObject("goods")

    # find all categories
    db_category = []
    db_prices = []
    for item in all_items:
        db_category.append(item['category'])
        db_prices.append(item['price'])

    unique_category = set(db_category)
    db_prices.sort()
    price_min = db_prices[0]
    price_max = db_prices[len(db_prices)-1]
    goods_current_category = website.data_access.getGoodsFromCurrentCategory(category, "goods")





    # filter_obj = {'name': re.compile(f".*{keyword}.*", re.IGNORECASE)}

    # if price_from is not None and price_to is not None:
    #     make_request(filter_obj, price_from, price_to)

    # if category != "all_categories":
    #     update_category(filter_obj, category)

    # filtered_goods = getAllObject("goods")

    # items = website.data_access.getAllObject('category')
    return render(request, "search/search.html", {"category": unique_category, "goods": goods_current_category, "price_min": price_min, "price_max": price_max})
