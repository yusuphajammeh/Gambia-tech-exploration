document.addEventListener('DOMContentLoaded', () => {

    /* =========================================
       1. MOBILE NAVIGATION
       ========================================= */
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    const icon = mobileToggle?.querySelector('i');

    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('active');

            // Toggle Icon
            if (icon) {
                icon.classList = isOpen ? 'fas fa-times' : 'fas fa-bars';
            }
        });

        // Close when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                if (icon) icon.classList = 'fas fa-bars';
            });
        });
    }

    /* =========================================
       2. SCROLL ANIMATIONS (Intersection Observer)
       ========================================= */
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -40px 0px"
    };

    const animateOnScroll = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once visible to save resources
                animateOnScroll.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Elements to animate
    const animatedElements = document.querySelectorAll('.fade-in-up, .glass-panel, h2, h3');
    animatedElements.forEach(el => {
        // Ensure they have the base class if not already
        if (!el.classList.contains('fade-in-up')) {
            el.classList.add('fade-in-up');
        }
        animateOnScroll.observe(el);
    });

    /* =========================================
       3. LIVE STATS FETCHER (DataSync)
       ========================================= */
    // Fetches data.json from the parent directory to simulate live stats
    const repoCountEl = document.getElementById('repo-count');
    const followerCountEl = document.getElementById('follower-count');
    const accountAgeEl = document.getElementById('account-age');
    const updateTimeEl = document.getElementById('update-time');

    async function fetchStats() {
        try {
            // Cache busting to ensure fresh data
            const response = await fetch('../data.json?v=' + Date.now());
            if (!response.ok) throw new Error('Stats file not found');

            const data = await response.json();

            // Animate Numbers Implementation
            const animateValue = (element, start, end, duration) => {
                let startTimestamp = null;
                const step = (timestamp) => {
                    if (!startTimestamp) startTimestamp = timestamp;
                    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                    element.innerHTML = Math.floor(progress * (end - start) + start);
                    if (progress < 1) {
                        window.requestAnimationFrame(step);
                    } else {
                        element.innerHTML = end; // Ensure final value is exact
                    }
                };
                window.requestAnimationFrame(step);
            };

            if (repoCountEl && data.repos !== undefined) {
                animateValue(repoCountEl, 0, data.repos, 1500);
            }

            if (followerCountEl && data.followers !== undefined) {
                animateValue(followerCountEl, 0, data.followers, 1500);
            }

            if (accountAgeEl && data.created) {
                accountAgeEl.textContent = data.created;
            }

            if (updateTimeEl && data.last_updated) {
                updateTimeEl.textContent = `LAST SYNC: ${data.last_updated} [GMT]`;
                updateTimeEl.style.color = 'var(--accent-cyan)';
            }

        } catch (error) {
            console.warn('Live Sync Offline:', error);
            if (updateTimeEl) updateTimeEl.textContent = 'Sync Offline';
        }
    }

    // Initialize Stats
    if (repoCountEl) fetchStats();

    /* =========================================
       4. SMOOTH SCROLLING
       ========================================= */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

});
