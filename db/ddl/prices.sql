CREATE TABLE finance.stg_prices (
  symbol                  VARCHAR(255),
  calculationPrice        VARCHAR(255),
  open                    VARCHAR(255),
  close                   VARCHAR(255),
  high                    VARCHAR(255),
  low                     VARCHAR(255),
  latestPrice             VARCHAR(255),
  latestSource            VARCHAR(255),
  latestUpdate            VARCHAR(255),
  latestVolumne           VARCHAR(255),
  change                  VARCHAR(255),
  changePercent           VARCHAR(255),
  peRatio                 VARCHAR(255),
  eventID                 VARCHAR(256)
);

GRANT ALL ON TABLE finance.stg_prices TO dataloader;