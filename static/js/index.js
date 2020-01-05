$(document).ready(function(e){
    getMusicData();
})
function getMusicData(){
    var first = true;
    $(function(){
        $.ajax({
            url: '../api/music.py',//送信先
            type: 'GET',//送信方法
            datatype: 'json',//受け取りデータの種類
            data:{
                'first' :  first   
            }
        })
        .done(function(response){
            $('.song').not('#songTitle').remove();
            Object.keys(response.music_data).forEach(function(key){
                var val = this[key];
                var dom = $('.song').not('#songTitle').first().clone();
                    //dom.find('.songIcon').text(val.songIcon);
                    dom.find('.songName').text(val.songName);
                    dom.find('.songArtist').text(val.songArtist);
                    dom.find('.songLength').text(val.songLength);
                    dom.show();
                    $('#songTitle').after(dom);
            },response.music_data)
        })
        .fail(function(response){
            console.log('通信失敗');
        })
    })     
}
