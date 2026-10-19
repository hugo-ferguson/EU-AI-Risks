# Older Adults' Health Assistant App SRS

## 1 Functional Requirements

### 1.1 User registration and profile management

FR-1.1 The system shall allow older adults to create an account using email, phone number, or caregiver-assisted registration.

FR-1.2 The system shall allow users to enter basic profile information such as name, age, gender, emergency contacts, medical conditions, allergies, and preferred language.

FR-1.3 The system shall allow users to update their health profile at any time.

FR-1.4 The system shall allow users to nominate caregivers, family members, or healthcare professionals who can access selected health information.

FR-1.5 The system shall support different user roles, including older adult, caregiver, doctor, nurse, and administrator.

FR-1.6 The system shall allow users to set accessibility preferences such as larger text, high contrast mode, simplified navigation, and voice interaction.

### 1.2 Medication management

FR-2.1 The system shall allow users to add prescribed medications, including dosage, frequency, timing, and special instructions.

FR-2.2 The system shall send medication reminders at scheduled times.

FR-2.3 The system shall allow users to confirm whether they have taken, skipped, or delayed a medication.

FR-2.4 The system shall notify caregivers if a critical medication is repeatedly missed.

FR-2.5 The system shall provide warnings for potential medication conflicts based on known user allergies or recorded medications.

FR-2.6 The system shall allow healthcare professionals or caregivers to update medication schedules with user permission.

### 1.3 AI health assistant

FR-3.1 The system shall provide an AI-powered virtual assistant that can answer general health-related questions in simple language.

FR-3.2 The system shall allow users to interact with the AI assistant using text or voice.

FR-3.3 The system shall provide health guidance based on the user’s profile, symptoms, and history where appropriate.

FR-3.4 The system shall clearly advise users to contact a healthcare professional or emergency service when symptoms may indicate a serious condition.

FR-3.5 The system shall not provide a final medical diagnosis without professional clinical review.

FR-3.6 The system shall explain AI-generated suggestions in plain, understandable terms.

### 1.4 Symptom checking and health monitoring

FR-4.1 The system shall allow users to record symptoms such as pain, dizziness, shortness of breath, fatigue, fever, or confusion.

FR-4.2 The system shall ask follow-up questions to better understand reported symptoms.

FR-4.3 The system shall classify symptoms by urgency, such as low, moderate, urgent, or emergency.

FR-4.4 The system shall recommend next steps, such as self-care, booking an appointment, contacting a caregiver, or calling emergency services.

FR-4.5 The system shall allow users to record daily health status, mood, sleep, appetite, and physical activity.

FR-4.6 The system shall detect unusual changes in health patterns and notify the user or caregiver where appropriate.

### 1.5 Vital signs and device integration

FR-5.1 The system shall allow users to manually enter vital signs such as blood pressure, heart rate, blood glucose, oxygen saturation, temperature, and weight.

FR-5.2 The system shall integrate with compatible wearable devices or home monitoring devices.

FR-5.3 The system shall display health trends over time using simple charts and summaries.

FR-5.4 The system shall alert users when recorded values fall outside safe or personalised ranges.

FR-5.5 The system shall allow healthcare providers to review shared vital sign data with user consent.

### 1.6 Appointment management

FR-6.1 The system shall allow users to record upcoming medical appointments.

FR-6.2 The system shall send reminders before scheduled appointments.

FR-6.3 The system shall allow users to store appointment details such as doctor name, clinic location, reason for visit, and preparation notes.

FR-6.4 The system shall allow caregivers to view or manage appointments with user permission.

FR-6.5 The system shall support telehealth appointment links where available.

FR-6.6 The system shall allow users to record questions they want to ask their doctor.

### 1.7 Emergency support

FR-7.1 The system shall provide a clearly visible emergency assistance button.

FR-7.2 The system shall allow users to contact emergency services from within the app.

FR-7.3 The system shall allow users to notify emergency contacts during a health emergency.

FR-7.4 The system shall share critical medical information with emergency contacts if the user has enabled this feature.

FR-7.5 The system shall detect emergency keywords or severe symptoms and recommend urgent action.

FR-7.6 The system shall provide location-sharing support during emergencies, subject to user consent and device permissions.

### 1.8 Caregiver and family support

FR-8.1 The system shall allow users to invite trusted caregivers or family members.

FR-8.2 The system shall allow users to control what information caregivers can see.

FR-8.3 The system shall notify caregivers about missed medication, abnormal health readings, emergency alerts, or major behaviour changes.

FR-8.4 The system shall allow caregivers to send reminders or supportive messages to the older adult.

FR-8.5 The system shall allow caregivers to view health summaries and trends.

FR-8.6 The system shall maintain an activity log of caregiver actions for transparency.

### 1.9 Health education

FR-9.1 The system shall provide educational content on healthy ageing, fall prevention, nutrition, exercise, chronic disease management, medication safety, and mental wellbeing.

FR-9.2 The system shall personalise educational content based on user profile and health goals.

FR-9.3 The system shall present educational material in simple language with large text and optional audio playback.

FR-9.4 The system shall allow users to save helpful articles or videos.

