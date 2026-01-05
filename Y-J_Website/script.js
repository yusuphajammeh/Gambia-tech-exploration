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

    // Mobile Menu Toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (menuBtn && navLinks) {
        // Helper function to toggle menu state
        const toggleMenu = (isOpen) => {
            if (isOpen) {
                navLinks.classList.add('active');
                menuBtn.setAttribute('aria-expanded', 'true');
                menuBtn.querySelector('i').classList.replace('fa-bars', 'fa-times');
            } else {
                navLinks.classList.remove('active');
                menuBtn.setAttribute('aria-expanded', 'false');
                menuBtn.querySelector('i').classList.replace('fa-times', 'fa-bars');
            }
        };
        
        menuBtn.addEventListener('click', () => {
            const isCurrentlyOpen = navLinks.classList.contains('active');
            toggleMenu(!isCurrentlyOpen);
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                toggleMenu(false);
            });
        });
    }

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
        heroContent.classList.add('fade-in-up', 'visible');
    }

    // 2.5 Multi-string Typing Effect
    const typingText = document.querySelector('.typing-text');
    const roles = ["Full-Stack Tech Explorer", "AI Automation Developer", "Software Enthusiast"];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typeSpeed = 100;

    function typeLine() {
        const currentRole = roles[roleIndex];

        if (isDeleting) {
            typingText.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            typeSpeed = 50;
        } else {
            typingText.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
            typeSpeed = 100;
        }

        if (!isDeleting && charIndex === currentRole.length) {
            isDeleting = true;
            typeSpeed = 2000; // Pause at end
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typeSpeed = 500;
        }

        setTimeout(typeLine, typeSpeed);
    }

    if (typingText) {
        typeLine();
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

    // 4. GitHub Stats Fetcher (Synchronized with Python Bridge)
    // 4. GitHub Stats Fetcher (Reaching out of the Yj-website folder)
    const repoCountEl = document.getElementById('repo-count');
    const followerCountEl = document.getElementById('follower-count');
    const accountAgeEl = document.getElementById('account-age');
    const updateTimeEl = document.getElementById('update-time');

    if (repoCountEl && followerCountEl && accountAgeEl) {
        // We use '../' to step OUT of Yj-website and into the Main Folder
        fetch('../data.json?v=' + new Date().getTime())
            .then(response => {
                if (!response.ok) throw new Error('data.json not found in main folder');
                return response.json();
            })
            .then(data => {
                repoCountEl.textContent = data.repos;
                followerCountEl.textContent = data.followers;
                accountAgeEl.textContent = data.created;

                if (updateTimeEl) {
                    updateTimeEl.textContent = data.last_updated;
                }
                console.log("✅ Sync successful from Main Folder!");
            })
            .catch(error => {
                console.warn('Path error: Ensure data.json is in the root.', error);
            });
    }

});
