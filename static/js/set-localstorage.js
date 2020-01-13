let search_data = JSON.parse(localStorage.getItem('search_data'));
if(!search_data) {
    search_data = {
        "bpm_division": [
            0,
            0,
            0
        ],
        "play_time_division": [
            0,
            0,
            0
        ]
    };
    localStorage.setItem('search_data', JSON.stringify(search_data));
}

/**
 * 指定された要素にクリックイベントを追加
 * @param target_dom
 * @param target_music_data
 */
function add_storage_event(target_dom, target_music_data) {
    $(target_dom).click(function (event) {
            search_data.bpm_division[target_music_data.bpm_division - 1]++;
            localStorage.setItem('search_data', JSON.stringify(search_data));
    });
}