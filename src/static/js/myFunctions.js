selected_word = null
words_to_be_anonymized = []
words_to_be_excluded = []

$(document).ready(function () {
    $("#anonymized_text").click(function () {
        // Get word
        word = window.getSelection().toString();
        if (word != '') {
            selected_word = word;
            fade_anonymize_word_button();
            document.getElementById('anonymize_word_button').style.opacity = 1;

        }
    });
});


$(document).ready(function () {
    $("#original_document").click(function () {
        // Get word
        word = window.getSelection().toString();
        if (word != '') {
            selected_word = word;
            fade_exclude_word_button();
            document.getElementById('exclude_word_button').style.opacity = 1;
        }
    });
});

function fade_anonymize_word_button() {
    var i = 0;
    var h1 = document.getElementById("anonymize_word_button");
    h1.style.opacity = 0.5;
    var k = window.setInterval(function () {
        if (i >= 10) {
            clearInterval(k);
        } else {
            h1.style.opacity = i / 10;
            i++;
        }
    }, 100);

}


function fade_exclude_word_button() {
    var i = 0;
    var h1 = document.getElementById("exclude_word_button");
    h1.style.opacity = 0.5;
    var k = window.setInterval(function () {
        if (i >= 10) {
            clearInterval(k);
        } else {
            h1.style.opacity = i / 10;
            i++;
        }
    }, 100);

}


function addWordsToBeAnonymized() {
    if (selected_word != null) {
        words_to_be_anonymized.push(selected_word)
    }
    selected_word = null;
    console.log(words_to_be_anonymized)
    // Document.activeElement.style.opacity = 0;
    window.getSelection().empty();

}


function addWordsToBeExcluded() {
    if (selected_word != null) {
        words_to_be_excluded.push(selected_word)
    }
    selected_word = null;
    console.log(words_to_be_excluded)
    // Document.activeElement.style.opacity = 0;
    window.getSelection().empty();

}

function updateText() {
    base_url = window.location.href.split('?')[0]
    // console.log(base_url)
    new_url = base_url + '?text_param=' + JSON.stringify(words_to_be_anonymized)
        + ';exclude_text_param=' + JSON.stringify(words_to_be_excluded);
    words_to_be_anonymized = [];
    selected_word = null;
    //     setTimeout(function () { window.location = new_url; }, 2000);
    //     // window.location = new_url;
    // }
    window.location = new_url;
}

function updateUserDictionary() {
    base_url = window.location.href.split('?')[0]
    new_url = base_url + '?user_dictionary_param=' + JSON.stringify(words_to_be_anonymized);
    words_to_be_anonymized = [];
    selected_word = null;
    window.location = new_url;
}

function updateExcludeUserDictionary() {
    base_url = window.location.href.split('?')[0]
    new_url = base_url + '?user_exclude_dictionary_param=' + JSON.stringify(words_to_be_excluded);
    words_to_be_excluded = [];
    selected_word = null;
    window.location = new_url;
}

function deleteWordsToBeAnonymized(n) {
    debugger;
    if (n == -1) {
        words_to_be_anonymized = [];
        base_url = window.location.href.split('?')[0]
        temp = base_url.split('/');
        new_url = '';
        for (i = 0; i < temp.length - 2; i++) {
            new_url += temp[i] + '/';
        }
        id = temp[temp.length - 1];
        new_url += 'delete_anonymized_words/' + id;
        window.location = new_url;

    }
    else if (n > -1) {
        words_to_be_anonymized.splice(n, 1);
    }
    else {
        console.log('Error not valid number of deleteWordsToBeAnonymized array');
    }
}

function deleteWordsToBeExcluded(n) {
    console.log('that.');
    debugger;
    if (n == -1) {
        words_to_be_excluded = [];
        base_url = window.location.href.split('?')[0]
        temp = base_url.split('/');
        new_url = '';
        for (i = 0; i < temp.length - 2; i++) {
            new_url += temp[i] + '/';
        }
        id = temp[temp.length - 1];
        new_url += 'delete_excluded_words/' + id;
        console.log(new_url);
        window.location = new_url;

    }
    else if (n > -1) {
        words_to_be_excluded.splice(n, 1);
    }
    else {
        console.log('Error not valid number of deleteWordsToBeExcluded array');
    }
}



