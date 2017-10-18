var xhr = new XMLHttpRequest();
var registerStatus = 0;

document.getElementById("repassword").addEventListener("input",function() {
  var password = document.getElementById("password").value;
  var repassword = document.getElementById("repassword").value;
  if (password != repassword) {
    document.getElementById("incorrect").style.display = 'block';
    document.getElementById("incorrect").innerHTML = "两次密码输入不一致";
    registerStatus = 0;
  } else {
    document.getElementById("incorrect").style.display = 'none';
    registerStatus = 1;
  }
})

document.getElementById("registerBTN").addEventListener("click",function() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var name = document.getElementById("name").value;
  if (email == '' || password == '' || name == '') {
    layer.msg("页面上标单项均为必填项");
    return;
  }
  if (registerStatus == 0) {
    layer.msg("两次密码输入不一致，请检查");
    return;
  }
  var formData = new FormData();
  var link = requestLink+"/register"
  formData.append('email', email);
  formData.append('password', password);
  formData.append('name', name);
  xhr.open('POST', link);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] != 1) {
            document.getElementById("incorrect").style.display = 'block';
            document.getElementById('incorrect').innerHTML = returnData['data'];
          } else {
            document.getElementById("incorrect").style.display = 'none';
            window.localStorage.setItem("ApiSysAccount",returnData['data']);
            window.location = 'projects.html';
          }
      }
  }
  xhr.send(formData);
  xhr.timeout = 3000;
  xhr.ontimeout = function(event){
    alert('请求超时！');
  }
})
