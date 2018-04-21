'use strict';

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function confirmForm() {
  let modal = $("#confirmModal");
  let faculty = $("#faculty option:selected").text();
  let remark = $("#remark").val();
  $("#contentConfirm").html(`発言者:${faculty}<br />発言:${remark}`);
  modal.modal();
}

function showSendingModal() {
  let modal = $("#sendingModal");
  modal.modal({backdrop: 'static', keyboard: false});
}

function hideSendingModal() {
  $('#sendingModal').modal('hide');
}

async function sendForm() {
  let faculty_id = $("#faculty").val();
  let remark = $("#remark").val();
  let data = { faculty_id: faculty_id, body: remark };
  let body = JSON.stringify(data);
  let headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' }; 
  let method = "POST";

  showSendingModal();

  let res = await Promise.all([fetch("/api/v1/remarks", { method, headers, body }), sleep(500)]);

  hideSendingModal();

  console.log(res);

  if (!res[0].ok) {
    toastr.error("失敗しました。");
    return;
  }

  let stat = await res[0].json();

  if (stat.success) {
    toastr.success("成功しました。");
  } else {
    toastr.error("失敗しました。");
  }
}

async function addFaculty() {
  let faculty_name = $("#new-faculty").val();

  let data = { name: faculty_name };
  let body = JSON.stringify(data);
  let headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' }; 
  let method = "POST";

  showSendingModal();

  let res = await Promise.all([fetch("/api/v1/faculties", { method, headers, body }), sleep(500)]);

  hideSendingModal();

  let result = await res[0].json();

  $("#faculty").append(`<option value=${result.id}>${faculty_name}</option>`);
}

$(() => {
  toastr.options.positionClass = 'toast-bottom-right';
  fetch("/api/v1/faculties").then(d => d.json()).then(d => {
    let faculty = $("#faculty");
    for (let f of d.results) {
      faculty.append(`<option value=${f.faculty_id}>${f.name}</option>`);
    }
  });

  $("#main-form").on('submit', e => {
    e.preventDefault();
    confirmForm();
  });

  $("#submitConfirm").click(() => {
    sendForm();
  });

  $("#addFaculty").click(() => {
    $("#addFacultyModal").modal();
  });

  $("#addFacultyConfirm").click(() => {
    addFaculty();
  });
});
