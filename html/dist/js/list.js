var pid = 0;
window.onload = function() {
  var url = document.location.toString();
　var arrUrl = url.split("#!");
  pid = arrUrl[1];
  getUserInfo();
  $('#apiData').DataTable();
}
