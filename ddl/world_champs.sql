CREATE TABLE baseball.world_champs (
  team_name   CHAR(3),
  year        DATE
);

GRANT SELECT ON TABLE baseball.game_data TO analyst;

INSERT INTO baseball.world_champs VALUES
('SFN', '2010-01-01'),
('SLN', '2011-01-01'),
('SFN', '2012-01-01'),
('BOS', '2013-01-01'),
('SFN', '2014-01-01'),
('KCA', '2015-01-01'),
('CHN', '2016-01-01'),
('HOU', '2017-01-01');
