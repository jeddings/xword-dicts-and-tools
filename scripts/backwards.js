



var list = ["emit", "repaid", "mined", "edit"];
var list_len = len(list);
var phrases = new Array();

function match(phrase, words[], length) {
	for (i = 0; i < words.length - 1; i++) {

		if (phrase.length + words[i].length == length) {
			return(phrase + words[i]);
		}
	}

	return "";
}



for (var i = 0; i < list_len - 1; i++) {
	
	var word = list[i];

	for (var j = 0; j < list_len - 1; j++) {
		var phrase = word + list[j];

		if (match(phrase, list, 15)) {
			phrases.append(phrase);
		} else {

			for (var k = 0; k < list_len - 1; k++) {
				var comp_2 = list[k];
				phrase = phrase + comp_2;
				if (match(phrase, list, 15)) {
					phrases.append(phrase);
				}

			}
		}
	}
}


/*
	for (var k = 0; k < len(phrases); k++) {
		var phrase = phrases[k];

		for (m = 0; m < len(phrases[k]); m++) {

			top_phrase
			bottom_phrase
			left_phrase
			right_phrase
			center_down_phrase
			center_across_phrase

			if top[4] = left[3]


			top_phrase[]

			for( )
			top_left_cross
			top_right_cross
			bottom_left_cross
			bottom_right_cross

		}
	}
*/
}


/* var list = ["emit", "repaid", "mined", "edit"];

for (var i = 0; i < len(list); i++) {
	
	var word = list[i];
	var word_len = len(word);
	var phrases = new Array();
	var phrases_2 = new Array();
	var phrases_3 = new Array();
	var phrases_4 = new Array();

	for (var j = 0; j < len(list[i]); j++) {
		var comp = list[j];
		var comp_len = len(comp);

		if (word_len + comp_len = 15) {
			phrases.append(word + " " + comp);
		}


	}

	for (var k = 0; k < len(phrases); k++) {
		var phrase = phrases[k];

		for (m = 0; m < len(phrases[k]); m++) {

			top_phrase
			bottom_phrase
			left_phrase
			right_phrase
			center_down_phrase
			center_across_phrase

			if top[4] = left[3]


			top_phrase[]

			for( )
			top_left_cross
			top_right_cross
			bottom_left_cross
			bottom_right_cross

		}
	}

}

*/

