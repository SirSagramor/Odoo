"""
    Task 5:
    Змоделювати роботу світлофорів на перехресті, є світлофор для автомобілів, є для пішоходів,
    існують режими роботи (нічний, звичайний). Потрібно щоб була можливість додавати видаляти світлофори,
    перемикати в ручному режимі. Без ручного режиму усі світлофори мають працювати синхронно один з одним.
    Модель максимально наближена до реального життя. Має бути передбачена можливість отримувати інформацію
    про поточний стан кожного світлофора (стан, режим, скільки часу до наступного стану) для виведення на екран,
    надсиланню по мережі, інші розширення.
"""
from threading import Timer


class Intersection:
    def __init__(self, time, day=True):
        self.carLights = {
            'north': [],
            'south': [],
            'west': [],
            'east': []
        }
        self.humanLights = {
            'north': [],
            'south': [],
            'west': [],
            'east': []
        }
        self.day = day
        self.time = time
        self.timer = Timer(time, self.change)
        self.timer.start()

    def change(self):
        for key in self.carLights:
            for i in range(len(self.carLights[key])):
                self.carLights[key][i].on = not self.carLights[key][i].on
        for key in self.humanLights:
            for i in range(len(self.humanLights[key])):
                self.humanLights[key][i].on = not self.humanLights[key][i].on
        self.timer = Timer(self.time, self.change)
        self.timer.start()


    def isWorking(self, side):
        on = True
        if side == 'north' or side == 'south':
            if self.carLights['north']:
                on = self.carLights['north'][0].on
            elif self.carLights['south']:
                on = self.carLights['south'][0].on
            elif self.carLights['west']:
                on = not self.carLights['west'][0].on
            elif self.carLights['east']:
                on = not self.carLights['east'][0].on
        else:
            if self.carLights['west']:
                on = self.carLights['west'][0].on
            elif self.carLights['east']:
                on = self.carLights['east'][0].on
            elif self.carLights['north']:
                on = not self.carLights['north'][0].on
            elif self.carLights['south']:
                on = not self.carLights['south'][0].on
        return on

    def addLight(self, side):
        if side in self.carLights:
            on = self.isWorking(side)
            self.carLights[side].append(TrafficLight(side, on))
            self.humanLights[side].append(TrafficLight(side, on))

    def manual(self, side, on):
        if side in self.carLights and self.carLights[side][0]:
            if self.carLights[side][0].on == on:
                return
            else:
                self.change()


    def delLight(self, side):
        if side in self.carLights:
            if self.carLights[side]:
                self.carLights.pop()
                self.humanLights.pop()

    def __str__(self):
        day = "Day" if self.day else "Night"
        northcar = list(map(lambda x: "Green" if x.on else "Red" ,self.carLights['north']))
        northhuman = list(map(lambda x: "Green" if x.on else "Red", self.carLights['north']))
        southcar = list(map(lambda x: "Green" if x.on else "Red", self.carLights['south']))
        southhuman = list(map(lambda x: "Green" if x.on else "Red", self.carLights['south']))
        westcar = list(map(lambda x: "Green" if x.on else "Red", self.carLights['west']))
        westhuman = list(map(lambda x: "Green" if x.on else "Red", self.carLights['west']))
        eastcar = list(map(lambda x: "Green" if x.on else "Red", self.carLights['east']))
        easthuman = list(map(lambda x: "Green" if x.on else "Red", self.carLights['east']))
        return '''
        Mode: {}
        Car traffic lights on north: {} and human lights: {}
        Car traffic lights on south: {} and human lights: {}
        Car traffic lights on west: {} and human lights: {}
        Car traffic lights on east: {} and human lights: {}
        '''.format(day, northcar, northhuman, southcar, southhuman, westcar, westhuman, eastcar, easthuman)


class TrafficLight:
    def __init__(self, side, on):
        self.side = side
        self.on = on

print("How many seconds need traffic light to change?")
seconds = int(input())
intro = Intersection(seconds)
while True:
    print("Would you like add traffic light, delete him, change manual, print all the lights or exit from the program?",
          "Press add, delete, change, print or exit")
    do = input()
    if do == 'add':
        print("Choose side: north, south, east, west")
        side = input()
        intro.addLight(side)
    elif do == 'delete':
        print("Choose side: north, south, east, west")
        side = input()
        intro.delLight(side)
    elif do == 'change':
        print("Choose side: north, south, east, west.")
        side = input().split()
        print("And choose red or green color")
        color = input()
        color = True if color == 'green' else False
        intro.manual(side, color)
    elif do == 'print':
        print(intro)
    elif do == 'exit':
        break
