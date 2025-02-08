document.getElementById('experience-form').addEventListener('submit', function(event) {
    event.preventDefault();
    addExperience();
});

document.getElementById('clear-button').addEventListener('click', function() {
    clearExperiences();
});

function addExperience() {
    const companyName = document.getElementById('company').value;
    const term = document.getElementById('term').value;

    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ 'company': companyName, 'term': term })
    })
    .then(response => response.json())
    .then(data => {
        const experienceList = document.getElementById('experience-list');
        const newItem = document.createElement('li');
        newItem.setAttribute('data-id', data.id);
        newItem.innerHTML = `<div><span>${data.company} - ${data.term} months</span></div>`;
        experienceList.appendChild(newItem);
        document.getElementById('experience-form').reset();
    })
    .catch(error => console.error('Error adding experience:', error));
}

function clearExperiences() {
    fetch('/clear', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        const experienceList = document.getElementById('experience-list');
        experienceList.innerHTML = '';
        console.log(data.message);
    })
    .catch(error => console.error('Error clearing experiences:', error));
}