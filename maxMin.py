def find_max_min(list):#function declaration
	list.sort();#call sort function
	return [list[0]] if list[0] is list[(len(list)-1)] else [list[0], list[(len(list)-1)]]#return maximum and minimum pairs