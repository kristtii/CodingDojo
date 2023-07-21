function addLikes(postNumber) {
    const likesElement = document.getElementById(`post-${postNumber}`);
    const currentLikes = parseInt(likesElement.textContent);
    const newLikes = currentLikes + 1;
    likesElement.textContent = `${newLikes} like(s)`;
}