var xhr = new XMLHttpRequest();

var createLink = requestLink+"/create/project";
var getLink = requestLink+"/get/projects";
var userId = window.localStorage.getItem("ApiSysAccount");
if (!userId) {
  window.location = "login.html"
}
projectListHtml = '<div class="row"><div class="col-xs-1"><img src="PROJECT_IMAGE" width="55px" class="img-circle" /></div><div class="col-xs-11"><h2 class="page-header"><a href="project_detail.html#!PROJECT_ID">PROJECT_NAME</a><div class="pull-right"><small class="pull-right"><i class="fa fa-bar-chart" aria-hidden="true"></i>0<i class="fa fa-user" aria-hidden="true"></i>0</small><br /><small>上次更新时间: 未获取</small></div><small>PROJECT_DESC</small></h2></div><!-- /.col --></div>'
window.onload = function() {
  getProjects();
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
  formData.append('user',userId),
  xhr.open('POST', createLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;/*忽略未完成的调用*/
      if (xhr.status === 200) {
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            var name = document.getElementById("projectName").value = '';
            var desc = document.getElementById("projectDesc").value = '';
            $('#myModal').modal('hide');
            getProjects();
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

/* 拉取项目列表 */
function getProjects() {
  document.getElementById("tab_1").innerHTML = '<img src="dist/image/loading.gif" />'
  var getMyProjectLink = getLink + "?user=" + userId + "&type=1";
  xhr.open('GET', getMyProjectLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
        document.getElementById("tab_1").innerHTML = ''
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            var name = document.getElementById("projectName").value = '';
            var desc = document.getElementById("projectDesc").value = '';
            $('#myModal').modal('hide');
            for (var i = 0; i < returnData['data'].length; i++) {
              project = projectListHtml.replace(/PROJECT_IMAGE/g,returnData['data'][i]['image']);
              project = project.replace(/PROJECT_NAME/g,returnData['data'][i]['name']);
              project = project.replace(/PROJECT_DESC/g,returnData['data'][i]['desc']);
              project = project.replace(/PROJECT_ID/g,returnData['data'][i]['pid']);
              document.getElementById("tab_1").innerHTML += project
            }
          }
      }
  }
  xhr.send();
}
