$(document).ready(function()	{	
	$("#txt_search").keyup(function() {		
	var	search = $("#txt_search").val();		
	if	(search.length	>	0)	{		
		$.ajax({type: "POST",		
				url: "suggest/",		
				data: "search="	+ search,		
				success:	function(message){		
					$("#suggest").empty();		
					if	(message.length	>	0)	{		
						message	=	"Do	you	mean:	"	+	message	+	"?";		
						$("#suggest").append(message);		
					}		
				}		
		});	
	}	else	{		
		//	Empty	suggestion	list		
		$("#suggest").empty();		
				}		
		});	
});	