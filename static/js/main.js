/**
 * Created by .
 * User: vladka
 * Date: 21.04.11
 * Time: 23:56
 * To change this template use File | Settings | File Templates.
 */

document.ready(function() {
   $('.ajax').click(function() {
        jElement = $(this)
        $.ajax({
                                 'method' : 'post',
                                 'url' : jElement.attr('href'),
                                 'data' : { ajax : 1 },
                                 success : function (text, status) {
                                     $('#content').html(text);
                                 },
                                 error : function(request, status, error) {
                                     $('#content').html(error);
                                 }
        });
   });

   $('.validate').validate({
                       rules: {
                           name: { required:true, minlength:3 },
                           email: { required:true, email:true }
                       },
                       messages: {
                           name: {
                               required: 'Заполните поле',
                               minlength: 'Удлинните имя'
                           },
                           email: {
                               required: 'Заполните поле',
                               email: 'Введите эл. почту'
                           }
                       }
   });

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


});