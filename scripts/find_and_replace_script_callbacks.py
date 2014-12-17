# me is this DAT.
# 
# scriptOP is the OP which is cooking.

def cook(scriptOP):
	scriptOP.clear()

	text = op('shader_out').text
	total_int = len(text)

	#scriptOP.write("#total length = ", total_int)


	#insert vUV in the appropriate place if IMG_THIS_PIXEL is found
	start_int = 0
	found_int = text.find("IMG_THIS_PIXEL(", start_int)
	while found_int > 0:
		#scriptOP.write("IMG_THIS_PIXEL( found at: ", found_int, "\n")
		found_int = text.find( ");", found_int )
		#scriptOP.write("); found at: ", found_int)
		hashlist = list(text)
		hashlist.insert(found_int, ", vUV.st")
		text = ''.join(hashlist)

		start_int = found_int
		found_int = text.find("IMG_THIS_PIXEL(", start_int)


	#insert vUV in the appropriate place if IMG_THIS_NORM_PIXEL is found
	start_int = 0
	found_int = text.find("IMG_THIS_NORM_PIXEL(", start_int)
	while found_int > 0:
		#scriptOP.write("IMG_THIS_PIXEL( found at: ", found_int, "\n")
		found_int = text.find( ");", found_int )
		#scriptOP.write("); found at: ", found_int)
		hashlist = list(text)
		hashlist.insert(found_int, ", vUV.st")
		text = ''.join(hashlist)

		start_int = found_int
		found_int = text.find("IMG_THIS_PIXEL(", start_int)



	text = text.replace("IMG_THIS_PIXEL", "texture")
	text = text.replace("IMG_THIS_NORM_PIXEL", "texture")
	text = text.replace("IMG_PIXEL", "texture")
	text = text.replace("IMG_NORM_PIXEL", "texture")
	text = text.replace("PASSINDEX", "uTDPass")

					


	#make this dynamic
	text = text.replace("inputImage", "sTD2DInputs[0]")
	

	text = text.replace("gl_FragColor", "fragColor")


	text = text.replace("vv_FragNormCoord", "vUV.st")
	#text = text.replace("vv_FragNormCoord", "vec2(vUV.s, vUV.t / 2.0)")
	text = text.replace("gl_FragCoord.xy", "vUV.st")

	scriptOP.write(text)



	return
