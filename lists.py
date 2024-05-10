def remove_elements(x):
	if len(x)>0:
		del x[0]
		if len(x)>3:
			del x[3]
			if len(x)>3:
				del x[3]
		return x			
	else:
		return x

def add_elements(x):
	x.insert(0,"Pink")
	x.insert(len(x), "Yellow")
	return x
#add_elements=['Red', 'Green', 'White', 'Black']
#print(add_elements(add_elements))

def is_empty(lista):
	if lista==[]:
		return True
	else:
		return False


def check_lists(x,y):
	if len(x)>2 and len(y)>2:
		if x[2]==y[2]: 
			return True
		else:
			return False
	else:
		return False


def list_of_lists(x):
	if len(x)>2:
		if len(x[0])>=1:
			p1 = x[0][0:2]
		else:
			p1=[]

		if len(x[1])>=2:
			p2=x[1][1:4]
		else:
			p2=[]
		if len(x[2])>=1:
			p3=x[2][-2:]
      		else:
			p3=[]
		return [p1, p2, p3]
