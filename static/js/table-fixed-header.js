(function ($) {

  $.fn.fixedHeader = function (options) {
    var config = {
        topOffset: 0
        //bgColor: 'white'
      };
    if (options) {
      $.extend(config, options);
    }

    return this.each(function () {
      var o = $(this); //呼叫此方法的 Dom 物件 

      var $win = $(window); //視窗物件
      var $head = $('thead.header', o); //抓取原始 table 的標頭
      var $head_height = $('thead.header', o).height(); //取得原始標頭的高度
      var isFixed = 0; //用來判斷是否顯示複製標頭的 flag
      //var headTop = $head.length && $head.offset().top - config.topOffset - $head_height;
      var headTop = $("nav")[0].offsetHeight;
      console.log(headTop);
      //當滑動的時候回執行這個函數
      function processScroll() {
        if (!o.is(':visible')) { //如果沒有視窗物件就不執行
          return;
        }
        if ($('thead.header-copy').length) {
          console.log("test");
          $('thead.header-copy').width($('thead.header').width()); //設定複製標頭的寬度
          $("thead.header-copy").attr('style','top:' + headTop + 'px'); //設定複製標頭的 top 
        }
        var i;
        var scrollTop = $win.scrollTop(); //滑了多少高度的值
        //var t = $head.length && $head.offset().top - config.topOffset - $head_height;
        var t =  $("nav")[0].offsetHeight;
        if (!isFixed && headTop !== t) { //這行好像永遠不會執行到....
          headTop = t;
        }
        console.log(scrollTop,headTop,isFixed)
        if (scrollTop >= headTop && !isFixed) {  //當 scroll 超過 headTop 就設定 flag = 1
          isFixed = 1; 
        } else if (scrollTop <= headTop && isFixed) {
          isFixed = 0;
        }
        isFixed ? $('thead.header-copy', o).offset({
          left: $head.offset().left
        }).removeClass('hide') : $('thead.header-copy', o).addClass('hide');
      }

      //當視窗改變呼叫此函數
      function windowResize(){
        var header_width = $head.width(); //取得原始標頭的 width
        o.find('thead.header-copy').width(header_width); // 設定複製標頭的 width
        o.find('thead.header > tr:first > th').each(function (i, h) {
          var w = $(h).width(); //取得原始標頭的 th 的寬度
          o.find('thead.header-copy> tr > th:eq(' + i + ')').width(w); //設定複製標頭的 th 的寬度
        });
        processScroll();
      }

      //監聽 window onscroll resize 的事件
      $win.on('scroll', processScroll);
      $win.on('resize', windowResize);

      // hack sad times - holdover until rewrite for 2.1
      $head.on('click', function () {
        if (!isFixed) {
          setTimeout(function () {
            $win.scrollTop($win.scrollTop() - 47);
          }, 10);
        }
      });

      $head.clone().removeClass('header').addClass('header-copy header-fixed').appendTo(o); //複製原始 table 的標頭至table下面,用來做 fixed 的
      var header_width = $head.width(); //取得原始標頭的 width
      o.find('thead.header-copy').width(header_width); // 設定複製標頭的 width
      o.find('thead.header > tr:first > th').each(function (i, h) {
        var w = $(h).width(); //取得原始標頭的 th 的寬度
        o.find('thead.header-copy> tr > th:eq(' + i + ')').width(w); //設定複製標頭的 th 的寬度
      });
      $head.css({
        margin: '0 auto',
        width: o.width(),
        'background-color': config.bgColor
      });
      processScroll(); 
    });
  };

})(jQuery);