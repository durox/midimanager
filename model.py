class Rack(object):
	"""handles all devices and connections"""
	def __init__(self):
		devices = {}

	def change(self, deviceID, paramName, newValue):
		"""
		changes one parameter of a device in this rack

		@param deviceID: unique ID of device
		@type deviceID: int
		@param paramName: unique Name of parameter
		@type paramName: string
		@param newValue: new value for parameter

		@return: true if successful
		@rtype: bool
		"""

		device = self.getDeviceByID(deviceID)
		if device.changeParam(paramName, newValue):
			return True
		else:
			return False

	def getDeviceByID(self, devID):
		"""
		returns device by ID

		@param devID: device ID
		@type devID: int

		@return: device with given ID or None
		@rtype: Device
		"""

		return self.devices.get(devID, None)


class Device(object):
	"""every part of the rack"""
	def __init__(self, arg):
		super(Device, self).__init__()
		self.arg = arg


class Instrument(Device):
	"""device that represents a hardware synthesizer"""
	def __init__(self, arg):
		self.parameters = {}
		
	def changeParam(self, paramName, value):
		"""
		changes parameter

		@param paramName: parameter Name
		@type paramName: string
		@param value: new value

		@return: true if succesful
		@rtype: bool
		"""
		param = self.getParamByName(paramName)
		if param:
			if param.change(value):
				return True
			else:
				return False
		else:
			return False

	def getParamByName(self, paramName):
		"""
		returns parameter by name
		"""
		return self.parameters.get(paramName, None)


class Parameter(object):
	"""one Parameter of an instrument"""
	def __init__(self, arg):
		super(Parameter, self).__init__()
		self.arg = arg


class Interface(midimanager.Utility):
	"""device to communicate with the MIDI Adapter"""
	def __init__(self, arg):
		super(Interface, self).__init__()
		self.arg = arg
