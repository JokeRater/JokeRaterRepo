$(function()){
	$('search').keyup(function()){
		$.ajax({
			type: "POST",
			url: "{% url 'profile' %}",
			data: {
				'search_text' $('#search').val(),
				'csrfmiddlewaretoken': $(""input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});

function searchSuccess(data, textStatus, jgXHR)
{
	$('#search-results').html(data);
}