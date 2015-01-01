# Selection sort
def sort(l):
	n = []
	max_index = -1
	for i in range(len(l)):
		for j in range(0, l):
			if the_max == -1:
				max_index = j
			elif l[j] > l[max_index]:
				max_index = j
		n.append(l[j])
	return n