/**
 * 指定された要素にクリックイベントを追加
 * @param target_dom
 * @param target_music_data
 */
function add_storage_event(target_dom, target_music_data) {
    $(target_dom).click(function (event) {
        console.log(event);
        console.log(target_music_data);
    });
}