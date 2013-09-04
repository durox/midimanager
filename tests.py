import unittest
import model

class TestRack(unittest.TestCase):
	"""tests for communication between rack, device, parameter"""
	def setUp(self):
		"""docstring for setUp"""
		self.r1 = model.Rack("testrack")
		d1 = model.Instrument("testinstrument1")
		p1 = model.NormalParam("normalparam1")
		d1.addParam(p1)
		self.r1.addDevice(1, d1)

	def test_change(self):
		"""tests rack change param"""
		self.assertFalse(self.r1.change(2, "param", 64))
		self.assertFalse(self.r1.change(1, "param", 64))
		self.assertFalse(self.r1.change(1, "normalparam1", 200))

		self.assertTrue(self.r1.change(1, "normalparam1", 64))
		self.assertEqual(self.r1.getDeviceByID(1).getParamByName("normalparam1").getValue(), 64)

	def test_messages(self):
		"""tests message delivery between devices"""
		pass


class TestDevice(unittest.TestCase):
	"""tests device"""
	def setUp(self):
		"""docstring for setUp"""
		self.i1 = model.Instrument("instrument1")
		p1 = model.NormalParam("param1")
		p2 = model.NormalParam("param2")
		self.i1.addParam(p1)
		self.i1.addParam(p2)
		self.i1.changeParam("param2", 100)


class TestParameter(unittest.TestCase):
	"""tests creation and manipulation of parameter classes"""
	def setUp(self):
		"""docstring for setUp"""
		pass

	def test_createNormal(self):
		"""tests normal param constructor"""
		np1 = model.NormalParam("normalparam")
		
		# valid values
		self.assertTrue(np1.setValue(60))
		self.assertEqual(np1.getValue(), 60)

		# negative values
		self.assertFalse(np1.setValue(-20))
		self.assertEqual(np1.getValue(), 60)

		# too big values
		self.assertFalse(np1.setValue(200))
		self.assertEqual(np1.getValue(), 60)

	def test_createEnum(self):
		"""tests enum param"""
		d = {"eins" : 1, "zwei" : 2, "drei" : 3}
		ep1 = model.EnumParam("enumparam", d)

		self.assertTrue(ep1.setValue("eins"))
		self.assertEqual(ep1.getValue(), "eins")
		self.assertEqual(ep1.getData(), 1)

		self.assertFalse(ep1.setValue("falsch"))

	def test_createPan(self):
		"""tests pan param constructor"""
		pp1 = model.PanParam("panparam")
		
		# valid values
		self.assertTrue(pp1.setValue(-20))
		self.assertEqual(pp1.getValue(), -20)
		self.assertEqual(pp1.getData(), 44)

		# negative values
		self.assertFalse(pp1.setValue(-80))
		self.assertEqual(pp1.getValue(), -20)

	def test_syncflag(self):
		"""tests correct behavior of sync flag"""
		np = model.NormalParam("param1")

		np.setValue(100)
		self.assertFalse(np.isInSync())

		self.assertTrue(np.update())

		self.assertTrue(np.isInSync())


if __name__ == '__main__':
	unittest.main()
