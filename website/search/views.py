from django.shortcuts import render
import re

from numpy import integer
import website.data_access

def update_search_category(filter_goods, get_category):
    if get_category is not None:
        filter_goods.update({
            'category': get_category
        })


def make_request(filter_goods, price_from, price_to):
    """
        > Greater than:   x > y
        < Less than:	x < y
        """
    if len(price_from) != 0 and len(price_to) != 0:
        filter_goods.update(
            {
                "$and": [
                    {'price': {'$gt': int(price_from)}},
                    {'price': {'$lt': int(price_to)}}
                ]
            }
        )
    elif len(price_from) == 0 and len(price_to) != 0:
        filter_goods.update(
            {'price': {'$lt': int(price_to)}}
        )

    elif len(price_from) != 0 and len(price_to) == 0:
        filter_goods.update(
            {'price': {'$gt': int(price_from)}}
        )

    return filter_goods

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
    #     update_search_category(filter_obj, category)

    # filtered_goods = website.data_access.getAllObject("goods")

    # items = website.data_access.getAllObject('category')
    return render(request, "search/search.html", {"category": unique_category, "goods": goods_current_category, "price_min": price_min, "price_max": price_max})
    # return render(request, "search/search.html", {"filter_good": filtered_goods, "keyword": keyword, "c_name": category, "category": items})
