-- Keep a log of any SQL queries you execute as you solve the mystery.

1)
SELECT description
FROM crime_scene_reports
WHERE day = "28" and month = "07" and year = "2021";
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time –
each of their interview transcripts mentions the bakery.

2)
SELECT transcript, name
FROM interviews
WHERE day = "28" and month = "07" and year = "2021";

3) -- Ruth: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot,
-- you might want to look for cars that left the parking lot in that time frame.

SELECT name
FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE day = "28" and month = "07" and year = "2021" and activity = "exit" and hour = 10 and minute >= 15 and minute <= 25;

List of suspects:
+---------+
| Vanessa |
| Bruce   |
| Barry   |
| Luca    |
| Sofia   |
| Iman    |
| Diana   |
| Kelsey  |

4) -- Eugene:  I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma s bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

SELECT name
FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE day = "28" and month = "07" and year = "2021" and atm_location = "Leggett Street" and transaction_type = "withdraw";

List of suspects:
| Bruce   |
| Diana   |
|   |
|    |
| Iman    |
| Luca    |
|   |
|  |

5) -- Raymond: As the thief was leaving the bakery, they called someone who talked to them for less than a minute.

SELECT name
FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE day = "28" and month = "07" and year = "2021" and duration < 60;

List of suspects:
|    |
|   |
| Bruce   |
|   |
|   |
| Diana   |
|   |
|    |
|  |

-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.

SELECT name
FROM people JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (SELECT id FROM flights WHERE year = 2021 and month = 7 and day = 29 and origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour);

List of suspects:
|   |
|   |
| Bruce  |
|  |
|  |
|  |
|   |
|    |

SELECT city
FROM airports
WHERE id = (SELECT destination_airport_id FROM flights WHERE year = 2021 and day = 29 and month = 7 and origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour, minute);

Destination: New York City

-- The thief then asked the person on the other end of the phone to purchase the flight ticket.

SELECT phone_number
FROM people
WHERE name = "Bruce";

| (367) 555-5533 |

SELECT name
FROM people
WHERE phone_number = (SELECT receiver FROM phone_calls WHERE year = 2021 and month = 7 and day = 28 and duration < 60 and caller = "(367) 555-5533");

| name  |
+-------+
| Robin |