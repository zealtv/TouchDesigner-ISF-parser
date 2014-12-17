import create_buffer

glop = op('GLSL')
current_uniform = 0
current_buffer = 0
resx = 1280
resy = 720

def reset_current_uniform():
	global current_uniform
	current_uniform = 0
	current_buffer = 0
	return


def set_glop_buf_num():
	print( "setting number of color buffers: ", current_buffer) 
	op('GLSL').par.numcolorbufs.val = current_buffer
	return



def make_generic_uniforms():
	global current_uniform

	current_uniform = 0

	glop = op('GLSL')

	#make TIME
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, "TIME")
	val = "value" + str(current_uniform) + "x"
	#setattr(glop.expr, val, "me.time.absSeconds")
	#THIS IS HACKY
	glop.par.value0x.expr = "me.time.absSeconds"

	current_uniform += 1

	#make RENDERSIZE
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, "RENDERSIZE")
	val = "value" + str(current_uniform) + "x"
	setattr(glop.par, val, resx)
	val = "value" + str(current_uniform) + "y"
	setattr(glop.par, val, resy)
	current_uniform += 1




def uFloat( data ):
	global current_uniform

	#get name
	name = data["NAME"]
	#write uniform to shader
	op('parsed_header').write( "uniform float ", name, ";\n" )
	#set uniform in operator
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, name)


	#check for and get default
	if "DEFAULT" in data:
		default = data["DEFAULT"]
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , default)


	#get min
	#get max
	#get label
	#get identity

	current_uniform += 1
	return




# NO INT IN ISF SPEC?
def uInt( data ):
	op('parsed_header').write( "uniform int ", data["NAME"], ";\n" )
	#get min
	#get max
	#get default
	#get label
	#get identity	
	return




def uBool( data ):
	global current_uniform

	#get name
	name = data["NAME"]
	#write uniform to shader
	op('parsed_header').write( "uniform bool ", name, ";\n" )
	#set uniform in operator
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, name)


	#check for and get default
	if "DEFAULT" in data:
		default = data["DEFAULT"]
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , default)

	#get min
	#get max
	#get label
	#get identity

	current_uniform += 1
	return	




def uEvent( data ):
	global current_uniform

	#get name
	name = data["NAME"]
	#write uniform to shader
	op('parsed_header').write( "uniform bool ", name, ";\n" )
	#set uniform in operator
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, name)


	#check for and get default
	if "DEFAULT" in data:
		default = data["DEFAULT"]
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , default)
	else:
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , 0)

	#get min
	#get max
	#get label
	#get identity

	current_uniform += 1	
	return





	#TODO - how to handle these?

def uLong( data ):
	global current_uniform

	#get name
	name = data["NAME"]
	#write uniform to shader
	op('parsed_header').write( "uniform int ", data["NAME"], ";\n" )
	#set uniform in operator
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, name)


	#check for and get default
	if "DEFAULT" in data:
		default = data["DEFAULT"]
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , default)


	#get min
	#get max
	#get default
	#get label
	#get identity
	#get VALUES
	#get LABELS	
	current_uniform += 1
	return





def uPoint2D( data ):
	global current_uniform

	#get name
	name = data["NAME"]
	#write uniform to shader
	op('parsed_header').write( "uniform vec2 ", data["NAME"], ";\n" )
	#set uniform in operator
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, name)


	#check for and get default
	if "DEFAULT" in data:
		default = data["DEFAULT"]
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , default[0])
		val = "value" + str(current_uniform) + "y"
		setattr(glop.par, val , default[1])

	#get min
	#get max
	#get label
	#get identity

	current_uniform += 1	
	return




def uColor( data ):
	global current_uniform

	#get name
	name = data["NAME"]
	#write uniform to shader
	op('parsed_header').write( "uniform vec4 ", data["NAME"], ";\n" )
	#set uniform in operator
	uni = "uniname" + str(current_uniform)
	setattr(glop.par, uni, name)


	#check for and get default
	if "DEFAULT" in data:
		default = data["DEFAULT"]
		val = "value" + str(current_uniform) + "x"
		setattr(glop.par, val , default[0])
		val = "value" + str(current_uniform) + "y"
		setattr(glop.par, val , default[1])
		val = "value" + str(current_uniform) + "z"
		setattr(glop.par, val , default[2])
		val = "value" + str(current_uniform) + "w"
		setattr(glop.par, val , default[3])

	#get min
	#get max
	#get label
	#get identity

	current_uniform += 1	
	return



def uImage( data ):
	#TODO - how to handle these?
	#op('parsed_header').write( "uniform sampler2DRect ", data["NAME"], ";\n" )
	# op('parsed_header').write( "uniform vec4 _", data["NAME"], "_imgRect;\n" )
	# op('parsed_header').write( "uniform vec2 _", data["NAME"], "_imgSize;\n" )
	# op('parsed_header').write( "uniform bool _", data["NAME"], "_flip;\n" )
	# op('parsed_header').write( "varying vec2 _", data["NAME"], "_texCoord;\n" )
	op('parsed_header').write( "\n" )

	#get min
	#get max
	#get default
	#get label
	#get identity	
	return




def uDefaultBuffer():
	global current_buffer

	current_buffer = 0

	op('parsed_header').write("layout (location = ", current_buffer, ") out vec4 fragColor;")
	op('parsed_header').write( "\n" )
	print("adding buffer #:", current_buffer)

	current_buffer += 1
	return



def uBuffer( nameString ):
	global current_buffer

	#write output location to header
	op('parsed_header').write("layout (location = ", current_buffer, ") out vec4 ", nameString,";")
	op('parsed_header').write( "\n" )

	#create buffer

	create_buffer.add_buffer(nameString, current_buffer)

	current_buffer += 1
	return


def uBufferDict( buffer_dict ):
	return


def clearBuffers():
	create_buffer.clear_buffers()
	return