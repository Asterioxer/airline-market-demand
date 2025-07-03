# ✈️ Airline Booking Market Demand Dashboard

A Python-powered web app to track and visualize airline booking trends across routes, powered by real-time data and AI insights.

> 🧪 Developed as part of a technical test for a developer internship role.  
> 🔥 Fast, insightful, and designed for business use.

---

## 📌 Features

- ✅ Fetches real-time flight data via **AviationStack API**
- ✅ Supports filters: **Departure**, **Arrival**, and **Airline**
- ✅ Displays top 5 busiest routes using **Chart.js**
- ✅ Generates smart insights using **Cohere’s AI**
- ✅ Supports **Dark / Light** themes with a toggle switch
- ✅ Built using **Flask**, **Pandas**, and **HTML/CSS/JS**

---

## 🛠️ Tech Stack

| Layer       | Tools / Libraries                    |
|-------------|---------------------------------------|
| Backend     | Python, Flask, Pandas, Requests       |
| Frontend    | HTML, CSS (theme support), Chart.js   |
| AI Insights | Cohere API (`command-r-plus` model)   |
| Data Source | AviationStack API (Free Tier)         |
| UI Add-ons  | Theme toggle, dropdown filters        |

---

## 📸 Screenshot - preview

![Dashboard Screenshot](assets/Screenshot%202025-07-03%20213350.png)
![Logs](assets/Screenshot%202025-07-03%20214613.png)

## Video - preview

![Watch the video](assets/Screen%20Recording%202025-07-03%20213437.mp4)


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/airline-market-demand.git
cd airline-market-demand
```

### 2. Create a Conda Environment

```bash
conda create -n airline-demand python=3.11
conda activate airline-demand
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup API Keys
Create a .env file with:
```bash
AVIATIONSTACK_API_KEY=your_aviationstack_key
COHERE_API_KEY=your_cohere_api_key
```

### 5. Run the App
```bash
python app.py
```
Visit http://127.0.0.1:5000 in your browser.

### ⚙️ Project Structure is provided as follows
(by arduino)
airline-market-demand/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── .env
├── requirements.txt
└── README.md

### 🎯 Use Case
- This dashboard is designed for hospitality or travel industry professionals to:

- Monitor flight route demands in real-time

- Compare trends using filters and visual insights

- Use AI-generated summaries for faster decisions

- Share and operate without needing coding expertise


### 💡 Future Enhancements

🔍 Searchable dropdowns

📈 Historical data visualization

🌐 Multi-language support

📱 Responsive/mobile UI

# 📄 License
- This project is open for educational and professional evaluation use. Reach out for full-time collaborations or enhancements.

👋 Author
Soham Mukherjee
Python Developer | AI Explorer | Web Dev Enthusiast
📫 Connect on LinkedIn : {https://www.linkedin.com/in/soham-mukherjee-895966212/}


```yaml


---

Let me know if you'd like this:
- Rendered in a real `.md` file
- Auto-exported to GitHub
- Compressed as a `.zip` for submission

Would you also like to add a short demo video/gif or "how it works" section?
```
