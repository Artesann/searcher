use thesaurus
SELECT f.file_name, t.term, tof.term_count FROM Files f
JOIN TermsOfFiles tof ON f.id = tof.file_id
JOIN Terms t ON tof.term_id = t.id
ORDER BY f.file_name
