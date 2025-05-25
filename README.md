
# Optimized Medical Scheduling: Predictive Machine Learning and Dynamic Resource Allocation

This project is a smart healthcare appointment scheduling system that leverages Machine Learning and Integer Linear Programming (ILP) to optimize hospital resource utilization, minimize patient waiting times, and prioritize emergency cases. Designed for real-time, flexible, and intelligent scheduling, the system supports both online and in-person booking modes, token-based queuing, emergency prioritization, and automated notifications.

## Key Features

- Real-Time Token Generation  
  Assigns tokens dynamically upon booking to manage queues efficiently.

- Predictive No-Show Handling  
  Uses machine learning (SVM) to predict patient no-shows and dynamically overbook.

- Priority-Based Scheduling (ILP)  
  Integer Linear Programming allocates appointment slots optimally based on urgency and availability.

- Dual Mode Booking (Online + Walk-In)  
  Supports both online patient appointments and in-person (staff-assisted) booking.

- Automated Notifications  
  Sends appointment confirmations, reminders, and rescheduling updates.

- Real-Time Patient Tracking  
  Tracks patients through the consultation process: waiting → in-progress → completed.

- Role-Based Access Control (RBAC)  
  Different interfaces and permissions for Admin, Doctor, Nurse, Staff, and Patient.

## Technology Stack

- Frontend: HTML, CSS, Bootstrap, JavaScript  
- Backend: Python, Flask  
- Database: MySQL  
- ML Libraries: Scikit-learn, NumPy, Pandas  
- Server: WAMP Server  
- Notification: Integrated SMS/email (via Twilio or similar API)

## ML Integration

- Model: Support Vector Machine (SVM)
- Use Case: Predicts whether a patient is likely to miss the appointment based on historical data.
- Overbooking Logic: Applies strategic overbooking (based on predicted no-show probability) with a penalty factor αk to maintain balance.

## Modules Overview

- Admin Module: Add/edit doctors, manage system config, and view performance.
- Doctor Module: View upcoming patients, access records, and update consults.
- Patient Module: Book appointments, view status, receive alerts.
- Staff/Nurse Module: Handle walk-ins, update vitals, assist in check-in flow.
- Priority Scheduler: Allocates slots using ILP with emergency weighting.

## Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/optimized-medical-scheduling.git
   cd optimized-medical-scheduling
   ```

2. Setup a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the MySQL database using `appointment_scheduling.sql`.

5. Run the Flask server:
   ```bash
   python main.py
   ```

6. Access the app at:  
   http://localhost:5000

## Results

| Metric                  | Traditional | Proposed System |
|-------------------------|-------------|------------------|
| Avg. Wait Time          | High        | Reduced by ~30%  |
| Appointment Utilization | ~52%        | 56.29%           |
| No-Show Rate Impact     | Not handled | ML-Predicted     |
| Emergency Handling      | Absent      | Prioritized      |

## Reference

Based on the research:  
"Smart Medical Appointment Scheduling: Optimization, Machine Learning, and Overbooking to Enhance Resource Utilization"

## Future Enhancements

- Mobile app integration
- EHR interoperability
- Teleconsultation module
- Blockchain-based patient identity and security
- Analytics dashboard for hospital performance

## Authors

- Bharaniram A  
- Karunoss R  
- Kaviarasu K  
- Lakshmi Narayanan R

Supervised by: Dr. K. Aruna, M.E., Ph.D.
