import sys
import linkage

print """usage: python transformable.py <linkage-file>
takes in a linkage, fixes (constrains as constant) its original angles,
and then breaks each link in half with a joint in the middle.
output is saved to default location of Linkage.save()"""

link = linkage.Linkage()
link.load(sys.argv[1])

n0 = len(link.vertices)
# split all edges at midpoints:
for l in range(len(link.edges)):
	i,j = link.edges.pop(0)
	xi,yi = link.vertices[i]
	xj,yj = link.vertices[j]
	k = len(link.vertices)
	vk = (0.5*(xi+xj), 0.5*(yi+yj))
	link.vertices.append(vk)
	link.edges.append((i,k))
	link.edges.append((j,k))

# adjacency matrix for original n0 vertices:
adjs = []
for i in range(n0):
	adj = []
	for j,k in link.edges:
		if j==i: adj.append(k)
		elif k==i: adj.append(j)
	adjs.append(adj)

def hasAngle(link,(i,j,k)):
	for a in link.angles:
		if i in a and j in a and k in a:
			return True
	return False

for i in range(len(adjs)):
	adj = adjs[i]
	for k in range(len(adj)-1):
		a = (i, adj[k], adj[k+1])
		if not hasAngle(link,a):
			link.angles.append(a)

link.save()
