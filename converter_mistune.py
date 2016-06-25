import sys, mistune

def read_md(filename, new_html):
	"""Open the markdown file and return a list containing the new HTML lines."""
	markdown = mistune.Markdown()
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			new_line = markdown(line)
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
