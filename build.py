import csv, json, os
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
rows=list(csv.DictReader(open('../MSB_catalogo_septiembre_2026.csv',encoding='utf-8-sig')))
cats={'PER':'Perfumes árabes','DIS':'Perfumes de diseñador','BEL':'Belleza','LIB':'Libros','TEC':'Tecnología y lifestyle'}
items=[]
for r in rows:
    k=r['ID'].split('-')[0]
    has=os.path.exists(f"img/products/{r['ID']}.jpg")
    items.append(dict(id=r['ID'],cat=cats.get(k,r['Categoría']),sec=r['Sección'],marca=r['Marca'],prod=r['Producto'],pres=r['Presentación/variante'],ref=r['Referencia olfativa (dupe / inspirado en)'],dur=r['Duración (según catálogo)'],img=1 if has else 0))
data=json.dumps(items,ensure_ascii=False)
tpl=open('template.html',encoding='utf-8').read().replace('__DATA__',data)
open('index.html','w',encoding='utf-8').write(tpl)
print(len(items),'products;',sum(i['img'] for i in items),'with image')
