# 🤖 Corvus AI - WhatsApp Ordering System

An automated Flask-based ordering system that integrates with WhatsApp for seamless business operations. Perfect for small businesses, restaurants, and e-commerce shops.

## ✨ Features

- **Multi-step Chat Interface**: Guide customers through product selection, quantity, name, and delivery location
- **WhatsApp Integration**: Direct links to complete orders on WhatsApp
- **QR Code Generation**: Create shareable QR codes linking to your ordering system
- **Admin Dashboard**: Manage businesses, products, and view all orders
- **Secure Authentication**: Session-based admin login with CSRF protection
- **Order Management**: Track all orders with customer details and timestamps
- **SQLite Database**: Lightweight, no setup database included
- **Production-Ready**: Security best practices, error handling, and logging

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rmg701/Rmg-.git
   cd Rmg-
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and change the secret key and admin credentials:
   ```
   FLASK_SECRET_KEY=your-secure-random-key-here
   ADMIN_USERNAME=your-admin-username
   ADMIN_PASSWORD=your-secure-password
   ```

5. **Run the application**
   ```bash
   python app.py
   ```
   
   Access at: `http://localhost:81`

## 📖 Usage

### For Admins

1. Navigate to `http://localhost:81/login`
2. Login with your admin credentials
3. Add businesses with their details:
   - Business ID (unique identifier)
   - Business Name
   - WhatsApp Phone Number
   - Products with prices (format: `item:price, item:price`)
4. Generate QR codes for customers
5. View all orders in the dashboard

### For Customers

1. Scan QR code or visit the link with business ID
2. Chat with the bot to:
   - Select a product
   - Enter quantity
   - Provide name
   - Enter delivery location
3. Click "Complete on WhatsApp" to finalize the order

## 📁 Project Structure

```
Rmg-/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── utils.py              # Helper functions and validators
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore patterns
├── README.md            # This file
├── corvus.db            # SQLite database (auto-created)
└── static/              # QR code images (auto-created)
```

## 🔒 Security Features

- ✅ CSRF Protection on admin forms
- ✅ Input validation and sanitization
- ✅ Secure session handling
- ✅ Parameterized SQL queries (prevents SQL injection)
- ✅ Password-protected admin panel
- ✅ Environment-based configuration
- ✅ Audit logging for admin actions
- ✅ HTTPONLY session cookies
- ✅ Error handling without exposing sensitive info

## 📋 API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page / customer chat interface |
| `/login` | GET, POST | Admin login |
| `/logout` | GET | Admin logout |
| `/admin` | GET, POST | Admin dashboard |
| `/dashboard/<biz_id>` | GET | View business orders |
| `/qr/<biz_id>` | GET | Generate QR code |

## 🗄️ Database Schema

### businesses
- `id` (TEXT, PRIMARY KEY): Unique business identifier
- `name` (TEXT): Business name
- `phone` (TEXT): WhatsApp phone number
- `products` (TEXT): Comma-separated products with prices
- `active` (INTEGER): 1 for active, 0 for inactive
- `created_at` (TIMESTAMP): Creation timestamp
- `updated_at` (TIMESTAMP): Last update timestamp

### orders
- `id` (INTEGER, PRIMARY KEY): Order ID
- `biz_id` (TEXT): Business ID (foreign key)
- `customer_name` (TEXT): Customer name
- `item` (TEXT): Product name
- `quantity` (INTEGER): Order quantity
- `location` (TEXT): Delivery location
- `total` (INTEGER): Order total in KSh
- `created_at` (TIMESTAMP): Order timestamp

### audit_log
- `id` (INTEGER, PRIMARY KEY): Log ID
- `action` (TEXT): Action performed
- `details` (TEXT): Additional details
- `user_ip` (TEXT): User IP address
- `created_at` (TIMESTAMP): Timestamp

## 🛠️ Configuration

Edit `.env` file to customize:

```env
FLASK_ENV=development          # development or production
FLASK_SECRET_KEY=your-key      # Change this! Use random string
ADMIN_USERNAME=admin           # Admin username
ADMIN_PASSWORD=corvus123       # Admin password
DATABASE_PATH=corvus.db        # Database file path
HOST=0.0.0.0                   # Server host
PORT=81                        # Server port
DEBUG=False                    # Debug mode
```

## 📱 Product Format

When adding products, use this format:
```
hoodie:3000, tshirt:1500, cap:500
```

- Item name and price separated by `:`
- Multiple items separated by `,`
- Prices in Kenya Shillings (KSh)

## 🔄 WhatsApp Integration

The system generates WhatsApp links with pre-filled messages:
```
https://wa.me/254XXXXXXXXX?text=John+ordered+2+hoodies+(KSh+6000)+to+Nairobi
```

Customer clicks the link and WhatsApp opens with the pre-filled order details.

## 📊 Order Flow

```
Customer → Select Product → Enter Quantity → Enter Name → Enter Location
                                                              ↓
                                        Order Saved to Database
                                                              ↓
                                   WhatsApp Link Generated
                                                              ↓
                                   Admin Notified (via WA link)
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change PORT in .env file to another port (e.g., 8000)
PORT=8000
```

### Database Errors
```bash
# Delete old database and restart (creates new one)
rm corvus.db
python app.py
```

### CSRF Token Errors
- Make sure `.env` has a strong `FLASK_SECRET_KEY`
- Restart the application
- Clear browser cookies

## 📈 Performance Tips

- Use a production WSGI server (Gunicorn) for deployment
- Enable proper logging for monitoring
- Regular database backups
- Use proper phone number validation for your region

## 🚀 Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:81 app:app
```

### Using Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t corvus .
docker run -p 81:81 corvus
```

## 📝 License

MIT License - feel free to use and modify

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📞 Support

For issues, questions, or suggestions, please open a GitHub issue.

---

**Made with ❤️ for businesses**