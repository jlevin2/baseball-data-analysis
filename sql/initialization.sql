-- Group for ad-hoc analysis
CREATE GROUP analyst;
CREATE USER josh PASSWORD 'redsox' IN GROUP analyst;
-- Kafka data loader
CREATE USER dataloader PASSWORD 'bigdata';
-- Create schemas for baseball (static data) and
-- Kafka loaded data
CREATE SCHEMA baseball;
CREATE SCHEMA kafka_test;
-- Setup perms on schemas
GRANT SELECT ON ALL TABLES IN SCHEMA baseball TO analyst;
ALTER SCHEMA kafka_test OWNER TO dataloader;