FR-9.5 The system shall provide reminders for healthy habits such as hydration, walking, stretching, and sleep routines.

### 1.10 Mental health and social wellbeing

FR-10.1 The system shall allow users to record mood and emotional wellbeing.

FR-10.2 The system shall detect signs of loneliness, anxiety, or low mood based on user inputs and interaction patterns.

FR-10.3 The system shall suggest supportive actions such as contacting a friend, doing a breathing exercise, or speaking with a professional.

FR-10.4 The system shall provide access to mental health helplines or support resources.

FR-10.5 The system shall allow caregivers to receive alerts if serious wellbeing concerns are detected, with user consent.

### 1.11 Personalised recommendations

FR-11.1 The system shall generate personalised health reminders based on the user’s age, health conditions, medication schedule, and activity patterns.

FR-11.2 The system shall recommend daily wellness activities suited to the user’s mobility and health status.

FR-11.3 The system shall adapt recommendations based on user feedback and past behaviour.

FR-11.4 The system shall avoid recommendations that conflict with known medical restrictions.

FR-11.5 The system shall clearly indicate when recommendations are AI-generated.

### 1.12 Notifications and reminders

FR-12.1 The system shall send notifications for medication, appointments, hydration, exercise, health checks, and follow-up tasks.

FR-12.2 The system shall allow users to customise notification frequency and style.

FR-12.3 The system shall support voice reminders for users with visual difficulties.

FR-12.4 The system shall repeat critical reminders if no response is received.

FR-12.5 The system shall avoid excessive notifications to reduce confusion or alarm.

### 1.13 Reports and health summaries

FR-13.1 The system shall generate daily, weekly, or monthly health summaries.

FR-13.2 The system shall allow users to export health reports for healthcare appointments.

FR-13.3 The system shall provide simple explanations of health trends.

FR-13.4 The system shall allow caregivers and doctors to access reports only with user permission.

FR-13.5 The system shall highlight important changes, missed medications, abnormal readings, or recurring symptoms.

### 1.14 Feedback and support

FR-14.1 The system shall allow users to provide feedback about app usability and AI responses.

FR-14.2 The system shall allow users to report incorrect or unsafe AI advice.

FR-14.3 The system shall provide access to technical support.

FR-14.4 The system shall include a help section with step-by-step instructions.

FR-14.5 The system shall allow users to request human assistance where available.

## 2 Non-Functional Requirements

### 2.1 Usability

NFR-1.1 The app shall use a simple and intuitive interface suitable for older adults.

NFR-1.2 The app shall minimise the number of steps required to complete common tasks.

NFR-1.3 The app shall use clear labels, large buttons, and plain language.

NFR-1.4 The app shall avoid technical medical jargon where possible.

NFR-1.5 The app shall provide confirmation messages after important actions, such as medication logging or emergency contact updates.

NFR-1.6 The app shall support guided onboarding for first-time users.

NFR-1.7 The app shall be usable by people with limited digital literacy.

### 2.2 Accessibility

NFR-2.1 The app shall comply with recognised accessibility guidelines such as WCAG 2.2 where applicable.

NFR-2.2 The app shall support large text sizes.

NFR-2.3 The app shall support screen readers.

NFR-2.4 The app shall provide high contrast display options.

NFR-2.5 The app shall support voice input and audio output.

NFR-2.6 The app shall avoid relying solely on colour to communicate important information.

NFR-2.7 The app shall support users with reduced vision, hearing, dexterity, or cognitive ability.

NFR-2.8 The app shall allow users to slow down or repeat voice instructions.

### 2.3 Safety

NFR-3.1 The app shall clearly state that AI advice does not replace professional medical advice.

NFR-3.2 The app shall escalate potentially serious symptoms to emergency or professional care guidance.

NFR-3.3 The app shall avoid providing unsafe, overconfident, or unsupported medical recommendations.

NFR-3.4 The app shall include safeguards against hallucinated medical advice.

NFR-3.5 The app shall provide clear emergency instructions when urgent symptoms are detected.

NFR-3.6 The app shall log AI-generated advice for auditing and safety review.

NFR-3.7 The app shall prioritise user safety over engagement or convenience.

### 2.4 Privacy

NFR-4.1 The app shall collect only the health data necessary for its intended functions.

NFR-4.2 The app shall obtain user consent before collecting, storing, or sharing health information.

NFR-4.3 The app shall allow users to view, edit, export, or delete their personal data.

NFR-4.4 The app shall allow users to control which caregivers or clinicians can access their information.

NFR-4.5 The app shall not share personal health data with third parties without explicit consent.

NFR-4.6 The app shall anonymise or de-identify data where used for analytics or model improvement.

NFR-4.7 The app shall clearly explain how user data is used.

### 2.5 Security

NFR-5.1 The app shall encrypt sensitive data in transit and at rest.

NFR-5.2 The app shall support secure authentication, such as passwords, PINs, biometrics, or multi-factor authentication.

NFR-5.3 The app shall automatically log users out after a period of inactivity where appropriate.

NFR-5.4 The app shall protect against unauthorised access to health records.

