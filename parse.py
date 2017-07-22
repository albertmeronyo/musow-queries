import pprint

keys = {'GQ' : 'general', 'CT' : 'catalogs', 'DR': 'libraries-repositories', 'DS' : 'datasets', 'DE' : 'digital-editions', 'SS': 'services-software', 'SO' : 'ontologies', 'FO' : 'formats', 'SN' : 'symbolic-notation', 'LD' : 'linked-open-datasets'}

f = open('README.md', 'r')
c = f.read()
l = c.split('</pre>')
names = []
for x in l:
    if len(x.split('**')) > 1:
        if x.split('**')[1][-1] == '.':
            names.append(x.split('**')[1][:-1])
        else:
            names.append(x.split('**')[1])

names = names[-91:]
l = l[:-1]
d = {}

for x in range(len(names)):
    d[names[x]] = l[x]

for key,value in d.iteritems():
    tag = key[0:2]
    d[key] = " ".join(value.split('**')[-1:]).replace('\n\n', '\n')
    d[key] = "#+ summary: " + d[key]
    d[key] = d[key].replace("<pre>", "#+ tags:\n#+    - " + keys[tag] + "\n").replace('&lt;', '<').replace('&gt;', '>')


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)

for key,value in d.iteritems():
    with open(key + '.sparql', 'w') as fw:
        fw.write(value)
