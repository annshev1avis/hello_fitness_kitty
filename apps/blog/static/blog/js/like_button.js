const likeButton = document.querySelector('[data-action="like"]');
const postId = Number(likeButton.dataset.postId);


class BrowserStorage {
    constructor() {
        this.LOCALSTORAGE_KEY = "likes";

        const browserData = localStorage.getItem(this.LOCALSTORAGE_KEY);
        this.likedPosts = browserData ? JSON.parse(browserData) : [];
    }

    isInList(postId) {
        const index = this.likedPosts.indexOf(postId);
        return index > -1;
    }

    addPost(postId) {
        this.likedPosts.push(postId);
        this.save();
    }

    removePost(postId) {
        const index = this.likedPosts.indexOf(postId);
        this.likedPosts.splice(index, 1);
        this.save();
    }

    save() {
        localStorage.setItem(
            this.LOCALSTORAGE_KEY,
            JSON.stringify(this.likedPosts)
        );
    }
}

function getCsrfToken () {
    return document.querySelector("[name='csrfmiddlewaretoken']").value;
}

class DbStorage {
    async isInList(postId) {
        const response = await fetch(`http://127.0.0.1:8000/favorites/${postId}/`);
        const data = await response.json();
        return data["result"];
    }

    async addPost(postId) {
        await fetch(`http://127.0.0.1:8000/favorites/${postId}/`,
            {
                method: "POST",
                headers: {"X-CSRFToken": getCsrfToken()}
            }
        );
    }

    async removePost(postId) {
        await fetch(`http://127.0.0.1:8000/favorites/${postId}/`,
            {
                method: "DELETE",
                headers: {"X-CSRFToken": getCsrfToken()}
            }
        );
    }
}

storage = USER_IS_AUTHENTICATED ? new DbStorage() : new BrowserStorage();

async function UpdateUi() {
    // Добавляет нужный класс кнопке Лайка

    if (await storage.isInList(postId)) {
        likeButton.classList.add("liked");
    } else {
        likeButton.classList.remove("liked");
    }
}

likeButton.addEventListener("click", async function() {
    if (await storage.isInList(postId)) {
        await storage.removePost(postId);
    } else {
        await storage.addPost(postId);
    }

    UpdateUi();
})

document.addEventListener('DOMContentLoaded', UpdateUi);
