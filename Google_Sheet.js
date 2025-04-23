const scriptURL = 'https://script.google.com/macros/s/AKfycbzGTds4ksGWSR_wtM6_QhSdH6QnAQ_lyz_eqIfgY3Nu3pkUX1jL1oJ9k4O6kciefOct/exec'

const form = document.forms['contact-form']

form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
  .then(response => alert("Thank you! your form is submitted successfully 🎉🎉🎉" ))
  .then(() => { window.location.reload(); })
  .catch(error => console.error('Error!', error.message))
})