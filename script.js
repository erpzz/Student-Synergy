/*
  Author: Eric Paiz
  Created: September 2024
  Description: Script for handling the Forgot Password form submission
*/

document.getElementById('forgot-password-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var email = document.getElementById('email').value;

    // Display the feedback message
    var feedbackMessage = document.getElementById('feedback-message');
    feedbackMessage.innerText = 'If the email is registered, you will receive a reset password email with instructions.';
    feedbackMessage.style.display = 'block';
});
