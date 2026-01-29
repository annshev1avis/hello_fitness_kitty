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

class DbStorage {

}

storage = USER_IS_AUTHENTICATED ? new DbStorage() : new BrowserStorage();

function UpdateUi() {
    // Добавляет нужный класс кнопке Лайка

    if (storage.isInList(postId)) {
        likeButton.classList.add("liked");
    } else {
        likeButton.classList.remove("liked");
    }
}

likeButton.addEventListener("click", function() {
    if (storage.isInList(postId)) {
        storage.removePost(postId);
    } else {
        storage.addPost(postId);
    }

    UpdateUi();
})

document.addEventListener('DOMContentLoaded', UpdateUi);
