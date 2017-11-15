// Some examples:
// findClosestCities('3039154', 3);
// findLexicalMatch('North');

$("#submit-proximity").click(function(event) {
    event.preventDefault();
    var cityId = $("#cityId").val();
    var numCities = $("#numCities").val();
    findClosestCities(cityId, numCities);
})

$("#submit-lexical").click(function(event) {
    event.preventDefault();
    var inputWord = $("#inputWord").val();
    findLexicalMatch(inputWord);
})


function findClosestCities(cityId, numCities) {

    var html_string = '<h3><center> Processing... </center></h3>';
    $("#result").html(html_string);
    $.getJSON('/findClosestCities/' + cityId + '/' + numCities, function (data) {
        console.log(data);
        if (data == 0){
            var html_string = '<h3><center> No Cities Found -- please try another City ID </center></h3>';
        } else {
            var html_string = '<h3><center> Closest Cities </center></h3><ul>';
            for (var i = 0; i < data.length; i++){
                html_string += '<li>' + data[i][2] + '</li>';
            }
            html_string += '</ul>';
        }
        $("#result").html(html_string);
    });
}

function findLexicalMatch(inputWord) {
    var html_string = '<h3><center> Processing... </center></h3>';
    $("#result").html(html_string);
    $.getJSON('/findLexicalMatch/' + inputWord, function (data) {
        console.log(data);
        var html_string = '<h3><center> Lexical Matches </center></h3><ul>';
        for (var i = 0; i < data.length; i++){
            html_string += '<li>' + data[i] + '</li>';
        }
        html_string += '</ul>';
        $("#result").html(html_string);
    });
}

