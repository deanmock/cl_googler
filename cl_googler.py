#cl_googler.py
#search google in command line

import sys, webbrowser
if len(sys.argv) > 1:
	search_term = ' '.join(sys.argv[1:])
else:
	print("Enter an actual search term")
webbrowser.open("https://www.google.com/search?source=hp&ei=O3p6XuipLcbisAWNr7m4Aw&q=" + search_term + "&oq=" + search_term + "&gs_l=psy-ab.3..0l10.12107.16959..17189...6.0..0.219.1563.11j3j2......0....1..gws-wiz.....6..0i362i308i154i357..26%3A93.v2y_LXzvtBY&ved=0ahUKEwios4jdhbToAhVGMawKHY1XDjcQ4dUDCAc&uact=5")

#is there a way to make this program open multiple tabs for multiple inputs?