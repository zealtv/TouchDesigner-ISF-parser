def cook(scriptOP):
	scriptOP.clear()
	
	body = False
	
	textfile = 	op('fs_in').text
	numChar = len(textfile)
	
	headStart = textfile.find( '/*' )
	headEnd = textfile.find( '*/' ) 
	
	scriptOP.write( 'number of lines: ', numChar, '\n')
	scriptOP.write( 'start of header: ', headStart, '\n')
	scriptOP.write( 'end of header: ', headEnd, '\n')	



	op('header_out').text = textfile[ headStart + 2 : headEnd ]
	op('shader_out').text = textfile[ headEnd + 2 : numChar ]
	
	
	return
