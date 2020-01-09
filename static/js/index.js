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
            const songdata =JSON.parse(response);
            $('tbody .song').not(':first').remove();
            console.log(songdata.data);
            Object.keys(songdata.data).forEach(function(key){
                var val = this[key];
                console.log(val);
                var dom = $('tbody .song').first().clone();
                    //dom.find('.songIcon').text(val.songIcon);
                    dom.find('.songName').text(val.song_name);
                    dom.find('.songArtist').text(val.artist_name);
                    dom.find('.songLength').text(val.play_time);
                    dom.show();
                    $('tbody').after(dom);
            },songdata.data)
        })
        .fail(function(response){
            console.log('通信失敗');
        })
    })     
}
