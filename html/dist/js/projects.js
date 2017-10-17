var xhr = new XMLHttpRequest();

window.onload = function() {
  var link = requestLink+"/projects/get"
}
document.getElementById("loginBTN").addEventListener("click",function() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var formData = new FormData();
  var link = requestLink+"/login"
  formData.append('email', email);
  formData.append('password', password);
  xhr.open('POST', link);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] != 1) {
            document.getElementById("incorrect").style.display = 'block';
            document.getElementById('incorrect').innerHTML = "<p>账户无效</p>";
          } else {
            document.getElementById("incorrect").style.display = 'none';
          }
      }
  }
  xhr.send(formData);
  xhr.timeout = 3000;
  xhr.ontimeout = function(event){
    alert('请求超时！');
  }
})
