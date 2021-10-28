String API
Check your string for how many uppercase letters, lowercase letters, numbers or special characters it has. Any combination is supported.  

required packages:
	1.Flask (pip install flask)

Endpoints:

1. /checkstring (POST)
	
	Endpoint accepts string and return json with result of calculations

	Arguments: "string" (type: string)
	
	Example of usage

	request -> http://127.0.0.1:5000/checkstring?string=Szymon
	
	response ->{"upper_case": 1, 
		"lower_case": 5, 
		"numbers": 0, 
		"special_characters": 0
		}
