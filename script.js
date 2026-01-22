document.addEventListener('DOMContentLoaded', () => {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            
            // Toggle active class
            question.classList.toggle('active');

            // Toggle max-height
            if (question.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + 'px';
            } else {
                answer.style.maxHeight = 0;
            }

            // Optional: Close others
            faqQuestions.forEach(otherQ => {
                if (otherQ !== question && otherQ.classList.contains('active')) {
                    otherQ.classList.remove('active');
                    otherQ.nextElementSibling.style.maxHeight = 0;
                }
            });
        });
    });
});
