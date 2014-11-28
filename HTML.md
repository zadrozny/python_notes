# HTML

'''
By default, HTML+ documents are made up of 8-bit characters from the ISO 8859 Latin-1 character set. The network protocol used to retrieve documents may translate the character set into a locally acceptable form, e.g. EBCDIC. The HTTP protocol uses the MIME standard (RFC 1341) to specify the document type and character set. ISO SGML entity definitions are used to include characters which are missing from the character set or which would otherwise be confused with markup elements, e.g:

<tt>
&amp;</tt>
    ampersand & 

&lt;
    less than sign < 

&gt;
    greater than sign > 

&quot;
    the double quote sign " 

http://www.w3.org/MarkUp/HTMLPlus/htmlplus_13.html
'''


'''
HTML Entities and/or ISO Latin-1 codes can be placed in source code like any other alphanumeric characters to produce special characters and symbols that cannot be generated in HTML with normal keyboard commands.

For example, to render Düsseldorf the HTML source should read

    D&uuml;sseldorf or D&#252;sseldorf
'''

# Replacing html entities with the corresponding utf-8 characters in Python 2.6 

http://stackoverflow.com/q/730299/1366410

'''
example_html = '&quot;Sign Up&quot; Soccer for Social Change, nysoccerproject),(Agency &amp; Media Innovators using Social Media Data for Brands'
'''