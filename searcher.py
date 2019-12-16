use thesaurus
SELECT f.file_name, COUNT(f.id) AS relev FROM Files f
JOIN TermsOfFiles tof ON f.id = tof.file_id
JOIN Terms t ON tof.term_id = t.id
WHERE term IN ('kekesss', 'uuuups')
GROUP BY f.file_name
ORDER BY relev DESC;
