car = [1, 1, 1, 1, 0, 1, 0]
truck = [1, 1, 0, 1, 1, 1, 0]
spec_machine = [1, 1, 0, 1, 0, 1, 1]

def check(line):
    l = line.split(';')
    if l[0] == 'car':
        for i in range(0, len(l)):
            if car[i] == 1 and l[i] == '':
                return False
            elif car[i] == 0 and l[i] != '' and l[i] != '\n':
                return False
        return 'car'
    elif l[0] == 'truck':
        for i in range(0, len(l)):
            if truck[i] == 1 and l[i] == '':
                return False
            elif truck[i] == 0 and l[i] != '' and l[i] != '\n':
                return False
        return 'truck'
    elif l[0] == 'spec_machine':
        for i in range(0, len(l)):
            if spec_machine[i] == 1 and l[i] == '':
                return False
            elif spec_machine[i] == 0 and l[i] != '' and l[i] != '\n':
                return False
        return 'spec_machine'


class Carbase(object):
    def __init__(self, list_of_atr):
        self.car_type = list_of_atr[0]
        self.brand = list_of_atr[1]
        self.carrying = list_of_atr[len(list_of_atr) - 1]
        self.photo_le_name = list_of_atr[3]

    def get_photo_be_ext(self):
        if self.photo_le_name.find('.') != len(self_photo_le_name) -1:
            self.ext = self.photo_le_name[self.photo_le_name.find('.'):]
            return self.ext
        else:
            return None

class Car(Carbase):
    def __init__(self, list_of_atr):
        Carbase.__init__(self, list_of_atr)
        self.passenger_seats_count = int(list_of_atr[2])

class Truck(Carbase):
    def __init__(self, list_of_atr):
        Carbase.__init__(self, list_of_atr)
        self.body_whl = list_of_atr[4]
        if self.body_whl != '':
            self.width = float(self.body_whl[:self.body_whl.find('x')])
            self.middle = self.body_whl[self.body_whl.find('x') + 1:]
            self.height = float(self.middle[:self.middle.find('x')])
            self.length = float(self.middle[self.middle.find('x') + 1:])
        else:
            self.width = 0
            self.height = 0
            self.length = 0

    def get_body_volume(self):
        self.volume = self.width * self.height * self.length
        return self.volume

class Specmachine(Carbase):
    def __init__(self, list_of_atr):
        super().__init__(list_of_atr)
        self.extra = list_of_atr[6]

def get_car_list(filename):
    try:
        object_list = []
        with open(filename) as f:
            for line in f.readlines():
                list_of_atr = line.split(';')
                final = check(line)
                if final == 'car':
                    object = Car(list_of_atr)
                    object_list.append(object)
                elif final == 'truck':
                    object = Truck(list_of_atr)
                    object_list.append(object)
                elif final == 'spec_machine':
                    object = Specmachine(list_of_atr)
                    object_list.append(object)
        return object_list
    except FileNotFoundError:
        print('File does not exist')


def main():
    print(get_car_list('solution.txt'))

if __name__ == '__main__':
        main()
