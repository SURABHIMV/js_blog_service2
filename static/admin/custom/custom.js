

function edit_product_image(){
    $('#image_present').hide()
    $('#image_not_present').show()
    $('#image_change').val("yes")
}

function edit_action(){
    event.preventDefault()
    var form_data = new FormData($('#blog_edit_form')[0]);
    // console.log("Form Data:");
    // Log form data to console for debugging
    // for (var pair of form_data.entries()) {
    // console.log(pair[0]+ ': ' + pair[1]); 
    // }


    // alert("SS"+form_data)
    // console.log("gggggg"+form_data)

    $.ajax({
        type: 'POST',
        url: "edit_blog_action",
        data: form_data,
        processData: false,
        contentType: false,
        success: function(data)
        {
            status = data['status']
            message = data['message']
            alert("SS"+message)
            if (status == "success"){
                alert("Form submission successful!"+message);
                document.getElementById('blog_edit_form').submit();
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }
            else{
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }

        }
    })

}

function blog_submit(){
    event.preventDefault()
    var form_data = new FormData($('#blog_form')[0]);
    // console.log("Form Data:");
    // Log form data to console for debugging
    // for (var pair of form_data.entries()) {
    // console.log(pair[0]+ ': ' + pair[1]); 
    // }


    // alert("SS"+form_data)
    // console.log("gggggg"+form_data)

    $.ajax({
        type: 'POST',
        url: "create_blog",
        data: form_data,
        processData: false,
        contentType: false,
        success: function(data)
        {
            status = data['status']
            message = data['message']
            // alert("SS"+message)
            if (status == "success"){
                alert("Form submission successful!"+message);
                document.getElementById('blog_form').submit();
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }
            else{
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }

        }
    })

}

function edit_blog(id){
    var url ="edit_blog";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
            
            success: function (data) {
                // console.log(data.rendered_template)
                // alert("Rendered template: " + data.rendered_template);
                $("#edit_blog_div2").html(data.rendered_template);
                $("#edit_blog_modal").modal("show");
            }


          });
}


function delete_submit(id){
    var url ="delete-blog";
            $.ajax({
            url: url,
            data: {
              'id': id
            },

            success: function(data) {
          
            status = data['status']
            message = data['message']
            // alert("SS"+message)
            if (status == "success"){
                alert("Are you sure to delete"+message);
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }
            
        } 


          });
}

function description_data(id){
    var url ="descriptionn";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
         
            // console.log("gggggg"+form_data)
            success: function (data) {
                // console.log(data.rendered_template)s
                $("#description_div2").html(data.rendered_template);
                $("#description_modal").modal("show");
            }


          });
}

function delete_imagee(id){
    var url ="delete-img";
            $.ajax({
            url: url,
            data: {
              'id': id
            },

            success: function(data) {
          
            status = data['status']
            message = data['message']
            // alert("SS"+message)

            $('#image_present').hide()
            $('#image_not_present').show()
            console.log('jjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            if (status == "success"){
                alert("Are you sure to delete"+message);
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }
            
        } 


          });
}

// function edit_image(id){
//     var url ="edit_blog_action";
//             $.ajax({
//             url: url,
//             data: {
//               'id': id
//             },

//             success: function(data) {
            
                
//             status = data['status']
//             message = data['message']
//             // alert("SS"+message)
//             if (status == "success"){
//                 alert("Are you sure to delete"+message);
//                 var toastMixin = Swal.mixin({
//                 toast: true,
//                 icon: status,
//                 title: 'General Title',
//                 animation: false,
//                 position: 'top-right',
//                 showConfirmButton: false,
//                 timer: 2000,
//                 timerProgressBar: true,
//                 didOpen: (toast) => {
//                     toast.addEventListener('mouseenter', Swal.stopTimer)
//                     toast.addEventListener('mouseleave', Swal.resumeTimer)
//                 }
//                 });
//                 toastMixin.fire({
//                 animation: true,
//                 title: message
//                 });
//             }
            
//         } 


//           });
// }

function check(id){
    var url ="check-box";
            $.ajax({
            url: url,
            data: {
              'id': id
            },

            success: function(data) {
          
            status = data['status']
            message = data['message']
            
            console.log('jjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            if (status == "success"){
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }
            
        } 


          });
}

function handleClick(checkbox) {
          var productId = checkbox.getAttribute('id'); 
          var url ="check-box";
            $.ajax({
            url: url,
            data: {
              'checked': checkbox.checked,
              'productId': productId
            },

            success: function(data) {
          
            status = data['status']
            message = data['message']
            console.log('kkkkkkkkkkk',checkbox.id)
            console.log('jjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            if (status == "success"){
                var toastMixin = Swal.mixin({
                toast: true,
                icon: status,
                title: 'General Title',
                animation: false,
                position: 'top-right',
                showConfirmButton: false,
                timer: 2000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
                });
                toastMixin.fire({
                animation: true,
                title: message
                });
            }
            
        } 


          });
    }
// function handleClick(checkbox) {
//     if (checkbox.checked) {
//         console.log(checkbox.value + " True");
//     } else {
//         console.log(checkbox.value + " False");
//     }
// }