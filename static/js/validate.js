/**
 * Created by PyCharm.
 * User: Elena
 * Date: 7/1/11
 * Time: 6:10 PM
 * To change this template use File | Settings | File Templates.
 */


$(function() {

    $(".validate").validate({
		rules: {
			username: {
				required: true,
				minlength: 2
			},
            
            name: {
				required: true,
				minlength: 2
			},
			password1: {
				required: true,
				minlength: 5
			},
			password2: {
				required: true,
				minlength: 5,
				equalTo: "#id_password1"
			},
			email: {
				required: true,
				email: true
			},
			first_name: {
				required: true,
				minlength: 2
			},
            last_name: {
				required: true,
				minlength: 2
			}
		}
	});
})