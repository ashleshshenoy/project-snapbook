function loginreq() {


  let status=document.getElementById('login-alert').style.display
  if(status=='none'){
    document.getElementById('login-alert').style.display='block';
  }else{
    document.getElementById('login-alert').style.display='none';
  }

}



$(document).ready(function(){
  $("#trail").click(function(){
    $("#login-alert").toast('show');
  });
});