NFR-5.5 The app shall maintain audit logs for access to sensitive information.

NFR-5.6 The app shall use role-based access control for older adults, caregivers, clinicians, and administrators.

NFR-5.7 The app shall regularly undergo security testing and vulnerability assessments.

### 2.6 Reliability

NFR-6.1 The app shall be available whenever users need to access critical health features.

NFR-6.2 The app shall continue to provide basic reminders even during temporary network issues.

NFR-6.3 The app shall recover gracefully from system errors.

NFR-6.4 The app shall prevent data loss during crashes or connectivity interruptions.

NFR-6.5 The app shall clearly inform users when a feature is unavailable.

NFR-6.6 The app shall maintain accurate reminder scheduling across time zones and daylight saving changes.

### 2.7 Performance

NFR-7.1 The app shall load key screens within a reasonable time on older smartphones.

NFR-7.2 The app shall respond quickly to user interactions.

NFR-7.3 The AI assistant shall provide responses within an acceptable timeframe.

NFR-7.4 The app shall minimise battery usage, especially when connected to wearable devices.

NFR-7.5 The app shall operate efficiently on devices with limited processing power or memory.

NFR-7.6 The app shall support offline access to essential information such as medication schedules and emergency contacts.

### 2.8 Accuracy

NFR-8.1 The app shall provide health recommendations based on reliable medical knowledge sources.

NFR-8.2 The app shall distinguish between confirmed user data and AI-inferred information.

NFR-8.3 The app shall avoid presenting uncertain AI outputs as facts.

NFR-8.4 The app shall provide confidence levels or uncertainty indicators where appropriate.

NFR-8.5 The app shall regularly update its medical knowledge base.

NFR-8.6 The app shall allow clinical review of high-risk AI outputs.

NFR-8.7 The app shall correct or remove inaccurate recommendations once identified.

### 2.9 Maintainability

NFR-9.1 The system shall be designed using modular components.

NFR-9.2 The system shall allow updates to AI models without disrupting core app functions.

NFR-9.3 The system shall support regular software updates and bug fixes.

NFR-9.4 The system shall maintain clear documentation for developers and administrators.

NFR-9.5 The system shall allow new health monitoring devices or integrations to be added in the future.

NFR-9.6 The system shall support testing of individual modules such as reminders, AI assistant, notifications, and data sharing.

### 2.10 Scalability

NFR-10.1 The system shall support an increasing number of users without major performance degradation.

NFR-10.2 The system shall support scaling of AI services during peak usage.

NFR-10.3 The system shall support large volumes of health data from users and connected devices.

NFR-10.4 The system shall allow expansion to additional languages, regions, and healthcare providers.

NFR-10.5 The system shall support future integration with hospitals, pharmacies, and electronic health record systems.

### 2.11 Interoperability

NFR-11.1 The app shall support integration with common wearable devices and health monitoring tools.

NFR-11.2 The app shall support standard healthcare data formats where applicable.

NFR-11.3 The app shall allow health data export in commonly used formats such as PDF or CSV.

NFR-11.4 The app shall support integration with telehealth platforms.

NFR-11.5 The app shall support future integration with electronic health record systems, subject to privacy and security requirements.

### 2.12 Ethical requirements

NFR-12.1 The app shall avoid ageist assumptions in its design and recommendations.

NFR-12.2 The app shall respect user autonomy and allow older adults to make their own decisions where possible.

NFR-12.3 The app shall clearly distinguish between AI advice and human clinical advice.

NFR-12.4 The app shall avoid manipulating users into unnecessary engagement.

NFR-12.5 The app shall be designed to support independence, not replace human care.

NFR-12.6 The app shall provide transparency about how AI decisions are made.

NFR-12.7 The app shall include processes for reviewing bias in AI recommendations.

### 2.13 Compliance

NFR-13.1 The app shall comply with relevant privacy and health data protection laws in the target region.

NFR-13.2 The app shall comply with medical software regulations if its features qualify as medical device functionality.

NFR-13.3 The app shall maintain records needed for clinical safety audits.

NFR-13.4 The app shall provide consent management features.

NFR-13.5 The app shall support data retention and deletion policies.

NFR-13.6 The app shall provide users with clear terms of use and privacy notices.

### 2.14 Availability and backup

NFR-14.1 The system shall maintain regular backups of user data.

NFR-14.2 The system shall support disaster recovery procedures.

NFR-14.3 The system shall minimise downtime for critical services.

NFR-14.4 The system shall notify users of planned maintenance where possible.

NFR-14.5 The system shall ensure emergency information remains accessible during service disruption.

### 2.15 User trust and transparency

NFR-15.1 The app shall explain why important alerts or recommendations were generated.

NFR-15.2 The app shall show users when data was last updated.

NFR-15.3 The app shall identify whether advice came from AI, a caregiver, or a healthcare professional.

NFR-15.4 The app shall allow users to challenge, correct, or dismiss AI-generated suggestions.

NFR-15.5 The app shall avoid creating false reassurance when symptoms may require medical attention.

NFR-15.6 The app shall provide clear disclaimers without overwhelming users.
