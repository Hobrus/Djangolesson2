from django.shortcuts import render

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    context = {'name': 'Всякие Фигнюшки'}
    return render(request, 'home.html', context)


def about(request):
    context = {'name': 'Anton', 'phone_number': '89021710101', 'email': 'inion13@gmail.com'}
    return render(request, 'about.html', context)


def item(request, item_id):
    global items
    result = {}
    for i in items:
        if i['id'] == item_id:
            result['name'] = i['name']
            if i['quantity'] != 0:
                result['quantity'] = i['quantity']
            else:
                result['quantity'] = 'товар отсутствует'
            break
    return render(request, 'item.html', result)


def get_items(request):
    global items
    result = {}
    products = []
    item_ids = []
    for i in items:
        products.append(i['name'])
        item_ids.append(i['id'])
    result['iter'] = products
    result['ids'] = item_ids
    return render(request, 'items.html', result)

