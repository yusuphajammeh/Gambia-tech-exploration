document.addEventListener('DOMContentLoaded', () => {

    // 1. Navigation Scroll Effect
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. Intersection Observer for Scroll Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Target elements to animate
    const sections = document.querySelectorAll('section');
    const cards = document.querySelectorAll('.project-card');
    const heroContent = document.querySelector('.hero-content');

    // Add initial hidden class and observe
    [...sections, ...cards].forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });

    if (heroContent) {
        heroContent.classList.add('fade-in-up', 'visible'); // Make hero visible immediately
    }

    // 3. Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 4. GitHub Stats Fetcher
    const username = 'YusuphaJammeh'; // Replace with your actual GitHub username
    const repoCountEl = document.getElementById('repo-count');
    const followerCountEl = document.getElementById('follower-count');
    const accountAgeEl = document.getElementById('account-age');

    // Only run if elements exist
    if (repoCountEl && followerCountEl && accountAgeEl) {
        fetch(`https://api.github.com/users/${username}`)
            .then(response => {
                if (!response.ok) throw new Error('User not found');
                return response.json();
            })
            .then(data => {
                // Update DOM
                repoCountEl.textContent = data.public_repos;
                followerCountEl.textContent = data.followers;

                // Calculate Account Age (Years)
                const createdYear = new Date(data.created_at).getFullYear();
                const currentYear = new Date().getFullYear();
                accountAgeEl.textContent = `${currentYear - createdYear} Years`;
            })
            .catch(error => {
                console.error('Error fetching GitHub stats:', error);
                repoCountEl.textContent = '-';
                followerCountEl.textContent = '-';
                accountAgeEl.textContent = '-';
            });
    }

});
