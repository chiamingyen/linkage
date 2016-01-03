import math
import linkage

class Turtle:
	EPS = 1

	def __init__(self,draws,angle,r=1,x0=0,y0=0):
		self.draws=draws
		self.angle=angle
		self.r=r
		self.x0=x0
		self.y0=y0

	def makeLinkage(self,s):
		"""build a linkage from the turtle graphics string s,
		connecting each vertex to the previous one,
		with duplicate/very-near vertices reduced to a single vertex."""
		link = linkage.Linkage()
		x,y,theta,i = (self.x0,self.y0,0,0)
		link.vertices.append((x,y))
		p=[]
		for c in s:
			if c=='[':
				p.append((x,y,theta,i))
			elif c==']':
				x,y,theta,i = p.pop()
			elif c=='+':
				theta += self.angle
			elif c=='-':
				theta -= self.angle
			if c in self.draws:
				x += self.r*math.cos(math.radians(theta))
				y += self.r*math.sin(math.radians(theta))
				j = link.findVertex(x,y)
				if link.vertexDist2(x,y,j)>=Turtle.EPS: # already a vertex here?
					j = len(link.vertices)
					link.vertices.append((x,y))
				if i<j and (i,j) not in link.edges:
					link.edges.append((i,j))
				elif i>j and (j,i) not in link.edges:
					link.edges.append((j,i))
				elif i==j: print 'TINY!' # step was very small...
				i = j
		return link
