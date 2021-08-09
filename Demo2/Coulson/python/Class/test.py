class vehicle(object):
	def __init__(self, speed, size):
		self.__speed = speed
		self.__size = size


class Car(vehicle):
	def __init__(self, speed, size):
		super().__init__(speed,size)

class plane(vehicle):
    def __init__(self, speed, size):
		super(vehicle,self).__init__(speed,size)

class train(vehicle):
	def __init__(self, speed, size):
		super().__init__(speed,size)

