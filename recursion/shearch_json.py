title = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}


def rec(sl, search):
    if search in sl.keys():
        return sl[search]

    for n in sl.values():
        if type(n) == dict:
            print(n, '\n')
            ret = rec(n, search)
            if ret != None:
                return ret


#print(rec(title, "GlossSeeAlso"))
rec(title, "GlossSeeAlso")