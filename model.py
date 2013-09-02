class Rack(object):
	"""handles all devices and connections"""
	def __init__(self, name):
		self.name = name
		self.devices = {}

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
		if not device:
			return False

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

	def addDevice(self, id, device):
		"""adds new device"""
		self.devices[id] = device


class Device(object):
	"""every part of the rack"""
	def __init__(self, arg):
		super(Device, self).__init__()
		self.arg = arg


class Instrument(Device):
	"""device that represents a hardware synthesizer"""
	def __init__(self, name):
		self.name = name
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
			if param.setValue(value):
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

	def addParam(self, param):
		"""adds new param"""
		self.parameters[param.getName()] = param

	def sync(self):
		"""
		syncs changed parameter with hardware
		"""
		for param in self.parameters.values():
			if not param.isInSync():
				self.send(param.update())


class Utility(Device):
	"""device that processes midi data"""
	def __init__(self, arg):
		super(Utilizy, self).__init__()
		self.arg = arg
		

class Interface(Utility):
	"""communicates with MIDI interface"""
	def __init__(self, arg):
		super(Interface, self).__init__()
		self.arg = arg
		

class Parameter(object):
	"""
	one parameter of a device
	
	@todo: move getName to superclass
	@todo: use super constructor
	"""
	def __init__(self, name):
		self.value = ""
		self.name = name

	def setValue(self, newvalue):
		"""
		sets new value
		"""
		self.value = value


class SynthParam(Parameter):
	"""parameter for an instrument"""
	def __init__(self, name):
		super(SynthParam, self).__init__(name)
		self.inSync = False
		self.midiTemplate = ""

	def update(self):
		"""
		returns MIDI Message to transfer current status to midi device
		"""
		self.setSyncFlag()
		return self.getMIDIMessage()

	def isInSync(self):
		"""returns true if in sync with hardware"""
		return self.inSync

	def setSyncFlag(self):
		"""sets in sync"""
		self.inSync = True

	def unsetSyncFag(self):
		"""unset in sync"""
		self.inSync = False

	def setValue(self, newvalue):
		"""sets new value"""
		if self.isValid(newvalue):
			self.value = newvalue
			self.unsetSyncFag()
			return True
		else:
			return False

	def getValue(self):
		"""gets value"""
		return self.value

	def getName(self):
		"""gets name"""
		return self.name

	def getMIDIMessage(self):
		"""returns midi message"""
		return True

		
class NormalParam(SynthParam):
	"""parameter from 0 to 127"""
	def __init__(self, name):
		super(NormalParam, self).__init__(name)
		self.value = 0

	def isValid(self, value):
		"""tests if value is valid"""
		return (0 <= value <= 127)

		
class EnumParam(SynthParam):
	"""parameter with n different values"""
	def __init__(self, name, valuedict):
		super(EnumParam, self).__init__(name)
		self.valuedict = valuedict
		# set value randomly
		self.value = valuedict.keys()[0]

	def isValid(self, value):
		"""tests if value is valid"""
		return (value in self.valuedict)

	def getData(self):
		"""returns data"""
		return self.valuedict[self.value]

		
class PanParam(SynthParam):
	"""parameter from -64 to 63"""
	def __init__(self, name):
		super(PanParam, self).__init__(name)

	def isValid(self, value):
		"""tests if value is valid"""
		return (-64 <= value <= 63)

	def getData(self):
		"""returns midi value"""
		return self.value + 64


class MIDIMessage(object):
	"""midi message ready to be sent"""
	def __init__(self, arg):
		super(MIDIMessage, self).__init__()
		self.arg = arg
		


class MIDITemplate(object):
	"""
	template for variable midi message
	
	@todo: subclasses for midi CC or PC templates	
	"""
	def __init__(self, arg):
		super(MIDIMessageTemplate, self).__init__()
		self.arg = arg

	def getMessage(self, value):
		"""makes message from value and template"""
		pass
