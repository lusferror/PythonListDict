all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(colores):
	return colores["label"]=="Red" or colores["label"]=="Orange" or colores["label"]=="Pink" or colores["label"]=="Violet"
new_list_colores =list(filter(filter_colors , all_colors))

def generate_li(colores):
	return "<li>"+colores["label"]+"<li>"
new_list_colores_li= list(map(generate_li,new_list_colores))
print(new_list_colores_li)