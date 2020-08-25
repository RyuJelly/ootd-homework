const API_KEY = '0c584632a7b7d1d11a962fcc005458c6';
// today = "", hours = "", minutes = "";
// weatherURL = "";
//https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={YOUR API KEY}

function getTime(){
    let today = new Date();
    //var week = new Array('일','월','화','수','목','금','토');
    var year = today.getFullYear();
    var month = today.getMonth()+1;
    var day = today.getDate();
    let hours = today.getHours();
    let minutes = today.getMinutes();

    return [today, hours, minutes];

    /*
    if(minutes < 10){ // 전 시간 30분
        hours = hours - 1;
        if(hours < 0){
            // 자정 이전은 전날로 계산
            today.setDate(today.getDate() - 1);
            day = today.getDate();
            month = today.getMonth()+1;
            year = today.getFullYear();
            hours = 23;
        }
        minutes = '30';
    }
    else if(minutes < 40){
        minutes = '00';
    }
    else{
        minutes = '30';
    }

    if(hours < 10) hours = '0'+hours;
    if(month < 10) month = '0' + month;
    if(day < 10) day = '0' + day;
    today = year+month+day;
    console.log("<h2>마지막발표: "+today+" "+hours+"시"+minutes+"분</h2>");
    */
}

function getURL(lat, lon){
    /* 좌표 */
    // 광진구 위도/경도: 37.5385° N, 127.0823° E
    // var lat = 37.5385,
    // lon = 127.0823;

    weatherURL = "https://api.openweathermap.org/data/2.5/onecall";
    weatherURL += "?lat=" + lat + "&lon=" + lon;
    weatherURL += "&exclude=" + "minutely,daily";
    //weatherURL += "&lang=kr";
    weatherURL += "&units=metric";
    weatherURL += "&appid="+API_KEY;
    console.log(weatherURL);

    return weatherURL;
}


function getWeather(lat, lng) {
    $.ajax({
        url: getURL(lat, lng),
        method: "GET",
        dataType: 'json',
        error: function(xhr, statud, error){
            alert(error)
        },
        success: function(data) {
            var json = JSON.parse(JSON.stringify(data));
            console.log("ok")
            
            return {
                current: {
                    weather: json.current.weather[0].desciption,
                    temp: json.current.temp
                },

                // ***************** 59분이면? 몇분기준으로 가져와야하나??????
                hourly_1: {
                    weather: json.hourly[1].weather[0].desciption,
                    temp: json.hourly[1].temp
                },

                hourly_2: {
                    weather: json.hourly[1].weather[0].desciption,
                    temp: json.hourly[1].temp
                }
            };

        } //success func 종료
    });
}


// getTime();

// // 실시간 날씨, 1시간 후 날짜 불러오는 URL
// getURL(lat, lng);

// getWeather();