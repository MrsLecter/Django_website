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
    db_ids = []
    for item in all_items:
        db_category.append(item['category'])
        db_ids.append(item['_id'])

    unique_category = set(db_category)
    goods_current_category = website.data_access.getGoodsFromCurrentCategory(category, "goods")

    print(keyword,price_from )




    # filter_obj = {'name': re.compile(f".*{keyword}.*", re.IGNORECASE)}

    # if price_from is not None and price_to is not None:
    #     make_request(filter_obj, price_from, price_to)

    # if category != "all_categories":
    #     update_search_category(filter_obj, category)

    # filtered_goods = website.data_access.getAllObject("goods")

    # items = website.data_access.getAllObject('category')
    return render(request, "search/search.html", {"category": unique_category, "goods": goods_current_category, "items": all_items, "ids": db_ids})
  
