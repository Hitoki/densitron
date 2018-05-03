$(document).ready(function () {
    // Accordion block (Latest Videos//Docs//What's Hap..)
    $('.accordion .header').click(function () {
        var content = $(this).next();
        var self = $(this);

        if ($('.accordion').hasClass('sidebar-accordion')) {
            content = $($('.accordion-content-box').children('.accordion-content')[$(this).index('.sidebar-accordion .sidebar .header')])
        }

        if($(this).hasClass('active')) {
            $('.accordion .active').removeClass('active');
            if (!content.hasClass('bespoke_orders')) {
                content.slideUp();
            }
            if ($('.accordion').hasClass('sidebar-accordion')) {
                $(this).next().slideUp();
            }
        } else {
            var active_content = $('.accordion-content.active');
            if ($('.accordion').hasClass('sidebar-accordion')) {
                var active_header = $('.accordion .header.active');
                active_header.removeClass('active');
                active_header.next().slideUp(function(){
                active_header.next().removeClass('active');
                });
                self.next().slideDown().addClass('active');
            } else {
                active_content.slideUp().removeClass('active');
                active_content.prev().removeClass('active');
                content.slideDown(function(){
                    content.addClass('active');
                });
            }
            self.addClass('active');
        }
        return false;
    });

    // Mobile latest block buttons
    $('.column-tabs li').click(function () {
        $('.column-tabs li').removeClass('active');
        var class_name = $(this).attr('class');
        $('.columns-container .column').hide();
        $('.columns-container .column.' + class_name).show();
        $(this).addClass('active')
    });

    // Product gallery slider
    if ($('.products-gallery-buttons').is(':visible')) {
        var product_gallery = $('.products-gallery');
        var product = product_gallery.children('.product');
        var current_product = 0;
        var distance = product_gallery.width()-product.width()*2;
        function init_gallery() { product.each(function (index) {
            if (index > 1) {$(this).css({top: 0, left: (product.width()*index+distance*index)+distance, position:'absolute'})}
            else {$(this).css({top: 0, left: product.width()*index+distance*index, position:'absolute'})}
        })}

        product_gallery.parent('.content-box').css({overflow:'hidden'});
        init_gallery();
        $( window ).resize(function() {
            product.each(function (index) {
            if (index > 1) { $(this).animate({left: (product.width()*index+distance*index)+distance})}
            else {$(this).animate({left: product.width()*index+distance*index})}
        })});

        $('.products-gallery-buttons .arrow').click(function() {
            if ($(this).hasClass('left')) {
                if (current_product == 0) {
                    product.each(function (index) {
                        if (index == product.length-2) {$(this).animate({left: 0})}
                        if (index == product.length-1) {$(this).animate({left: product.width()+distance})}
                        if (index < product.length-2) {$(this).animate({left: product.width()*(index+2-product.length)+distance*(index+2-product.length)-distance})}
                    });
                    current_product = product.length-2
                } else {
                    product.each(function (index) {
                        var bonus_right = 0;
                        if (index == current_product-1 || index == current_product+1) {bonus_right = distance}
                        $(this).animate({left: $(this).position().left+product.width()+distance+bonus_right});
                    });
                    current_product  -= 1;
                }
            }
            if ($(this).hasClass('right')) {
                if (current_product+2 == product.length) {
                    product.each(function (index) {
                        if (index > 1) { $(this).animate({left: (product.width()*index+distance*index)+distance})}
                        else {$(this).animate({left: product.width()*index+distance*index})}
                    });
                    current_product = 0;
                } else {
                    product.each(function (index) {
                        var bonus_left = 0;
                        if (index == current_product+2 || index == current_product) {bonus_left = distance}
                        $(this).animate({left: $(this).position().left-product.width()-distance-bonus_left});
                    });
                    current_product  += 1;
                }
            }
        });
    }

    // Tell us what you need tab
    $('.content-box.what_you_need .tab-header li').click(function(index){
        if(!$(this).hasClass('active')) {
            $('.content-box.what_you_need .tab-header li').removeClass('active');
            var cep_element = $('.content-box.what_you_need .cep-holder .cep-element');
            cep_element.removeClass('active');
            $(this).addClass('active');
            $(cep_element[$(this).index()]).addClass('active');
        }
    });

    // Home worldpay carousel
    if ($('.content-box.worldpay_screen-box')) {
        $('.worldpay_screen-box .carousel-button').click(function(index) {
            if(!$(this).hasClass('active')) {
                $('.worldpay_screen-box .carousel-button.active').removeClass('active');
                $('.worldpay_screen-box .carousel-item.active').animate({opacity:0}, 'slow').removeClass('active');
                $(this).addClass('active');
                $($('.worldpay_screen-box .carousel-item')[$(this).index()])
                    .animate({opacity:1}, 'slow').addClass('active');
            }
        });
        setInterval(function(){
            //$('.worldpay_screen-box .carousel-button.active').next().trigger('click');
            if ($('.worldpay_screen-box .carousel-button.active').next().length) {
                $('.worldpay_screen-box .carousel-button.active').next().trigger('click');
            }
            else {
                $(".worldpay_screen-box .carousel-button:first").trigger('click');
            }
        }, 10000);
    }

    // Get in touch block
    if ($('#get_in_touch-box')) {
        $('#get_in_touch_ico').click(function(){
            $('#get_in_touch').animate({ right: '50%' });
            $('.get_in_touch_wrapper').show();
        });
        $('#get_in_touch .glyphicon-close-blue').click(function(){
            $('#get_in_touch').animate({ right: '-500%' });
            $('.get_in_touch_wrapper').hide();
        });
        $('.call_us select.contact-select').on('change', function() {
            $('.call_us h1' ).hide();
            $('.call_us h1.'+this.value).show()
        });
        $('.email_us-form button').click(function() {
            $.ajax({
                url : "/ajax/get-in-touch/",
                type : "POST",
                data : {
                    data: JSON.stringify($('.email_us-form').serializeArray())
                },
                success : function(json) {
                    $.each($('.email_us-form'), function(i, item) {
                        item.reset()
                    });
                    if ($('.contact-form-box').is(':visible')) {
                        $('.contact-form-box .contact-form-box-holder').remove();
                        $('.contact-form-box .contact-form-box-holder-response').show();
                        $('.contact-form-box .contact-form-box-holder-response h3').text(json['first_name']+', your message has been submitted successfully.');
                        $.each(json, function(i, item) {
                            $('.contact-form-box .contact-form-box-holder-response .contact-response').append(
                                '<p class="text"><span>'+i.replace('_', ' ')+': </span>'+item+'</p>'
                            )
                        })
                    }
                    $('#get_in_touch ').animate({ right: '-500%' });
                    $('.get_in_touch_wrapper').hide();
                },
                error : function(xhr,errmsg,err) {
                    var obj = $.parseJSON(xhr.responseText);
                    $.each(obj, function(i, item) {
                        $('.email_us-form label[for=id_'+i+']').append(
                            '<img class="error" src="/static/images/fill_out_error.png" >'
                        )
                    });
                    setTimeout( function () {
                       $('.email_us-form img').hide('slow')
                    }, 3000 );
                }
            });
        });
    }

    // Product category wrapper
    if ($('.product-category-header')){
        var element = $('.product-bar-wrapper .product_in_bar');
        $('.product-category-header ol li:first').addClass('active');
        $('.product-bar-wrapper .product_in_bar:first').addClass('active');
        $('.product-category-header ol li').click(function(){
            $('.product-category-header ol li.active').removeClass('active');
            element.removeClass('active');
            $(this).addClass('active');
            $(element[$(this).index()]).addClass('active');
        })
    }

    // Product detail gallery
    if ($('.content-box.product-box')) {
        //var main_images = $('.content-box.product-box .main-image-holder img');
        var sec_images = $('.content-box.product-box .product-secondary-holder img');
        var sec_distance = 6;

        function init_second_gallery() { sec_images.each(function (index) {
            $(this).css({left: (sec_images.width()+2)*index+sec_distance*index})
        })}

        init_second_gallery();
    }

    // AJAX filter search on main page
    if ($('#what_need_product_filter').is(":visible")) {
        var filter_block =  $('#what_need_product_filter :input');
    } else {
        var filter_block = $('.wizard-product-found-block .sidebar.product_find :input')
    }

    function ajax_filter_products(event) {
        var $inputs = filter_block, data = {};
        $inputs.each(function () {
            if (this.type != 'submit' && this.type != 'hidden') {
                if (this.type === 'checkbox') {
                    data[this.name] = $(this).is(":checked").toString();
                }
                else if (this.type === 'radio') {
                    if ($(this).is(":checked")) {
                        data[this.name] = this.value
                    }
                }
                else {
                    data[this.name] = $(this).val();
                }
            }
        });
        if (event.type == 'change' && event.currentTarget.name == 'sort_product' || $('.wizard-product-found-block').is(":visible")) {
            data['s'] = $('#sort_product').find("option:selected").val();
            if ($('.paginat.paginator-page').length == 1) {
                $('.paginat.paginator-page').addClass('active')
            }
            data['page'] = ($($('.paginat.paginator-page.active')[0])[0].innerText).toString();
            if ('category' in getUrlParameter('category')) {
                data['category'] = getUrlParameter('category')['category'];
            }
            if ($(event.target) && $(event.target).hasClass('paginat')) {
                if ($(event.target).hasClass('left')) {
                    data['page'] = (parseInt($($('.paginat.paginator-page.active')[0])[0].innerText)-1).toString();
                } else if ($(event.target).hasClass('right')) {
                    data['page'] = (parseInt($($('.paginat.paginator-page.active')[0])[0].innerText)+1).toString();
                } else {
                    data['page'] = $($(event.target)[0])[0].innerText;
                }
            }
            $.ajax({
                url: "/ajax/path_filter_sort/",
                type: "POST",
                data: {
                    data: JSON.stringify(data)
                },
                success: function (json) {
                    window.location.href = '?' + json['filter_href'];
                },
                error: function (xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        } else {
            $.ajax({
                url : "/ajax/product_filter/",
                type : "POST",
                data : {
                    data: JSON.stringify(data)
                },
                success : function(json) {
                    $("#find_product").text(json['count']);
                    $("#what_need_product_filter a").attr('href', '/product_found/?'+json['filter_href']);
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        }
    }

    $('#find_key_product').click(function(){
        $.ajax({
            url : "/ajax/product_key_filter/",
            type : "POST",
            data : {
                data: JSON.stringify($('#existing')[0].value)
            },
            success : function(json) {
                if (json['id']) {
                    window.location.href = '/products/'+json['category']+'/'+json['technology']+'/'+json['id']+'/';
                } else if (json['products_keys']) {
                    window.location.href = '/product_found/?page=1&q='+json['products_keys'];
                } else {
                    window.location.href = '/product_found/?page=1';
                }
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });

    $('#sort_product').change(function(event) {
        ajax_filter_products(event)
    });
    if (filter_block) {
        if (filter_block.selector == '#what_need_product_filter :input') {
            filter_block.click(function(event) {ajax_filter_products(event)});
            filter_block.keyup(function(event) {ajax_filter_products(event)});
        } else {
            filter_block.click(function(event) {
                if (event.target.type == 'radio'){
                    setTimeout(function()  {
                        ajax_filter_products(event)
                    }, 2000);
                }
            });
            filter_block.keyup(function(event) {
                setTimeout(function()  {
                    ajax_filter_products(event)
                }, 5000);

            });
        }
    }


    $('.paginator span').click(function(event){
        if (event.target.innerText != '...') {
            ajax_filter_products(event)
        }

    });

    if ($('.wizard-product-found-block .sidebar.bespoke_orders').is(":visible")) {
        $('.wizard-product-found-block .sidebar.bespoke_orders :input').change(function(event) {
            var _data = {};
            _data[event.target.name] = event.target.value;
            $.ajax({
                url : "/ajax/bespoke_orders/",
                type : "POST",
                data : _data,
                success : function(json) {
                    if (json['Technology']) {
                        $('.accordion-content .further-block h3').text(json['Technology'] +' - Custom Display');
                    }
                    $('.accordion-content .further-block .text .parameter').remove();
                    $.each(json, function(i, item) {
                        $(".accordion-content .further-block .text").append(
                            '<span class="parameter">'+ i + ': <strong>' + item + '</strong> | </span>'
                        );
                    })
                },

                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        });
    }

    // Compare selected products
    $('.product-box input[type=checkbox]').change(function() {
        var old_val = $('#compare-products');
        var prefix = '';
        if (jQuery.inArray($(this).val(), old_val.val().split(',')) !== -1) {
            var new_val = old_val.val().split(',');
            new_val.splice(jQuery.inArray($(this).val(), new_val), 1);
            $('#compare-products').val(new_val.toString());
        } else {
            if (old_val.val()) {
                prefix = ','
            }
            $('#compare-products').val(old_val.val()+prefix+$(this).val());
        }
        if (old_val.val()){
            old_val.css({opacity: 1, cursor: 'pointer'});
            old_val.find('span').text($('#compare-products').val().split(',').length)
        } else {
            old_val.css({opacity: 0.5, cursor: 'not-allowed'});
            old_val.find('span').text('0')
        }
    });
    $('#compare-products').click(function(){
        if ($(this).css('opacity') == 1){
            $.ajax({
                url : "/ajax/compare_product/",
                type : "POST",
                data : {
                    data: JSON.stringify($(this)[0].value)
                },
                success : function(json) {
                    $(".compare-block .product-box").remove();
                    $(".compare-block ").addClass('active');
                    $(".compare-holder ").addClass('active');
                    $.each(json['products'], function(i, item) {
                        $(".compare-block").append(
                            '<div class="product-box no-checked">'+
                            '<a href="'+item['path']+'" class="title">'+item['name']+'</a>'+
                            '<ul></ul>'+
                            '</div>'
                        );
                        $.each(item, function(key, value) {
                            if (key !== 'name' && key !== 'path' && key !== 'image') {
                                $(".compare-block .product-box").last().find('ul').append(
                                    '<li name="product-'+slug(key)+'"><span>'+key+':</span> <span>'+value+'</span></li>'
                                );
                            } else if (key == 'image') {
                                $(".compare-block .product-box").last().prepend(
                                     '<div class="image-holder"><img src="'+value+'"></div>'
                                );
                            }
                        })
                    })
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        }
    });
    $('.compare-block .close').click(function(){
        $(".compare-block ").removeClass('active');
        $(".compare-holder ").removeClass('active');
    });

    // Bespoke orders mobile buttons
    $('.build_display_but').click(function() {
        $('.sidebar-accordion .sidebar').show('slow');
    });
    $('.sidebar-accordion .shut-down').click(function (event) {
        if ($(this).hasClass('done')){
            ajax_filter_products(event)
        }
        $('.sidebar-accordion .sidebar').hide('slow');
    });

    // Close our people
    $('.content-box.our-people .member .name').click(function(){
        $($(this)[0].parentElement).next().show()
    });
    $('.content-box.our-people .close').click(function(){
        $($(this)[0].parentElement.parentElement).hide()
    });

    // Download Doc
    $('.content-box.product-box .download-but').click(function(){
        $('.content-box .download-holder').show()
    });
    $('.content-box.product-box .download-holder .close').click(function(){
        $($(this)[0].parentElement.parentElement).hide()
    });
    $('.content-box.product-box .download-holder .submit').click(function(e){
        if ($('.content-box.product-box .download-holder form')[0].checkValidity()) {
            var dd = $('.content-box.product-box .download-holder form').serialize();
            dd['doc'] = $('.content-box.product-box .download-holder form #doc').first().val;
            $.ajax({
                url : "/ajax/download_docs/",
                type : "POST",
                data : dd,
                success : function(data) {
                     location = data['url'];
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        } else {
            $('.content-box.product-box .download-holder form').find(':submit').click()
        }
    })

    // Browse box filter
    if ($('.content-box.latest-box.browse-box').is(":visible")) {
        $('#browse-select').change(function() {
            var browse = $(this).context.value;
            $.ajax({
                url : window.location.pathname,
                type : "GET",
                data : {},
                success : function() {
                    window.location.href = '?docs=1&videos=1&faqs=1&browse='+browse;
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            });
        })
    }

    // Search
    if ($('.search').is(":visible")) {
        $('.search').keypress(function (e) {
            if (e.which == 13) {
                if ($(this).hasClass('knowledge_base_search')) {
                    var browse = '';
                    $.each(getUrlParameter(), function(key, value) {
                        if (key == 'browse') {
                            browse = '&browse='+value;
                        }
                    });
                    window.location.href = '/knowledge-base/?docs=1&videos=1&faqs=1'+browse+'&q='+e.target.value;
                    return false;
                } else {
                    window.location.href = '/search_results/?page=1&q='+e.target.value;
                    return false;
                }
            }
        });
    }

    // Video block in latest box
    $('.column-video-container .video-holder').click(function() {
        if ($(this).hasClass('active')) {
            $(this).prev().removeClass('active');
            $(this).removeClass('active')
        } else {
            $(this).prev().addClass('active');
            $(this).addClass('active')
        }
    });
});

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'), sParameterName, i, data = {};

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');
        data[sParameterName[0]] = sParameterName[1];
    }
    if (sParam) {
        var new_data = {};
        new_data[sParam] = data[sParam];
        data = new_data
    }
    return data
};

var slug = function(str) {
    var $slug = '';
    var trimmed = $.trim(str);
    $slug = trimmed.replace(/[^a-z0-9-]/gi, '-').
    replace(/-+/g, '-').
    replace(/^-|-$/g, '');
    return $slug.toLowerCase();
};
