
class Lindenmayer:
	def __init__(self,rules):
		"""construct a Lindenmayer with the given map from characters to strings"""
		self.rules = rules

	def step(self,s):
		"""perform one step on the string s"""
		s1 = ''
		for c in s:
			if c in self.rules:
				s1+=self.rules[c]
			else:
				s1+=c
		return s1

	def iter(self,s,n):
		"""perform n steps on the string s"""
		for i in range(n):
			s = self.step(s)
		return s
