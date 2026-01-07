document.addEventListener("DOMContentLoaded", () => {
    const bubbles = document.querySelectorAll('.bubble');
    const selectedInput = document.getElementById('selected-bubbles');

    let selected = [];

    bubbles.forEach(bubble => {
        bubble.addEventListener('click', () => {
            const name = bubble.dataset.name;
            if (selected.includes(name)) {
                selected = selected.filter(b => b !== name);
                bubble.classList.remove('bg-purple-700', 'text-white');
                bubble.classList.add('bg-purple-200');
            } else {
                selected.push(name);
                bubble.classList.add('bg-purple-700', 'text-white');
                bubble.classList.remove('bg-purple-200');
            }
            selectedInput.value = selected.join(',');
            console.log("Selected bubbles:", selectedInput.value); // for testing
        });
    });
});
