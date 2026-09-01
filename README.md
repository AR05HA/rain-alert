# Rain Alert ☔

An automated Python script that checks the upcoming weather forecast via OpenWeatherMap and sends an email alert whenever rain or adverse weather is expected in the next 12 hours.

---

## Features

* **Real-Time Forecast Checks:** Queries the OpenWeatherMap 5-day / 3-hour forecast API for the next 12 hours (`cnt: 4`).
* **Smart Detection:** Identifies weather condition IDs below `700` (covering Thunderstorms, Drizzle, Rain, and Snow).
* **Automated Notifications:** Sends direct email alerts via Gmail SMTP.
* **Scheduled Runs:** Configured to run automatically via GitHub Actions workflows.

---

## Prerequisites

* Python 3.8+
* An [OpenWeatherMap API Key](https://home.openweathermap.org/users/sign_up)
* A Gmail account with an [App Password](https://myaccount.google.com/apppasswords) enabled (required if 2-Factor Authentication is active)

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/AR05HA/rain-alert.git](https://github.com/AR05HA/rain-alert.git)
cd rain-alert
