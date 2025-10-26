// Simple JavaScript for interactive elements
document.addEventListener('DOMContentLoaded', function() {
    // Add to cart functionality
    const addToCartButtons = document.querySelectorAll('.btn-primary');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.closest('.product-details') || this.textContent.includes('Add to Cart')) {
                e.preventDefault();
                const productName = this.closest('.product-info').querySelector('h2, h4').textContent;
                alert(`🌸 ${productName} added to cart!`);
            }
        });
    });

    // Add to wishlist functionality
    const wishlistButtons = document.querySelectorAll('.btn-secondary');

    wishlistButtons.forEach(button => {
        if (button.textContent.includes('Wishlist')) {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                const productName = this.closest('.product-info').querySelector('h2, h4').textContent;
                alert(`💖 ${productName} added to wishlist!`);
            });
        }
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Form validation
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !message) {
                e.preventDefault();
                alert('Please fill in all fields before submitting.');
            }
        });
    }
});