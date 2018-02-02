def cript_string(word):
	SIZE = len(word)
	HALF = SIZE / 2;
	
	//Shift 3
	for i in range()(int i = 0; i < len; i++){
		if(isalpha(word[i])){
			word[i] = char(word[i]+3);
		}		
	}
	
	//reverse
	string reverse = "";
	
	for(int i = len - 1; i >=  0; i--){
		reverse += word[i];		
	}
	
	word = reverse;
	
	for(int i = half; i < len; i++){
		word[i] = char(word[i]-1);
	}
	
	return word;


times = int(raw_input())

for i in range(times):
	word = raw_input()
