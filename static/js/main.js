/**
 * Created by .
 * User: vladka
 * Date: 21.04.11
 * Time: 23:56
 * To change this template use File | Settings | File Templates.
 */
$(function() {
    $('#userlogin').focus(function() {
        if($(this).attr('value') == 'Логин...')
            $(this).attr('value','')
    })
    $('#userlogin').focusout(function() {
        if($(this).attr('value') == '')
            $(this).attr('value','Логин...')
    })

    $('#userpassword').focus(function() {
        if($(this).attr('value') == 'Логин...')
            $(this).attr('value','')
    })
    $('#userpassword').focusout(function() {
        if($(this).attr('value') == '')
            $(this).attr('value','Логин...')
    })

    $('.ajax').click(function() {
        var jElement = $(this)
        $.ajax({
                    'method' : 'post',
                    'url' : jElement.attr('href'),
                    'data' : { ajax : 1 },
                    success : function (text, status) {
                        jElement.html(text);
                    },
                    error : function(request, status, error) {
                        jElement.html(error);
                    }
                });
        return false;
    });

    $('.input').click(function() {
        jElement = $(this)
        jElement.next().css('display', 'block')
        jElement.css('display', 'none')
    })

    $('.focus').blur(function() {
        var jElement = $(this)
        $.ajax({
            url: jElement.attr('rel'),
            data: 'name=' + jElement.attr('name') + '&value=' + jElement.attr('value'),
            type: 'get',
            success: function(text, statuc) {
                jElement.hide()
                jElement.prev().html(text)
                jElement.prev().show()
            },
            error: function(request, status, error) {
                jElement.hide()
                jElement.prev().html(error)
                jElement.prev().show()
            }
        })
    })

    $('.focus').keyup(function(e){
        if(e.keyCode == 13) {
            var jElement = $(this)
            $.ajax({
                url: jElement.attr('rel'),
                data: 'name=' + jElement.attr('name') + '&value=' + jElement.attr('value'),
                type: 'get',
                success: function(text, statuc) {
                    jElement.hide()
                    jElement.prev().html(text)
                    jElement.prev().show()
                },
                error: function(request, status, error) {
                    jElement.hide()
                    jElement.prev().html(error)
                    jElement.prev().show()
                }
            })
        }
    })

    var options = {
        target: "#step1_div",
        // data: qString,
        url: $("#step1").attr('action'),
        beforeSubmit: function(arr, form, options) {
            return ($("#step1").validate().form());
        },
        success: function(responseText, statusText) {
            $("#step1_div").toggle('');
            $("#step2_div").toggle('');
            $('#veteran_id').attr('value', responseText);
            //$.createElement("input").attr(  { type: 'hidden', name: 'veteran_id', 'value': responseText } ).appendTo("#step2_div");
            return false;
        }
    };
    $('.ajaxform').ajaxForm();
})

