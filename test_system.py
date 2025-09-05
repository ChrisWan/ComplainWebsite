"""
Test script for the Complaint Management System
Tests all major functionality without user interaction
"""

import json
import os
from datetime import datetime
import sys
sys.path.append('.')

from config.quotes import ENCOURAGING_QUOTES
from config.settings import Config

def test_configuration():
    """Test configuration setup"""
    print("🧪 Testing Configuration...")
    print(f"✅ Found {len(ENCOURAGING_QUOTES)} encouraging quotes")
    print(f"✅ Complaints file: {Config.COMPLAINTS_FILE}")
    print(f"✅ Host: {Config.HOST}:{Config.PORT}")
    return True

def test_quotes():
    """Test quotes functionality"""
    print("\n💭 Testing Quotes...")
    import random
    quote = random.choice(ENCOURAGING_QUOTES)
    print(f"✅ Random quote: {quote}")
    return True

def test_file_structure():
    """Test file structure"""
    print("\n📁 Testing File Structure...")
    required_files = [
        'app.py',
        'config/settings.py',
        'config/quotes.py',
        'config/__init__.py',
        'templates/index.html',
        'static/css/styles.css',
        'static/js/main.js',
        'requirements.txt',
        'README.md',
        'start_server.bat'
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {file_path} ({size:,} bytes)")
        else:
            print(f"❌ {file_path} - MISSING!")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def test_complaint_storage():
    """Test complaint storage functionality"""
    print("\n💾 Testing Complaint Storage...")
    
    # Create test complaints
    test_complaints = [
        {
            'id': 1,
            'text': 'Test complaint for system validation',
            'timestamp': datetime.now().isoformat(),
            'status': 'open'
        }
    ]
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Test saving
    with open(Config.COMPLAINTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(test_complaints, f, ensure_ascii=False, indent=2)
    print("✅ Complaint saving works")
    
    # Test loading
    with open(Config.COMPLAINTS_FILE, 'r', encoding='utf-8') as f:
        loaded_complaints = json.load(f)
    print(f"✅ Complaint loading works ({len(loaded_complaints)} complaints)")
    
    # Cleanup
    os.remove(Config.COMPLAINTS_FILE)
    print("✅ Test cleanup completed")
    
    return True

def main():
    """Run all tests"""
    print("🚀 Complaint Management System - Test Suite")
    print("=" * 50)
    
    tests = [
        test_configuration,
        test_quotes,
        test_file_structure,
        test_complaint_storage
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! The system is ready to use.")
        print("\n🚀 To start the server:")
        print("   • Double-click 'start_server.bat'")
        print("   • Or run: python app.py")
        print("   • Then open: http://localhost:5000")
    else:
        print("⚠️ Some tests failed. Please check the output above.")
    
    return failed == 0

if __name__ == "__main__":
    main()
