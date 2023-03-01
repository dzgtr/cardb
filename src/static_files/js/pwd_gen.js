
function pwd_generator() {
    var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-_@+/?=";
    var string_length = 16;
    var randomstring = '';
    for (var i=0; i < string_length; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        randomstring += chars.substring(rnum,rnum+1);
    }
    console.log(randomstring);
    document.getElementById('id_password1').value = randomstring;
}

function show_pwd() {
    var x = document.getElementById("id_password1");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}