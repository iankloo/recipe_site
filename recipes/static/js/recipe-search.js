document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('recipe-search');
    const recipeCards = document.querySelectorAll('.recipe-card');
    const noResultsMessage = document.getElementById('no-results');

    if (!searchInput) return;

    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase().trim();
        let visibleCount = 0;

        recipeCards.forEach(function(card) {
            const title = card.querySelector('.recipe-title')?.textContent.toLowerCase() || '';
            const description = card.querySelector('.recipe-description')?.textContent.toLowerCase() || '';
            const categories = card.querySelector('.recipe-categories')?.textContent.toLowerCase() || '';
            
            const isMatch = title.includes(searchTerm) || 
                           description.includes(searchTerm) || 
                           categories.includes(searchTerm);

            if (isMatch || searchTerm === '') {
                card.style.display = 'block';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        // Show/hide no results message
        if (noResultsMessage) {
            noResultsMessage.style.display = (visibleCount === 0 && searchTerm !== '') ? 'block' : 'none';
        }
    });

    // Clear search functionality
    const clearButton = document.getElementById('clear-search');
    if (clearButton) {
        clearButton.addEventListener('click', function() {
            searchInput.value = '';
            recipeCards.forEach(function(card) {
                card.style.display = 'block';
            });
            if (noResultsMessage) {
                noResultsMessage.style.display = 'none';
            }
        });
    }
});