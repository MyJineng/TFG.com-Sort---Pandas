import requests
import lxml.html as lh
import pandas as pd

url = 'https://tfgames.site/?module=search&engine=35'
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')

tr_elements = doc.xpath('//tr')
col = []
i = 0

for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    print('%d:"%s"'%(i, name))
    col.append((name, []))
# print([[len(T) for T in tr_elements[:107]]]) #107 size 7
for j in range(1, len(tr_elements)):
    T = tr_elements[j]

    if len(T) != 7:
        break
    i = 0
    for t in T.iterchildren():
        data = t.text_content()
        # if i > 0:
        #     try:
        #         data = int(data)
        #     except:
        #         pass
        col[i][1].append(data)
        i += 1
print([len(C) for (title, C) in col])
Dict = {title: column for (title, column) in col}
df = pd.DataFrame(Dict)
df.loc[len(df.index)] = ['Name', 'Author', 'Last Update', 'Rating', 'Likes', 'Engine', 'Themes']
print(df.head())
df.to_excel(r'C:\Users\Andrew Amato\PTFG.xlsx', index = False)


