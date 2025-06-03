(function($) {
    'use strict';

    // Mobile menu functionality
    class ResponsiveMenu {
        constructor() {
            this.init();
        }

        init() {
            this.bindEvents();
        }

        bindEvents() {
            // Mobile menu toggle
            $(document).on('click', '.menu-collapse a', (e) => {
                e.preventDefault();
                const menu = $(e.currentTarget).closest('.u-menu');
                this.toggleMenu(menu);
            });

            // Close menu button
            $(document).on('click', '.u-menu-close', (e) => {
                e.preventDefault();
                const menu = $(e.currentTarget).closest('.u-menu');
                this.closeMenu(menu);
            });

            // Close menu when clicking overlay
            $(document).on('click', '.u-menu-overlay', (e) => {
                const menu = $(e.currentTarget).closest('.u-menu');
                this.closeMenu(menu);
            });

            // Close menu on escape key
            $(document).on('keyup', (e) => {
                if (e.keyCode === 27) {
                    $('.u-menu.open').each((i, el) => {
                        this.closeMenu($(el));
                    });
                }
            });

            // Close menu on window resize
            $(window).on('resize', () => {
                $('.u-menu.open').each((i, el) => {
                    this.closeMenu($(el));
                });
            });
        }

        toggleMenu(menu) {
            if (menu.hasClass('open')) {
                this.closeMenu(menu);
            } else {
                this.openMenu(menu);
            }
        }

        openMenu(menu) {
            menu.addClass('open');
            $('body').addClass('menu-open');
            this.disableScroll();
        }

        closeMenu(menu) {
            menu.removeClass('open');
            $('body').removeClass('menu-open');
            this.enableScroll();
        }

        disableScroll() {
            $('body').css('overflow', 'hidden');
        }

        enableScroll() {
            $('body').css('overflow', '');
        }
    }

    // Smooth scrolling for anchor links
    class SmoothScroll {
        constructor() {
            this.init();
        }

        init() {
            $(document).on('click', 'a[href^="#"]', (e) => {
                const href = $(e.currentTarget).attr('href');
                
                if (href === '#' || href === '#!') return;
                
                const target = $(href);
                if (target.length) {
                    e.preventDefault();
                    this.scrollToTarget(target);
                }
            });
        }

        scrollToTarget(target) {
            const offset = 80; // Account for sticky header
            const targetPosition = target.offset().top - offset;
            
            $('html, body').animate({
                scrollTop: targetPosition
            }, 800, 'swing');
        }
    }

    // Simple form handling
    class FormHandler {
        constructor() {
            this.init();
        }

        init() {
            $(document).on('submit', '.u-form form', (e) => {
                this.handleSubmit(e);
            });
        }

        handleSubmit(e) {
            const form = $(e.currentTarget);
            const submitBtn = form.find('button[type="submit"]');
            
            // Basic validation
            if (!this.validateForm(form)) {
                e.preventDefault();
                return false;
            }

            // Disable submit button to prevent double submission
            submitBtn.prop('disabled', true);
            
            // You can add AJAX submission here if needed
            // For now, let the form submit normally
        }

        validateForm(form) {
            let isValid = true;
            
            // Check required fields
            form.find('[required]').each(function() {
                const field = $(this);
                if (!field.val().trim()) {
                    field.addClass('error');
                    isValid = false;
                } else {
                    field.removeClass('error');
                }
            });

            // Email validation
            const emailField = form.find('input[type="email"]');
            if (emailField.length) {
                const email = emailField.val();
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                
                if (email && !emailRegex.test(email)) {
                    emailField.addClass('error');
                    isValid = false;
                } else {
                    emailField.removeClass('error');
                }
            }

            return isValid;
        }
    }

    // Header scroll behavior
    class HeaderScroll {
        constructor() {
            this.header = $('.u-sticky');
            this.lastScrollY = 0;
            this.init();
        }

        init() {
            if (!this.header.length) return;

            $(window).on('scroll', () => {
                this.handleScroll();
            });
        }

        handleScroll() {
            const currentScrollY = $(window).scrollTop();
            
            // Add/remove scrolled class for styling
            if (currentScrollY > 50) {
                this.header.addClass('scrolled');
            } else {
                this.header.removeClass('scrolled');
            }

            this.lastScrollY = currentScrollY;
        }
    }

    // Initialize components when DOM is ready
    $(document).ready(function() {
        new ResponsiveMenu();
        new SmoothScroll();
        new FormHandler();
        new HeaderScroll();

        // Add any other initialization here
        console.log('Courier App initialized');
    });

    // Expose to global scope if needed
    window.CourierApp = {
        ResponsiveMenu,
        SmoothScroll,
        FormHandler,
        HeaderScroll
    };

})(jQuery);

// Additional utility functions
function initActiveMenuLinks() {
    const currentPath = window.location.pathname;
    const currentPage = currentPath.split('/').pop() || 'home';
    
    $('.u-nav-link').each(function() {
        const link = $(this);
        const href = link.attr('href');
        
        if (href === currentPage || 
            (currentPage === 'home' && (href === '' || href === '/'))) {
            link.closest('.u-nav-item').addClass('active');
        }
    });
}

// Initialize active menu links when page loads
$(window).on('load', function() {
    initActiveMenuLinks();
});