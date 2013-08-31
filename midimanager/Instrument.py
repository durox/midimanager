class Instrument(Device):
	"""device that represents a hardware synthesizer"""
	def __init__(self, arg):
		super(Instrument, self).__init__()
		self.arg = arg
		
