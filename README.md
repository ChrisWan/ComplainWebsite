# Complaint Management System 💝

A colorful and animated web application designed to help manage complaints with encouraging quotes and fun animations!

## 🌟 Features

- **📅 Real-time Clock & Date Display** - Updates every second
- **💭 Encouraging Quotes** - 25+ inspiring quotes that rotate every minute
- **✈️ Animated Complaint Submission** - Paper plane flies from text field to mailbox
- **📋 Complaint Management** - Dropdown to view all open complaints
- **✅ Mark as Resolved** - Remove complaints when they've been addressed
- **💾 Persistent Storage** - All complaints saved in JSON format
- **🌈 Colorful Design** - Gradient backgrounds, animated text, and modern UI
- **📱 Responsive** - Works on desktop and mobile devices

## 📁 Project Structure

```
ComplainWebsite/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── config/               # Configuration files
│   ├── __init__.py
│   ├── settings.py       # App settings and configuration
│   └── quotes.py         # Encouraging quotes collection
├── templates/            # HTML templates
│   └── index.html        # Main page template
├── static/               # Static assets
│   ├── css/
│   │   └── styles.css    # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
└── data/                 # Data storage
    └── complaints.json   # Persistent complaint storage (auto-created)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd ComplainWebsite
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## 🎮 How to Use

1. **View the Time & Quotes**: The homepage displays the current date/time and an encouraging quote that changes every minute.

2. **Submit a Complaint**: 
   - Type your complaint in the text area
   - Press Enter or click "Send to the Universe"
   - Watch the paper plane animation fly to the mailbox!

3. **View Open Complaints**:
   - Use the dropdown to select and view previous complaints
   - See when each complaint was submitted

4. **Mark as Resolved**:
   - Select a complaint from the dropdown
   - Click "Mark as Resolved" to remove it from the list

## 🛠️ Configuration

You can modify the application settings in `config/settings.py`:

- **COMPLAINTS_FILE**: Path to the JSON file storing complaints
- **HOST**: Server host (default: '0.0.0.0')
- **PORT**: Server port (default: 5000)
- **DEBUG**: Enable/disable debug mode

## 📝 Adding New Quotes

To add more encouraging quotes, edit the `ENCOURAGING_QUOTES` list in `config/quotes.py`.

## 🎨 Customizing the Design

- **Colors & Styles**: Modify `static/css/styles.css`
- **Animations**: Adjust animation timings and effects in the CSS file
- **Layout**: Update `templates/index.html` for structural changes

## 🔧 Development

The application is built with:
- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Storage**: JSON file (lightweight, no database required)
- **Styling**: Custom CSS with animations and gradients

## 🎯 Perfect For

- Managing daily complaints with a positive twist
- Providing emotional support through encouraging quotes
- Making the complaint process more visually engaging
- Keeping track of issues that need resolution

## 💝 Made with Love

This system turns complaint time into a more positive, visual experience while still allowing proper expression and tracking of concerns. The encouraging quotes and fun animations help lift the mood! 

---

*Press Ctrl+C in the terminal to stop the server when done.*
