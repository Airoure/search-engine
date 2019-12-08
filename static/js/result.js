window.onload =function () {
	f();
	}
	function f() {
		tag=GetQueryString('tag');
		//alert(tag);

		document.getElementsByClassName("active")
		document.getElementById(tag).className='active';

	}
	function GetQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);//search,查询？后面的参数，并匹配正则
     if(r!=null)return  unescape(r[2]); return null;
}

var a_idx = 0;
jQuery(document).ready(function($) {
    $("body").click(function(e) {
        var a = new Array("富强", "民主", "文明", "和谐", "自由", "平等", "公正" ,"法治", "爱国", "敬业", "诚信", "友善");
        var $i = $("<span/>").text(a[a_idx]);
        a_idx = (a_idx + 1) % a.length;
        var x = e.pageX,
        y = e.pageY;
        $i.css({
            "z-index": 999999999999999999999999999999999999999999999999999999999999999999999,
            "top": y - 20,
            "left": x,
            "position": "absolute",
            "font-weight": "bold",
            "color": "#ff6651"
        });
        $("body").append($i);
        $i.animate({
            "top": y - 180,
            "opacity": 0
        },
        1500,
        function() {
            $i.remove();
        });
    });
});

$(function(){
        	$("#formid").submit(function(){
        		var search=$("#text").val();
				if (search == "")
				{
					$("#text").val("{{request.values.get('wd')}}")
				}
        	});
        });
$(function() {
    var e = $("#rocket-to-top"),
    t = $(document).scrollTop(),
    n,
    r,
    i = !0;
    $(window).scroll(function() {
        var t = $(document).scrollTop();
        t == 0 ? e.css("background-position") == "0px 0px" ? e.fadeOut("slow") : i && (i = !1, $(".level-2").css("opacity", 1), e.delay(100).animate({
            marginTop: "-1000px"
        },
        "normal",
        function() {
            e.css({
                "margin-top": "-125px",
                display: "none"
            }),
            i = !0
        })) : e.fadeIn("slow")
    }),
    e.hover(function() {
        $(".level-2").stop(!0).animate({
            opacity: 1
        })
    },
    function() {
        $(".level-2").stop(!0).animate({
            opacity: 0
        })
    }),
    $(".level-3").click(function() {
        function t() {
            var t = e.css("background-position");
            if (e.css("display") == "none" || i == 0) {
                clearInterval(n),
                e.css("background-position", "0px 0px");
                return
            }
            switch (t){
            case "0px 0px":
                e.css("background-position", "-298px 0px");
                break;
            case "-298px 0px":
                e.css("background-position", "-447px 0px");
                break;
            case "-447px 0px":
                e.css("background-position", "-596px 0px");
                break;
            case "-596px 0px":
                e.css("background-position", "-745px 0px");
                break;
            case "-745px 0px":
                e.css("background-position", "-298px 0px");
            }
        }
        if (!i) return;
        n = setInterval(t, 50),
        $("html,body").animate({scrollTop: 0},"slow");
    });
});

// 当网页向下滑动 20px 出现"返回顶部" 按钮
window.onscroll = function() {scrollFunction()};

function scrollFunction() {console.log(121);
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// 点击按钮，返回顶部
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}



