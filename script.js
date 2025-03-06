document.addEventListener("DOMContentLoaded", function() {
    let btn = document.createElement("button");
    btn.innerText = "Bấm vào tôi";
    btn.style.padding = "10px 20px";
    btn.style.fontSize = "16px";
    btn.onclick = function() {
        alert("Nút đã được bấm!");
    };
    document.body.appendChild(btn);
});
