$(document).ready(function () {
    $("a[href='#back-to-top']").click(function() {
            $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

    $(".lang-dropdown").change(function() {
        $.ajax({
            url : "/ajax/update_country/",
            type : "POST",
            data : {'country': $(this).val()},
            success : function(json) {
                location.reload();
            },
            error : function(xhr,errmsg,err) {
            }
        });
    });

    $(".header-panel-box ol li ul").hover(
        function() {
            $(this).parent("li").children("a")
                .addClass("header-panel-box-active")
        }, function() {
            $(this).parent("li").children("a")
                .removeClass("header-panel-box-active")
        }
    );

    $("span.glyphicon-close").click(function() {
        $(this).parent("div").hide()
    });

    $(".mobile-menu").click(function() {
        $(this).parent("div").children("ol").toggle("slow")
    })
});