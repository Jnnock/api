var group = 1;
var newApi = '<tr id="argvGroupNEWAPI_ID"><td><input type="text" class="form-control" name="param[]"/></td><td class="mailbox-star"><input type="text" class="form-control" name="type[]" /></td><td class="mailbox-name"><select class="form-control" name="must[]"><option value="1">是</option><option value="0">否</option></select></td><td class="mailbox-subject"><input type="text" class="form-control" name="intro[]" /></td><td class="mailbox-date"><input type="text" class="form-control" name="example[]" /></td><td class="mailbox-date"><button type="button" class="btn btn-block btn-danger" onclick="delGroup(NEWAPI_ID)">删除</button></td></tr>'

function delGroup(groupId) {
    var body = document.getElementById("argvBody");
    var argv = document.getElementById("argvGroup"+groupId);
    body.removeChild(argv);
}

document.getElementById("addGroupBtn").addEventListener("click",function() {
  var body = document.getElementById("argvBody");
  html = newApi.replace(/NEWAPI_ID/g,group);
  body.innerHTML += html;
  group ++;
});

/* 保存API */
document.getElementById("saveData").addEventListener("click",function() {
  var xhr = new XMLHttpRequest();
  var getProjectModelsLink = requestLink + "/saveApi";
  var form = document.getElementById("apiData");
  var formData = new FormData(form);
  alert(formData);return;
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
})
