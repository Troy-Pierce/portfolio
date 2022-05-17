$(window).on("DOMContentLoaded", function(){
    document.documentElement.style.setProperty('--deg-val', Math.floor(Math.random()*361).toString()+"deg");
    $("#root").hide().fadeIn(1000).promise().done(function(){
        $("body").css("overflow", "auto");
    });
}).on( "load", function(){
    $("#root-content").css("transition", "all ease-in-out 1s").css("transform", "translateY(0%)");
    
    $(document).on('click', 'a[href!="javascript:void(0);"][target!="_blank"]', function(event) {
        event.preventDefault();
        $("body").css("overflow", "hidden");
        $("#root-content").css("transition", "all 1s ease-in-out").css("transform", "translateY(-200%)");
        $("#root").fadeTo(1000, 0).promise().done(function(){
            window.open(event.target.getAttribute("href"), event.target.getAttribute("target")!=undefined ? event.target.getAttribute("target") : "_self");
        })
    });
    setTimeout(function(){
        list = $(".caret");
        lsize = list.length, size = 0;
        list.each(function(){
            if($(this).parent().attr('caret-text')!=undefined){
                for(i = 0; i < $(this).parent().attr('caret-text').length; i++){
                    var $this = $(this);
                    setTimeout(function(value, last){
                        $this.before($this.parent().attr('caret-text').charAt(value));
                        if(value == last-1){
                            $this.remove();
                            size++;
                            if(size==lsize){
                                $("#content").fadeTo(1000,1);
                            }
                        }
                    }, (($this.parent().attr('caret-speed')!=undefined?parseInt($this.parent().attr('caret-speed')) : 200)*i), i, $(this).parent().attr('caret-text').length)
                }
            }
        })
    }, 1000)
});

function contact(){
    str = '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';
    str = str.split("-");
    newstr = '';
    for(i = 0; i<str.length;i++){
        newstr += String.fromCharCode(str[i].length);
    }
    window.open(newstr);
}

function displayFrame(link){
    policy = document.createElement('div');
    policy.classList.add('policy-bg');
    policy.zIndex = -1;
    policy.onclick = function(){
        policy.remove();
    }
    frame = document.createElement('iframe');
    frame.classList.add('policy-frame');
    frame.src = link;
    policy.appendChild(frame);
    document.body.prepend(policy);
}