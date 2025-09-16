// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
if (navToggle && navMenu) {
  navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('open');
  });
}

// Demo enroll interactions
const enrollButtons = document.querySelectorAll('.enroll');
const enrollModal = document.getElementById('enrollModal');
const title = document.getElementById('enrollCourseTitle');
enrollButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const course = btn.getAttribute('data-course') || 'Course';
    if (title) title.textContent = `Enroll: ${course}`;
    if (enrollModal && typeof enrollModal.showModal === 'function') {
      enrollModal.showModal();
    } else {
      alert(`Enroll: ${course}`);
    }
  });
});

// Navigation buttons (placeholder)
document.getElementById('loginBtn')?.addEventListener('click', () => {
  window.location.hash = '#login';
  alert('Login page will be implemented with Django backend.');
});
document.getElementById('registerBtn')?.addEventListener('click', () => {
  window.location.hash = '#register';
  alert('Register page with UPI ID and UTR will be built in backend phase.');
});


