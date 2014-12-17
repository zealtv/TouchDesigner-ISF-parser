import json
import uniform_maker



def cook(scriptOP):

	op('create_glop').run()
	print("running clear buffers")
	uniform_maker.clearBuffers()


	scriptOP.clear()
	headertext = op( 'header_out' ).text
	header_dict = json.loads(headertext)
	dict_len = len(header_dict)

	ph = op('parsed_header')
	ph.clear()
	uniform_maker.reset_current_uniform()


 
	#op('res')[0,0] = eval(op('in1').width)
	#op('res')[0,1] = eval(op('in1').height)
	#me.parent().store('width', op('in1').width)
	#me.parent().store('height', op('in1').height)


	#meta
	if "DESCRIPTION" in header_dict:
		description = header_dict["DESCRIPTION"]
		#scriptOP.write("description: ", description, '\n')
		op('META')[0,0] = description
		ph.write("//DESCRIPTION: ", description, "\n")

	if "CREDIT" in header_dict:
		credit = header_dict["CREDIT"]
		#scriptOP.write("credit: ", credit, '\n')
		op('META')[0,1] = credit
		ph.write("//CREDIT: ", credit, "\n")

	#scriptOP.write("\n\n")

	#categories
	category_list = header_dict["CATEGORIES"]
	num_categories = len(category_list)
	#scriptOP.write("number of categories: ", num_categories, '\n')
	ph.write("//Categories: ")

	for i in range (0,num_categories):
		ph.write(category_list[i])
		if i + 1 < num_categories:
			ph.write(", ")

		#scriptOP.write("category ", i, ": ", category_list[i], '\n')

	ph.write("\n\n")

	ph.write("uniform float TIME;\n")
	ph.write("uniform int PASSINDEX;\n")
	ph.write("uniform vec2 RENDERSIZE;\n")

	uniform_maker.make_generic_uniforms()

	ph.write("varying vec2 vv_FragNormCoord;\n")
	ph.write("varying vec3 vv_VertNorm;\n")
	ph.write("varying vec3 vv_VertPos;\n")

	ph.write("\n")

	op('META')[0,2] = category_list

	#scriptOP.write("\n\n")






	#inputs
	num_inputs = len(header_dict["INPUTS"])
	#scriptOP.write("number of inputs: ", num_inputs, "\n")

	for i in range(0,num_inputs):
		input_keys = header_dict["INPUTS"][i].keys()
		#scriptOP.write(header_dict["INPUTS"][i]["TYPE"], "\n")

		if header_dict["INPUTS"][i]["TYPE"] == "float":
			uniform_maker.uFloat( header_dict["INPUTS"][i] )


		if header_dict["INPUTS"][i]["TYPE"] == "int":
			uniform_maker.uInt( header_dict["INPUTS"][i] )

		if header_dict["INPUTS"][i]["TYPE"] == "bool":
			uniform_maker.uBool( header_dict["INPUTS"][i] )


		if header_dict["INPUTS"][i]["TYPE"] == "event":
			uniform_maker.uEvent( header_dict["INPUTS"][i] )

		if header_dict["INPUTS"][i]["TYPE"] == "long":
			uniform_maker.uLong( header_dict["INPUTS"][i] )


		if header_dict["INPUTS"][i]["TYPE"] == "point2D":
			uniform_maker.uPoint2D( header_dict["INPUTS"][i] )

		if header_dict["INPUTS"][i]["TYPE"] == "color":
			uniform_maker.uColor( header_dict["INPUTS"][i] )


		if header_dict["INPUTS"][i]["TYPE"] == "image":
			uniform_maker.uImage( header_dict["INPUTS"][i] )
 
		# scriptOP.write( "input ", i, "\n")		
		# for j in range(0,len(input_keys)):
		# 	key = list(input_keys)[j]
		# 	value = header_dict["INPUTS"][i][key]
		# 	scriptOP.write("\t\t", key, ": ", value, "\n")
		
		#scriptOP.write("\n")

	#scriptOP.write("\n")

	

	#passes
	#TODO if a pass has a key TARGET, that is the buffer to render in that pass
	#if it is not a persistent buffer, a temporary one is created and dies each frame
	# if "PASSES" in header_dict:
	# 	num_passes = len(header_dict["PASSES"])
	# 	scriptOP.write("number of passes: ", num_passes, "\n")

	# 	for i in range(0,num_passes):
	# 		input_keys = header_dict["PASSES"][i].keys()

	# 		#if name key exists, make uniform
	# 		if "NAME" in header_dict["PASSES"][i]:
	# 			uniform_maker.uImage( header_dict["PASSES"][i] )

	# 		scriptOP.write( "pass ", i, "\n")		
	# 		for j in range(0,len(input_keys)):
	# 			key = list(input_keys)[j]
	# 			value = header_dict["PASSES"][i][key]
	# 			scriptOP.write("\t\t", key, ": ", value, "\n")
			
	# 		scriptOP.write("\n")

	# scriptOP.write("\n")


	


	uniform_maker.uDefaultBuffer()




	#persistent buffers
	#could be a an array of strings (names) or a dict with width and height keys
	#TODO: check for string or dict
	#!!!may or may not have keys  
	#this is causing errors when there are no keys
	if "PERSISTENT_BUFFERS" in header_dict:

		#check is string or dict

		buffer_list = header_dict["PERSISTENT_BUFFERS"]
		num_buffers = len(buffer_list)
		scriptOP.write("number of persistent buffers: ", num_buffers, "\n")


		if isinstance(buffer_list[0], str):
			scriptOP.write("STRING!\n")
			for i in range(0, num_buffers):
				uniform_maker.uBuffer(buffer_list[i])

		



		#check for dict
		if isinstance(buffer_list[0], dict):
			scriptOP.write("DICT!\n")






		# buffer_keys = header_dict["PERSISTENT_BUFFERS"].keys()


		# for i in range(0,num_buffers):
		# 	buffer_key = list(buffer_keys)[i]
		# 	this_buffer = header_dict["PERSISTENT_BUFFERS"][buffer_key]
		# 	num_buffer_items = len(this_buffer)
		# 	scriptOP.write( "buffer ", i, "\n")
		# 	scriptOP.write( "\t\t", buffer_key , "\n")

		# 	for j in range(0,num_buffer_items):
		# 		key = list(this_buffer)[j]
		# 		value = this_buffer[key]
		# 		scriptOP.write("\t\t", key, ": ", value, "\n")
		
		scriptOP.write("\n")

	scriptOP.write("\n\n")


	#may need to check for a name key, if doesn't exist use key for dictionary
	if "IMPORTED" in header_dict:
		import_dict = header_dict["IMPORTED"]
		num_imports = len(import_dict)
		scriptOP.write("number of imports: ", num_imports, "\n")
		import_keys = import_dict.keys()

		for i in range(0,num_imports):
			import_key = list(import_keys)[i]
			this_import = import_dict[import_key]
			num_buffer_items = len(this_import)
			scriptOP.write("import ", i, "\n")
			scriptOP.write( "\t\t", import_key , "\n")

			for j in range(0,num_buffer_items):
				key = list(this_import)[j]
				value =this_import[key]
				scriptOP.write("\t\t", key, ": ", value, "\n")

			scriptOP.write("\n")

	scriptOP.write("\n\n")


	#set number of color buffers in glop
	uniform_maker.set_glop_buf_num()
	


	return


