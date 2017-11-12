$(document).ready(function() {
            


  setTimeout(function() {
    $("#main").removeClass("is-loading");
  }, 500)



    $('#submit_btn1').on('click', function(){


          if($("#r1").is(':checked'))
          {
            console.log('hiiiiii');
            console.log($("#r1").val());

          }
          else
          {
            console.log('bye');           
          }

});

    $('#submit_btn').on('click', function(){
           // var fd = new FormData(document.querySelector("form"));


           var value = $("#emailsubmit").val();
           var selected_vals_array = [];

          if($("#r1").is(':checked'))
          {
             selected_vals_array.push($("#r1").val());            
          }
           if($("#r2").is(':checked'))
          {
             selected_vals_array.push($("#r2").val());            
          }
           if($("#r3").is(':checked'))
          {
             selected_vals_array.push($("#r3").val());            
          }
           if($("#r4").is(':checked'))
          {
             selected_vals_array.push($("#r4").val());            
          }
           if($("#r5").is(':checked'))
          {
             selected_vals_array.push($("#r5").val());            
          }
           if($("#r6").is(':checked'))
          {
             selected_vals_array.push($("#r6").val());            
          }

           if($("#r7").is(':checked'))
          {
             selected_vals_array.push($("#r7").val());            
          }
           if($("#r8").is(':checked'))
          {
             selected_vals_array.push($("#r8").val());            
          }
           if($("#r9").is(':checked'))
          {
             selected_vals_array.push($("#r9").val());            
          }
           if($("#r10").is(':checked'))
          {
             selected_vals_array.push($("#r10").val());            
          }
           if($("#r11").is(':checked'))
          {
             selected_vals_array.push($("#r11").val());            
          } if($("#r12").is(':checked'))
          {
             selected_vals_array.push($("#r12").val());            
          }
           if($("#r13").is(':checked'))
          {
             selected_vals_array.push($("#r13").val());            
          }
           
           console.log(selected_vals_array)

           $.ajax({
              url: "/uploader",
              type: "POST",
              data: JSON.stringify({ 'post':$("#emailsubmit").val(), 'selected_vals':selected_vals_array }),
              contentType: 'application/json;charset=UTF-8',

              success: function(data) {
                        $('#response').html(data);
                    }
            });
          });


    $('#adventure')
      .css('cursor', 'pointer')
      .click(
        function(){
         alert('Click event is fired');
        }
      )
      .hover(
        function(){
          $(this).css('background', '#ff00ff');
        },
        function(){
          $(this).css('background', '');
        }
      );




});


