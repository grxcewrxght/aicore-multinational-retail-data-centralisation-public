import data_extraction as de
import numpy as np 
import pandas as pd

class DataCleaning:
  # Handling NULL values, date errors, incorrect information, and potential typing errors
  def clean_user_data(self, user_df):
        user_df.dropna(subset=['important_column'], inplace=True)  # Replace 'important_column' with the key column
        user_df['date_column'] = pd.to_datetime(user_df['date_column'], errors='coerce')
        user_df['numeric_column'] = pd.to_numeric(user_df['numeric_column'], errors='coerce')
        user_df = user_df[user_df['some_column'] != 'incorrect_value']
        return user_df

  
  def clean_card_data(self, pdf_df):
    # Checking for NULL entries and dropping rows with invalid entries
    pdf_df.dropna(subset=['card_number'], inplace=True)
    pdf_df.replace('NULL', np.nan, inplace=True)
    pdf_df = pdf_df[pdf_df['card_number'] != 'NULL']
    # Checking for whole number values in card numbers and updating pdf_df
    pdf_df = pdf_df[pdf_df['card_number'].apply(lambda x: str(x).isdigit())]
    return pdf_df

  
  def clean_store_data(self, pdf_df):
    codes = pd.DataFrame({'country_code': ['US', 'GB', 'DE']})
        # Find unique codes
        unique_codes = set(pdf_df['country_code'].unique())
        invalid_countries = unique_codes.difference(codes['country_code'])
        invalid = pdf_df['country_code'].isin(invalid_countries)
        valid_rows = pdf_df[~invalid]
        # Using .replace for cleaning
        valid_rows = valid_rows.replace(to_replace=['eeEurope', 'eeAmerica'], value=['Europe', 'America'])
        return valid_rows

  
  def convert_product_weights(self, product_df):
    # Convert 'weight' column to string and replace specific values
    product_df['weight'] = product_df['weight'].astype(str)
    product_df['weight'].replace({'12 x 100g': '1200g', '8 x 150g': '1200g'}, inplace=True)
    # Extract numbers and units from the weight column, converting weight to a float
    product_df['units'] = product_df['weight'].str.extract('([^\d.]+)')
    product_df['weight'] = product_df['weight'].str.extract('([\d.]+)').astype(float)
    # Convert 'kg' to 'g'
    kg_mask = product_df['units'] == 'kg'
    product_df.loc[kg_mask, 'weight'] *= 1000
    # Convert 'g' and 'ml' to 'g' (no change needed)
    g_ml_mask = (product_df['units'] == 'g') | (product_df['units'] == 'ml')
    product_df.loc[g_ml_mask, 'weight'] = product_df.loc[g_ml_mask, 'weight']
    # Drop the 'units' column after conversion
    product_df.drop(columns='units', inplace=True)
    return product_df

  
  def clean_products_data(self, product_df):
        # Remove first_name, last_name, and '1' columns before upload
        product_df.drop(columns=['first_name', 'last_name', '1'], inplace=True, errors='ignore')
        return product_df

  
  # Obtain necessary information
  def clean_orders_data(self, product_df):
        product_df = product_df[['index', 'date_uuid', 'user_uuid', 'card_number', 'store_code', 'product_code', 'product_quantity']]
        return product_df
