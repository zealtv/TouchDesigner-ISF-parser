#if op('GLSL'):
#	op('GLSL').destroy()
buffer_list = []


def add_buffer(name, index, width = None, height = None):
	global buffer_list
	

	buffer = me.parent().create(renderselectTOP, name)

	buffer_list.append(name)

	buffer.nodeX = me.nodeX
	buffer.nodeY = me.nodeY - (100 * index)
	
	
	op('GLSL').inputConnectors[index].connect(buffer)
	
	buffer.par.top = 'GLSL'
	buffer.par.colorbufindex = index


	if width == None or height == None:
		return

	buffer.par.outputresolution = 9
	buffer.par.resolution1 = width
	buffer.par.resolution2 = height

	return
	

def clear_buffers():
	global buffer_list
	
	print("inside clear buffers")

	for i in range(len(buffer_list), 0):
		print("deleting ", buffer_list[i])
		op(buffer_list[i]).destroy()
	
	buffer_list = []

	return


