$(document).ready(function() {
    $('.post-likes').click(function() {
        var id;
        id = $(this).attr('data-post-id');
        $.get('/blog/posts', {
            post_id: id
        }, function(data) {
            $('.like_count_blog').html(data);
        });
    });
});