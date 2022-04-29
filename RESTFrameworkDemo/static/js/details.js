function details(){
    let btn = document.getElementById('show_detail')
    let closeBtn = document.getElementById('close_detail')
    let content = document.getElementsByClassName('box-content')[0]
    btn.addEventListener("click", ()=>{
        content.hidden = false;
        btn.hidden = true
    })
    closeBtn.addEventListener("click", ()=>{
        content.hidden = true
        btn.hidden = false
    })
}

details()