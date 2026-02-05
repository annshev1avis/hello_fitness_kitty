function getCsrfToken () {
    return document.querySelector("[name='csrfmiddlewaretoken']").value;
}

async function synchronizeLikes() {
    // Отправляет лайки из localStorage на бэкенд
    // для добавления в базу данных
    const likedPostsIds = JSON.parse(localStorage.getItem("likes"));

    if (likedPostsIds.length === 0) return;

    for (const postId of likedPostsIds) {
        await fetch(`/api/favorites/${postId}/`,
            {
                method: "POST",
                headers: {"X-CSRFToken": getCsrfToken()}
            }
        );
    }
    localStorage.setItem("likes", "[]");
}

document.addEventListener("DOMContentLoaded", synchronizeLikes)