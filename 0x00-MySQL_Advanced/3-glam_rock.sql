-- List bands with Glam rock as main style, ranked by longevity
-- SQL script that lists all bands with Glam rock as main style, ranked by longevity
-- Requirements:
-- Import this table dump: metal_bands.sql.zip
-- Column names must be: band_name and lifespan (in years until 2022)
-- should use attributes formed and split for computing the lifespan
-- script can be executed on any database
SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
