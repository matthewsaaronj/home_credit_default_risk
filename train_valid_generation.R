
library(tidyverse)
library(tidymodels)
library(RODBC)
library(janitor)
library(pins)

db <- odbcDriverConnect('DRIVER={SQL SERVER};SERVER=LAPTOP-LT2BSKO0\\SQLEXPRESS;DATABASE=HOME_CREDIT')

'%notin%' <- Negate(`%in%`)


hc_data <- 
  sqlQuery(
    db,
    "
    SELECT *
    
    FROM dbo.APPLICATION_DATA
    WHERE DATA_SPLIT = 'TRAIN'
    
    "
  ) %>% 
  clean_names() %>% 
  mutate(target = as.factor(target))


set.seed(42)
splits <- initial_split(hc_data, strata = target, prop = .80)

train <- training(splits)
validate <- testing(splits)

# create both csv files and pins (for working within both R & Python)
board <- board_folder(getwd())

board %>% 
  pin_write(train, name = 'hc_train', type = 'csv')

board %>% 
  pin_write(validate, name = 'hc_valid', type = 'csv')

train %>% 
  write_csv('hc_train.csv')

validate %>% 
  write_csv('hc_valid.csv')


