def convert_c_to_f(temp_C):
	temp_F = temp_C * 1.8 + 32
	return temp_F

def main_code():
	temp_C_str = input("Enter temp in degC: ")
	temp_C = float(temp_C_str)
	temp_F = convert_c_to_f(temp_C)
	print("The temperature is {} degF.".format(temp_F))

def fever_detection(temp_list):
	max_temp = max(temp_list)
	fever_threshold = 100.5
	is_fever = False
	for temperature in temp_list:
		if temperature > fever_threshold:
			is_fever = True
	return max_temp, is_fever

if __name__ == "__main__":
	main_code()
