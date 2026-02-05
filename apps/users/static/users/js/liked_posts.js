const container = document.querySelector(".posts__list");

LOCALSTORAGE_KEY = "likes";

async function getLikedPosts() {
    const likedPostsIds = JSON.parse(localStorage.getItem(LOCALSTORAGE_KEY));

    if (likedPostsIds.length === 0)
        return [];

    const posts = await fetch(`/api/posts/${likedPostsIds.join(",")}/`)
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Не получилось загрузить посты с сервера");
            }
    });

    return posts; 
}

function showText(text) {
    const textElement = document.createElement("p");
    textElement.classList.add("text");
    textElement.textContent = text;
    container.appendChild(textElement);
}


function createPost(postData) {
    const post = document.createElement("article");
    post.className = "card card_size_gallery-grid card_orientation_vertical";

    if (postData["cover_url"]) {
        const img = document.createElement("img");
        img.className = "card__image card__image_orientation_vertical";
        img.src = postData["cover_url"];
        post.appendChild(img);
    }

    const content = document.createElement("div");
    content.className = "card__content";
    post.appendChild(content);

    const text = document.createElement("div");
    text.className = "card__text";
    content.appendChild(text);

    const title = document.createElement("h3");
    title.className = "title-h3 card__title";
    title.textContent = postData["name"];
    text.appendChild(title);

    const description = document.createElement("p");
    description.className = "text card__description";
    description.textContent = postData["description"];
    text.appendChild(description);

    const button = document.createElement("a");
    button.className = "button text card__button";
    button.textContent = "Читать";
    button.href = `/posts/${postData["slug"]}`;
    content.appendChild(button);

    return post;
}


document.addEventListener("DOMContentLoaded", async () => {
    try {
        const likedPosts = await getLikedPosts();

        if (likedPosts.length === 0) {
            showText(`Здесь пока ничего нет. Поищите интересные посты на главной странице!`);
        }

        const fragment = document.createDocumentFragment();
        for (const postData of likedPosts) {
            fragment.appendChild(createPost(postData));
        }
        container.appendChild(fragment);
    } catch (err) {
        showText(`Упс... ${ err.message }`);
    }
})
