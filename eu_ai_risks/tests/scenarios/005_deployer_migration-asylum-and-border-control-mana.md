FR-01 - The system shall capture travel document data by scanning the passport’s visual inspection zone (VIZ), machine-readable zone (MRZ), and embedded chip, and by accepting images taken under visible, infrared, and ultraviolet light.

FR-02 - The system shall extract and cross-validate the data from the MRZ, VIZ, and RFID chip, including checking MRZ check digits and flagging any inconsistencies between the printed data and the electronically stored data.

FR-03 - The system shall verify the chip’s digital signatures and certificate chain against trusted issuing-authority certificates (e.g., the ICAO Public Key Directory) to confirm that the chip data is genuine and has not been altered.

FR-04 - The system shall analyze the document’s physical and visual security features, such as holograms, watermarks, microprinting, fonts, laminate integrity, and photo substitution, and use AI models to detect signs of forgery, tampering, or counterfeiting.

FR-05 - The system shall compare the photograph in the document with the traveler’s live-captured face image using facial recognition, and return a match confidence score.

FR-06 - The system shall check document and traveler details against lost, stolen, and revoked document databases and watchlists (e.g., Interpol SLTD) in near real time.

FR-07 - The system shall produce an authenticity assessment for each document, including an overall risk score, a classification (genuine, suspicious, or likely forged), and an explanation of the specific indicators behind the result, so officers can review the reasoning.

FR-08 - The system shall present results to immigration officers through an interface that highlights flagged areas on the document image, and shall allow officers to confirm, override, or escalate each decision, with their feedback recorded to improve model accuracy.

FR-09 - The system shall maintain secure, auditable logs of all verification transactions, enforce role-based access control, and encrypt stored and transmitted personal data in compliance with applicable data protection regulations.