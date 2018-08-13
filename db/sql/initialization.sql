-- Group for ad-hoc analysis
CREATE GROUP analyst;
CREATE USER josh PASSWORD 'redsox' IN GROUP analyst;
-- Kafka data loader
CREATE USER dataloader PASSWORD 'bigdata';
-- Create schemas for baseball (static data) and
-- Kafka loaded data
CREATE SCHEMA baseball;
CREATE SCHEMA finance;
-- Setup perms on schemas
GRANT USAGE ON SCHEMA baseball TO analyst;
ALTER SCHEMA finance OWNER TO dataloader;