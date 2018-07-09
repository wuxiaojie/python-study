$(document).ready(function(){
   $("#btn").bind("click",function(){
//    console.log("xx")
    $.ajax({
          type:"get",
          url:"/myapp/studentsinfo/",
          dataType:"json",
          success:function(data,status){
            console.log(data)
            var d = data["data"]
            for(var i = 0; i < d.length; i++){
            document.write('<p>'+d[i][0]+'</p>')
            }
          }
    })
   })
})
