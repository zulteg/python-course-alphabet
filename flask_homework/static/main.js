$(document).ready(function () {
    $(document).on("keypress", ".input-group:has(input:input) input:input", function (e) {
        if (e.which === 13) {
            $(this).closest(".input-group").find(".btn").click();
        }
    });

    $('.add-item-btn').on('click', function () {
        let action = '/' + $('[data-name]').data('name') + '/add';
        $.ajax({
            type: "POST",
            url: action,
            data: JSON.stringify({
                item: $(this).closest('.input-group').find('input').val()
            }),
            contentType: "application/json; charset=utf-8",
            success: function () {
                location.reload();
            }
        });
    });

    $('.rm-item-btn').on('click', function () {
        let action = '/' + $('[data-name]').data('name') + '/rm';
        $.ajax({
            type: "POST",
            url: action,
            data: JSON.stringify({
                item: $(this).siblings('[data-item]').text()
            }),
            contentType: "application/json; charset=utf-8",
            success: function () {
                location.reload();
            }
        });
    });
});