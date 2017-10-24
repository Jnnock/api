var pid = 0;
window.onload = function() {
  var url = document.location.toString();
　var arrUrl = url.split("#!");
  pid = arrUrl[1];
  getUserInfo();
  getProjectModels();
  getProjectInfo();
  getUsersNum();
}

projectLink = requestLink + "/create/projectModel"
apiLink = requestLink + "/create/apiModel"

/* 新建项目模块 */
document.getElementById("createProject").addEventListener("click",function() {
  $('#myModal').modal('show');
  document.getElementById("myModalLabel").innerHTML = "新建项目模块";
  document.getElementById("createType").value = '1';
  document.getElementById("nameArea").innerHTML = "项目模块名称";
  document.getElementById("descArea").innerHTML = "项目模块说明";
  document.getElementById("name").setAttribute("placeholder",'输入项目模块名称');
  document.getElementById("desc").setAttribute("placeholder","输入项目模块说明");
})

/* 新建API模块 */
document.getElementById("createAPI").addEventListener("click",function() {
  $('#myModal').modal('show');
  document.getElementById("myModalLabel").innerHTML = "新建API模块";
  document.getElementById("createType").value = '2';
  document.getElementById("nameArea").innerHTML = "API模块名称";
  document.getElementById("descArea").innerHTML = "API模块说明";
  document.getElementById("name").setAttribute("placeholder",'输入API模块名称');
  document.getElementById("desc").setAttribute("placeholder","输入API模块说明");
})

/* 新建数据提交 */
document.getElementById("create").addEventListener("click",function() {
  var xhr = new XMLHttpRequest();
  var name = document.getElementById('name').value;
  var desc = document.getElementById("desc").value;
  var type = document.getElementById("createType").value;
  if (type == 1) {
    link = projectLink;
  } else if (type == 2) {
    link = apiLink;
  }
  var formData = new FormData();
  formData.append('name', name);
  formData.append('desc', desc);
  formData.append('project',pid);
  xhr.open('POST', link);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;/*忽略未完成的调用*/
      if (xhr.status === 200) {
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            var name = document.getElementById("name").value = '';
            var desc = document.getElementById("desc").value = '';
            $('#myModal').modal('hide');
            layer.msg("添加成功");
            if(type == 1) {
              getProjectModels();
            } else if (type == 2) {
              getApiModels();
            }
          }
      }
  }
  xhr.send(formData);
  xhr.timeout = 3000;
  xhr.ontimeout = function(event){
    alert('请求超时！');
  }
})

/* 新建取消 */
document.getElementById("cancleCreate").addEventListener("click",function() {
  var name = document.getElementById("name").value = '';
  var desc = document.getElementById("desc").value = '';
  $('#myModal').modal('hide');
})

projectListHtml = '<div class="row" style="padding:0 20px 0 20px"><div class="col-xs-12"><h2 class="page-header"><a href="list.html#!MODEL_ID">MODEL_NAME</a><small>MODEL_DESC</small></h2></div><!-- /.col --></div>'

function getProjectModels() {
  var xhr = new XMLHttpRequest();
  document.getElementById("tab_1").innerHTML = '<img src="dist/image/loading.gif" />'
  var getProjectModelsLink = requestLink + "/get/projectModels?project=" + pid;
  xhr.open('GET', getProjectModelsLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
        document.getElementById("tab_1").innerHTML = ''
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            for (var i = 0; i < returnData['data'].length; i++) {
              model = projectListHtml.replace(/MODEL_NAME/g,returnData['data'][i]['name']);
              model = model.replace(/MODEL_DESC/g,returnData['data'][i]['desc']);
              model = model.replace(/MODEL_ID/g,returnData['data'][i]['id']);
              document.getElementById("tab_1").innerHTML += model;
            }
          }
      }
  }
  xhr.send();
}

document.getElementById("APIMODEL").addEventListener('click',getApiModels);
document.getElementById("PROJECTMODEL").addEventListener('click',getApiModels);

/* 获取API模块 */
function getApiModels() {
  var xhr = new XMLHttpRequest();
  document.getElementById("tab_2").innerHTML = '<img src="dist/image/loading.gif" />'
  var getProjectModelsLink = requestLink + "/get/apiModels?project=" + pid;
  xhr.open('GET', getProjectModelsLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
        document.getElementById("tab_2").innerHTML = ''
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            for (var i = 0; i < returnData['data'].length; i++) {
              model = projectListHtml.replace(/MODEL_NAME/g,returnData['data'][i]['name']);
              model = model.replace(/MODEL_DESC/g,returnData['data'][i]['desc']);
              model = model.replace(/MODEL_ID/g,returnData['data'][i]['id']);
              document.getElementById("tab_2").innerHTML += model;
            }
          }
      }
  }
  xhr.send();
}

function getProjectInfo() {
  var xhr = new XMLHttpRequest();
  var getProjectLink = requestLink + "/get/project?project=" + pid;
  xhr.open('GET', getProjectLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
        document.getElementById("tab_2").innerHTML = ''
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            document.getElementById("projectName").innerHTML = returnData['data']['name'];
            document.getElementById("projectDesc").innerHTML = returnData['data']['desc'];
            document.getElementById("projectImage").setAttribute("src",returnData['data']['image']);
          }
      }
  }
  xhr.send();
}

function getUsersNum() {
  var xhr = new XMLHttpRequest();
  var getProjectLink = requestLink + "/get/projectUserNum?project=" + pid;
  xhr.open('GET', getProjectLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
        document.getElementById("tab_2").innerHTML = ''
          returnData = eval('(' + xhr.responseText + ')');
          if (returnData['code'] == '1') {
            document.getElementById("usersNum").innerHTML = returnData['data']['number'];
          }
      }
  }
  xhr.send();
}

document.getElementById("checkUsers").addEventListener("click",function() {
  var xhr = new XMLHttpRequest();
  var getUsersLink = requestLink + "/get/usersList?project=" + pid;
  xhr.open('GET', getUsersLink);
  xhr.onreadystatechange = function () {
      if (xhr.readyState !== 4) return;//忽略未完成的调用
      if (xhr.status === 200) {
        $('#userModal').modal('show');
        userInfo = '<div class="row" style="margin-bottom:20px"><div class="col-md-1"><img width="40px" src="USER_IMAGE" class="img-circle"></div><div class="col-md-11"><div><h4><b>USER_NAME</b>USER_LABEL <div class="pull-right"><small>加入时间：USER_JOIN_TIME<small></div></h4></div></div></div>'
        labelInfo = '<small class="label label-small bg-primary" style="font-size:8px"> 创建者 </small>'
        returnData = eval('(' + xhr.responseText + ')');
        if (returnData['code'] == '1') {
          for (var i = 0; i < returnData['data'].length; i++) {
            model = userInfo.replace(/USER_IMAGE/g,returnData['data'][i]['image']);
            model = model.replace(/USER_NAME/g,returnData['data'][i]['name']);
            model = model.replace(/USER_JOIN_TIME/g,returnData['data'][i]['time']);
            if (returnData['data'][i]['relation'] == 1) {
              model = model.replace(/USER_LABEL/g,labelInfo);
            } else {
              model = model.replace(/USER_LABEL/g,'');
            }
            document.getElementById("userList").innerHTML += model;
          }
        }
      }
  }
  xhr.send();
})
