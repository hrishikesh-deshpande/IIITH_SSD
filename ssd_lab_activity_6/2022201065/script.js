function checkUN() {
  //   let un = document.getElementById("ip3");
  //   const pattern = "test";
  const unt = document.getElementById("ip3").value;
  //   console.log(typeof unt);
  var un = document.getElementById("ivun");
  if (unt.match("(?=.*[A-Z])") && unt.match("(?=.*\\d)")) {
    un.innerHTML = "";
  } else un.innerHTML = "Invalid Username";
}
function checkPW() {
  const f1 = document.getElementById("ip4").value;
  const f2 = document.getElementById("ip5").value;
  let pw = document.getElementById("ivpw");
  if (f1 != f2) {
    pw.innerHTML = "Passwords Don't Match";
  } else pw.innerHTML = "";
}
function submit() {
  const unt = document.getElementById("ip3").value;
  const f1 = document.getElementById("ip4").value;
  const f2 = document.getElementById("ip5").value;
  if (unt.match("(?=.*[A-Z])") && unt.match("(?=.*\\d)") && f1 != f2) {
    alert("Form Submitted Successfully");
  } else {
    alert("Form Submission failed");
  }
}
