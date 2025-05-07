-- Active: 1746560294327@@127.0.0.1@3306

UPDATE Drivers
SET
    points = (
        SELECT SUM(
                Bahrain + "Saudi Arabia" + Australia + Japan + China + Miami + "Emilia-Romagna" + Monaco + Canada + Spain + Austria + "Great Britain" + Hungary + Belgium + Netherlands + Italy + Azerbaijan + Singapore + "United States" + Mexico + Brazil + "Las Vegas" + Qatar + "Abu Dhabi"
            )
        FROM Points
        WHERE
            Points.driver_id = Drivers.driver_id
    );

UPDATE Drivers
SET
    fastest_laps = (
        SELECT COUNT(*)
        FROM Fastest_laps
        WHERE
            Fastest_laps.driver_id = Drivers.driver_id
    );

UPDATE Teams
SET
    team_points = (
        SELECT SUM(points)
        FROM Drivers
        WHERE
            Drivers.team_id = Teams.team_id
    );

ALTER TABLE Drivers ADD COLUMN World_Champion BOOLEAN DEFAULT False;

UPDATE Drivers
SET
    World_Champion = True
WHERE
    driver_id IN (10, 16, 6);

ALTER TABLE Tracks ADD COLUMN layout_image TEXT;

