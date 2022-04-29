async function solve() {
    let btn = document.getElementById('btn')
    btn.addEventListener("click", like)
}

async function show_likes() {
    let res = await fetch("http://127.0.0.1:8000/likes_count");
    let likeValue = document.getElementById('likes');
    let likesCount = await res.json();
    likeValue.textContent = likesCount.length;
}

async function like() {
    let res = await fetch("http://127.0.0.1:8000/like_add/", {
        method: 'POST',
        headers: {"Content-Type": 'application/json'},
        body: JSON.stringify({'like': 1})
    });
    await show_likes()
}

show_likes()
solve()