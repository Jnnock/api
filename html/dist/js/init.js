/* 身份验证 */

var userId = window.localStorage.getItem("ApiSysAccount");
if (!userId) {
  window.location = "login.html"
}

var getUser = requestLink+"/get/user";
/* 获取用户信息 */
function getUserInfo() {
  var xhr = new XMLHttpRequest();
  var getUserInfoLink = getUser + "?user=" + userId;
  xhr.open('GET', getUserInfoLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            document.getElementById("userName").innerHTML = returnData['data']['name'];
            document.getElementById("userImage").setAttribute("src",returnData['data']['image']);
            document.getElementById("userName2").innerHTML = returnData['data']['name'];
            document.getElementById("userImage2").setAttribute("src",returnData['data']['image']);
            document.getElementById("userName3").innerHTML = returnData['data']['name'];
            document.getElementById("userImage3").setAttribute("src",returnData['data']['image']);
            document.getElementById("userRegTime").innerHTML = returnData['data']['regTime'];
          }
      }
  }
  xhr.send();
}

/* 登出 */
document.getElementById("signOut").addEventListener("click", function() {
  window.localStorage.removeItem("ApiSysAccount");
  window.location = 'login.html';
});
