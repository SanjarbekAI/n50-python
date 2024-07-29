"""
Aviachiptalarni sotib olish uchun dastur tuzish kerak.
Har bitta operatsiyani log faylga yozib borish kerak.
Try exceptlardan foydalaning

Auth menu:
    - Login
    - Register
    - Exit

Admin:
    - Add plane (CRUD): id, name, capacity
    - Add airport (CRUD): name, country
    - Add flight: plane, from_airport, to_airport, flight_time, landing_time, status, tickets=0, price
    - Show all flights:
    - Logout

User:
    - Search flights: from_airport, to_airport -> all the available flights:
        - Buy ticket
            - Passport number, gmail
        - Back
    - My booked flights:
    - Logout
"""


