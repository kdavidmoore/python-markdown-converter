import sys

def read_md(filename, new_html):
	"""Open the markdown file and return a list containing the new HTML lines."""
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			new_line = ''
			level = 0
			for char in line:
				if char == "#":
					level += 1
					f.seek(1, 1)
					if f.read(1) == "#":
						level += 1
						f.seek(1, 1)
						if f.read(1) == "#":
							level += 1
							f.seek(1, 1)
							if f.read(1) == "#":
								level += 1
			if level == 1:
				new_line += '<h1>'
				new_line += line[2:]
				new_line += '</h1>'
			elif level == 2:
				new_line += '<h2>'
				new_line += line[3:]
				new_line += '</h2>'
			elif level == 3:
				new_line += '<h3>'
				new_line += line[4:]
				new_line += '</h3>'
			elif level == 4:
				new_line += '<h4>'
				new_line += line[5:]
				new_line += '</h4>'
			elif len(line) > 1:
				new_line += '<p>'
				new_line += line
				new_line += '</p>'
			else:
				pass
			new_html.append(new_line)
	f.close()
	return new_html

def write_html(filename, new_html):
	"""Write the new HTML to an HTML file."""
	with open(filename[:-3] + '.html', 'w') as f:
		f.write('')
		for line in new_html:
			f.write(line + '\n')
	f.close()

def main(argv):
	html = []
	new_html = read_md(argv[1], html)
	write_html(argv[1], new_html)

if __name__ == "__main__":
	main(sys.argv)
