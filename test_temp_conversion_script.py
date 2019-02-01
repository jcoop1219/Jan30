from temp_conversion_script import convert_c_to_f
from temp_conversion_script import fever_detection

def test_convert_c_to_f():
	answer = convert_c_to_f(20.0)
	expected = 68.0
	assert answer == expected

def test2():
	answer = convert_c_to_f(-40.0)
	expected = -40.0
	assert answer == expected

def test_fever_detection():
	temp_list = [93.0, 98.0, 100.0, 105.0, 101.0]
	max_temp, is_fever = fever_detection(temp_list)
	expected_max = 105.0
	is_fever = True
	assert max_temp == expected_max
