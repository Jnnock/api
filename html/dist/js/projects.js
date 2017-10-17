var xhr = new XMLHttpRequest();

var createLink = requestLink+"/create/project";
var getLink = requestLink+"/get/projects"

window.onload = function() {

}

/* 新建项目数据提交 */
document.getElementById("createProject").addEventListener("click",function() {
  var image = document.getElementById('projectImage');
  var name = document.getElementById("projectName").value;
  var desc = document.getElementById("projectDesc").value;
  var formData = new FormData();
  var link = requestLink+"/login"
  formData.append('name', name);
  formData.append('desc', desc);
  formData.append('image', image.files[0]);
  xhr.open('POST', createLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            var name = document.getElementById("projectName").value = '';
            var desc = document.getElementById("projectDesc").value = '';
            $('#myModal').modal('hide');
            alert(returnData['data'])
          }
      }
  }
  xhr.send(formData);
  xhr.timeout = 3000;
  xhr.ontimeout = function(event){
    alert('请求超时！');
  }
})

/* 新建项目取消 */
document.getElementById("cancleCreate").addEventListener("click",function() {
  var name = document.getElementById("projectName").value = '';
  var desc = document.getElementById("projectDesc").value = '';
  $('#myModal').modal('hide');
})
