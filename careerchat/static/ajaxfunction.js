//Ajax function for chatting
//career student advisor

function exitfunction()
{
	var ext = confirm("Are you sure you want to exit chat?");
	if (ext == true){ $.get('/career/');}
	else
	{}
}


function sendfunction(name)
{
	var inputBox = alert(document.getElementById("chatmsg").value);
	var usernm = name;
	$.ajax({
		type: "POST",
		url: '/careerchat/testajax/',
		dataType: "json",
		data: {
			client_response: $('#chatmsg').val(),
			csrfmiddlewaretoken: '{{ csrf_token }}',
			user_name: usernm,
			},
			success: function(data) {
				$('#messagelist').append('<li>'++'</li>');
			}
	});
}


