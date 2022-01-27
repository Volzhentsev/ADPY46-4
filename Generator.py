from Data_2 import nested_list

def flat_generator(some_list):
    for item in some_list:
        for item_2 in item:
            yield item_2

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
	    print(item)
    x = list(flat_generator(nested_list))
    print(x)