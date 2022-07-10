$(document).ready(function(){
    $(".stars").on("click",'.rate' ,function(event){
        event.preventDefault();
        var id = $(this).data('id');
        var parent_id = $(this).parent().attr('id');
        var content = ` `;
        var rating = $(this).parent().data('rate_id');
       
        var site_url = $(this).parent().data('url');
        console.log(site_url)
        
        $.ajax({
            type: 'GET',
            url: site_url,
            data:{
                'artist_id':rating,
                
            },
            success: function (response)
            {
                  console.log(response['artist'])
            }


        })


        for(var i=1; i<=5; i++)
        {
            
            if(i<= id)
            {       
                
                content = content + `<span  class="fa fa-star checked rate" data-id =`+i+`></span> `;
            }
            else
            {
                content =
                  content +
                  `<span  class="fa fa-star rate"data-id =` +i+`></span> `;
            }
            
        };

        $('#'+parent_id).html(content);

    })
})