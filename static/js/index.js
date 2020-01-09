$(document).ready(function(e){
    getMusicData();
})
function getMusicData(){
    var first = true;
    $(function(){
        $.ajax({
            url: 'api/music',//送信先
            type: 'GET',//送信方法
            datatype: 'json',//受け取りデータの種類
            data:{
                'first' :  first   
            }
        })
        .done(function(response){
            console.log(response.data);
            $('.song').not('#songTitle').remove();
            Object.keys(response.data).forEach(function(key){
                var val = this[key];
                var dom = $('.song').not('#songTitle').first().clone();
                console.log(val.play_time);
                    //dom.find('.songIcon').text(val.songIcon);
                    dom.find('.songName').text(val.song_name);
                    dom.find('.songArtist').text(val.artist_name);
                    dom.find('.songLength').text(val.play_time);
                    dom.show();
                    $('#songTitle').after(dom);
            },response.music_data)
        })
        .fail(function(response){
            console.log('通信失敗');
        })
    })     
}
