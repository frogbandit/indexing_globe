var numTweets = '';
var twitterHandle = '';

$("#numTweets").change(function(){
    numTweets = $('#numTweets').val();
    if ((numTweets != '') && (twitterHandle != '')){
        console.log(twitterHandle, numTweets)
        get_data(twitterHandle, numTweets)
    }
})

$("#twitterHandle").change(function(){
    twitterHandle = $('#twitterHandle').val();
    if ((numTweets != '') && (twitterHandle != '')){
        console.log(twitterHandle, numTweets)
        get_data(twitterHandle, numTweets)
    }
})


// some examples: ishantlguru, realDonaldTrump, justinbieber
findClosestCities('3039154', 3);

function findClosestCities(cityId, numCities) {
    var startTime = new Date();
    $('#container').append('<div style="height: 800px" id="total_chart"></div>');

    console.log('hi');
    $.getJSON('/findClosestCities/' + cityId + '/' + numCities, function (data) {
        console.log(data);
    });
}

