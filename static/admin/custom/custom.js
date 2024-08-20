function edit_product_image(){
    $('#image_present').hide()
    $('#image_not_present').show()
    $('#image_change').val("yes")
}

function edit_action(){
    event.preventDefault()
    var form_data = new FormData($('#blog_edit_form')[0]);
    
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
            da=data['data']
            id=da["id"]
        
            if (status == "success"){
                
                // alert("Form submission successful!*^^^^^^^^^^^^^"+'#table' + id);
               $('#blog-table').load(location.href + " #blog-table");
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
            da=data['data']
            $('#blog_form')[0].reset();
   
            // alert("SS"+message)
            if (status == "success"){
                // alert("Form submission successful!"+message);
                // alert('yssssssssssssssssssssssssssss',da)
                console.log(da['id'])
                
                // Update the table
                // $('#blog-table').append("<tr>" +
                //     "<td>" + da["id"] + "</td>" +
                //     "<td>" + da["auther_name"] + "</td>" +
                //     "<td>" + da["date"] + "</td>" +
                //     "<td>" + "<img src='" + da["image_url"] + "' alt='Image' />" + "</td>"+
                //     "<td>" + da["title"] + "</td>" +
                //     "<td>" + '<button type="button" class="btn btn-info btn-sm" onclick="description_data(\'' + da["id"] + '\')">' +
                //     '<i class="mdi mdi-pencil"></i> View' +
                //     '</button>' +"</td>" +
                //     "<td>" + '<input type="checkbox" id="' + da["id"] + '" onclick="handleClick(this);" ' + (da["status"] ? 'checked' : '') + '>' + "</td>" +
                //     "<td>" + 
                //     '<button type="button" class="btn btn-success btn-sm" onclick="edit_blog(\'' + da["id"] + '\')">' +
                //         '<i class="mdi mdi-pencil"></i> Edit' +
                //     '</button>' +
                //     '<button type="button" class="btn btn-danger btn-sm" onclick="delete_submit(\'' + da["id"] + '\')">' +
                //         '<i class="fas fa-trash-alt"></i> Delete' +
                //     '</button>' + "</td>" +

                // "</tr>");
                // #reloading the te table only 
                $('#blog-table').load(location.href + " #blog-table");
                // $('#blog-table').load(location.href + " #blog-table");  
                // // #to reload the a row 
                // $('#table{{id}}').load(location.href + " #table{{id}}");
                // // to load complete window
                // $(document).ajaxStop(function(){
                //     setTimeout("window.location = 'Blog'",100);
                //   });
                // document.getElementById('blog_form').submit();
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
                console.log(data)
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
            if (status == "success"){
                $('#blog-table').load(location.href + " #blog-table");
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


// var newRow = `
//             <tr>
//                 <td>${da['id']}</td>
//                 <td>${da['auther_name']}</td>
//                 <td>${da['date']}</td>
//                 <td class="py-3">
//                     ${da['image'] ? `<img src="${da['image']}" alt="${da['auther_name']}">` : `<p>no image</p>`}
//                 </td>
//                 <td>${da['title']}</td>
//                 <td> 
//                     <button type="button" class="btn btn-info btn-sm" onclick="description_data('${da['id']}')">
//                         <i class="mdi mdi-pencil"></i>view
//                     </button>
//                 </td>
//                 <td>
//                     <input type="hidden" name="blog_id" value="${da['id']}">
//                     <input type="checkbox" id="${da['id']}" onclick='handleClick(this);' ${da['status'] ? 'checked' : ''}>
//                 </td>
//                 <td>
//                     <button type="button" class="btn btn-success btn-sm" onclick="edit_blog('${da['id']}')">
//                         <i class="mdi mdi-pencil"></i> Edit
//                     </button>
//                     <button type="button" class="btn btn-danger btn-sm" onclick="delete_submit('${da['id']}')">
//                         <a href="#" style="color:white;"><i class="fas fa-trash-alt"></i> Delete</a>
//                     </button>
//                 </td>
//             </tr>
//         `;

//         // Append the new row to the table body
//         $('#blog-table').append(newRow);

// Reloading the page methods

//  // #reloading the te table only 
//  $('#blog-table').load(location.href + " #blog-table");  
//  // #to reload the a row 
//  $('#table{{id}}').load(location.href + " #table{{id}}");
//  // to load complete window
//  $(document).ajaxStop(function(){
//      setTimeout("window.location = 'Blog'",100);
//    });

// 
// 
// 

// service


function edit_product_image_service(){
    $('#image_present').hide()
    $('#image_not_present').show()
    $('#image_change').val("yes")
}

function edit_service_actionn(){
    event.preventDefault()
    var form_data = new FormData($('#service_edit_form')[0]);
    // console.log("Form Data:");
    // Log form data to console for debugging
    // for (var pair of form_data.entries()) {
    // console.log(pair[0]+ ': ' + pair[1]); 
    // }


    // alert("SS"+form_data)
    // console.log("gggggg"+form_data)

    $.ajax({
        type: 'POST',
        url: "edit_service_action",
        data: form_data,
        processData: false,
        contentType: false,
        success: function(data)
        {
            status = data['status']
            message = data['message']
            
            // alert("SS"+message)
            if (status == "success"){
                // alert("Form submission successful!"+data.success);
                // to refresh the page automaticaly
                // $(document).ajaxStop(function(){
                //     setTimeout("window.location = 'Blog'",100);
                //   });
                // if (data.success){
                //     console.log('hello')
                //     $("#blog-table").load("#blog-table");
                // }
               
                $('#service-table').load(location.href + " #service-table");
                
                // document.getElementById('blog_edit_form').submit();
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

function service_submit(){
    event.preventDefault()
    var form_data = new FormData($('#service_form')[0]);
    // console.log("Form Data:");
    // Log form data to console for debugging
    // for (var pair of form_data.entries()) {
    // console.log(pair[0]+ ': ' + pair[1]); 
    // }


    // alert("SS"+form_data)
    // console.log("gggggg"+form_data)

    $.ajax({
        type: 'POST',
        url: "create_service",
        data: form_data,
        processData: false,
        contentType: false,
        success: function(data)
        {
            status = data['status']
            message = data['message']
            da=data['data']
    
            if (status == "success"){
                
                $('#service_form').trigger('reset');
                
                $("#data_table").html(data.template);
                // Update the table
                // $('#Service-table').append("<tr>" +
                //     "<td>" + da["sid"] + "</td>" +
                //     "<td>" + da["stitle"] + "</td>" +
                //     "<td>" + '<button type="button" class="btn btn-info btn-sm" onclick="description_data(\'' + da["sid"] + '\')">' +
                //     '<i class="mdi mdi-pencil"></i> View' +
                //     '</button>' +"</td>" +
                //     "<td>" + "<img src='" + da["simage_url"] + "' alt='Image' />" + "</td>"+
                //     "<td>" + '<input type="checkbox" id="' + da["sid"] + '" onclick="handleClick(this);" ' + (da["sstatus"] ? 'checked' : '') + '>' + "</td>" +
                //     "<td>" + 
                //     '<button type="button" class="btn btn-success btn-sm" onclick="edit_blog(\'' + da["sid"] + '\')">' +
                //         '<i class="mdi mdi-pencil"></i> Edit' +
                //     '</button>' +
                //     '<button type="button" class="btn btn-danger btn-sm" onclick="delete_submit(\'' + da["sid"] + '\')">' +
                //         '<i class="fas fa-trash-alt"></i> Delete' +
                //     '</button>' + "</td>" +

                // "</tr>");
                // #reloading the te table only   
                // // #to reload the a row 
                // $('#blog-table').load(location.href + " #blog-table");
               
                // $('#service-table').load(location.href + " #service-table");

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

function edit_servicee(id){
    var url ="edit_service";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
            
            success: function (data) {
                // console.log(data.rendered_template)
                // alert("Rendered template: " + data.rendered_template);
                $("#edit_service_div2").html(data.rendered_template);
                $("#edit_service_modal").modal("show");
            }


          });
}


function service_delete_submit(id){
  
    var url ="delete-service";
            $.ajax({
            url: url,
            data: {
              'id': id
            },

            success: function(data) {
          
            status = data['status']
            message = data['message']
           
            if (status == "success"){
               
                // alert("Are you sure to delete"+message);
                $('#sig').load(location.href + " #sig");
                // $("#data_table").html(data.template);
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

function service_description_data(id){
    var url ="description_service";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
         
            // console.log("gggggg"+form_data)
            success: function (data) {
                // console.log(data.rendered_template)s
                $("#description_service_div2").html(data.rendered_template);
                $("#description_service_modal").modal("show");
            }
          });
}

function delete_service_imagee(id){
    var url ="delete-service-img";
            $.ajax({
            url: url,
            data: {
              'id': id
            },

            success: function(data) {
          
            status = data['status']
            message = data['message']
            // alert("SS"+message)

            $('#image_service_present').hide()
            $('#image_not_service_present').show()
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

function check_service(id){
    var url ="check-service-box";
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

function shandleClick(checkbox) {
          var productId = checkbox.getAttribute('id'); 
          var url ="service_check-box";
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


function delete_service_imagee(id){
        var url ="delete_img_service";
                $.ajax({
                url: url,
                data: {
                  'id': id
                },
    
                success: function(data) {
              
                status = data['status']
                message = data['message']
                // alert("SS"+message)
                
                $('#image_presentt').hide()
                $('#image_not_presentt').show()
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
    