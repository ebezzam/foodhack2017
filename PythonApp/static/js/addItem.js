$(function(){
	$('#btnaddItem').click(function(){

		$.ajax({
			url: '/addItem',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});


	});
});
