if op('GLSL'):
	op('GLSL').destroy()

glop = me.parent().create(glslmultiTOP, 'GLSL')

glop.nodeX = me.nodeX
glop.nodeY = me.nodeY - 100
glop.inputConnectors[0].connect(op('in1'))
op('out1').inputConnectors[0].connect(glop)
glop.par.pdat = 'FRAG_SHADER'