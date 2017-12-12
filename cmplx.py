class Cmplx:
	def __init__ (self, real, imaginary):
		self.r = real
		self.i = imaginary
	def __str__ (self):
		if self.i == 0 and self.r == 0:
			return "0+0i"
		elif self.i == 0:
			return str(self.r)
		elif self.r == 0:
			return str(self.i) + "i"
		elif self.i < 0:
			return 	str(self.r) + str(self.i) + "i"
		return str(self.r) + "+" + str(self.i) + "i"
	def __repr__ (self):
		return '(%s, %s)' % (self.r, self.i)
	def __bool__ (self):
		if self.r <> 0 and self.i <> 0:
			return True
		return False
	def __eq__ (first, second):
		if first.r <> second.r and first.i <> second.i:
			return False
		return True
	def __ne__ (first, second):
		return not (first == second)
	def __abs__ (self):
		return (self.r ** 2 + self.i ** 2) ** (0.5)
	def __invert__ (self):
		return Cmplx(self.r, -self.i)
	def __add__ (first, second):
		return Cmplx(first.r + second.r, first.i + second.i)
	def __iadd__ (first, second):
		return Cmplx(first.r + second.r, first.i + second.i)
	def __sub__ (minuend, subtrahend):
		return Cmplx(minuend.r - subtrahend.r, minuend.i - subtrahend.i)
	def __isub__ (minuend, subtrahend):
		return Cmplx(minuend.r - subtrahend.r, minuend.i - subtrahend.i)
	def __mul__ (first, second):
		return Cmplx(first.r * second.r - first.i * second.i, first.r * second.i + first.r * second.i)
	def __imul__ (first, second):
		return Cmplx(first.r * second.r - first.i * second.i, first.r * second.i + first.r * second.i)
	def __div__ (first, second):
		first.r  = float(first.r)
		first.i  = float(first.i)
		second.r = float(second.r)
		second.i = float(second.i)
		r = (first.r * second.r + first.i * second.i) / ((first.r ** 2) + (first.i ** 2))
		i = (first.i * second.r - first.r * second.i) / ((first.r ** 2) + (first.i ** 2))
		return Cmplx(r, i)
	def __neg__ (self):
		return Cmplx(-self.r, -self.i)
	def __pow__ (self, p):
		for i in range(p):
			self *= self
		return self
