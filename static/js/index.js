
const clickTracker = document.querySelector('#click');
let clicks = 0;
document.addEventListener('click', e => {
    clickTracker.textContent = ++clicks;
});
