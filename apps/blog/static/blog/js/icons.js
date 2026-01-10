const shareLinkButton = document.querySelector('[data-action="share-link"]');
const shareTgButton = document.querySelector('[data-action="share-tg"]');


async function callDialog(title, text="") {
    const dialog = document.querySelector(".dialog");

    const titleEl = dialog.querySelector(".dialog__title");
    const textEl = dialog.querySelector(".dialog__text");

    titleEl.textContent = title;
    textEl.textContent = text;

    dialog.show();

    await new Promise(resolve => setTimeout(resolve, 5000));

    dialog.close();
}

shareLinkButton.addEventListener("click", async () => {
    try {
        const url = window.location.href;
        await navigator.clipboard.writeText(url);
        callDialog("Ссылка скопирована");
    } catch (err) {
        callDialog(
            "Не получилось скопировать ссылку",
            "Попробуйте скопировать из адресной строки"
        );
        console.log(err);
    }
})

shareTgButton.addEventListener("click", async () => {
    try {
        const url = encodeURIComponent(window.location.href);
        const text = encodeURIComponent("Очень интересная статья");
        const tgShareLink = `https://t.me/share/url?url=${url}&text=${text}`;
        window.open(tgShareLink, "_blank");
    } catch (err) {
        callDialog(
            "Не получилось отправить через TG",
            "Попробуйте скопировать из адресной строки"
        );
    }
})
