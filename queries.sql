-- S2a: Average Resolution Time by Department

SELECT department, AVG(resolution_hours)
FROM tickets
JOIN teams ON tickets.team_id = teams.team_id
GROUP BY department;


-- S2b: Teams with Average Resolution Above 24 Hours

SELECT team, AVG(resolution_hours)
FROM tickets
JOIN teams ON tickets.team_id = teams.team_id
GROUP BY team
HAVING AVG(resolution_hours) > 24;


-- S2c: Top 2 Channels with SLA Breaches

SELECT channel, COUNT(*) AS breach_count
FROM tickets
WHERE resolution_hours > 24
GROUP BY channel
ORDER BY breach_count DESC, channel ASC
LIMIT 2;


-- Diagnostic: Check Tickets for Each Team

SELECT team, COUNT(ticket_id) AS total_tickets
FROM teams
LEFT JOIN tickets ON teams.team_id = tickets.team_id
GROUP BY team;