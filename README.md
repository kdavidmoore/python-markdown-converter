# Markdown-to-HTML Converter: Python Edition

Demonstrating markdown-to-HTML conversion using Python.

## Contents
1. `converter_custom.py` - a custom Python script that converts markdown headings and paragrahs into their corresponding HTML elements. Currently, there is no support for other types of markdown content (such as lists, code snippets, etc.).
#### Usage
Type into a terminal window: `python converter_custom.py markdown_file_to_convert.md`
An HTML file of the same name (but different file extension) will be automatically generated.
2. `converter_mistune.py` - a command-line tool that uses [mistune](http://mistune.readthedocs.io/en/latest/) to convert Markdown files into HTML files. Support for tables (a la GitHub markdown) should be added.
#### Usage
Type into a terminal window: `python converter_mistune.py markdown_file_to_convert.md`
An HTML file of the same name (but different file extension) will be automatically generated.