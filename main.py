import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

room1 = {}

room1.update({
    "id_room": "1",
    "№_room": "200",
    "status": "free",
    "class_id": "3",
    "price": "1.300",
    "number_of_places": "1",
})

room2 = {}
room2.update({
    "id_room": "2",
    "№_room": "201",
    "status": "busy",
    "class_id": "1",
    "price": "3.000",
    "number_of_places": "2",
})

room3 = {}
room3.update({
    "id_room": "3",
    "№_room": "202",
    "status": "busy",
    "class_id": "1",
    "price": "3.500",
    "number_of_places": "3",
})

room4 = {}
room4.update({
    "id_room": "4",
    "№_room": "203",
    "status": "free",
    "class_id": "2",
    "price": "2.700",
    "number_of_places": "1",
})

room5 = {}
room5.update({
    "id_room": "5",
    "№_room": "204",
    "status": "busy",
    "class_id": "3",
    "price": "2.900",
    "number_of_places": "2",
})
while True:
    print("Списко номеров: 200, 201, 202, 203, 204, 205")
    guests = int(input("Про какой номер хотите узнать информацию: "))

    if guests == 200:
        print([room1.get(k) for k in ("№_room", "status", "price", "number_of_places")])
        print()
    elif guests == 201:
        print([room2.get(k) for k in ("№_room", "status", "price", "number_of_places")])
        print()
    elif guests == 202:
        print([room3.get(k) for k in ("№_room", "status", "price", "number_of_places")])
        print()
    elif guests == 203:
        print([room4.get(k) for k in ("№_room", "status", "price", "number_of_places")])
        print()
    elif guests == 204:
        print([room5.get(k) for k in ("№_room", "status", "price", "number_of_places")])
        print()
    elif guests == 205:
        print("Извините, но этот номер пока что находится на ремонте. Приносим извинение!")
        print()

