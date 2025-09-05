// Complaint Management System - Main JavaScript

let complaints = [];
let selectedComplaintId = null;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    updateDateTime();
    updateQuote();
    loadComplaints();
    
    // Update time every second
    setInterval(updateDateTime, 1000);
    
    // Update quote every minute
    setInterval(updateQuote, 60000);
    
    // Setup event listeners
    setupEventListeners();
});

function setupEventListeners() {
    // Allow Enter key to submit (but not Shift+Enter for new line)
    document.getElementById('complaintInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            submitComplaint();
        }
    });
}

// Date and Time Functions
function updateDateTime() {
    const now = new Date();
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };
    document.getElementById('datetime').textContent = now.toLocaleDateString('en-US', options);
}

// Quote Functions
function updateQuote() {
    fetch('/api/quote')
        .then(response => response.json())
        .then(data => {
            const quoteElement = document.getElementById('quote');
            quoteElement.style.opacity = '0';
            setTimeout(() => {
                quoteElement.textContent = data.quote;
                quoteElement.style.opacity = '1';
            }, 250);
        })
        .catch(error => console.error('Error fetching quote:', error));
}

// Complaint Management Functions
function loadComplaints() {
    fetch('/api/complaints')
        .then(response => response.json())
        .then(data => {
            complaints = data;
            updateDropdown();
        })
        .catch(error => console.error('Error loading complaints:', error));
}

function updateDropdown() {
    const dropdown = document.getElementById('complaintsDropdown');
    dropdown.innerHTML = '<option value="">Select a complaint to view...</option>';
    
    complaints.forEach(complaint => {
        const option = document.createElement('option');
        option.value = complaint.id;
        const date = new Date(complaint.timestamp).toLocaleDateString();
        option.textContent = `${date} - ${complaint.text.substring(0, 50)}${complaint.text.length > 50 ? '...' : ''}`;
        dropdown.appendChild(option);
    });
}

function viewComplaint() {
    const dropdown = document.getElementById('complaintsDropdown');
    const complaintId = parseInt(dropdown.value);
    
    if (!complaintId) {
        document.getElementById('complaintView').style.display = 'none';
        return;
    }
    
    const complaint = complaints.find(c => c.id === complaintId);
    if (complaint) {
        selectedComplaintId = complaintId;
        document.getElementById('selectedComplaintText').textContent = complaint.text;
        document.getElementById('selectedComplaintDate').textContent = 
            `Submitted on: ${new Date(complaint.timestamp).toLocaleString()}`;
        document.getElementById('complaintView').style.display = 'block';
        document.getElementById('complaintView').classList.add('fade-in');
    }
}

// Animation Functions
function createPaperPlaneAnimation(startElement) {
    const plane = document.createElement('div');
    plane.className = 'paper-plane';
    plane.textContent = '✈️';
    
    const rect = startElement.getBoundingClientRect();
    plane.style.left = rect.left + 'px';
    plane.style.top = rect.top + 'px';
    
    document.body.appendChild(plane);
    
    // Animate plane to mailbox
    setTimeout(() => {
        plane.style.right = '10px';
        plane.style.top = '10px';
        plane.style.transform = 'rotate(45deg)';
    }, 100);
    
    // Remove plane and add bounce to mailbox
    setTimeout(() => {
        document.body.removeChild(plane);
        document.querySelector('.mailbox').classList.add('bounce');
        setTimeout(() => {
            document.querySelector('.mailbox').classList.remove('bounce');
        }, 1000);
    }, 2100);
}

// Main Functions
function submitComplaint() {
    const input = document.getElementById('complaintInput');
    const complaintText = input.value.trim();
    
    if (!complaintText) {
        alert('Please enter a complaint first! 😊');
        return;
    }
    
    // Create paper plane animation
    createPaperPlaneAnimation(input);
    
    // Submit to server
    fetch('/api/complaints', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({complaint: complaintText})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            input.value = '';
            loadComplaints();
            setTimeout(() => {
                alert('Your complaint has been safely stored! 📮✨');
            }, 2200);
        } else {
            alert('Error: ' + (data.error || 'Unknown error occurred'));
        }
    })
    .catch(error => {
        console.error('Error submitting complaint:', error);
        alert('Oops! Something went wrong. Please try again.');
    });
}

function removeComplaint() {
    if (!selectedComplaintId) return;
    
    if (confirm('Mark this complaint as resolved? 🎉')) {
        fetch(`/api/complaints/${selectedComplaintId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                loadComplaints();
                document.getElementById('complaintView').style.display = 'none';
                document.getElementById('complaintsDropdown').value = '';
                selectedComplaintId = null;
            }
        })
        .catch(error => console.error('Error removing complaint:', error));
    }
}
